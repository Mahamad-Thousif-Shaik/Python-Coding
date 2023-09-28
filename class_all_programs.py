class AllPrograms:

    def armstrong(self):
        num = int(input("Enter a number: "))
        if num < 0:
            print("Enter the positive number.")
        else:
            temp = num
            sum = 0
            while temp > 0:
                digit = temp % 10
                sum += digit ** 3
                temp //= 10
            if sum == num:
                print(num, " is an armstrong number.")
            else:
                print(num, " is not an armstrong number.")
    def hcf(self):
        def HCF(x, y):
            if x > y:
                small = y
            else:
                small = x
            for i in range(small, 0, -1):
                if x % i == 0 and y % i == 0:
                    return i

        x = int(input("Enter a number: "))
        y = int(input("Enter a number: "))
        print("The H.C.F of {} and {} is: ".format(x, y), HCF(x, y))
    def ascii_value(self):
        character = input("Enter a character: ")
        print("The ascii value of {} is:".format(character), ord(character))
    def binary_conversion_recursion(self):
        def bin_conv(n):
            if n > 1:
                bin_conv(n // 2)
            print(n % 2, end="")

        n = int(input("Enter the positive number: "))
        print("The binary conversion of decimal number {} is:".format(n))
        bin_conv(n)
    def decimal_conversions(self):
        num = int(input("Enter the decimal number: "))
        print("The different converted values of decimal number {} is:".format(num))
        print("In binary:", bin(num))
        print("In hexadecimal:", hex(num))
        print("In octagonal:", oct(num))
    def factorial(self):
        num = int(input("Enter the number"))
        fact = 1
        if num < 0:
            print("Factorial is not possible for negative numbers.")
        elif num == 0:
            print("Factorial of {} is {}".format(num, 1))
        else:
            for i in range(1, num + 1):
                fact = fact * i
            print("Factorial of {} is {}".format(num, fact))
    def factors(self):
        def factors(x):
            return [i for i in range(1, x + 1) if x % i == 0]

        x = int(input("Enter the number: "))
        print("Factors of {} are:".format(x), factors(x))
    def fibonacci_series(self):
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        n = int(input("Enter the number of fibonacci sequences: "))
        print("The fibonacci sequence is:")
        for i in range(n):
            print(fibonacci(i), end=" ")
    def fibonacci_series_upto_number(self):
        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n - 1) + fibonacci(n - 2)

        n = int(input("Enter the number of fibonacci sequences: "))
        print("The fibonacci sequence is:")
        for i in range(n):
            if fibonacci(i) >= n:
                break
            else:
                print(fibonacci(i), end=" ")
    def largest_number_given_numbers(self):
        num1 = float(input("Enter the number "))
        num2 = float(input("Enter the number "))
        num3 = float(input("Enter the number "))
        if num1 >= num2 and num1 >= num3:
            largest = num1
        elif num2 >= num1 and num2 >= num3:
            largest = num2
        else:
            largest = num3
        print(largest, " is the largest number.")
    def lcm(self):
        x = int(input("Enter the number: "))
        y = int(input("Enter the number: "))

        def LCM(x, y):
            if x > y:
                greater = x
            else:
                greater = y
            while (True):
                if (greater % x == 0) and (greater % y == 0):
                    return greater
                greater += 1

        print("LCM of {} and {} is:".format(x, y), LCM(x, y))
    def leap_year(self):
        year = int(input("Enter the year"))
        if (year % 400) == 0 and (year % 100) == 0:
            print("{} is a leap year.".format(year))
        elif (year % 4) == 0 and (year % 100) != 0:
            print("{} is a leap year.".format(year))
        else:
            print("{} is not a leap year.".format(year))
    def palindrome(self):
        word = input("Enter a string: ")
        word = word.casefold()
        reverse_word = reversed(word)
        if list(word) == list(reverse_word):
            print("Palindrome")
        else:
            print("Not Palindrome")
    def powers_of_two(self):
        terms = int(input("Enter the number of terms: "))
        result = list(map(lambda x: 2 ** x, range(terms)))
        print("The total terms are:")
        for i in range(terms):
            print(result[i])
    def prime_or_not(self):
        num = int(input("Enter the number "))
        flag = False
        if num <= 1:
            print(num, "is not a prime number.")
        elif num > 2:
            for i in range(2, num // 2):
                if num % i == 0:
                    flag = True
                    break
        if flag == True:
            print(num, "is not a prime number.")
        else:
            print(num, "is a prime number.")
    def prime_number_series(self):
        lower = int(input("Enter the lower limit number"))
        upper = int(input("Enter the upper limit number"))
        if lower > 1:
            for i in range(lower, upper + 1):
                for num in range(2, i // 2 + 1):
                    if i % num == 0:
                        break
                else:
                    print(i)
    def random_integer(self):
        from random import randint as ri
        print(ri(10, 100))
    def sub_arrays(self):
        from itertools import combinations
        n = int(input("Enter the length of array: "))
        l = [int(input()) for i in range(n)]
        comb = []
        for i in range(n + 1):
            comb += ([list(j) for j in combinations(l, i)])
        print(comb)
    def natural_numbers(self):
        num = int(input("Enter the number: "))
        if num <= 0:
            print("Please enter the positive number.")
        else:
            sum = 0
            print("Sum of natural numbers upto {} is".format(num), end=" ")
            while num > 0:
                sum += num
                num -= 1
            print(sum)


programs = AllPrograms()
list_of_all_methods = dir(AllPrograms)
list_of_methods = [method for method in list_of_all_methods if method.startswith("__") is False]
list_of_methods.sort()


def operation(array):
    def list_of_programs(array):
        for i in range(len(array)):
            print("{}. {}".format(i+1, array[i]))
    list_of_programs(array)
    print("If you want to exit the operation Enter 'exit'")
    while(True):
        print("Enter the operation name you want to do: ")
        task_to_do = input()
        if task_to_do != 'exit':
            if task_to_do in list_of_methods  :
                cls = globals()['AllPrograms']
                emp = cls()
                func = getattr(emp,task_to_do)
                func()
            else:
                print("Enter among the above operations.")
        else:
            return


operation(list_of_methods)
