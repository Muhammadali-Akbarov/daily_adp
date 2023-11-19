"""
The Singleton pattern is a design pattern that ensures a class has only
one instance and provides a global point of access to that instance.
It's often used in scenarios where exactly one object is needed to coordinate
actions across the system.
"""
import unittest

import colorama


class PaymeApi:
    """
    the payme provider api.
    """
    _instance = None

    def __init__(self, payme_id: str = None, payme_key: str = None) -> None:
        # pylint: disable=E0203
        if not self._initialized:
            self.payme_id = payme_id
            self.payme_key = payme_key
            self._initialized = True

    def __new__(cls, payme_id=None, payme_key=None) -> None:
        if cls._instance is None:
            cls._instance = super(PaymeApi, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def add_card(self) -> None:
        """
        cards.create method of payme JSONRPC
        """
        raise NotImplementedError(
            "not implemented yet."
        )


class PaymeApiTestCase(unittest.TestCase):
    """
    payme api test cases for checking singleton point.
    """
    def setUp(self) -> None:
        self.payme_api_first = PaymeApi(
            payme_id="782dc54f-a10c-44b8-a879-e92b12df55b5",
            payme_key="74f289a9-761c-4112-97db-c13d03e2f194"
        )
        self.payme_api_second = PaymeApi()

    def test_payme_api_singleton(self) -> None:
        """
        test objects point in memory
        """
        id_1 = hex(id(self.payme_api_first))
        id_2 = hex(id(self.payme_api_second))

        print(colorama.Fore.GREEN + f"address of payme_api_first {self.payme_api_first}")
        print(colorama.Fore.GREEN + f"address of payme_api_first {self.payme_api_second}")

        self.assertEqual(first=id_1, second=id_2)


if __name__ == "__main__":
    unittest.main()
