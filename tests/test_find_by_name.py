import collections
import mock
from nose.tools import raises
from rightscale.util import find_by_name


def test_find_by_name_returns_unpacked():
    """
    find_by_name() should return sole item unpacked from list
    """
    exp_item = 1
    col = mock.MagicMock()
    col.index.return_value = [exp_item]
    ret = find_by_name(col, 'dummy')
    assert exp_item == ret
    assert not isinstance(ret, collections.Sequence)


@raises(ValueError)
def test_found_too_many_by_name():
    """
    find_by_name() should fail when more than one found
    """
    col = mock.MagicMock()
    col.index.return_value = [1, 2, 3]
    find_by_name(col, 'dummy')
