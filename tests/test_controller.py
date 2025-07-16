import unittest
from atm.models import Account, Card
from atm.controller import ATMController

class TestATMController(unittest.TestCase):
    def setUp(self):
        checking = Account("checking", 100)
        savings = Account("savings", 200)
        card = Card("1234", "4321", {"checking": checking, "savings": savings})
        self.controller = ATMController(cards={"1234": card})

    def test_full_flow(self):
        self.controller.insert_card("1234")
        self.controller.enter_pin("4321")
        self.controller.select_account("checking")
        self.assertEqual(self.controller.get_balance(), 100)

        self.controller.deposit(50)
        self.assertEqual(self.controller.get_balance(), 150)

        self.controller.withdraw(20)
        self.assertEqual(self.controller.get_balance(), 130)

    def test_wrong_pin(self):
        self.controller.insert_card("1234")
        with self.assertRaises(ValueError):
            self.controller.enter_pin("1111")

    def test_invalid_account(self):
        self.controller.insert_card("1234")
        self.controller.enter_pin("4321")
        with self.assertRaises(ValueError):
            self.controller.select_account("investment")

if __name__ == "__main__":
    unittest.main()