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

def prime_division(n):
    result = [1]
    if is_prime(n):
        result.append(n)
        return result
    # when n is not a prime number
    divisors = [i for i in range(2, n//2+1) if n%i == 0 and is_prime(i)]
    for divisor in divisors:
        while n % divisor == 0:
            result.append(divisor)
            n //= divisor
    return result   

flag = True
while flag:
    test = int(input("Enter an integer: "))
    if test < 0:
        flag = False
        break
    print("The prime division of ", test, " is: ")
    print(prime_division(test))