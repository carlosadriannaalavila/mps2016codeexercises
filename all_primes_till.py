#Definition of Prime number
#Be n a positive number and integer. We know that 1 and n divide n. If n > 1 and no oher number besides 1 and n divide it, then n is prime.
def extract_prime_numbers_from(var):

    for p in range(2, var+1):
        for i in range(2, p):
            if p % i == 0:
         	    break
        else:
        	print('Prime: %r' % p)

print("Hi I'm a program that detects prime numbers from 0 to a number limit declared by you.")
try:
    x = int(raw_input("Please Enter the number limit: "))
    if x>0:
        print('The limit number is %r, now the prime numbers:' % x)
        extract_prime_numbers_from(x)
    else:
	    print("You entered a negative number, next time use only 'positive integer numbers'")
except ValueError:
    print("You entered a weird input entry, next time use only 'positive integer numbers'")