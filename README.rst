===============
boxme-api
===============

Creating delicious APIs for Django apps modified by BoxMe API.

Currently in beta (v0.1.0) but being used actively in production on several
sites.


Requirements
============

Core
----

* Python 2.7+ or Python 3.4+
* Django 1.8 or 1.11 (LTS releases)
* dateutil (http://labix.org/python-dateutil) >= 2.1

Format Support
--------------

* XML: lxml 3 (http://lxml.de/) and defusedxml (https://pypi.python.org/pypi/defusedxml)
* YAML: pyyaml (http://pyyaml.org/)
* binary plist: biplist (http://explorapp.com/biplist/)

Optional
--------

* HTTP Digest authentication: python3-digest (https://bitbucket.org/akoha/python-digest/)


What's It Look Like?
====================

A basic example looks like:

.. code:: python

    # myapp/api.py
    # ============
    from bmga.resources import ModelResource
    from myapp.models import Entry


    class EntryResource(ModelResource):
        class Meta:
            queryset = Entry.objects.all()


    # urls.py
    # =======
    from django.conf.urls import url, include
    from bmga.api import Api
    from myapp.api import EntryResource

    v1_api = Api(api_name='v1')
    v1_api.register(EntryResource())

    urlpatterns = [
        # The normal jazz here then...
        url(r'^api/', include(v1_api.urls)),
    ]

That gets you a fully working, read-write API for the ``Entry`` model that
supports all CRUD operations in a RESTful way. JSON/XML/YAML support is already
there, and it's easy to add related data/authentication/caching.

You can find more in the documentation at
https://boxme-api.boxme.io/.


Why BoxMeAPI?
=============

There are other API frameworks out there for Django. You need to
assess the options available and decide for yourself. That said, here are some
common reasons for bmga.

* You need an API that is RESTful and uses HTTP well.
* You want to support deep relations.
* You DON'T want to have to write your own serializer to make the output right.
* You want an API framework that has little magic, very flexible and maps well to
  the problem domain.
* You want/need XML serialization that is treated equally to JSON (and YAML is
  there too).


Reference Material
==================
* http://en.wikipedia.org/wiki/REST
* http://en.wikipedia.org/wiki/List_of_HTTP_status_codes
* http://www.ietf.org/rfc/rfc2616.txt
* http://jacobian.org/writing/rest-worst-practices/


Getting Help
============


Security
========

BoxMeAPI is committed to providing a flexible and secure API, and was designed
with many security features and options in mind. Due to the complex nature of
APIs and the constant discovery of new attack vectors and vulnerabilities,
no software is immune to security holes.
If you come across a security hole **please do not open a Github issue**.
Instead, **drop us an email** at ``diepdt@peacesoft.net``

We'll then work together to investigate and resolve the problem so we can
announce a solution along with the vulnerability.
