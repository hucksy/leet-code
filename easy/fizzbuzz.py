from typing import List

def fizz_buzz(n: int) -> List[str]:
    a = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            a.append("FizzBuzz")
        elif i % 3 == 0:
            a.append("Fizz")
        elif i % 5 == 0:
            a.append("Buzz")
        else:
            a.append(str(i))

    return a


def fizz_buzz_lc(n: int) -> List[str]:
    return ['Fizz'*(not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


print(fizz_buzz(6))
print(fizz_buzz_lc(8))

