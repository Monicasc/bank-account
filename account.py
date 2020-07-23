from datetime import datetime
class BankAccount:
    bank="KCB"
    deposit_history = []
    loan = {}
    loan_balance = 0
    applied_for_loan = False
    withdrawal = []
  
    
    def __init__(self, first_name, second_name,phone_number):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0
        self.phone_number=phone_number

    def _getCurrentTime(self):
        now = datetime.now()
        now_formatted = now.strftime("%b %d %Y, %H:%M:%S")
        return now_formatted

    def account_name(self):
        name= "{} account for {} {} ".format(self.bank, self.first_name,self.second_name)
        return name
    def deposit(self,amount):
        try:
          amount + 1
        except TypeError:
          print("you must enter the amount in figures")
          return 
        if amount >0:
            self.balance+=amount
            timeDate = self._getCurrentTime()
            transaction_details = {"amount": amount, "date":timeDate}
            self.deposit_history.append(transaction_details)
            print("You have deposited {} to your account at {}".format(amount, timeDate))
        else:
            print("Too low ")
  
  
    def withdraw(self, amount):
         try:
          amount + 1
         except TypeError:
          print("you must enter the amount in figures")
          return 
         if amount > 0:
            self.balance -= amount
            self.withdrawal.append(amount)
            timeDate = self._getCurrentTime()
            print("You have withdrawed {} on {} from your account and your balance is {}".format(amount,timeDate,self.balance))
         else:
            print("Amount too low")
    def get_balance(self):
        return "The balance of {} is {} ".format(self.account_name(),self.balance)
    
    def get_statement(self):

      for statement_item in self.deposit_history:
         print("On",statement_item['date'], ", you deposited KES", statement_item['amount'])
     
    def get_withdrawal_statement(self):
        for statement_item in self.withdrawal:
            print("On",statement_item['date'], ", you deposited KES", statement_item['amount'])        
    
    def getLoanBalance(self):
        print("Your balance is KES",self.loan_balance,"for loan KES", self.loan["amount_borrowed"],"Borrowed on", self.loan["date"])
    def requestLoan(self, amount):
        try:
          amount + 1
        except TypeError:
          print("you must enter the amount in figures")
          return 
        if not self.loan_balance > 0:
            timeDate = self._getCurrentTime()
            self.loan["date"] = timeDate
            self.loan["amount_borrowed"] = amount
            self.loan_balance += amount
   
        else:
            print("Err:Loan Request Failed Reason:", end="")
            print(self.getLoanBalance())
            
    def payLoan(self,amount):
        try:
          amount + 1
        except TypeError:
          print("you must enter the amount in figures")
          return 
        if self.loan_balance == 0:
            print("You have no loan balance")
        elif amount > self.loan_balance:
            self.loan_balance = 0
        elif amount <= self.loan_balance:
            self.loan_balance -= amount

        return

    
acc1=BankAccount("Monica","Abich",254767895646)
acc2=BankAccount("Joan", "Otieno",25478900034)

acc1.deposit(-1000)
acc2.deposit(50)
acc1.deposit(100)
acc2.deposit(30)
acc1.withdraw(10)
acc2.withdraw(30)
acc1.withdraw(20)
acc2.withdraw(10)

acc2.get_statement()
acc1.requestLoan(2000)
acc1.requestLoan(899)
acc1.payLoan(200)
acc1.getLoanBalance()
print(acc1.get_balance())
print(acc2.get_balance())

print(acc1.account_name())
print(acc2.account_name())