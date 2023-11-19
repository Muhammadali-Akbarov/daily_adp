"""
The Bridge design pattern in Python is a structural pattern that
separates an object's abstraction (i.e., its high-level logic)
from its implementation (i.e., its low-level details) so that they can vary independently.
This separation allows you to change and extend the implementations without affecting
the abstraction or high-level code.
"""
import abc


class Implementor(abc.ABC):
    """
    abcstrac implementor class.
    """
    @abc.abstractmethod
    def operation(self) -> None:
        """
        abstract operation.
        """
        raise NotImplementedError(
            "not implemented yet!"
        )


class ConcreteImplementorA(Implementor):
    """
    way to to implement.
    """
    def operation(self) -> str:
        print("implemented with way a")
        return "implemented with way a"


class ConcreteImplementorB(Implementor):
    """
    way to to implement.
    """
    def operation(self) -> str:
        print("implemented with way b")
        return "implemented with way b"


class Abstraction:
    """
    abstraction class.

    usages:
        impl_a = ConcreteImplementorA()
        abstraction1 = ConcreteAbstraction1(impl_a)
        print(abstraction1.operation())
    """
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self) -> str:
        """
        the operation
        """
        return f"Abstraction operation using {self.implementor.operation()}"


class ConcreteAbstraction1(Abstraction):
    """
    concrete abstraction class.
    """


class ConcreteAbstraction2(Abstraction):
    """
    concrete abstraction class.
    """
