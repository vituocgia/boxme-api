from django.contrib.auth.models import User
from django.db import models
from django import forms
from bmga.utils import now


class Note(models.Model):
    user = models.ForeignKey(User, related_name='notes',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.updated = now()
        return super(Note, self).save(*args, **kwargs)


class AnnotatedNote(models.Model):
    note = models.OneToOneField(Note, related_name='annotated',
                                on_delete=models.CASCADE)
    annotations = models.TextField()

    def __unicode__(self):
        title = None
        try:
            title = self.note.title
        except Note.DoesNotExist:
            pass

        return u"Annotated %s" % title


class SlugBasedNote(models.Model):
    slug = models.SlugField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"SlugBased %s" % self.title


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = []
