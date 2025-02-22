def get_non_negative_integer() -> int:
    """
    Obtains a non-negative integer input from the user.
    Returns:
        int: The validated non-negative integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter a non-negative integer: ").strip())
            if number >= 0:
                return number
            print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.
    Args:
        n (int): The non-negative integer.
    Returns:
        int: The calculated factorial of the given number.
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main() -> None:
    """
    Main function to execute the factorial calculator program.
    """
    user_number = get_non_negative_integer()
    result = calculate_factorial(user_number)
    print(f"The factorial of {user_number} is: {result}")

if __name__ == "__main__":
    main()
