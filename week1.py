def validate_weight(weight):
    try:
        weight = float(weight)
        if weight > 0 and weight < 300:  
            return True
        else:
            return False
    except ValueError:
        return False

def input_weights_and_names(num_pupils):
    names = []
    weights = []

    print("Enter the names and weights of", num_pupils, "pupils:")

    for i in range(num_pupils):
        name = input("Enter the name of pupil {}: ".format(i + 1))
        weight = input("Enter the weight of pupil {} (in kilograms): ".format(name))

        while not validate_weight(weight):
            print("Invalid weight! Please enter a valid weight.")
            weight = input("Enter the weight of pupil {} (in kilograms): ".format(name))

        names.append(name)
        weights.append(float(weight))

    return names, weights

def calculate_weight_difference(initial_weights, final_weights):
    differences = [final - initial for initial, final in zip(initial_weights, final_weights)]
    return differences

def output_weight_changes(names, differences):
    print("\nPupil Weight Changes:")
    for name, difference in zip(names, differences):
        if abs(difference) > 2.5:
            if difference > 0:
                change_type = "rise"
            else:
                change_type = "fall"
            print(f"{name}: {abs(difference):.2f} kg {change_type}")

def main():
    num_pupils = 30  
    initial_names, initial_weights = input_weights_and_names(num_pupils)
    final_weights = []

    print("\nEnter the weights of pupils on the last day of term:")
    for name in initial_names:
        weight = input(f"Enter the weight of pupil {name} (in kilograms): ")
        while not validate_weight(weight):
            print("Invalid weight! Please enter a valid weight.")
            weight = input(f"Enter the weight of pupil {name} (in kilograms): ")
        final_weights.append(float(weight))

    weight_differences = calculate_weight_difference(initial_weights, final_weights)
    output_weight_changes(initial_names, weight_differences)

if __name__ == "__main__":
    main()
