def one_max(current, number):
    if current > number:
        return
    print(current)
    one_max(current + 1, number)
numb = int(input("Enter max number: "))
one_max(1, numb)
