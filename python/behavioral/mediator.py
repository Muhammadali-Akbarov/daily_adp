"""
The Mediator design pattern is a behavioral design pattern that
is used to reduce the complexity and dependencies between tightly-coupled
objects communicating directly with each other. In Python, as in other
object-oriented languages, the Mediator pattern is implemented by encapsulating
the interactions between a set of objects within a mediator object.
This pattern promotes loose coupling by keeping objects from referring
to each other explicitly and allows their interaction to be handled by a central mediator.
"""
import abc


class Mediator(abc.ABC):
    """
    abstract mediator.
    """
    @abc.abstractmethod
    def notify(self, sender, event) -> None:
        """
        abstract mediator notify.
        """


class Payment:
    """
    the payment component.
    """
    def pay(self):
        """
        the implementation of pay method.
        """
        print("payment was successfull")


class Driver:
    """
    the driver component.
    """
    def finish_trip(self):
        """
        the implementation of finish method.
        """
        print("trip finished successfully")


class ConcreteMediator(abc.ABC):
    """
    concrete mediator class.
    """
    def __init__(self, component_payment, component_driver) -> None:
        self._component_payment: Payment = component_payment
        self._component_driver: Driver = component_driver

    def notify(self, event) -> None:
        """
        the implementation of notify method.
        """
        if event == "driver":
            print("mediator reacts on driver and triggers following operations")
            self._component_driver.finish_trip()

        if event == "payment":
            print("mediator reacts on payment and triggers following operations")
            self._component_payment.pay()


if __name__ == "__main__":
    component_driver = Driver()
    component_payment = Payment()

    mediator = ConcreteMediator(
        component_driver=component_driver,
        component_payment=component_payment
    )

    mediator.notify(
        event="driver"
    )
    mediator.notify(
        event="payment"
    )
