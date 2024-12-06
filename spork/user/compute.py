from spork.lib.samples import fibonacci_dp, is_palindrome, calculator


def main():
    # Perform a series of calculations
    numbers = [(5, 3, "add"), (10, 4, "subtract"), (7, 2, "multiply"), (9, 0, "divide"), (12, 4, "divide")]
    print("Performing calculations:")
    for a, b, operation in numbers:
        result = calculator(a, b, operation)
        print(f"{operation.capitalize()} {a} and {b}: {result}")

    print("\nFibonacci sequence and palindrome check integration:")
    # Generate Fibonacci numbers and check if they are palindromes
    fib_count = 15
    for i in range(fib_count):
        fib_number = fibonacci_dp(i)
        is_pal = is_palindrome(str(fib_number))
        print(f"Fibonacci({i}): {fib_number} {'(Palindrome)' if is_pal else ''}")

    print("\nCombining calculations and Fibonacci numbers:")
    # Perform calculations using Fibonacci numbers
    fib_pairs = [(2, 5), (3, 7), (5, 6)]
    operations = ["add", "subtract", "multiply", "divide"]

    for pair in fib_pairs:
        a, b = fibonacci_dp(pair[0]), fibonacci_dp(pair[1])
        for operation in operations:
            result = calculator(a, b, operation)
            print(f"{operation.capitalize()} Fibonacci({pair[0]}) = {a} and Fibonacci({pair[1]}) = {b}: {result}")

    numbers = [(55, 33, "add"), (101, 44, "subtract")]
    print("Performing second set of calculations:")
    for a, b, operation in numbers:
        result = calculator(a, b, operation)
        print(f"{operation.capitalize()} {a} and {b}: {result}")


if __name__ == "__main__":
    main()

