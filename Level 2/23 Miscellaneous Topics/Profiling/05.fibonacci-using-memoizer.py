import profile


class memoize:
    # from http://avinashv.net/2008/04/python-decorators-syntactic-sugar/
    def __init__(self, function):
        self.function = function
        self.memoized = {}

    def __call__(self, *args):
        try:
            return self.memoized[args]
        except KeyError:
            self.memoized[args] = self.function(*args)
            return self.memoized[args]


@memoize
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n - 1) + fib(n - 2)


def fibonacci_seq(n):
    seq = []
    if n > 0:
        seq.extend(fibonacci_seq(n - 1))
    seq.append(fib(n))
    return seq


profile.run('print(fibonacci_seq(20)); print()')

1
