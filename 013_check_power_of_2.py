def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

# Example
num = int(input("Enter a number: "))
if is_power_of_two(num):
    print(f"{num} is a power of 2")
else:
    print(f"{num} is NOT a power of 2")
