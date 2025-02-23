from Customer_1 import Customer

class PremiumCustomer(Customer):
  def __init__(self, FullName, Address, Email, PhoneNumber, Reward):         #Atributes 
    super().__init__(FullName, Address, Email, PhoneNumber, Reward)
    self.premium_reward = Reward
    self.Membership = "Premium"  


  #String representation of an object 
  def __str__(self):                  
    return f"{self.premium_reward}"
