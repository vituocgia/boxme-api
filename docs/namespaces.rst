.. _namespaces:

==========
Namespaces
==========

For various reasons you might want to deploy your API under a namespaced URL path. To support that bmga includes ``NamespacedApi`` and ``NamespacedModelResource``.

A sample definition of your API in this case would be something like::

    from django.conf.urls import url, include
    from bmga.api import NamespacedApi
    from my_application.api.resources import NamespacedUserResource

    api = NamespacedApi(api_name='v1', urlconf_namespace='special')
    api.register(NamespacedUserResource())

    urlpatterns = [
        url(r'^api/', include(api.urls, namespace='special')),
    ]

And your model resource::

    from django.contrib.auth.models import User
    from bmga.resources import NamespacedModelResource
    from bmga.authorization import Authorization

    class NamespacedUserResource(NamespacedModelResource):
        class Meta:
            resource_name = 'users'
            queryset = User.objects.all()
            authorization = Authorization()
