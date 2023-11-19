"""
The Template Method design pattern is a behavioral pattern
that defines the skeleton of an algorithm in a method,
deferring some steps to subclasses. This pattern lets subclasses
redefine certain steps of an algorithm without changing the algorithm's structure.
It's particularly useful when there is a common workflow or series of steps,
but some steps may vary in their implementation across different contexts or subclasses.
"""
import abc


class PaymentProcessor(abc.ABC):
    """
    the payment processor template.
    """
    def process_payment(self, amount) -> None:
        """
        the template methods
        """
        self.authenticate()
        self.validate()
        self.create_check(amount)
        self.pay_check(amount)

    def authenticate(self):
        """
        Common step for authentication (can be overridden if necessary)
        """
        print("Authentication successful.")

    def validate(self):
        """
        Common step for validation (can be overridden if necessary)
        """
        print("Validation successful.")

    @abc.abstractmethod
    def create_check(self, amount):
        """
        create check method.
        """

    @abc.abstractmethod
    def pay_check(self, amount):
        """
        pay check method.
        """

    def hook(self):
        """
        override this method in your child classe
        """


class Payme(PaymentProcessor):
    """
    implementation of payment processor via payme
    """
    def create_check(self, amount):
        print(f"creating check with Payme amount: {amount}")

    def pay_check(self, amount):
        print(f"paying check with Payme amount: {amount}")


class Payze(PaymentProcessor):
    """
    implementation of payment processor via payme
    """
    def create_check(self, amount):
        print(f"creating check with Payze amount: {amount}")

    def pay_check(self, amount):
        print(f"paying check with Payze amount: {amount}")


class UniPost(PaymentProcessor):
    """
    implementation of payment processor via payme
    """
    def create_check(self, amount):
        print(f"creating check with UniPost amount: {amount}")

    def pay_check(self, amount):
        print(f"paying check with UniPost amount: {amount}")

    def validate(self):
        print("Validation successfull using UniPost")


def client_code(payment_processor: PaymentProcessor, amount: float):
    """
    client code for payment processor.
    """
    payment_processor.process_payment(amount)


if __name__ == "__main__":
    client_code(Payme(), 100)
    client_code(Payze(), 100)
    client_code(UniPost(), 100)
