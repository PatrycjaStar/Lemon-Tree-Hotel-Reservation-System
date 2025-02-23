class Customer:
  def __init__(self, FullName, Address, Email, PhoneNumber, Reward):    #initialised      #Atributes 
    self.FullName = FullName
    self.Address =  Address
    self.Email = Email
    self.PhoneNumber = PhoneNumber
    self.Reward = Reward
 

  def showInfo(self):
    print(f"Full Name:\t {self.FullName}\n"
          f"Address:\t {self.Address}\n"
          f"Email:\t         {self.Email}\n"
          f"Phone Number:\t {self.PhoneNumber}\n"
          f"Reward:\t         {self.Reward}\n")