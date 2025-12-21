from __future__ import annotations

from typing import TYPE_CHECKING, Self, override

from typed_linq_collections.collections.q_dict import QDict

if TYPE_CHECKING:
    from collections.abc import Iterable


class QKeyInterningDict[TValue](QDict[str, TValue]):
    """A specialized QDict that automatically interns all string keys before storing them.

    String interning is a method of storing only one copy of each distinct string value.
    This can save memory when the same string keys are used repeatedly across multiple
    dictionaries, and can make key lookups faster (since interned strings can be compared
    by identity rather than value).

    All string keys added to this dictionary are automatically interned using Python's
    sys.intern() function. This applies to keys added via any method: initialization,
    __setitem__, update, setdefault, etc.

    Inheritance:
    - Inherits from QDict[str, TValue], providing all dictionary operations with automatic key interning
    - Maintains all LINQ-style query operations from QIterable on the keys

    Examples:
        >>> qdict = QKeyInterningDict([("name", "Alice"), ("city", "NYC")])
        >>> # All stored keys are interned
        >>> "name" in qdict  # Uses interned comparison
        True
        >>> qdict["country"] = "USA"
        >>> # "country" is automatically interned before storage
    """
    __slots__: tuple[str, ...] = ()

    @override
    def __init__(self, elements: Iterable[tuple[str, TValue]] = ()) -> None:
        """Initializes a new QKeyInterningDict with interned keys from the given iterable.

        All string keys in the input iterable are automatically interned before being added
        to the dictionary.

        Args:
            elements: An iterable of (key, value) tuples to initialize the dictionary with.
                     All keys will be interned automatically.
                     Defaults to an empty sequence.
        """
        super().__init__(self._intern_keys(elements))

    @staticmethod
    def _intern_keys(elements: Iterable[tuple[str, TValue]]) -> Iterable[tuple[str, TValue]]:
        """Interns all keys in the given iterable of key-value pairs.

        Args:
            elements: An iterable of (key, value) tuples.

        Returns:
            An iterable of (interned_key, value) tuples.
        """
        import sys
        return ((sys.intern(key), value) for key, value in elements)

    @override
    def __setitem__(self, key: str, value: TValue) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Sets the value for an interned version of the key.

        Args:
            key: The string key to intern and use.
            value: The value to associate with the key.
        """
        import sys
        super().__setitem__(sys.intern(key), value)

    @override
    def __delitem__(self, key: str) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Deletes the value associated with the interned version of the key.

        Args:
            key: The string key to intern and delete.
        """
        import sys
        super().__delitem__(sys.intern(key))

    @override
    def __getitem__(self, key: str) -> TValue:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Gets the value associated with the interned version of the key.

        Args:
            key: The string key to intern and look up.

        Returns:
            The value associated with the key.
        """
        import sys
        return super().__getitem__(sys.intern(key))

    @override
    def __contains__(self, key: object) -> bool:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Checks if the interned version of the key exists in the dictionary.

        Args:
            key: The key to check for.

        Returns:
            True if the key exists in the dictionary, False otherwise.
        """
        import sys
        if isinstance(key, str):
            return super().__contains__(sys.intern(key))
        return super().__contains__(key)

    @override
    def get(self, key: str, default: TValue | None = None) -> TValue | None:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Gets the value for an interned key, returning a default if not found.

        Args:
            key: The string key to intern and look up.
            default: The value to return if the key is not found.

        Returns:
            The value associated with the key, or the default value.
        """
        import sys
        return super().get(sys.intern(key), default)

    @override
    def setdefault(self, key: str, default: TValue | None = None) -> TValue | None:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Gets the value for an interned key, setting it to default if not present.

        Args:
            key: The string key to intern and look up/set.
            default: The value to set if the key is not found.

        Returns:
            The value associated with the key.
        """
        import sys
        return super().setdefault(sys.intern(key), default)

    @override
    def pop(self, key: str, *args: TValue) -> TValue:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Removes and returns the value for an interned key.

        Args:
            key: The string key to intern and remove.
            *args: Optional default value to return if key not found.

        Returns:
            The value associated with the key.
        """
        import sys
        return super().pop(sys.intern(key), *args)

    @override
    def update(self, *args: Iterable[tuple[str, TValue]] | dict[str, TValue], **kwargs: TValue) -> None:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Updates the dictionary with interned keys from the given mappings.

        Args:
            *args: Iterables of (key, value) tuples or dictionaries to update from.
            **kwargs: Keyword arguments to add to the dictionary.
        """
        import sys

        # Handle positional arguments
        for arg in args:
            if isinstance(arg, dict):
                for key, value in arg.items():
                    super().__setitem__(sys.intern(key), value)
            else:
                for key, value in arg:
                    super().__setitem__(sys.intern(key), value)

        # Handle keyword arguments
        for key, value in kwargs.items():
            super().__setitem__(sys.intern(key), value)

    @classmethod
    @override
    def fromkeys(cls, keys: Iterable[str], value: TValue | None = None) -> Self:  # pyright: ignore[reportIncompatibleMethodOverride]
        """Creates a new dictionary with interned keys from an iterable and values set to value.

        Args:
            keys: An iterable of string keys to intern.
            value: The value to set for all keys.

        Returns:
            A new QKeyInterningDict with the given keys.
        """
        import sys
        interned_keys = (sys.intern(key) for key in keys)
        result = cls()
        for key in interned_keys:
            result[key] = value  # type: ignore[assignment]
        return result
