from user import User

class Account:
    """
    Base class for all account types.
    Demonstrates composition (Account has a User).
    """

    def __init__(self, account_no: str, balance: float, branch: str, user: User):
        self.account_no = account_no
        self.balance = balance
        self.branch = branch
        self.user = user

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise Exception("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdrawal(self, amount: float) -> None:
        if amount <= 0:
            raise Exception("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise Exception("Insufficient balance.")
        self.balance -= amount

    def check_balance(self) -> float:
        return self.balance
