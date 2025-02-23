1. Creational Design Patterns

Factory Pattern:

The CustomerFactory.py pattern is used in this project to create instances of StandardCustomer and PremiumCustomer:
-	The object creation logic is abstracted by the pattern and kept apart from the main program (Main.py).
-	It makes expansion simple, so new customer types can be added without changing entirely the code that already exists.
-	It makes code more scalable and maintainable by lowering reliance on particular classes.
-	This strategy indicates that the system will continue to be flexible and simple to change, making it an appropriate choice for real-world uses.

2. Behavioral Design Patterns

Strategy Pattern:

-	Customers can pay with cash or a credit card in the Lemon Tree Hotel Reservation System as a result of the Strategy Pattern used in Main.py to manage payment method selection.
-	Encapsulates the logic for processing payments, maintaining the main program's modularity and cleanliness.
-	Makes it easier to add new payment methods without modifying entirely the code that already exists.

Observer Pattern:

-	This pattern drives the notification system in the hotel reservation system, making sure that end-users are informed in real time about the status of their reservations and any modifications.
-	The system maintains its scalability, adaptability, and ease of maintenance by utilising this design pattern, which enhances user experience and functionality.
