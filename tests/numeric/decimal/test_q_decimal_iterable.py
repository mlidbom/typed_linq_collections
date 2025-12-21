from __future__ import annotations

from decimal import Decimal

import pytest

from typed_linq_collections.collections.numeric.q_decimal_types import QDecimalFrozenSet, QDecimalIterable, QDecimalIterableImplementation, QDecimalList, QDecimalSequence, QDecimalSet
from typed_linq_collections.q_errors import EmptyIterableError
from typed_linq_collections.q_iterable import query


def test_sum_returns_sum_of_the_values() -> None:
    assert query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().sum() == Decimal(6)

def test_sum_returns_zero_on_empty_collection() -> None:
    assert query([]).as_decimals().sum() == Decimal(0)

def test_min_returns_min_of_the_values() -> None:
    assert query([Decimal(6), Decimal(2), Decimal(5), Decimal(3)]).as_decimals().min() == Decimal(2)

def test_min_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_decimals().min()

def test_max_returns_max_of_the_values() -> None:
    assert query([Decimal(1), Decimal(5), Decimal(3)]).as_decimals().max() == Decimal(5)

def test_max_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_decimals().max()

def test_min_or_default_returns_min_of_the_values() -> None:
    assert query([Decimal(6), Decimal(2), Decimal(5), Decimal(3)]).as_decimals().min_or_default() == Decimal(2)

def test_min_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_decimals().min_or_default() == Decimal(0)

def test_max_or_default_returns_max_of_the_values() -> None:
    assert query([Decimal(1), Decimal(5), Decimal(3)]).as_decimals().max_or_default() == Decimal(5)

def test_max_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_decimals().max_or_default() == Decimal(0)

def test_average_returns_average_of_the_values() -> None:
    assert query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().average() == Decimal(2)

def test_average_throws_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_decimals().average()

def test_average_or_default_returns_average_of_the_values() -> None:
    assert query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().average_or_default() == Decimal(2)

def test_average_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_decimals().average_or_default() == Decimal(0)

def test_where_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3), Decimal(4)]).as_decimals().where(lambda x: x > Decimal(2))
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(3), Decimal(4)]

def test_where_not_none_returns_qdecimal_iterable() -> None:
    # Create a mixed-type collection first, then convert to decimals, then call where_not_none
    # This tests the where_not_none override method on QDecimalIterable
    result = query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().where_not_none()
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(1), Decimal(2), Decimal(3)]

def test_distinct_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(2), Decimal(3)]).as_decimals().distinct()
    assert isinstance(result, QDecimalIterable)
    assert set(result) == {Decimal(1), Decimal(2), Decimal(3)}

def test_distinct_by_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(-2), Decimal(3), Decimal(-4)]).as_decimals().distinct_by(abs)
    assert isinstance(result, QDecimalIterable)
    assert len(list(result)) == 4  # All are distinct by absolute value

def test_take_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3), Decimal(4)]).as_decimals().take(2)
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(1), Decimal(2)]

def test_take_while_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3), Decimal(4)]).as_decimals().take_while(lambda x: x < Decimal(3))
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(1), Decimal(2)]

def test_take_last_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3), Decimal(4)]).as_decimals().take_last(2)
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(3), Decimal(4)]

def test_skip_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3), Decimal(4)]).as_decimals().skip(2)
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(3), Decimal(4)]

def test_skip_last_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3), Decimal(4)]).as_decimals().skip_last(2)
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(1), Decimal(2)]

def test_reversed_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().reversed()
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(3), Decimal(2), Decimal(1)]

def test_concat_returns_qdecimal_iterable() -> None:
    result = query([Decimal(1), Decimal(2)]).as_decimals().concat([Decimal(3), Decimal(4)])
    assert isinstance(result, QDecimalIterable)
    assert list(result) == [Decimal(1), Decimal(2), Decimal(3), Decimal(4)]

def test_to_list_returns_qdecimal_list() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().to_list()
    assert isinstance(result, QDecimalList)
    assert list(result) == [Decimal(1), Decimal(2), Decimal(3)]

def test_to_sequence_returns_qdecimal_sequence() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().to_sequence()
    assert isinstance(result, QDecimalSequence)
    assert list(result) == [Decimal(1), Decimal(2), Decimal(3)]

def test_to_tuple_returns_tuple_of_decimals() -> None:
    result: tuple[Decimal, ...] = query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().to_tuple()
    assert isinstance(result, tuple)
    assert result == (Decimal(1), Decimal(2), Decimal(3))

def test_to_set_returns_qdecimal_set() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().to_set()
    assert isinstance(result, QDecimalSet)
    assert set(result) == {Decimal(1), Decimal(2), Decimal(3)}

def test_to_frozenset_returns_qdecimal_frozenset() -> None:
    result = query([Decimal(1), Decimal(2), Decimal(3)]).as_decimals().to_frozenset()
    assert isinstance(result, QDecimalFrozenSet)
    assert set(result) == {Decimal(1), Decimal(2), Decimal(3)}

def test_qdecimal_iterable_implementation_constructor() -> None:
    impl = QDecimalIterableImplementation(lambda: (Decimal(1), Decimal(2), Decimal(3)))
    assert list(impl) == [Decimal(1), Decimal(2), Decimal(3)]
    assert isinstance(impl, QDecimalIterable)
