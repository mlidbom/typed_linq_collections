from __future__ import annotations

from typed_linq_collections.collections.q_frozen_set import QFrozenSet


def test_q_frozen_set_empty_constructor() -> None:
    empty_set = QFrozenSet()
    assert len(empty_set) == 0
    assert empty_set.to_list() == []


def test_q_frozen_set_with_iterable() -> None:
    test_set = QFrozenSet([1, 2, 3, 2])  # Duplicates should be removed
    assert len(test_set) == 3
    assert set(test_set.to_list()) == {1, 2, 3}


def test_q_frozen_set_empty_static_method() -> None:
    empty_set = QFrozenSet.empty()
    assert len(empty_set) == 0
    assert empty_set.to_list() == []


def test_q_frozen_set_qcount() -> None:
    test_set = QFrozenSet([1, 2, 3])
    assert test_set.qcount() == 3

    empty_set = QFrozenSet()
    assert empty_set.qcount() == 0


# Binary operators
def test_union_operator_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]) | QFrozenSet([3, 4, 5])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1, 2, 3, 4, 5})


def test_reverse_union_operator_returns_qfrozenset_with_the_correct_values() -> None:
    result = frozenset({3, 4, 5}) | QFrozenSet([1, 2, 3])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1, 2, 3, 4, 5})


def test_intersection_operator_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]) & QFrozenSet([2, 3, 4])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({2, 3})


def test_reverse_intersection_operator_returns_qfrozenset_with_the_correct_values() -> None:
    result = frozenset({2, 3, 4}) & QFrozenSet([1, 2, 3])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({2, 3})


def test_difference_operator_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]) - QFrozenSet([2, 3, 4])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1})


def test_reverse_difference_operator_returns_qfrozenset_with_the_correct_values() -> None:
    result = frozenset({2, 3, 4}) - QFrozenSet([1, 2, 3])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({4})


def test_symmetric_difference_operator_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]) ^ QFrozenSet([2, 3, 4])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1, 4})


def test_reverse_symmetric_difference_operator_returns_qfrozenset_with_the_correct_values() -> None:
    result = frozenset({2, 3, 4}) ^ QFrozenSet([1, 2, 3])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1, 4})


# Methods
def test_copy_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]).copy()
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1, 2, 3})


def test_union_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]).union([3, 4, 5])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1, 2, 3, 4, 5})


def test_intersection_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]).intersection([2, 3, 4])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({2, 3})


def test_difference_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]).difference([2, 3, 4])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1})


def test_symmetric_difference_returns_qfrozenset_with_the_correct_values() -> None:
    result = QFrozenSet([1, 2, 3]).symmetric_difference([2, 3, 4])
    assert isinstance(result, QFrozenSet)
    assert result == frozenset({1, 4})
