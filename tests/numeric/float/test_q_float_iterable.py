from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from typed_linq_collections.collections.numeric.q_float_types import QFloatFrozenSet, QFloatIterable, QFloatIterableImplementation, QFloatList, QFloatSequence, QFloatSet
from typed_linq_collections.q_errors import EmptyIterableError
from typed_linq_collections.q_iterable import query

if TYPE_CHECKING:
    from collections.abc import Iterable


def test_sum_returns_sum_of_the_values() -> None:
    assert query([1.0, 2.0, 3.0]).as_floats().sum() == 6.0

def test_sum_returns_zero_on_empty_collection() -> None:
    assert query([]).as_floats().sum() == 0.0

def test_min_returns_min_of_the_values() -> None:
    assert query([6.0, 2.0, 5.0, 3.0]).as_floats().min() == 2.0

def test_min_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_floats().min()

def test_max_returns_max_of_the_values() -> None:
    assert query([1.0, 5.0, 3.0]).as_floats().max() == 5.0

def test_max_raises_empty_iterable_error_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_floats().max()

def test_min_or_default_returns_min_of_the_values() -> None:
    assert query([6.0, 2.0, 5.0, 3.0]).as_floats().min_or_default() == 2.0

def test_min_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_floats().min_or_default() == 0.0

def test_max_or_default_returns_max_of_the_values() -> None:
    assert query([1.0, 5.0, 3.0]).as_floats().max_or_default() == 5.0

def test_max_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_floats().max_or_default() == 0.0

def test_average_returns_average_of_the_values() -> None:
    assert query([1.0, 2.0, 3.0]).as_floats().average() == 2.0

def test_average_throws_on_empty_collection() -> None:
    with pytest.raises(EmptyIterableError):
        query([]).as_floats().average()

def test_average_or_default_returns_average_of_the_values() -> None:
    assert query([1.0, 2.0, 3.0]).as_floats().average_or_default() == 2.0

def test_average_or_default_returns_0_on_empty_collection() -> None:
    assert query([]).as_floats().average_or_default() == 0.0

def test_where_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 3.0, 4.0]).as_floats().where(lambda x: x > 2.0)
    assert isinstance(result, QFloatIterable)
    assert list(result) == [3.0, 4.0]

def test_where_not_none_returns_qfloat_iterable() -> None:
    # This tests the where_not_none override method on QFloatIterable
    result = query([1.0, 2.0, 3.0]).as_floats().where_not_none()
    assert isinstance(result, QFloatIterable)
    assert list(result) == [1.0, 2.0, 3.0]

def test_distinct_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 2.0, 3.0]).as_floats().distinct()
    assert isinstance(result, QFloatIterable)
    assert set(result) == {1.0, 2.0, 3.0}

def test_distinct_by_returns_qfloat_iterable() -> None:
    result = query([1.0, -2.0, 3.0, -4.0]).as_floats().distinct_by(abs)
    assert isinstance(result, QFloatIterable)
    assert len(list(result)) == 4  # All are distinct by absolute value

def test_take_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 3.0, 4.0]).as_floats().take(2)
    assert isinstance(result, QFloatIterable)
    assert list(result) == [1.0, 2.0]

def test_take_while_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 3.0, 4.0]).as_floats().take_while(lambda x: x < 3.0)
    assert isinstance(result, QFloatIterable)
    assert list(result) == [1.0, 2.0]

def test_take_last_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 3.0, 4.0]).as_floats().take_last(2)
    assert isinstance(result, QFloatIterable)
    assert list(result) == [3.0, 4.0]

def test_skip_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 3.0, 4.0]).as_floats().skip(2)
    assert isinstance(result, QFloatIterable)
    assert list(result) == [3.0, 4.0]

def test_skip_last_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 3.0, 4.0]).as_floats().skip_last(2)
    assert isinstance(result, QFloatIterable)
    assert list(result) == [1.0, 2.0]

def test_reversed_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0, 3.0]).as_floats().reversed()
    assert isinstance(result, QFloatIterable)
    assert list(result) == [3.0, 2.0, 1.0]

def test_concat_returns_qfloat_iterable() -> None:
    result = query([1.0, 2.0]).as_floats().concat([3.0, 4.0])
    assert isinstance(result, QFloatIterable)
    assert list(result) == [1.0, 2.0, 3.0, 4.0]

def test_order_by_returns_qfloat_ordered_iterable() -> None:
    result = query([3.0, 1.0, 2.0]).as_floats().order_by(lambda x: x)
    # Should be QFloatOrderedIterable which inherits from QFloatIterable
    assert isinstance(result, QFloatIterable)
    assert list(result) == [1.0, 2.0, 3.0]

def test_order_by_descending_returns_qfloat_ordered_iterable() -> None:
    result = query([1.0, 3.0, 2.0]).as_floats().order_by_descending(lambda x: x)
    # Should be QFloatOrderedIterable which inherits from QFloatIterable
    assert isinstance(result, QFloatIterable)
    assert list(result) == [3.0, 2.0, 1.0]

def test_to_list_returns_qfloat_list() -> None:
    result = query([1.0, 2.0, 3.0]).as_floats().to_list()
    assert isinstance(result, QFloatList)
    assert list(result) == [1.0, 2.0, 3.0]

def test_to_sequence_returns_qfloat_sequence() -> None:
    result = query([1.0, 2.0, 3.0]).as_floats().to_sequence()
    assert isinstance(result, QFloatSequence)
    assert list(result) == [1.0, 2.0, 3.0]

def test_to_tuple_returns_tuple_of_floats() -> None:
    result: tuple[float, ...] = query([1.0, 2.0, 3.0]).as_floats().to_tuple()
    assert isinstance(result, tuple)
    assert result == (1.0, 2.0, 3.0)

def test_to_set_returns_qfloat_set() -> None:
    result = query([1.0, 2.0, 3.0]).as_floats().to_set()
    assert isinstance(result, QFloatSet)
    assert set(result) == {1.0, 2.0, 3.0}

def test_to_frozenset_returns_qfloat_frozenset() -> None:
    result = query([1.0, 2.0, 3.0]).as_floats().to_frozenset()
    assert isinstance(result, QFloatFrozenSet)
    assert set(result) == {1.0, 2.0, 3.0}

def test_qfloat_iterable_implementation_constructor() -> None:
    def factory() -> Iterable[float]:
        return iter([1.0, 2.0, 3.0])

    impl = QFloatIterableImplementation(factory)
    assert list(impl) == [1.0, 2.0, 3.0]
    assert isinstance(impl, QFloatIterable)
