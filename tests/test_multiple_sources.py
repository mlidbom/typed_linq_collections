"""Tests for multiple sources (*sources) functionality in collection constructors."""
from __future__ import annotations

from typing import override

from typed_linq_collections.collections.q_frozen_set import QFrozenSet
from typed_linq_collections.collections.q_immutable_sequence import QImmutableSequence
from typed_linq_collections.collections.q_list import QList
from typed_linq_collections.collections.q_set import QSet
from typed_linq_collections.q_iterable import query


# Test classes for type variance scenarios
class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    @override
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Animal) and self.name == other.name
    @override
    def __hash__(self) -> int:
        return hash(self.name)

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# QSet tests
def test_q_set_multiple_sources() -> None:
    result = QSet([1, 2], [3, 4], [5, 6])
    assert len(result) == 6
    assert set(result) == {1, 2, 3, 4, 5, 6}

def test_q_set_multiple_sources_with_duplicates() -> None:
    result = QSet([1, 2], [2, 3], [3, 4])
    assert len(result) == 4
    assert set(result) == {1, 2, 3, 4}

def test_q_set_single_source() -> None:
    result = QSet([1, 2, 3])
    assert len(result) == 3
    assert set(result) == {1, 2, 3}

def test_q_set_empty() -> None:
    result = QSet[int]()
    assert len(result) == 0

def test_q_set_with_heterogeneous_subtypes() -> None:
    dogs: QSet[Dog] = QSet([Dog("Buddy"), Dog("Max")])
    cats: QSet[Cat] = QSet([Cat("Whiskers"), Cat("Mittens")])

    # Combine into base type
    all_animals: QSet[Animal] = QSet(dogs, cats)

    assert len(all_animals) == 4
    names = {animal.name for animal in all_animals}
    assert names == {"Buddy", "Max", "Whiskers", "Mittens"}

# QList tests
def test_q_list_multiple_sources() -> None:
    result = QList([1, 2], [3, 4], [5, 6])
    assert len(result) == 6
    assert result.to_list() == [1, 2, 3, 4, 5, 6]

def test_q_list_multiple_sources_preserves_order() -> None:
    result = QList([1, 2], [3, 4], [5, 6])
    assert result[0] == 1
    assert result[3] == 4
    assert result[5] == 6

def test_q_list_multiple_sources_preserves_duplicates() -> None:
    result = QList([1, 2], [2, 3], [3, 4])
    assert len(result) == 6
    assert result.to_list() == [1, 2, 2, 3, 3, 4]

def test_q_list_single_source() -> None:
    result = QList([1, 2, 3])
    assert len(result) == 3
    assert result.to_list() == [1, 2, 3]

def test_q_list_empty() -> None:
    result = QList[int]()
    assert len(result) == 0

def test_q_list_with_heterogeneous_subtypes() -> None:
    dogs: QList[Dog] = QList([Dog("Buddy"), Dog("Max")])
    cats: QList[Cat] = QList([Cat("Whiskers"), Cat("Mittens")])
    more_dogs: QList[Dog] = QList([Dog("Rex")])

    # Combine into base type
    all_animals: QList[Animal] = QList(dogs, cats, more_dogs)

    assert len(all_animals) == 5
    assert all_animals[0].name == "Buddy"
    assert all_animals[2].name == "Whiskers"
    assert all_animals[4].name == "Rex"

# QFrozenSet tests
def test_q_frozen_set_multiple_sources() -> None:
    result = QFrozenSet([1, 2], [3, 4], [5, 6])
    assert len(result) == 6
    assert set(result) == {1, 2, 3, 4, 5, 6}

def test_q_frozen_set_multiple_sources_with_duplicates() -> None:
    result = QFrozenSet([1, 2], [2, 3], [3, 4])
    assert len(result) == 4
    assert set(result) == {1, 2, 3, 4}

def test_q_frozen_set_single_source() -> None:
    result = QFrozenSet([1, 2, 3])
    assert len(result) == 3
    assert set(result) == {1, 2, 3}

def test_q_frozen_set_empty() -> None:
    result = QFrozenSet[int]()
    assert len(result) == 0

def test_q_frozen_set_with_heterogeneous_subtypes() -> None:
    dogs: QFrozenSet[Dog] = QFrozenSet([Dog("Buddy"), Dog("Max")])
    cats: QFrozenSet[Cat] = QFrozenSet([Cat("Whiskers"), Cat("Mittens")])

    # Combine into base type
    all_animals: QFrozenSet[Animal] = QFrozenSet(dogs, cats)

    assert len(all_animals) == 4
    names = {animal.name for animal in all_animals}
    assert names == {"Buddy", "Max", "Whiskers", "Mittens"}

# QImmutableSequence tests
def test_q_immutable_sequence_multiple_sources() -> None:
    result = QImmutableSequence([1, 2], [3, 4], [5, 6])
    assert len(result) == 6
    assert list(result) == [1, 2, 3, 4, 5, 6]

def test_q_immutable_sequence_multiple_sources_preserves_order() -> None:
    result = QImmutableSequence([1, 2], [3, 4], [5, 6])
    assert result[0] == 1
    assert result[3] == 4
    assert result[5] == 6

def test_q_immutable_sequence_single_source() -> None:
    result = QImmutableSequence([1, 2, 3])
    assert len(result) == 3
    assert list(result) == [1, 2, 3]

def test_q_immutable_sequence_empty() -> None:
    result = QImmutableSequence[int]()
    assert len(result) == 0

def test_q_immutable_sequence_with_heterogeneous_subtypes() -> None:
    dogs = QImmutableSequence([Dog("Buddy"), Dog("Max")])
    cats = QImmutableSequence([Cat("Whiskers"), Cat("Mittens")])

    # Combine into base type
    all_animals: QImmutableSequence[Animal] = QImmutableSequence(dogs, cats)

    assert len(all_animals) == 4
    assert all_animals[0].name == "Buddy"
    assert all_animals[2].name == "Whiskers"

# query() function tests
def test_query_multiple_sources() -> None:
    result = query([1, 2], [3, 4], [5, 6])
    assert result.to_list() == [1, 2, 3, 4, 5, 6]

def test_query_multiple_sources_preserves_order() -> None:
    result = query([1, 2], [3, 4], [5, 6])
    items = result.to_list()
    assert items[0] == 1
    assert items[3] == 4
    assert items[5] == 6

def test_query_multiple_sources_preserves_duplicates() -> None:
    result = query([1, 2], [2, 3], [3, 4])
    assert result.to_list() == [1, 2, 2, 3, 3, 4]

def test_query_single_source() -> None:
    result = query([1, 2, 3])
    assert result.to_list() == [1, 2, 3]

def test_query_with_heterogeneous_subtypes() -> None:
    dogs = QSet([Dog("Buddy"), Dog("Max")])
    cats = QSet([Cat("Whiskers"), Cat("Mittens")])

    # Combine into base type query
    all_animals = query(dogs, cats)

    count = all_animals.qcount()
    assert count == 4

# Mixed collection types
def test_mixed_collection_types_in_q_list() -> None:
    # QList can accept different collection types
    set_data = {1, 2, 3}
    list_data = [4, 5, 6]
    tuple_data = (7, 8, 9)

    result = QList(set_data, list_data, tuple_data)
    assert len(result) == 9
    # Set order is not guaranteed, but total count should be 9

def test_mixed_collection_types_in_q_set() -> None:
    # QSet can accept different collection types
    set_data = {1, 2, 3}
    list_data = [2, 3, 4]
    tuple_data = (3, 4, 5)

    result = QSet(set_data, list_data, tuple_data)
    assert len(result) == 5
    assert set(result) == {1, 2, 3, 4, 5}
