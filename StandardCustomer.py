from Customer_1 import Customer

class StandardCustomer(Customer):
  def __init__(self, FullName, Address, Email, PhoneNumber, Reward):          #Atributes 
    super().__init__(FullName, Address, Email, PhoneNumber, Reward)
    self.standard_reward = Reward
    self.Membership = "Standard"

  #String representation of an object 
  def __str__(self):                 
      return f"No Reward"
