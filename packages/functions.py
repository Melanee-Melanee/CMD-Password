def fib(n) : # return fibonacci series
    result = []
    a , b = 0 , 1
    while a < n :
        result.append(a)
        a , b = b , a + b
    return result


def sayHello(name) :
    return 'Hello, {}'.format(name)