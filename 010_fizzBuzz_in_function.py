def fizz_buzz(max_num):
    for num in range(1, max_num+1):
        if num % 3 == 0 and num % 5 == 0:
            print('Fizz_Buzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
number=int(input("Enter number : "))
fizz_buzz(number)