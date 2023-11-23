import math
class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.total = 0
    self.total_deposit = 0

  def __str__(self):
    print(self.category.center(30, "*"))
    for i in self.ledger:
      # print(f"{i['description'][:23].ljust(23)}{i['amount']:7.2f}")
      description = i["description"][:23]
      amount = f"{i['amount']:.2f}"
      print(f"{description:<23}{amount:>7}")
    print(f"Total: {self.total:7.2f}")
    
  def deposit(self, amount, description=""):
    self.total += amount
    self.total_deposit += amount
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": description})
    return self.check_funds
    
  def get_balance(self):
    return self.total

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.total -= amount
      self.withdraw(amount, f"Transfer to {budget_category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
    return self.check_funds
  
  def check_funds(self, amount):
    if self.total < amount:
      return False
    return True

def create_spend_chart(categories):
  list_spend = []
  for i in categories:
    list_spend.append(i.total-i.total_deposit)
  Total_spend = sum(list_spend)

  list_percentage = []
  for i in list_spend:
    list_percentage.append(math.floor((i/Total_spend)*10))
  
  print("Percentage spent by category")

  n = 10
  for i in reversed(range(0,101,10)):
    str = f"{i}| "
    for j in list_percentage:
      if j <= i:
        str += "o  "
      else:
        str += "   "
    print(str)

  print(f"    {'-'*(len(categorie)*3+1)}")
    
  
  
