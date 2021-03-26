def fizzbuzz(num):
    return ', '.join(['Fizz Buzz' if x % 15 == 0
                      else 'Fizz' if x % 3 == 0
                      else 'Buzz' if x % 5 == 0
                      else str(x) for x in range(1, num)])
