def main():
    numbers = generate_random_list(10)
    numbers.sort()
    print(numbers)
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Division by zero")
    
def generate_random_list(n):
#  Create a list of random numbers
    import random
    random_numbers = []
    for i in range(n):
        random_numbers.append(random.randint(1, 100))
    return random_numbers

main()
