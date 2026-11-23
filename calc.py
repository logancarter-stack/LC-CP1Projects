def calc(*args, function="sum"):
    if len(args) == 0:
        return "Error: No numbers provided."

    if function == "sum":
        return sum(args)

    elif function == "average":
        return sum(args) / len(args)

    elif function == "max":
        return max(args)

    elif function == "min":
        return min(args)

    elif function == "product":
        result = 1
        for number in args:
            result *= number
        return result

    else:
        return "Invalid function."


def get_num():
    numbers = []

    print("Enter numbers (type 'done' when finished):")

    while True:
        user_input = input("Number: ")

        if user_input == "done":
            break

        try:
            number = float(user_input)
            numbers.append(number)

        except ValueError:
            print(" enter a valid number or type 'done'.")

    return numbers


def welcome():
    print("Welcome!")
    print("Available operations: sum, average, max, min, product")

    while True:
        function = input(
            "\nWhich function would you like to perform bruh :  "
        )
        if function not in ["sum", "average", "max", "min", "product"]:
            print("Invalid function. try again.")
            continue

        numbers = get_num()

        if len(numbers) == 0:
            print("You no number silly.")
            continue

        print(f"\nCalculating {function} of: {', '.join(map(str, numbers))}")

        anwser = calc(*numbers, function=function)

        print(f"Result: {anwser}")

        more = input(
            "\n do you wanna perform another calculation :  (yes/no) "
        )
        if more != "yes":
            break

    print("\nThank bruh")

welcome