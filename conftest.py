import pytest


@pytest.fixture()
def san_fran_coord():
    return '37.7891838', '-122.4033522'


@pytest.fixture()
def san_fran_text():
    return 'One Montgomery Tower'


@pytest.fixture()
def moscow_coord():
    return '55.753544', '37.621202'


@pytest.fixture()
def moscow_text():
    return 'Lobnoye Mesto'
