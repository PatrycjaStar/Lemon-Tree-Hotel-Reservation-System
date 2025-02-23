from Customer_1 import Customer         #class
from StandardCustomer import StandardCustomer
from PremiumCustomer import PremiumCustomer
from Reservation1 import Reservation
from CustomerFactory import CustomerFactory


def create_reservation():
    FullName = input("Enter Full Name: ")
    Address = input("Enter Address: ")
    Email = input("Enter Email: ")
    PhoneNumber = input("Enter Phone Number: ")

    RoomType = input("Enter room type (S-Single, D-Double): ")
    #Parameters for Atributes
    RoomType = RoomType.upper()
    if RoomType == "S":
        RoomType = "Single"
    else:
        RoomType = "Double"
    while True:
        try:
            NumberofRooms = int(input("Enter number of rooms: "))
            break
        except ValueError:
            print("Try again with a number...")
            continue

    BookingDate = input("Enter booking dates (DD/MM/YYYY)-(DD/MM/YYYY): ")

    PurposeofStaying = input("Enter purpose of staying (L-Leisure, B-Business): ")
    PurposeofStaying = PurposeofStaying.upper()
    if PurposeofStaying == "L":
        PurposeofStaying = "Leisure"
    else:
        PurposeofStaying = "Business"
    while True:
        try:
            NumberofAdults = int(input("Enter number of adults: "))
            break
        except ValueError:
            print("Try again with a number...")
            continue

    while True:
        try:
            NumberofChildren = int(input("Enter number of children: "))
            break
        except ValueError:
            print("Try again with a number...")
            continue

    PetsIncluded = input("Pets included? (Y-Yes, N-No): ")
    PetsIncluded = PetsIncluded.upper()
    if PetsIncluded == "Y":
        PetsIncluded = "Yes"
    else:
        PetsIncluded = "No"

    PayMethod = input("Enter payment method (Cash/Card): ")
    PayMethod = PayMethod.upper()
    if PayMethod == "Cash":
        PayMethod = "Paid with Cash"
    else:
        PayMethod == "Card"
        PayMethod = "Paid with Card"


    CustomerProfile = input("Select Membership (S-Standard, P-Premium): ")

    # Create customer using the factory class
    customer = CustomerFactory.create_customer(
        account_status_type=CustomerProfile,
        full_name=FullName,
        address=Address,
        email=Email,
        phone_number=PhoneNumber
    )
    # Create reservation using the factory
    reservation = CustomerFactory.create_reservation(
        customer=customer,
        number_of_rooms=NumberofRooms,
        booking_date=BookingDate,
        purpose_of_staying=PurposeofStaying,
        room_type=RoomType,
        number_of_adults=NumberofAdults,
        number_of_children=NumberofChildren,
        pets_included=PetsIncluded,
        payment_method=PayMethod
    )

    return reservation


reservations_list =  []

menu = ("-------------------------------\n"
    "Welcome to the Lemon Tree Hotel\n"
          "Book with us!\n"
                "-------------------------------\n")
menu += "\nMenu\n"
menu += "1. New Reservation\n"
menu += "2. Show Reservations\n"
menu += "3. Cancel a Reservation\n"
# menu += "4. Log Out\n"
menu += "\nSelect an option (1, 2, 3): "
menu_option = int(input(menu))
while(menu_option !=4):
    if menu_option ==1:
        reservation = create_reservation()
        reservations_list.append(reservation)
        message = "\nThe reservation has been booked\n"
        print("".join(message))
        reservation.showReservation()
        menu_option = int(input(menu))

    elif (menu_option ==2):
        bookings_count = len(reservations_list)
        print(f"------------------")
        print(f"Display all reservations, "
              f"\n{bookings_count} booked today\n")
        for reservation in reservations_list: 
            reservation.showReservation()
            print("___________________")
        menu_option = int(input(menu))

    elif (menu_option == 3):
        find_reservation = input("Enter BookingID: ").strip()
        bookings_count = len(reservations_list)
        print(f"\n{bookings_count} Reservations booked with us\n")

        if (bookings_count > 0):
            found = False
            for reservation in reservations_list:
                if reservation.bookingID == find_reservation:
                    reservation.cancel_reservation()
                    print("This reservation has been cancelled successfully!")
                    found = True
                    menu_option =int(input(menu))

        if not found:
            print("Reservation not found. Please check the BookingID")


        else:
            print("Try again with a 4 digits booking ID")

print("-------------------------------------------------------")
print("Thank you for using Lemon Tree Hotel Reservation System")
print("-------------------------------------------------------")

#Declaration for Create Reservation
hello = create_reservation()
