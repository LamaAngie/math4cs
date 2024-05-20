#write a function that takes an integer as input and returns True if the integer is a prime number

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


test = int(input("Enter an integer: "))
print(is_prime(test))

print("Find all prime numbers between 1 and 1000: ")
for i in range(1, 1001):
    if is_prime(i):
        print(i, end=" ")