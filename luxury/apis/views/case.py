def is_prime(number):
    return all([(number % e) == 0 for e in range(1, number)])