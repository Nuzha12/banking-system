from account import Account


class CurrentAccount(Account):


    def __init__(self, account_no, balance, branch, user, cheque_ids: list):
        super().__init__(account_no, balance, branch, user)
        self.cheque_ids = cheque_ids

    def add_cheque_id(self, cheque_id) -> None:
        self.cheque_ids.append(cheque_id)

    def search_cheque_id(self, cheque_id) -> bool:
        return cheque_id in self.cheque_ids
