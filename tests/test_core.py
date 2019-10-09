import pytest
from hwsdk import core  # noqa
# ==============================


def test_getting_life():
    assert core.get_life() != ''

# __________________________________


def test_not_to_accept():
    with pytest.raises(RuntimeError):
        core.do_not_accept_this()


def test_to_fail():
    assert 2 == 2
