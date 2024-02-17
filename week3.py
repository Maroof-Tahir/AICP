# TASK 1 - Record the yield

# Initialize an empty dictionary to store the milk yields for each cow
cow_yields = {}

# Function to record milk yield for a cow
def record_yield():
    cow_id = input("Enter the 3-digit identity code of the cow: ")
    yield_amount = float(input("Enter the milk yield (in litres) for the cow: "))
    
    if cow_id in cow_yields:
        cow_yields[cow_id].append(yield_amount)
    else:
        cow_yields[cow_id] = [yield_amount]

# Record yields for the week (14 times as each cow can be milked twice a day for 7 days)
for _ in range(14):
    record_yield()

# TASK 2 - Calculate the statistics

# Function to calculate total weekly volume of milk for the herd
def calculate_total_volume():
    total_volume = sum(sum(yields) for yields in cow_yields.values())
    return round(total_volume)

# Function to calculate average yield per cow in a week
def calculate_average_yield():
    total_cows = len(cow_yields)
    total_volume = calculate_total_volume()
    average_yield = total_volume / total_cows
    return round(average_yield)

# TASK 3 - Identify the most productive cow and cows with low volume of milk

# Function to identify the most productive cow
def identify_most_productive_cow():
    max_yield = 0
    most_productive_cow = None
    for cow_id, yields in cow_yields.items():
        total_yield = sum(yields)
        if total_yield > max_yield:
            max_yield = total_yield
            most_productive_cow = cow_id
    return most_productive_cow, max_yield

# Function to identify cows with a yield of less than 12 litres of milk for four or more days
def identify_low_yield_cows():
    low_yield_cows = []
    for cow_id, yields in cow_yields.items():
        days_below_threshold = sum(1 for yield_amount in yields if yield_amount < 12)
        if days_below_threshold >= 4:
            low_yield_cows.append(cow_id)
    return low_yield_cows

# Display the results
print("\nTASK 2 - Statistics:")
print(f"Total weekly volume of milk for the herd: {calculate_total_volume()} litres")
print(f"Average yield per cow in a week: {calculate_average_yield()} litres")

most_productive_cow, max_yield = identify_most_productive_cow()
print("\nTASK 3 - Most Productive Cow:")
print(f"Identity code number of the most productive cow: {most_productive_cow}")
print(f"Weekly yield of the most productive cow: {max_yield} litres")

low_yield_cows = identify_low_yield_cows()
print("\nTASK 3 - Cows with Low Volume of Milk:")
if low_yield_cows:
    print("Identity code numbers of cows with low volume of milk:")
    print("\n".join(low_yield_cows))
else:
    print("No cows with a yield of less than 12 litres of milk for four or more days this week.")
