"""Module description goes here."""

from nameko.rpc import rpc


class {{ cookiecutter.service_name.title().replace("_", "") }}:
    """Service's description goes here."""

    name = "{{ cookiecutter.service_name }}"

    @rpc
    def foo(self):
        """Service's method description goes here."""

        return "foo"

    @rpc
    def bar(self):
        """Service's method description goes here."""

        return "bar"
