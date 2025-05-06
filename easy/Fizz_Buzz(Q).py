# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true

    for i in range(1, n+1):

def fizzBuzz(n: int) -> List[str]:
        elif i % 5 == 0:
            result.append("Buzz")

    return result

        if i % 15 == 0:
            result.append("FizzBuzz")
        else:
            result.append(str(i))

    result = []
        elif i % 3 == 0:
            result.append("Fizz")