##Robert Fernandez
##Complete
##User will be able to enter 10 integars and the program will display numbers that are greater than n.


def main_function():
    numbers = []
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter a number {i + 1}/10: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid integer.")
    while True:
        try:
            n = int(input("Enter the number you wish to test if the list elements are greater than : "))
            break
        except ValueError:
            print("Please enter a valid integer.")
    larger_numbers = display_larger(numbers, n)
    print("List of numbers:", numbers)
    print("Numbers larger than", n, ":", larger_numbers)
    
##Takes a list of numbers and a number n and returns a list of numbers that are greater than n.
def display_larger(numbers, n):
    result = []
    for number in numbers:
        if number > n:
            result.append(number)
    return result


# Call the main function
if __name__ == "__main__":
    main_function()
