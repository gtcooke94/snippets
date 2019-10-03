import pytest

from challenge import Challenge, BlogChallenge, BiteChallenge


def test_should_not_instantiate_abc():
    with pytest.raises(TypeError):
        ch = Challenge(0, 'Should not instantiate ABC')
        ch.number


def test_super_and_abst_method_implementation():
    try:
        blog = BlogChallenge(1, 'Wordvalues', [41, 42, 44])
    except TypeError:
        pytest.fail("Unexpected TypeError, missing methods/properties?")

    assert blog.verify(41)
    assert not blog.verify(43)
    assert blog.pretty_title == 'PCC1 - Wordvalues'


def test_super_and_abst_property_implementation():
    try:
        bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')
    except TypeError:
        pytest.fail("Unexpected TypeError, missing methods/properties?")

    assert bite.verify('my result')
    assert not bite.verify('other result')
    assert bite.pretty_title == 'Bite 24. ABC and class inheritance'
