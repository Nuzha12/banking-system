from account import Account


class SavingsAccount(Account):

    INTEREST_RATE = 0.03

    def __init__(self, account_no, balance, branch, user, atm_card_no):
        super().__init__(account_no, balance, branch, user)
        self.atm_card_no = atm_card_no

    def add_interest(self) -> None:
        self.balance += self.balance * self.INTEREST_RATE
