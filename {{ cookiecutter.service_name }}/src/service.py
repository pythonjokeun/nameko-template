"""Module description goes here."""
{% if cookiecutter.service_extension == "RPC" %}
from nameko.rpc import rpc
{% elif cookiecutter.service_extension == "HTTP" %}
from nameko.web.handlers import http
{% endif %}

class {{ cookiecutter.service_name.title().replace("_", "") }}:
    """Service's description goes here."""

    name = "{{ cookiecutter.service_name }}"
    {% if cookiecutter.service_extension == "RPC" %}
    @rpc
    def foo(self):
        """Service's method description goes here.

        For more information:
        https://nameko.readthedocs.io/en/stable/built_in_extensions.html#rpc
        """

        return "foo"

    @rpc
    def bar(self):
        """Service's method description goes here.

        For more information:
        https://nameko.readthedocs.io/en/stable/built_in_extensions.html#rpc
        """

        return "bar"
    {% elif cookiecutter.service_extension == "HTTP" %}
    @http("GET", "/foo")
    def foo(self, request):
        """Service's method description goes here.

        For more information:
        https://nameko.readthedocs.io/en/stable/built_in_extensions.html#http
        """

        return "foo"

    @http("POST", "/bar")
    def bar(self, request):
        """Service's method description goes here.

        For more information:
        https://nameko.readthedocs.io/en/stable/built_in_extensions.html#http
        """

        return "bar"
    {% endif %}
