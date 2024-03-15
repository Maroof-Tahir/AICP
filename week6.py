import datetime

# Constants for ticket prices
# All the prices are in dollars
TICKET_PRICES = {
    "one_day": {
        "adult": 20.00,
        "child": 12.00,
        "senior": 16.00,
        "family": 60.00,
        "group": 15.00
    },
    "two_days": {
        "adult": 30.00,
        "child": 18.00,
        "senior": 24.00,
        "family": 90.00,
        "group": 22.50
    }
}

# Constants for extra attraction prices
EXTRA_ATTRACTIONS = {
    "lion_feeding": 2.50,
    "penguin_feeding": 2.00,
    "evening_barbecue": 5.00
}

# Function to display ticket options and extra attractions
def display_options():
    print("Ticket Options:")
    print("---------------")
    print("One-Day Tickets:")
    print("  - Adult: $20.00")
    print("  - Child: $12.00")
    print("  - Senior: $16.00")
    print("  - Family: $60.00")
    print("  - Group: $15.00 per person")
    print("\nTwo-Day Tickets:")
    print("  - Adult: $30.00")
    print("  - Child: $18.00")
    print("  - Senior: $24.00")
    print("  - Family: $90.00")
    print("  - Group: $22.50 per person")
    print("\nExtra Attractions:")
    print("  - Lion Feeding: $2.50")
    print("  - Penguin Feeding: $2.00")
    print("  - Evening Barbecue (Two-Day Tickets only): $5.00")

# Function to get the booking date(s) from the user
def get_booking_dates():
    print("\nDays available for booking:")
    for i in range(7):
        day = datetime.date.today() + datetime.timedelta(days=i)
        print(f"{i+1}. {day.strftime('%A, %B %d, %Y')}")
    while True:
        try:
            choice = int(input("\nEnter the number corresponding to the booking date: "))
            if 1 <= choice <= 7:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to process a booking
def process_booking():
    print("\nProcessing Booking...")
    booking_date = get_booking_dates()
    ticket_type = input("Enter the ticket type (one_day/two_days): ").strip().lower()
    while ticket_type not in ["one_day", "two_days"]:
        print("Invalid ticket type. Please enter either 'one_day' or 'two_days'.")
        ticket_type = input("Enter the ticket type (one_day/two_days): ").strip().lower()
    ticket_prices = TICKET_PRICES[ticket_type]
    extra_attractions = []
    while True:
        extra = input("Enter extra attraction (leave blank to finish): ").strip().lower()
        if extra == "":
            break
        elif extra in EXTRA_ATTRACTIONS:
            extra_attractions.append(extra)
        else:
            print("Invalid extra attraction. Please enter a valid option.")
    total_cost = 0
    for ticket, price in ticket_prices.items():
        count = int(input(f"Enter number of {ticket} tickets: "))
        total_cost += count * price
    for attraction in extra_attractions:
        total_cost += len(extra_attractions) * EXTRA_ATTRACTIONS[attraction]
    print("\nBooking Details:")
    print("----------------")
    print("Booking Date:", datetime.date.today() + datetime.timedelta(days=booking_date-1))
    print("Total Cost:", "${:.2f}".format(total_cost))
    print("Unique Booking Number:", f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{booking_date}")


while True:
    print("\nWelcome to the Wildlife Park Ticketing System")
    print("-------------------------------------------")
    print("1. Display Ticket Options and Extra Attractions")
    print("2. Make a Booking")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
        display_options()
    elif choice == "2":
        process_booking()
    elif choice == "3":
        print("Thank you for using the Wildlife Park Ticketing System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter either 1, 2, or 3.")
