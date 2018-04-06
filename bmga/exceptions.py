from __future__ import unicode_literals
from django.http import HttpResponse


class BoxmeError(Exception):
    """A base exception for other bmga-related errors."""
    pass


class HydrationError(BoxmeError):
    """Raised when there is an error hydrating data."""
    pass


class NotRegistered(BoxmeError):
    """
    Raised when the requested resource isn't registered with the ``Api`` class.
    """
    pass


class NotFound(BoxmeError):
    """
    Raised when the resource/object in question can't be found.
    """
    pass


class Unauthorized(BoxmeError):
    """
    Raised when the request object is not accessible to the user.

    This is different than the ``bmga.http.HttpUnauthorized`` & is handled
    differently internally.
    """
    pass


class ApiFieldError(BoxmeError):
    """
    Raised when there is a validation error with an ``ApiField``.
    """
    pass


class UnsupportedFormat(BoxmeError):
    """
    Raised when an unsupported serialization/deserialization format is requested.
    Two more specific subclasses are provided, ``UnsupportedSerializationFormat``
    and ``UnsupportedDeserializationFormat``.
    """
    _msg_template = '%s'

    def __init__(self, msg, *args, **kwargs):
        msg = self._msg_template % msg
        super(UnsupportedFormat, self).__init__(msg, *args, **kwargs)


class UnsupportedSerializationFormat(UnsupportedFormat):
    """
    Raised when an unsupported serialization format is requested.
    """
    _msg_template = "The format indicated '%s' had no available serialization method. Please check your ``formats`` and ``content_types`` on your Serializer."


class UnsupportedDeserializationFormat(UnsupportedFormat):
    """
    Raised when an unsupported deserialization format is requested.
    """
    _msg_template = "The format indicated '%s' had no available deserialization method. Please check your ``formats`` and ``content_types`` on your Serializer."


class BadRequest(BoxmeError):
    """
    A generalized exception for indicating incorrect request parameters.

    Handled specially in that the message tossed by this exception will be
    presented to the end user.
    """
    pass


class BlueberryFillingFound(BoxmeError):
    pass


class InvalidFilterError(BadRequest):
    """
    Raised when the end user attempts to use a filter that has not been
    explicitly allowed.
    """
    pass


class InvalidSortError(BadRequest):
    """
    Raised when the end user attempts to sort on a field that has not been
    explicitly allowed.
    """
    pass


class ImmediateHttpResponse(BoxmeError):
    """
    This exception is used to interrupt the flow of processing to immediately
    return a custom HttpResponse.

    Common uses include::

        * for authentication (like digest/OAuth)
        * for throttling

    """
    _response = HttpResponse("Nothing provided.")

    def __init__(self, response):
        self._response = response

    @property
    def response(self):
        return self._response
