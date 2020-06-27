def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")


check_prime(2)
check_prime(4)
