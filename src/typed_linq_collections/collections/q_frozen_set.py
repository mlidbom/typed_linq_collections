from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING, Never, Self, override

from typed_linq_collections.q_iterable import QIterable

if TYPE_CHECKING:
    from collections.abc import Iterable

class QFrozenSet[TItem](frozenset[TItem], QIterable[TItem]):
    """An immutable set that extends Python's built-in frozenset with LINQ-style query operations.

    QFrozenSet provides all the functionality of Python's standard frozenset while also implementing
    the full QIterable interface for LINQ-style operations. It maintains all the performance
    characteristics and immutability of the built-in frozenset, making it a drop-in replacement
    that adds powerful querying capabilities.

    Being immutable, QFrozenSet instances are hashable and can be used as dictionary keys or
    stored in other sets. All LINQ operations return new collections rather than modifying
    the original.

    Inheritance:
    - Inherits from frozenset[TItem] for all standard immutable set operations and seamless interoperability with the built-in frozenset
    - Implements QIterable[TItem] for LINQ-style query operations

    Key Features:
    - **Immutable**: Cannot be modified after creation, ensuring thread safety
    - **Hashable**: Can be used as dictionary keys or set elements
    """
    __slots__: tuple[str, ...] = ()

    def __new__(cls, *sources: Iterable[TItem]) -> QFrozenSet[TItem]:
        """Creates a new QFrozenSet with unique elements from one or more iterables.

        Duplicate elements in the input iterables are automatically removed, maintaining
        only unique values as per standard frozenset behavior. When multiple sources are
        provided, they are concatenated in order before uniqueness is applied.

        Args:
            *sources: One or more iterables of elements to initialize the frozenset with.
                      Duplicates will be automatically removed.
                      Defaults to an empty sequence when no arguments provided.

        Returns:
            A new QFrozenSet instance containing the unique elements from the iterables.

        Examples:
            >>> QFrozenSet([1, 2, 3])
            frozenset({1, 2, 3})
            >>> QFrozenSet([1, 2], [2, 3], [3, 4])
            frozenset({1, 2, 3, 4})
            >>> # Combining subtypes into base type
            >>> dogs: QFrozenSet[Dog] = ...
            >>> cats: QFrozenSet[Cat] = ...
            >>> all_animals: QFrozenSet[Animal] = QFrozenSet(dogs, cats)
        """
        if not sources:
            return super().__new__(cls)
        if len(sources) == 1:
            return super().__new__(cls, sources[0])
        return super().__new__(cls, chain(*sources))

    @override
    def _optimized_length(self) -> int: return len(self)

    # Binary operators
    @override
    def __or__(self, other: frozenset[TItem]) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        return type(self)(super().__or__(other))

    def __ror__(self, other: frozenset[TItem]) -> Self:
        return type(self)(super().__ror__(other))  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType, reportAttributeAccessIssue]

    @override
    def __and__(self, other: frozenset[TItem]) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        return type(self)(super().__and__(other))

    def __rand__(self, other: frozenset[TItem]) -> Self:
        return type(self)(super().__rand__(other))  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType, reportAttributeAccessIssue]

    @override
    def __sub__(self, other: frozenset[TItem]) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        return type(self)(super().__sub__(other))

    def __rsub__(self, other: frozenset[TItem]) -> Self:
        return type(self)(super().__rsub__(other))  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType, reportAttributeAccessIssue]

    @override
    def __xor__(self, other: frozenset[TItem]) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        return type(self)(super().__xor__(other))

    def __rxor__(self, other: frozenset[TItem]) -> Self:
        return type(self)(super().__rxor__(other))  # pyright: ignore[reportUnknownMemberType, reportUnknownArgumentType, reportAttributeAccessIssue]

    # Methods
    @override
    def copy(self) -> Self:
        return type(self)(super().copy())

    @override
    def union(self, *others: Iterable[TItem]) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        return type(self)(super().union(*others))

    @override
    def intersection(self, *others: Iterable[TItem]) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        return type(self)(super().intersection(*others))

    @override
    def difference(self, *others: Iterable[TItem]) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        return type(self)(super().difference(*others))

    @override
    def symmetric_difference(self, other: Iterable[TItem]) -> Self:
        return type(self)(super().symmetric_difference(other))

    _empty_set: QFrozenSet[Never]

    @staticmethod
    @override
    def empty() -> QFrozenSet[Never]:
        return QFrozenSet._empty_set


QFrozenSet._empty_set = QFrozenSet()  # pyright: ignore [reportGeneralTypeIssues, reportPrivateUsage]
