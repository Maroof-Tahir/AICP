class Outing:
    def __init__(self):
        self.costs = {
            '12-16': {'coach': 150, 'meal': 14.00, 'ticket': 21.00},
            '17-26': {'coach': 190, 'meal': 13.50, 'ticket': 20.00},
            '27-39': {'coach': 225, 'meal': 13.00, 'ticket': 19.00}
        }
        self.min_seniors = 10
        self.max_seniors = 36
        self.base_carers = 2
        self.additional_carer = 1
        self.carer_threshold = 24

    def calculate_cost(self, num_seniors):
        if num_seniors < self.min_seniors or num_seniors > self.max_seniors:
            return None, None

        num_carers = self.base_carers
        if num_seniors > self.carer_threshold:
            num_carers += self.additional_carer

        total_cost = self.costs['12-16']['coach']
        for group in self.costs.values():
            total_cost += group['meal'] * num_seniors
            total_cost += group['ticket'] * num_seniors

        total_cost += (num_seniors - 12) // 10 * 40  # Incremental coach cost for age groups
        total_cost += num_carers * (self.costs['12-16']['meal'] + self.costs['12-16']['ticket'])

        cost_per_person = total_cost / (num_seniors + num_carers)
        return total_cost, cost_per_person

    def record_outing(self, num_seniors, num_paid):
        total_cost, cost_per_person = self.calculate_cost(num_seniors)
        if total_cost is None:
            return "Invalid number of seniors."

        num_carers = self.base_carers
        if num_seniors > self.carer_threshold:
            num_carers += self.additional_carer

        total_people = num_seniors + num_carers
        total_income = num_paid * (self.costs['12-16']['meal'] + self.costs['12-16']['ticket'])

        profit_or_loss = total_income - total_cost

        outing_info = {
            "Total Cost": total_cost,
            "Cost per Person": cost_per_person,
            "Total People": total_people,
            "Total Income": total_income,
            "Profit/Loss": profit_or_loss
        }

        return outing_info


# Main program
outing_planner = Outing()

# Task 1
num_seniors = int(input("Enter the number of senior citizens interested in the outing: "))
total_cost, cost_per_person = outing_planner.calculate_cost(num_seniors)
if total_cost is not None:
    print(f"Total Cost of the outing: ${total_cost}")
    print(f"Cost per Person: ${cost_per_person}")
else:
    print("Invalid number of seniors.")

# Task 2
num_paid = int(input("Enter the number of senior citizens who have paid: "))
outing_info = outing_planner.record_outing(num_seniors, num_paid)
if isinstance(outing_info, dict):
    print("\nRecording who is going on the outing...")
    for key, value in outing_info.items():
        print(f"{key}: {value}")
else:
    print(outing_info)
