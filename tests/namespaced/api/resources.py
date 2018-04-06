from django.contrib.auth.models import User
from bmga import fields
from bmga.resources import NamespacedModelResource
from bmga.authorization import Authorization
from basic.models import Note


class NamespacedUserResource(NamespacedModelResource):
    class Meta:
        resource_name = 'users'
        queryset = User.objects.all()
        authorization = Authorization()


class NamespacedNoteResource(NamespacedModelResource):
    user = fields.ForeignKey(NamespacedUserResource, 'user')

    class Meta:
        resource_name = 'notes'
        queryset = Note.objects.all()
        authorization = Authorization()
