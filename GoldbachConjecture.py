import math

'''
this file involves two methods to find two prime numbers that sum up to a even number that is larger than 2.
The correct method is the exhaustive method that loops through all the prime numbers before the target number.
'''


def find_target_index(target,pime_array):
    for i in range(1,len(prime_array)):
        if prime_array[i] >= target:
            return i-1
    return -1

#two pointer method from beginning and at the end to the middle
def find_two_prime(target, prime_array):
    #initialize the indexes
    small_index = 0
    big_index = find_target_index(target, prime_array)
    #loop through the prime array before the target number
    while big_index >= small_index:
        if prime_array[big_index] + prime_array[small_index] == target:
            return prime_array[small_index], prime_array[big_index]
        elif prime_array[big_index] + prime_array[small_index] < target:
            small_index += 1
        else :
            big_index -= 1
    return None, None



def find_two_prime_exhaustive(target, prime_array):
    for i in range(0, len(prime_array)):
        for j in range(i, len(prime_array)):
            if prime_array[i] + prime_array[j] == target:
                return prime_array[i], prime_array[j]
    return None, None



#initialize the prime array
prime_array = [2]
max = 10000
for num in range(3,max,2):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        prime_array.append(num)

# target = input("what is your target number ? ")
# target = int(target)
# prime1, prime2 = find_two_prime(target, prime_array)
# print("The two prime numbers are: ", prime1, prime2)
        
value = 4
while value <= max: 
    prime1, prime2 = find_two_prime_exhaustive(value, prime_array)
    if prime1 == None:
        print("The two prime numbers are not found for ", value)
    value += 2      
print("Done! Goldbach Conjecture is true for all even numbers less than 10000.")

