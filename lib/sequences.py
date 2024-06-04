def print_fibonacci(length):
    """Prints a list of the first n Fibonacci numbers."""
    if length <= 0:
        print([])
        return

    # The first two Fibonacci numbers
    fibonacci_list = [0, 1]

    # Generate the rest of the Fibonacci sequence up to length
    while len(fibonacci_list) < length:
        next_value = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_value)

    # Print the Fibonacci sequence
    print(fibonacci_list[:length])
