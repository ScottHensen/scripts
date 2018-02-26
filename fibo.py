# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

# Add this to make this module command line runnable and accepting 1 arg
# (python replaces __name__ (fibo) with __main__ when on command line
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
