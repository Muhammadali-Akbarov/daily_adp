"""
The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.
"""
import abc
import typing
import unittest
from io import StringIO
from unittest.mock import patch


class Payment(abc.ABC):
    """
    the adapter class.
    """
    @abc.abstractmethod
    def pay(self, amount) -> bool:
        """
        the pay abstract method
        """

        raise NotImplementedError(
            "not implemented yet!"
        )


class Credit:
    """
    the credit payment.
    """
    def pay_credit(self, amount) -> bool:
        """
        payment for a credit.
        """
        print(f"payment for credit: {amount}")
        return True


class Debt:
    """
    the debt payment.
    """
    def pay_debt(self, amount) -> bool:
        """
        payment for debt.
        """
        print(f"payment for debt: {amount}")
        return True


class Trip:
    """
    the trip payment.
    """
    def pay_trip(self, amount) -> bool:
        """
        the pay trip.
        """
        print(f"payment for trip: {amount}")
        return True


class PayAdapter(Payment):
    """
    the payment adapter.
    usage:
        credit = Credit()
        payment = PayAdapter(credit)
        payment.pay(amount=2000)

        debt = Debt()
        payment = PayAdapter(reason=debt)
        payment.pay(amount=1000)

        debt = Trip()
        payment = PayAdapter(reason=debt)
        payment.pay(amount=4000)
    """
    def __init__(self, reason: typing.Union[Credit, Debt, Trip]) -> None:
        self.reason = reason

    def pay(self, amount) -> bool | Exception:
        if isinstance(self.reason, Credit):
            return self.reason.pay_credit(amount)
        if isinstance(self.reason, Debt):
            return self.reason.pay_debt(amount)
        if isinstance(self.reason, Trip):
            return self.reason.pay_trip(amount)

        raise Exception(f"unknown reason: {self.reason}")


class TestPayment(unittest.TestCase):
    """
    the test payment.
    """
    def test_payment_abstract_method(self) -> None:
        """
        You cannot create an instance of an abstract class
        """
        # pylint: disable=E0110
        with self.assertRaises(TypeError):
            payment = Payment()
            payment.pay(1000)


class TestCredit(unittest.TestCase):
    """
    test credit payment.
    """
    def test_pay_credit(self) -> None:
        """
        test pay credit.
        """
        credit = Credit()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = credit.pay_credit(2000)
            self.assertTrue(result)
            self.assertEqual(mock_stdout.getvalue().strip(), "payment for credit: 2000")


class TestDebt(unittest.TestCase):
    """
    test debt payment.
    """
    def test_pay_debt(self) -> None:
        """
        test payment debt.
        """
        debt = Debt()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = debt.pay_debt(1000)
            self.assertTrue(result)
            self.assertEqual(mock_stdout.getvalue().strip(), "payment for debt: 1000")


class TestTrip(unittest.TestCase):
    """
    test debt payment.
    """
    def test_pay_trip(self) -> None:
        """
        test pay trip method.
        """
        trip = Trip()
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = trip.pay_trip(4000)
            self.assertTrue(result)
            self.assertEqual(mock_stdout.getvalue().strip(), "payment for trip: 4000")


class TestPayAdapter(unittest.TestCase):
    """
    test adapter payment.
    """
    def test_pay_adapter_credit(self) -> None:
        """
        test pay adapter credit method.
        """
        credit = Credit()
        payment_adapter = PayAdapter(credit)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = payment_adapter.pay(2000)
            self.assertTrue(result)
            self.assertEqual(mock_stdout.getvalue().strip(), "payment for credit: 2000")

    def test_pay_adapter_debt(self) -> None:
        """
        test pay adapter debt.
        """
        debt = Debt()
        payment_adapter = PayAdapter(debt)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = payment_adapter.pay(1000)
            self.assertTrue(result)
            self.assertEqual(mock_stdout.getvalue().strip(), "payment for debt: 1000")

    def test_pay_adapter_trip(self) -> None:
        """
        test pay adapter trip.
        """
        trip = Trip()
        payment_adapter = PayAdapter(trip)
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = payment_adapter.pay(4000)
            self.assertTrue(result)
            self.assertEqual(mock_stdout.getvalue().strip(), "payment for trip: 4000")

    def test_pay_adapter_unknown_reason(self) -> None:
        """
        test pay unknown reason
        """
        unknown_reason = "Unknown"
        payment_adapter = PayAdapter(unknown_reason)
        with self.assertRaises(Exception) as context:
            payment_adapter.pay(1000)
        self.assertEqual(str(context.exception), f"unknown reason: {unknown_reason}")


if __name__ == '__main__':
    unittest.main()
