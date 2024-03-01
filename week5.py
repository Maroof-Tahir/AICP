
WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
DAY_PRICES = {'Sunday': {'before_16': 2.00, 'after_16': 2.00},
              'Monday': {'before_16': 10.00, 'after_16': 2.00},
              'Tuesday': {'before_16': 10.00, 'after_16': 2.00},
              'Wednesday': {'before_16': 10.00, 'after_16': 2.00},
              'Thursday': {'before_16': 10.00, 'after_16': 2.00},
              'Friday': {'before_16': 10.00, 'after_16': 2.00},
              'Saturday': {'before_16': 3.00, 'after_16': 2.00}}
DISCOUNT_BEFORE_16 = 0.10
DISCOUNT_AFTER_16 = 0.50

# Task 1: Calculating the price to park
def calculate_parking_price(day, arrival_hour, parking_hours, frequent_parking_number=None):
    if day not in WEEKDAYS:
        return "Invalid day input"
    
    if not (0 <= arrival_hour <= 23):
        return "Invalid arrival hour input"

    if not (1 <= parking_hours <= 8):  
        return "Invalid parking hours input"

    price_per_hour = DAY_PRICES[day]['before_16']
    discount = DISCOUNT_BEFORE_16

    if arrival_hour >= 16:
        price_per_hour = DAY_PRICES[day]['after_16']
        discount = DISCOUNT_AFTER_16

    total_price = price_per_hour * parking_hours

    if frequent_parking_number:
        if check_frequent_parking_number(frequent_parking_number):
            total_price *= (1 - discount)

    return total_price

def check_frequent_parking_number(number):
    if len(number) != 5:
        return False

    try:
        digits = [int(digit) for digit in number[:-1]]
        check_digit = int(number[-1])
    except ValueError:
        return False

    check_sum = sum(digit * (i + 1) for i, digit in enumerate(digits)) % 11
    return check_sum == check_digit

# Task 2: Keeping a total of the payments
def calculate_daily_total():
    daily_total = 0.0
    while True:
        day = input("Enter the day of the week: ")
        if day.lower() == 'done':
            break
        
        if day not in WEEKDAYS:
            print("Invalid day input")
            continue
        
        arrival_hour = int(input("Enter the hour of arrival (0-23): "))
        parking_hours = int(input("Enter the number of hours for parking: "))
        frequent_parking_number = input("Enter your frequent parking number (if available): ")

        price = calculate_parking_price(day, arrival_hour, parking_hours, frequent_parking_number)
        print(f"Price to park: ${price:.2f}")

        payment = float(input("Enter amount paid: "))
        if payment < price:
            print("Insufficient payment. Please pay the correct amount.")
            continue

        daily_total += payment

    print(f"Total payments for the day: ${daily_total:.2f}")

# Testing Task 1
print("Task 1:")
print(calculate_parking_price('Sunday', 14, 5, '12345'))  # Should return 10.00
print(calculate_parking_price('Saturday', 18, 3, '54329'))  # Should return 3.00

# Testing Task 2
print("\nTask 2:")
calculate_daily_total()
