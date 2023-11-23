
class Category:
  
  def __init__(self, category):
    self.category = category
    self.ledger = []
    self.total = 0
    self.total_deposit = 0

  def __str__(self):
    s = self.category.center(30, "*")
    for i in self.ledger:
      # print(f"{i['description'][:23].ljust(23)}{i['amount']:7.2f}")
      description = i["description"][:23]
      amount = f"{i['amount']:.2f}"
      s += f"\n{description:<23}{amount:>7}"
    s += f"\nTotal: {self.total:.2f}"
    return s
  
  def deposit(self, amount, description=""):
    self.total += amount
    self.total_deposit += amount
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": description})
    return self.check_funds(amount)
  
  def get_balance(self):
    return self.total

  def transfer(self, amount, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.category}")
      budget_category.deposit(amount, f"Transfer from {self.category}")
    return self.check_funds(amount)
  
  def check_funds(self, amount):
    if self.total < amount:
      return False
    return True

def create_spend_chart(categories):
  list_spend = []
  for i in categories:
    val = i.total-i.total_deposit
    list_spend.append(val)
  Total_spend = sum(list_spend)

  list_percentage = []
  for i in list_spend:
    list_percentage.append((i*10)//Total_spend)
  
  str = "Percentage spent by category"

  n = 10
  for i in reversed(range(0,101,10)):
    str += f"\n{i:>3}| "
    for j in list_percentage:
      if j >= n:
        str += "o  "
      else:
        str += "   "
    n -= 1

  str += f"\n    {'-'*(len(categories)*3+1)}\n"
    
  c_names = [i.category for i in categories]
  max_len = max(len(i) for i in c_names)
  for i in range(0,max_len):
    str += f"     "
    for j in c_names:
      if i < len(j):
        str += f"{j[i]}  "
      else:
        str += "   "
    if i != max_len-1:
      str += "\n"
  return str
