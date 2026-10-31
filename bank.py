class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма должна быть положительной")
            return
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
            return
        self.balance -= amount
    def show_balance(self):
        print(f"Владелец: {self.owner}, баланс: {self.balance}")
account = BankAccount("Юра")
account.deposit(100)
account.withdraw(30)
account.withdraw(100)
account.deposit(-5)
account.show_balance()