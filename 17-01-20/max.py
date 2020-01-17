# print the greatest of three numbers

def max(a, b) :
    if (a>b) :
        return a
    else :
        return b

a,b,c=input("Enter your numbers separated by space : ").split()

a=float(a)
b=float(b)
c=float(c)

print("Max : ", max(a,max(b,c)))
