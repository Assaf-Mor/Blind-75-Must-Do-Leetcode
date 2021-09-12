def fibonacci(n):
    a,b = 0,1
    while n > 0:
        print ("{} and {}".format(a,b))
        a, b = b, a+b
        n -= 1

def fibonacciecursive(n,a,b):
    if(n == 0):
        return
    else:
        print ("{} and {}".format(a,b))
        n-=1
        fibonacciecursive (n, b, a + b)

