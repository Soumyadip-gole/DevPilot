import sys

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python prime_checker.py <number>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Invalid input. Please provide an integer.")
        sys.exit(1)
