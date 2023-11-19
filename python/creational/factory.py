"""
The Factory Method is a creational design pattern
that provides an interface for creating objects but
allows subclasses to alter the type of objects that will be created.
It is useful when you have a class that cannot anticipate
the class of objects it needs to create, or when a class wants to delegate
the responsibility of object creation to its subclasses.
"""
import abc

import unittest
from unittest.mock import patch

from io import StringIO


class IPayment(abc.ABC):
    """
    the payment abstract class.
    """
    @abc.abstractmethod
    def pay(self, amount: float) -> bool:
        """
        the pay abstract method.
        """
        raise NotImplementedError(
            "not implemented error."
        )


class Payme(IPayment):
    """
    the implementation of payment abstract class.
    """
    def pay(self, amount: float) -> bool:
        """
        the pay abstract method implementation.
        """
        print(f"payment processed with payme amount: {amount}")
        return True


class Payze(IPayment):
    """
    the implementation of payment abstract class.
    """
    def pay(self, amount: float) -> bool:
        """
        the pay abstract method implementation.
        """
        print(f"payment processed with payze amount: {amount}")
        return True


class UniPost(IPayment):
    """
    the implementation of payment abstract class.
    """
    def pay(self, amount: float) -> bool:
        """
        the pay abstract method implementation.
        """
        print(f"payment processed with uni-post amount: {amount}")
        return True


class Factory:
    """
    the factory implementation.
    """

    def get_payment(self, provider: str) -> IPayment:
        """
        the payment abstract method implementation.
        includes provider types ("payme", "payze", "unipost")
        """
        payment: IPayment = None

        if provider == "payme":
            payment = Payme()

        if provider == "payze":
            payment = Payze()

        if provider == "unipost":
            payment = UniPost()

        return payment


class TestPayment(unittest.TestCase):
    """
    the payment test.
    """
    def setUp(self):
        self.factory = Factory()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_payment_output(self, provider, amount, expected_output, mock_stdout) -> None:
        """
        the payment test output.
        """
        payment = self.factory.get_payment(provider)
        payment.pay(amount)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_payme_payment(self) -> None:
        """
        the payme payment test output.
        """
        self.assert_payment_output("payme", 15000, "payment processed with payme amount: 15000")

    def test_payze_payment(self) -> None:
        """
        the payze payment test output.
        """
        self.assert_payment_output("payze", 17000, "payment processed with payze amount: 17000")

    def test_unipost_payment(self) -> None:
        """
        the test unipost payment.
        """
        self.assert_payment_output("unipost", 18000, "payment processed with uni-post amount: 18000")


if __name__ == '__main__':
    unittest.main()
