import random
import datetime

def calculate_age(birthdate):
    """Calculates age based on birthdate."""
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def generate_random_list(length):
    """Generates a list of random numbers."""
    return [random.randint(1, 100) for _ in range(length)]

def main():
    """Main function to demonstrate various features."""

    # Basic code completion
    name = "Alice"
    print(f"Hello, {name}!")  # Code Assist will suggest 'name'

    # Code generation
    birthdate = datetime.date(1995, 5, 10)
    age = calculate_age(birthdate)  # Code Assist can generate the 'calculate_age' function
    print(f"{name} is {age} years old.")

    # Code refactoring
    numbers = generate_random_list(10)
    sorted_numbers = numbers.sort() # Code Assist might suggest using 'numbers.sort()' for in-place sorting

    # Error handling
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero.")

    # Type hinting
    def greet(name: str) -> str:
        return f"Hi, {name}!"

    greeting = greet("Bob")  # Code Assist will provide type hints for 'name' and the return value

if __name__ == "__main__":
    main()
