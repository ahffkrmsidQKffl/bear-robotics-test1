
from atm.models import Card, Account

class ATMController:
    def __init__(self, cards: dict[str, Card]):
        self.cards = cards  # card_number: Card
        self.current_card = None
        self.authenticated = False
        self.selected_account = None

    def insert_card(self, card_number: str):
        if card_number not in self.cards:
            raise ValueError("Card not recognized")
        self.current_card = self.cards[card_number]

    def enter_pin(self, pin: str):
        if not self.current_card:
            raise RuntimeError("No card inserted")
        if self.current_card.pin != pin:
            raise ValueError("Incorrect PIN")
        self.authenticated = True

    def select_account(self, account_type: str):
        if not self.authenticated:
            raise RuntimeError("User not authenticated")
        if account_type not in self.current_card.accounts:
            raise ValueError("Account type not found")
        self.selected_account = self.current_card.accounts[account_type]

    def get_balance(self) -> int:
        self._ensure_account_selected()
        return self.selected_account.get_balance()

    def deposit(self, amount: int):
        self._ensure_account_selected()
        self.selected_account.deposit(amount)

    def withdraw(self, amount: int):
        self._ensure_account_selected()
        self.selected_account.withdraw(amount)

    def _ensure_account_selected(self):
        if not self.selected_account:
            raise RuntimeError("No account selected")