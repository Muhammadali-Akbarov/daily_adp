"""
The Chain of Responsibility pattern is a behavioral
design pattern that allows you to pass requests along a
chain of handlers. Each handler decides whether to process
the request or pass it to the next handler in the chain.
This pattern promotes loose coupling between the sender and receiver
of a request and allows you to add or modify processing steps dynamically.

key concepts:
    1) handler: This is an abstract class or interface that defines
        the interface for handling requests. It typically contains a
            reference to the next handler in the chain.

    2) concrete: These are concrete implementations of the Handler interface.
        Each ConcreteHandler decides whether to handle the request or
            pass it to the next handler in the chain.

    3) client: The Client is responsible for initiating requests.
        It sends requests to the first handler in the chain.

advantages of the chain of responsibility pattern:
    1) decoupling: The pattern decouples senders and receivers of requests,
        allowing them to vary independently.

    2) dynamic Chain: You can add or remove handlers at runtime,
        creating dynamic chains of responsibility.

    3) single Responsibility: Each handler has a single responsibility,
        making the code easier to maintain and extend.

example:
     a full ATM (Bankomat) program with the Chain of Responsibility
        pattern involves multiple classes and a user interface,
            which is beyond the scope of a single response. However,
                I can provide you with a simplified example that demonstrates
                    the concept of using the Chain of Responsibility pattern to get cash from an ATM.
"""
import abc


class CashDispenser(abc.ABC):
    """
    Handler interface
    """
    def __init__(self):
        self.next_handler = None  # Initialize next_handler to None

    @abc.abstractmethod
    def dispense(self, amount):
        """
        disperses the given amount.
        """


class HundredDollarDispenser(CashDispenser):
    """
    ConcreteHandler for $100 bills
    """
    def dispense(self, amount):
        num_bills = amount // 100
        remainder = amount % 100
        if num_bills > 0:
            print(f"Dispensing {num_bills} $100 bills")
        if remainder > 0 and self.next_handler:
            self.next_handler.dispense(remainder)


class FiftyDollarDispenser(CashDispenser):
    """
    ConcreteHandler for $50 bills
    """
    def dispense(self, amount):
        num_bills = amount // 50
        remainder = amount % 50
        if num_bills > 0:
            print(f"Dispensing {num_bills} $50 bills")
        if remainder > 0 and self.next_handler:
            self.next_handler.dispense(remainder)


class TwentyDollarDispenser(CashDispenser):
    """
    ConcreteHandler for $20 bills.
    """
    def dispense(self, amount):
        num_bills = amount // 20
        remainder = amount % 20
        if num_bills > 0:
            print(f"Dispensing {num_bills} $20 bills")
        if remainder > 0 and self.next_handler:
            self.next_handler.dispense(remainder)


class TenDollarDispenser(CashDispenser):
    """
    ConcreteHandler for $10 bills
    """
    def dispense(self, amount):
        num_bills = amount // 10
        remainder = amount % 10

        if num_bills > 0:
            print(f"Dispensing {num_bills} $10 bills")
        if remainder > 0 and self.next_handler:
            self.next_handler.dispense(remainder)


# Client code to set up the chain
if __name__ == "__main__":
    dispenser100 = HundredDollarDispenser()
    dispenser50 = FiftyDollarDispenser()
    dispenser20 = TwentyDollarDispenser()
    dispenser10 = TenDollarDispenser()

    # Link the handlers in the desired order
    dispenser100.next_handler = dispenser50
    dispenser50.next_handler = dispenser20
    dispenser20.next_handler = dispenser10

    dispenser100.dispense(230)
