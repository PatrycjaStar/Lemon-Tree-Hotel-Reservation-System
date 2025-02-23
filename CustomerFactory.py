from StandardCustomer import StandardCustomer
from PremiumCustomer import PremiumCustomer
from Reservation1 import Reservation


class CustomerFactory:
    @staticmethod
    def create_customer(account_status_type, full_name, address, email, phone_number):     #Atributes 

        account_status_type = account_status_type.upper()

        if account_status_type == "P":
            # Create a PremiumCustomer
            return PremiumCustomer(
                FullName=full_name,
                Address=address,
                Email=email,
                PhoneNumber=phone_number,
                Reward="Breakfast Meals Included",
            )
        
        elif account_status_type == "S":
            # Create a StandardCustomer
            return StandardCustomer(
                FullName=full_name,
                Address=address,
                Email=email,
                PhoneNumber=phone_number,
                Reward="No Reward"
            )

        while True:
            try:
                print("Select Account Type...")
                CustomerProfile = input("Select Account Type (S-Standard, P-Premium): ")
                break
            except ValueError:
                continue



    @staticmethod
    def create_reservation(
            customer, number_of_rooms, booking_date, purpose_of_staying, room_type,
            number_of_adults, number_of_children, pets_included, payment_method, status="Active"
    ):

        account_status = "Standard" if isinstance(customer, StandardCustomer) else "Premium"

        return Reservation(
            NumberofRooms=number_of_rooms,
            BookingDate=booking_date,
            PurposeofStaying=purpose_of_staying,
            RoomType=room_type,
            CustomerProfile=customer,
            NumberofAdults=number_of_adults,
            NumberofChildren=number_of_children,
            PetsIncluded=pets_included,
            Membership=account_status,
            PayMethod=payment_method,
            Status=status
        )
