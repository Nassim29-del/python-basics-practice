# Prints numbers 1..n, replacing multiples of 3 with Fizz, 5 with Buzz, both with FizzBuzz.

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(int(input("Count up to: ")))
