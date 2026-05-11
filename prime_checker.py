def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main():
    import sys
    if len(sys.argv) > 1:
        raw = sys.argv[1]
    else:
        raw = input("Enter a number: ").strip()
    try:
        n = int(raw)
    except ValueError:
        print(f"'{raw}' is not a valid integer.")
        return
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


if __name__ == "__main__":
    main()
