#monica adhiambo
#python 3.7.1
class BankAccount:
  bank="Barclays"
  
  def __init__(self,first_name,last_name):
    self.first_name=first_name
    self.last_name=last_name
    self.balance=0
  
  def account_name(self):
    name="{} account for {} {}".format(
    self.bank,self.first_name,self.last_name)
    return name
  
  def deposit(self,amount):
    self.balance+=amount
    if amount>0:
       print("you have deposited {} to your account".format(amount))
    else:
       print("The account has not accepted a deposite of {} to your account".format(amount))
  def get_balance(self):
    return "The balance for {} is {}".format(self.account_name(),self.balance)
  def withdraw(self,amount):
   self.balance -=amount
   print("you have withdrawn {} from your account".format(amount))

acc1=BankAccount("Joy","Akoth")
acc2=BankAccount("May","Awor")
acc3=BankAccount("Josh","Brian")
acc4=BankAccount("Maria","Sandra")
acc5=BankAccount("Lola","Grand")

acc1.deposit(1100)
acc2.deposit(40)
acc1.deposit(95)
acc2.deposit(-20)

print(acc2.get_balance())
print(acc1.get_balance())

acc3.deposit(200)
acc4.deposit(500)
acc5.deposit(10000)

print(acc3.get_balance())
print(acc4.get_balance())
print(acc5.get_balance())


acc3.withdraw(120)
acc3.withdraw(-60)
acc4.withdraw(10000)
acc4.withdraw(700)

print(acc3.get_balance())
print(acc4.get_balance())
