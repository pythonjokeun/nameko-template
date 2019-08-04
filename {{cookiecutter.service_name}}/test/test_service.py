from nameko.testing.services import worker_factory
from src.service import {{ cookiecutter.service_name.title().replace("_", "") }}


def test_service():
    service = worker_factory({{ cookiecutter.service_name.title().replace("_", "") }})

    assert service.foo() == "foo"
    assert service.bar() == "bar"
