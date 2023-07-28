import {{ project_name }}


def test_hello():
    assert({{ project_name }}.hello.hello_world(), "Hello world")


