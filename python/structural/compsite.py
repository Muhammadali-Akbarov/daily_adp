"""
The Composite design pattern is a structural design pattern that allows
you to compose objects into tree structures to represent part-whole hierarchies.
It lets you treat individual objects and compositions of objects uniformly,
making it easier to work with complex hierarchies.

usage:
    Graphics Systems:
        Representing shapes, where a shape can be a simple geometric
        figure (like a line or circle) or a complex composite shape
        made up of several simple shapes.

    File Systems:
        Representing files and directories as a tree structure.

    UI Components:
        Building complex user interfaces with nested components,
        such as windows containing panels containing buttons.
"""
import abc


class PaymentComponent(abc.ABC):
    """
    component abstract base class.
    """
    @abc.abstractmethod
    def p2p(self, amount) -> None:
        """
        the operation, should be implement
        """


class PaymeLeaf(PaymentComponent):
    """
    hese are the individual objects that do not have children in the hierarchy.
    they implement the operations defined by the Component interface.
    """
    FEE = 0.02

    def p2p(self, amount) -> float:
        """
        payme fee 0.2%
        """
        fee = amount * self.FEE
        finally_amount = amount + fee

        return f"finally amount with payme: {finally_amount}"


class PayzeLeaf(PaymentComponent):
    """
    hese are the individual objects that do not have children in the hierarchy.
    they implement the operations defined by the Component interface.
    """
    FEE = 0.01

    def p2p(self, amount) -> float:
        """
        payze fee 0.1%
        """
        fee = amount * self.FEE
        finally_amount = amount + fee

        return f"finally amunt with payze: {finally_amount}"


class UniPostLeaf(PaymentComponent):
    """
    hese are the individual objects that do not have children in the hierarchy.
    they implement the operations defined by the Component interface.
    """
    FEE = 0.0

    def p2p(self, amount) -> float:
        """
        uni-post fee 0.0%
        """
        fee = amount * self.FEE
        finally_amount = amount + fee

        return f"finally amunt with uni-post: {finally_amount}"


class PaymentComposite(PaymentComponent):
    """
    composite components.
    """
    def __init__(self):
        self.children = []
        self.result = []

    def add(self, component) -> None:
        """
        adding components.
        """
        self.children.append(component)

    def p2p(self, amount=None) -> float:
        for child in self.children:
            self.result.append(child.p2p(amount))

        print(f"the results of child classes: {self.result}")


if __name__ == "__main__":
    payme_leaf = PaymeLeaf()
    payze_leaf = PayzeLeaf()
    unipost_leaf = UniPostLeaf()

    composite = PaymentComposite()

    composite.add(payme_leaf)
    composite.add(payze_leaf)
    composite.add(unipost_leaf)

    # show results.
    composite.p2p(
        amount=100_000
    )
