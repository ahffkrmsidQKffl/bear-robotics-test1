from atm.models import Account, Card
from atm.controller import ATMController

if __name__ == "__main__":
    # 카드, 계좌 세팅
    checking = Account("checking", 300)
    card = Card("9999", "1234", {"checking": checking})
    atm = ATMController(cards={"9999": card})

    # 카드 삽입
    card_number = input("📇 카드 번호를 입력하세요: ")
    atm.insert_card(card_number)

    # PIN 입력
    pin = input("🔐 PIN 번호를 입력하세요: ")
    atm.enter_pin(pin)

    # 계좌 선택
    account_type = input("🏦 계좌 유형을 입력하세요 (checking): ")
    atm.select_account(account_type)

    # 잔액 확인
    print("💰 현재 잔액:", atm.get_balance())

    # 입금
    deposit = int(input("➕ 입금할 금액을 입력하세요: "))
    atm.deposit(deposit)
    print("입금 후 잔액:", atm.get_balance())

    # 출금
    withdraw = int(input("➖ 출금할 금액을 입력하세요: "))
    atm.withdraw(withdraw)
    print("출금 후 잔액:", atm.get_balance())