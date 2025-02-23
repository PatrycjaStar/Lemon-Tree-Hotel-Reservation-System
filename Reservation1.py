from tkinter import StringVar         #To generate variable for Booking ID 

from StandardCustomer import StandardCustomer
from PremiumCustomer import PremiumCustomer
import random

#Create Reservation 
class Reservation:

  def __init__(self, NumberofRooms, BookingDate, PurposeofStaying, RoomType, CustomerProfile,      #Atributes 
               NumberofAdults, NumberofChildren, PetsIncluded, Membership,
               PayMethod, Status):

    # Generate a random booking ID
    self.bookingID = str(random.randint(1, 200))
    # Declaring parameters 
    self.NumberofRooms = NumberofRooms
    self.BookingDate = BookingDate
    self.PurposeofStaying = PurposeofStaying
    self.RoomType = RoomType
    self.CustomerProfile = CustomerProfile
    self.NumberofAdults = NumberofAdults
    self.NumberofChildren = NumberofChildren
    self.PetsIncluded = PetsIncluded
    self.Membership = Membership
    self.PayMethod = PayMethod
    self.Reservation_Status = Status

  def showReservation(self):
    print(f"BookingID:\t\t {self.bookingID}\n"
          f"Number of Rooms:\t {self.NumberofRooms}\n"
          f"Booking Dates:\t\t {self.BookingDate}\n"
          f"Purpose of Staying:\t {self.PurposeofStaying}\n"
          f"Room Type:\t         {self.RoomType}\n"
          f"Number of Adults:\t {self.NumberofAdults}\n"
          f"Number of Children:\t {self.NumberofChildren}\n"
          f"Pets Included?:\t         {self.PetsIncluded}\n"
          f"Account Type:\t         {self.Membership}\n"
          f"Payment Method:\t         {self.PayMethod}\n"
          f"Reservation Status:\t {self.Reservation_Status}\n")
    self.CustomerProfile.showInfo()

  def cancel_reservation(self):
    self.Reservation_Status = "This reservation has been cancelled"
