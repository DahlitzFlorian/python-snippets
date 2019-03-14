import pytest


class Mario:
    pass


class Luigi:
    pass


@pytest.fixture(params=[Mario, Luigi])
def plumber(request):
    plumber_cls = request.param

    return plumber_cls()


def test_backwards_compatibility(plumber):
    assert 1 == 1
