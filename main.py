import math


def isPrime(number):
    """
    Check if a number is prime

    Arguments:
        n (int): Number to check

    Returns:
        bool: True if number is prime, False otherwise
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i <= math.sqrt(number):
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True


def find_primes_in_range(start, end):
    """
    Find all prime numbers in range from the starting number to the ending number

    Args:
        start (int): Staring number.
        end (int): Ending number.

    Returns:
        list: List of prime number.
    """
    return [num for num in range(start, end + 1) if isPrime(num)]


if __name__ == "__main__":
    start, end = map(
        int, input("Enter the start point and end point (start end): ").split()
    )
    primes = find_primes_in_range(start, end)
    print(f"All prime number from {start} to {end}:")
    print(primes)
