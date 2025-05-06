class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance.copy()

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._is_valid_account(account1) or not self._is_valid_account(account2):
            return False
        if self.accounts[account1 - 1] < money:
            return False
        self.accounts[account1 - 1] -= money
        self.accounts[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        self.accounts[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid_account(account):
            return False
        if self.accounts[account - 1] < money:
            return False
        self.accounts[account - 1] -= money
        return True

    def _is_valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.accounts)