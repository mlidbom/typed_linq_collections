from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from typed_linq_collections.collections.numeric.q_int_types import QIntFrozenSet, QIntIterable, QIntIterableImplementation, QIntList, QIntSequence, QIntSet
from typed_linq_collections.q_errors import EmptyIterableError
from typed_linq_collections.q_iterable import query

if TYPE_CHECKING:
    from collections.abc import Iterable


def test_sum_returns_sum_of_the_values() -> None:
    assert query([1, 2, 3]).as_ints().sum() == 6

def test_sum_returns_zero_on_empty_collection() -> None:
    assert query([]).as_ints().sum() == 0

def test_min_returns_min_of_the_values() -> None:
    assert query([6, 2, 5, 3]).as_ints().min() == 2

def test_min_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_ints().min()

def test_max_returns_max_of_the_values() -> None:
    assert query([1, 5, 3]).as_ints().max() == 5

def test_max_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_ints().max()

def test_min_or_default_returns_min_of_the_values() -> None:
    assert query([6, 2, 5, 3]).as_ints().min_or_default() == 2

def test_min_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_ints().min_or_default() == 0

def test_max_or_default_returns_max_of_the_values() -> None:
    assert query([1, 5, 3]).as_ints().max_or_default() == 5

def test_max_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_ints().max_or_default() == 0

def test_average_returns_average_of_the_values() -> None:
    assert query([1, 2, 3]).as_ints().average() == 2.0

def test_average_throws_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_ints().average()

def test_average_or_default_returns_average_of_the_values() -> None:
    assert query([1, 2, 3]).as_ints().average_or_default() == 2.0

def test_average_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_ints().average_or_default() == 0.0

def test_where_returns_qint_iterable() -> None:
    result = query([1, 2, 3, 4]).as_ints().where(lambda x: x > 2)
    assert isinstance(result, QIntIterable)
    assert list(result) == [3, 4]

def test_where_not_none_returns_qint_iterable() -> None:
    result = query([1, 2, 3]).as_ints().where_not_none()
    assert isinstance(result, QIntIterable)
    assert list(result) == [1, 2, 3]

def test_distinct_returns_qint_iterable() -> None:
    result = query([1, 2, 2, 3]).as_ints().distinct()
    assert isinstance(result, QIntIterable)
    assert set(result) == {1, 2, 3}

def test_distinct_by_returns_qint_iterable() -> None:
    result = query([1, -2, 3, -4]).as_ints().distinct_by(abs)
    assert isinstance(result, QIntIterable)
    assert len(list(result)) == 4  # All are distinct by absolute value

def test_take_returns_qint_iterable() -> None:
    result = query([1, 2, 3, 4]).as_ints().take(2)
    assert isinstance(result, QIntIterable)
    assert list(result) == [1, 2]

def test_take_while_returns_qint_iterable() -> None:
    result = query([1, 2, 3, 4]).as_ints().take_while(lambda x: x < 3)
    assert isinstance(result, QIntIterable)
    assert list(result) == [1, 2]

def test_take_last_returns_qint_iterable() -> None:
    result = query([1, 2, 3, 4]).as_ints().take_last(2)
    assert isinstance(result, QIntIterable)
    assert list(result) == [3, 4]

def test_skip_returns_qint_iterable() -> None:
    result = query([1, 2, 3, 4]).as_ints().skip(2)
    assert isinstance(result, QIntIterable)
    assert list(result) == [3, 4]

def test_skip_last_returns_qint_iterable() -> None:
    result = query([1, 2, 3, 4]).as_ints().skip_last(2)
    assert isinstance(result, QIntIterable)
    assert list(result) == [1, 2]

def test_reversed_returns_qint_iterable() -> None:
    result = query([1, 2, 3]).as_ints().reversed()
    assert isinstance(result, QIntIterable)
    assert list(result) == [3, 2, 1]

def test_concat_returns_qint_iterable() -> None:
    result = query([1, 2]).as_ints().concat([3, 4])
    assert isinstance(result, QIntIterable)
    assert list(result) == [1, 2, 3, 4]

def test_order_by_returns_qint_ordered_iterable() -> None:
    result = query([3, 1, 2]).as_ints().order_by(lambda x: x)
    # Should be QIntOrderedIterable which inherits from QIntIterable
    assert isinstance(result, QIntIterable)
    assert list(result) == [1, 2, 3]

def test_order_by_descending_returns_qint_ordered_iterable() -> None:
    result = query([1, 3, 2]).as_ints().order_by_descending(lambda x: x)
    # Should be QIntOrderedIterable which inherits from QIntIterable
    assert isinstance(result, QIntIterable)
    assert list(result) == [3, 2, 1]

def test_to_list_returns_qint_list() -> None:
    result = query([1, 2, 3]).as_ints().to_list()
    assert isinstance(result, QIntList)
    assert list(result) == [1, 2, 3]

def test_to_sequence_returns_qint_sequence() -> None:
    result = query([1, 2, 3]).as_ints().to_sequence()
    assert isinstance(result, QIntSequence)
    assert list(result) == [1, 2, 3]

def test_to_tuple_returns_tuple_of_ints() -> None:
    result: tuple[int, ...] = query([1, 2, 3]).as_ints().to_tuple()
    assert isinstance(result, tuple)
    assert result == (1, 2, 3)

def test_to_set_returns_qint_set() -> None:
    result = query([1, 2, 3]).as_ints().to_set()
    assert isinstance(result, QIntSet)
    assert set(result) == {1, 2, 3}

def test_to_frozenset_returns_qint_frozenset() -> None:
    result = query([1, 2, 3]).as_ints().to_frozenset()
    assert isinstance(result, QIntFrozenSet)
    assert set(result) == {1, 2, 3}

def test_qint_iterable_implementation_constructor() -> None:
    def factory() -> Iterable[int]:
        return iter([1, 2, 3])

    impl = QIntIterableImplementation(factory)
    assert list(impl) == [1, 2, 3]
    assert isinstance(impl, QIntIterable)
