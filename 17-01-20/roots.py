# roots of quadratic equation

print("Enter coefficients separated by space in the following line")
a,b,c=input().split()

a=float(a)
b=float(b)
c=float(c)

root1=(-b+((b*b)-(4*a*c)))/(2*a)
root2=(-b-((b*b)-(4*a*c)))/(2*a)

print("Roots are : ", root1, root2)
