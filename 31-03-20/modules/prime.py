def isPrime(number):
    check=True
    for i in range(2, int(number/2)):
        if(number%i==0):
            check=False
    return check
