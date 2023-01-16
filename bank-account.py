class BankAccount:
    def __init__(self,owner,deposit) -> None:
        self.owner = owner
        self.amt = deposit
        print(f"{owner} created a bank account with ${self.amt}")

    def deposit(self,deposit):
        self.amt+=deposit
        print(f"{self.owner} deposited ${deposit}\nAvailable balance is: ${self.amt}")

    def withdrawl(self,withdrawl):
        if withdrawl<=self.amt:
            self.amt-=withdrawl
            print(f'Collect cash :${withdrawl}\nAvailable balance: ${self.amt}')
        else:
            print(f'Withdrawl exceeds the amount present!!')
        

sunil=BankAccount('Sunil', 5000)
sunil.deposit(1000)
sunil.withdrawl(2000)
sunil.withdrawl(5000)