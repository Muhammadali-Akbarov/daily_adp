"""
The Prototype design pattern is part of the creational patterns,
which deal with object creation mechanisms. It is particularly useful
in situations where the construction of objects is costly or complex.
The Prototype pattern lets you copy existing objects without making your
code dependent on their classes, thus reducing the complexity of creating new instances.

use cases:
    1) Useful in scenarios where you want to avoid repeating
        the initialization process that is costly or complex.

    2) Suitable for systems needing to be independent of how its objects are created,
        composed, and represented.

    interface: prototype
    methods: clone, and deep_clone.
"""
import copy
import typing

import unittest


class Car:
    """
    the car class.
    """
    def __init__(self, name: str) -> None:
        self.name = name


class Prototype:
    """
    the prototype class.
    """
    def clone(self):
        """
        Create a shallow copy of the object.
        """
        return copy.copy(self)

    def deep_clone(self):
        """
        Create a deep copy of the object.
        """
        return copy.deepcopy(self)


class ConcretePrototype(Prototype):
    """
    con create prototype class.
    usages:
        prototype = ConcretePrototype(obj=Car)
        cloned_prototype = prototype.clone()
        deep_cloned_prototype = prototype.deep_clone()
    """
    def __init__(self, obj: typing.Any) -> None:
        self.obj = obj


class TestPrototypePattern(unittest.TestCase):
    """
    Unit tests for the Prototype pattern implementation.
    """

    def test_shallow_clone(self) -> None:
        """
        the test shallow clone.
        """
        car = Car("Original Car")
        prototype = ConcretePrototype(obj=car)
        cloned_prototype = prototype.clone()

        self.assertIsNot(prototype, cloned_prototype)
        self.assertEqual(prototype.obj.name, cloned_prototype.obj.name)

    def test_deep_clone(self) -> None:
        """
        the test deep clone
        """
        car = Car("Original Car")
        prototype = ConcretePrototype(obj=car)
        deep_cloned_prototype = prototype.deep_clone()

        self.assertIsNot(prototype, deep_cloned_prototype)
        self.assertIsNot(prototype.obj, deep_cloned_prototype.obj)
        self.assertEqual(prototype.obj.name, deep_cloned_prototype.obj.name)


if __name__ == '__main__':
    unittest.main()
