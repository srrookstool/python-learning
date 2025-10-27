class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = initial_balance
    def __str__(self):
        return f"Account #{self.account_number} - Owner: {self.owner} - Balance: ${self.__balance:.2f}"
    def deposit(self, amount):
        if amount <= 0:
            print("ERROR: deposited amount invalid")
        else:
            self.__balance += amount
            return self.__balance
    def withdraw(self, amount):
        if self.__balance - amount >=0:
            self.__balance -= amount
            return self.__balance
        else: print("Insufficient funds")
    
    @property
    def balance(self):
        return self.__balance
    
class SavingsAccount(BankAccount):
    def __init__(self,account_number,owner,initial_balance,interest_rate):
        BankAccount.__init__(self,account_number,owner,initial_balance)
        if interest_rate <= 1:
            self.interest_rate = interest_rate
        else: self.interest_rate = (interest_rate / 100)
    def add_interest(self):
        interest = self.balance * self.interest_rate
        BankAccount.deposit(self, interest)
        return interest

    def withdraw(self, amount):
        if self.balance - amount < 100:
            print("Cannot go below $100 minimum")
        else: BankAccount.withdraw(self, amount)
        
        
# Test your code
if __name__ == "__main__":
# Regular account
    regular = BankAccount("1001", "Alice", 500)
    print(regular)
    regular.deposit(100)
    print(f"After deposit: ${regular.balance}")
    regular.withdraw(200)
    print(f"After withdrawal: ${regular.balance}")
    print("\n" + "="*40 + "\n")
    # Savings account
    savings = SavingsAccount("2001", "Bob", 1000, 0.02)
    print(savings)
    interest = savings.add_interest()
    print(f"Interest earned: ${interest:.2f}")
    print(f"New balance: ${savings.balance}")
    # Try to go below minimum
    savings.withdraw(950) # Should fail
    savings.withdraw(500) # Should work
    print(f"Final balance: ${savings.balance}")