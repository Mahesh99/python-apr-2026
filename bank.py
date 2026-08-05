class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner      = owner        # public
        self._bank_name = "PramanicusBank"  # protected
        self.__balance  = balance      # private
        self.__pin      = 1234        # private

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Wrong PIN!")
            return
        if amount > self.__balance:
            print("Insufficient funds")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance   # controlled read access

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())      # 1500
# print(acc.__balance)        ← AttributeError
# print(acc._BankAccount__balance)  ← works (name mangling)