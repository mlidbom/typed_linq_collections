from __future__ import annotations

from fractions import Fraction
from typing import TYPE_CHECKING

import pytest

from typed_linq_collections.collections.numeric.q_fraction_types import QFractionFrozenSet, QFractionIterable, QFractionIterableImplementation, QFractionList, QFractionSequence, QFractionSet
from typed_linq_collections.q_errors import EmptyIterableError
from typed_linq_collections.q_iterable import query

if TYPE_CHECKING:
    from collections.abc import Iterable


def test_sum_returns_sum_of_the_values() -> None:
    assert query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().sum() == Fraction(6)

def test_sum_returns_zero_on_empty_collection() -> None:
    assert query([]).as_fractions().sum() == Fraction(0)

def test_min_returns_min_of_the_values() -> None:
    assert query([Fraction(6), Fraction(2), Fraction(5), Fraction(3)]).as_fractions().min() == Fraction(2)

def test_min_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_fractions().min()

def test_max_returns_max_of_the_values() -> None:
    assert query([Fraction(1), Fraction(5), Fraction(3)]).as_fractions().max() == Fraction(5)

def test_max_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_fractions().max()

def test_min_or_default_returns_min_of_the_values() -> None:
    assert query([Fraction(6), Fraction(2), Fraction(5), Fraction(3)]).as_fractions().min_or_default() == Fraction(2)

def test_min_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_fractions().min_or_default() == Fraction(0)

def test_max_or_default_returns_max_of_the_values() -> None:
    assert query([Fraction(1), Fraction(5), Fraction(3)]).as_fractions().max_or_default() == Fraction(5)

def test_max_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_fractions().max_or_default() == Fraction(0)

def test_average_returns_average_of_the_values() -> None:
    assert query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().average() == Fraction(2)

def test_average_throws_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_fractions().average()

def test_average_or_default_returns_average_of_the_values() -> None:
    assert query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().average_or_default() == Fraction(2)

def test_average_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_fractions().average_or_default() == Fraction(0)

def test_where_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3), Fraction(4)]).as_fractions().where(lambda x: x > Fraction(2))
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(3), Fraction(4)]

def test_where_not_none_returns_qfraction_iterable() -> None:
    # This tests the where_not_none override method on QFractionIterable
    result = query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().where_not_none()
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(1), Fraction(2), Fraction(3)]

def test_distinct_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(2), Fraction(3)]).as_fractions().distinct()
    assert isinstance(result, QFractionIterable)
    assert set(result) == {Fraction(1), Fraction(2), Fraction(3)}

def test_distinct_by_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(-2), Fraction(3), Fraction(-4)]).as_fractions().distinct_by(abs)
    assert isinstance(result, QFractionIterable)
    assert len(list(result)) == 4  # All are distinct by absolute value

def test_take_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3), Fraction(4)]).as_fractions().take(2)
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(1), Fraction(2)]

def test_take_while_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3), Fraction(4)]).as_fractions().take_while(lambda x: x < Fraction(3))
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(1), Fraction(2)]

def test_take_last_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3), Fraction(4)]).as_fractions().take_last(2)
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(3), Fraction(4)]

def test_skip_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3), Fraction(4)]).as_fractions().skip(2)
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(3), Fraction(4)]

def test_skip_last_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3), Fraction(4)]).as_fractions().skip_last(2)
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(1), Fraction(2)]

def test_reversed_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().reversed()
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(3), Fraction(2), Fraction(1)]

def test_concat_returns_qfraction_iterable() -> None:
    result = query([Fraction(1), Fraction(2)]).as_fractions().concat([Fraction(3), Fraction(4)])
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]

def test_order_by_returns_qfraction_ordered_iterable() -> None:
    result = query([Fraction(3), Fraction(1), Fraction(2)]).as_fractions().order_by(lambda x: x)
    # Should be QFractionOrderedIterable which inherits from QFractionIterable
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(1), Fraction(2), Fraction(3)]

def test_order_by_descending_returns_qfraction_ordered_iterable() -> None:
    result = query([Fraction(1), Fraction(3), Fraction(2)]).as_fractions().order_by_descending(lambda x: x)
    # Should be QFractionOrderedIterable which inherits from QFractionIterable
    assert isinstance(result, QFractionIterable)
    assert list(result) == [Fraction(3), Fraction(2), Fraction(1)]

def test_to_list_returns_qfraction_list() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().to_list()
    assert isinstance(result, QFractionList)
    assert list(result) == [Fraction(1), Fraction(2), Fraction(3)]

def test_to_sequence_returns_qfraction_sequence() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().to_sequence()
    assert isinstance(result, QFractionSequence)
    assert list(result) == [Fraction(1), Fraction(2), Fraction(3)]

def test_to_tuple_returns_tuple_of_fractions() -> None:
    result: tuple[Fraction, ...] = query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().to_tuple()
    assert isinstance(result, tuple)
    assert result == (Fraction(1), Fraction(2), Fraction(3))

def test_to_set_returns_qfraction_set() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().to_set()
    assert isinstance(result, QFractionSet)
    assert set(result) == {Fraction(1), Fraction(2), Fraction(3)}

def test_to_frozenset_returns_qfraction_frozenset() -> None:
    result = query([Fraction(1), Fraction(2), Fraction(3)]).as_fractions().to_frozenset()
    assert isinstance(result, QFractionFrozenSet)
    assert set(result) == {Fraction(1), Fraction(2), Fraction(3)}

def test_qfraction_iterable_implementation_constructor() -> None:
    def factory() -> Iterable[Fraction]:
        return iter([Fraction(1), Fraction(2), Fraction(3)])

    impl = QFractionIterableImplementation(factory)
    assert list(impl) == [Fraction(1), Fraction(2), Fraction(3)]
    assert isinstance(impl, QFractionIterable)
