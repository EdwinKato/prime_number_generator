def generate_prime_numbers(n):
    """Function to generate prime numbers"""

    j = 2
    prime_numbers = []
    while j <= n:
        k = 2
        while not(k == j) and not(j%k == 0):
            k = k + 1
        if k == j:
            prime_numbers.append(j)
        j = j + 1
    print prime_numbers

generate_prime_numbers(10)