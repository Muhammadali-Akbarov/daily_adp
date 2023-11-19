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

    def __init__(self, payme_id: str, payme_key: str):
        self.payme_id = payme_id
        self.payme_key = payme_key

    def add_card(self) -> None:
        """
        cards.create method
        """
        raise NotImplementedError(
            "not implemented yet."
        )


class PaymeApiTestCase(unittest.TestCase):
    """
    payme api test cases for checking simple init.
    """
    def setUp(self) -> None:
        self.payme_api_first = PaymeApi(
            payme_id="782dc54f-a10c-44b8-a879-e92b12df55b5",
            payme_key="74f289a9-761c-4112-97db-c13d03e2f194"
        )
        self.payme_api_second = PaymeApi(
            payme_id="b760c177-f2dc-40fe-a5d2-d0e7ffab6de5",
            payme_key="792740c6-96fb-476a-acc0-a02ae1f65ce1"
        )

    def test_payme_api_singleton(self) -> None:
        """
        test objects point in memory
        """
        id_1 = hex(id(self.payme_api_first))
        id_2 = hex(id(self.payme_api_second))

        print(colorama.Fore.GREEN + f"address of payme_api_first {self.payme_api_first}")
        print(colorama.Fore.GREEN + f"address of payme_api_first {self.payme_api_second}")

        self.assertNotEqual(first=id_1, second=id_2)


if __name__ == "__main__":
    unittest.main()
