from __future__ import annotations

from typed_linq_collections.collections.q_set import QSet


def test_q_set_empty_constructor() -> None:
    empty_set = QSet()
    assert len(empty_set) == 0
    assert empty_set.to_list() == []


def test_q_set_with_iterable() -> None:
    test_set = QSet([1, 2, 3, 2])  # Duplicates should be removed
    assert len(test_set) == 3
    assert set(test_set.to_list()) == {1, 2, 3}


def test_q_set_contains() -> None:
    test_set = QSet([1, 2, 3])
    assert test_set.contains(2)
    assert not test_set.contains(4)


def test_q_set_qcount() -> None:
    test_set = QSet([1, 2, 3])
    assert test_set.qcount() == 3

    empty_set = QSet()
    assert empty_set.qcount() == 0


# Binary operators
def test_union_operator_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]) | QSet([3, 4, 5])
    assert isinstance(result, QSet)
    assert result == {1, 2, 3, 4, 5}


def test_reverse_union_operator_returns_qset_with_the_correct_values() -> None:
    result = {3, 4, 5} | QSet([1, 2, 3])
    assert isinstance(result, QSet)
    assert result == {1, 2, 3, 4, 5}


def test_intersection_operator_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]) & QSet([2, 3, 4])
    assert isinstance(result, QSet)
    assert result == {2, 3}


def test_reverse_intersection_operator_returns_qset_with_the_correct_values() -> None:
    result = {2, 3, 4} & QSet([1, 2, 3])
    assert isinstance(result, QSet)
    assert result == {2, 3}


def test_difference_operator_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]) - QSet([2, 3, 4])
    assert isinstance(result, QSet)
    assert result == {1}


def test_reverse_difference_operator_returns_qset_with_the_correct_values() -> None:
    result = {2, 3, 4} - QSet([1, 2, 3])
    assert isinstance(result, QSet)
    assert result == {4}


def test_symmetric_difference_operator_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]) ^ QSet([2, 3, 4])
    assert isinstance(result, QSet)
    assert result == {1, 4}


def test_reverse_symmetric_difference_operator_returns_qset_with_the_correct_values() -> None:
    result = {2, 3, 4} ^ QSet([1, 2, 3])
    assert isinstance(result, QSet)
    assert result == {1, 4}


# In-place operators
def test_inplace_union_operator_returns_qset_with_the_correct_values() -> None:
    qs = QSet([1, 2, 3])
    qs |= QSet([3, 4, 5])
    assert isinstance(qs, QSet)
    assert qs == {1, 2, 3, 4, 5}


def test_inplace_intersection_operator_returns_qset_with_the_correct_values() -> None:
    qs = QSet([1, 2, 3])
    qs &= QSet([2, 3, 4])
    assert isinstance(qs, QSet)
    assert qs == {2, 3}


def test_inplace_difference_operator_returns_qset_with_the_correct_values() -> None:
    qs = QSet([1, 2, 3])
    qs -= QSet([2, 3, 4])
    assert isinstance(qs, QSet)
    assert qs == {1}


def test_inplace_symmetric_difference_operator_returns_qset_with_the_correct_values() -> None:
    qs = QSet([1, 2, 3])
    qs ^= QSet([2, 3, 4])
    assert isinstance(qs, QSet)
    assert qs == {1, 4}


# Methods
def test_copy_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]).copy()
    assert isinstance(result, QSet)
    assert result == {1, 2, 3}


def test_union_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]).union([3, 4, 5])
    assert isinstance(result, QSet)
    assert result == {1, 2, 3, 4, 5}


def test_intersection_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]).intersection([2, 3, 4])
    assert isinstance(result, QSet)
    assert result == {2, 3}


def test_difference_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]).difference([2, 3, 4])
    assert isinstance(result, QSet)
    assert result == {1}


def test_symmetric_difference_returns_qset_with_the_correct_values() -> None:
    result = QSet([1, 2, 3]).symmetric_difference([2, 3, 4])
    assert isinstance(result, QSet)
    assert result == {1, 4}
