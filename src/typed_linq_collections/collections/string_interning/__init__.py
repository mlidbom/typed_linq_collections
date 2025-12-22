"""String interning collections for memory-efficient string storage.

This module provides specialized collection classes that automatically intern string values,
reducing memory usage when the same strings are stored repeatedly.

Classes:
    QInterningList: A list that interns all string elements.
    QInterningStringSet: A set that interns all string elements.
    QKeyInterningDict: A dictionary that interns string keys.
    QKeyValueInterningDict: A dictionary that interns both string keys and values.
"""

from __future__ import annotations

from typed_linq_collections.collections.string_interning.q_interning_list import QInterningList
from typed_linq_collections.collections.string_interning.q_interning_string_set import QInterningStringSet
from typed_linq_collections.collections.string_interning.q_key_interning_dict import QKeyInterningDict
from typed_linq_collections.collections.string_interning.q_key_value_interning_dict import QKeyValueInterningDict

__all__ = [
    "QInterningList",
    "QInterningStringSet",
    "QKeyInterningDict",
    "QKeyValueInterningDict",
]
