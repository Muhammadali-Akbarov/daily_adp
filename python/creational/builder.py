"""
The Builder design pattern is a creational pattern that
provides a flexible solution to construct complex objects.
It's particularly useful when an object needs to be created with
many optional and required configurations.
The Builder pattern separates the construction of a complex object from
its representation, making it possible to use the same construction process
to create different representations.

Use cases:
    1) Used for constructing complex objects with multiple optional
        and mandatory fields or properties, like constructing GUI elements,
            complex documents, or various types of composite objects.

    2) Enhances readability and maintainability, especially when creating
        an object with numerous properties, some of which may be optional.
"""
import unittest


class PaymentProvider:
    """
    The abstract payment provider class.
    """
    def __init__(self) -> None:
        self.provider_name = None
        self.is_global = None

    def get_provider_name(self) -> str:
        """
        Get provider name method.
        """
        return self.provider_name

    def get_is_global(self) -> bool:
        """
        Get is_global method.
        """
        return self.is_global


class PaymentProviderBuilder:
    """
    The payment provider builder class.
    """
    def __init__(self) -> None:
        self.provider = PaymentProvider()

    def set_payment_provider(self, provider_name: str) -> 'PaymentProviderBuilder':
        """
        The payment provider setter that sets the provider name for abstract payment provider.
        """
        self.provider.provider_name = provider_name
        return self

    def set_is_global(self, is_global: bool) -> 'PaymentProviderBuilder':
        """
        Is global payment provider setter.
        """
        self.provider.is_global = is_global
        return self

    def build(self) -> PaymentProvider:
        """
        The payment provider builder method.
        """
        return self.provider


class PaymentDirector:
    """
    The payment director.
    """
    def construct_payme_provider(self, builder: PaymentProviderBuilder) -> PaymentProvider:
        """
        The payment director constructor that returns a new instance of the payment provider.
        usage:
            director = PaymentDirector()
            builder = PaymentProviderBuilder()
            payme = director.construct_payme_provider(builder)
        """
        builder.set_payment_provider(provider_name="payme").set_is_global(is_global=False)
        return builder.build()

    def construct_payze_provider(self, builder: PaymentProviderBuilder) -> PaymentProvider:
        """
        The payment director constructor that returns a new instance of the payment provider.

        usage:
            director = PaymentDirector()
            builder = PaymentProviderBuilder()
            payze = director.construct_payze_provider(builder)
        """
        builder.set_payment_provider(provider_name="payze").set_is_global(is_global=True)
        return builder.build()


class TestPaymentProvider(unittest.TestCase):
    """
    Unit tests for the PaymentProvider class.
    """
    def test_get_provider_name(self) -> None:
        """
        test the get provider name
        """
        provider = PaymentProvider()
        provider.provider_name = "TestProvider"
        self.assertEqual(provider.get_provider_name(), "TestProvider")

    def test_get_is_global(self) -> None:
        """
        test the get_is_global method.
        """
        provider = PaymentProvider()
        provider.is_global = True
        self.assertTrue(provider.get_is_global())


class TestPaymentProviderBuilder(unittest.TestCase):
    """
    Unit tests for the PaymentProviderBuilder class.
    """
    def test_build_payment_provider(self) -> None:
        """
        test the build payment provider.
        """
        builder = PaymentProviderBuilder()
        provider = builder.set_payment_provider("TestProvider").set_is_global(True).build()
        self.assertIsInstance(provider, PaymentProvider)
        self.assertEqual(provider.get_provider_name(), "TestProvider")
        self.assertTrue(provider.get_is_global())


class TestPaymentDirector(unittest.TestCase):
    """
    Unit tests for the PaymentDirector class.
    """
    def test_construct_payme_provider(self) -> None:
        """
        test construct payme provider.
        """
        director = PaymentDirector()
        builder = PaymentProviderBuilder()
        provider = director.construct_payme_provider(builder)
        self.assertEqual(provider.get_provider_name(), "payme")
        self.assertFalse(provider.get_is_global())

    def test_construct_payze_provider(self) -> None:
        """
        test construct payze provider.
        """
        director = PaymentDirector()
        builder = PaymentProviderBuilder()
        provider = director.construct_payze_provider(builder)
        self.assertEqual(provider.get_provider_name(), "payze")
        self.assertTrue(provider.get_is_global())


if __name__ == '__main__':
    unittest.main()
