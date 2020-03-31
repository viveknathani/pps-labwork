def fib(n):
    if n<1:
        return -1
    elif n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_series(m):
    series=[]
    for var in range(1, m+1):
        x=fib(var)
        if x==-1:
            break
        else:
            series.append(x)
    return series
