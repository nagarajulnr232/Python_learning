val=int(input("Eneter number: "))
def pyramid(val):
    num=1
    for i in range(1,val+1):
        print("  " * (val - i),end="")
        for j in range (2*i-1):
            print(f"{num} ", end="")
            num+=1
        print()

    for i in range(val-1,0,-1):
        print("  " * (val - i),end="")
        for j in range (2*i-1):
            print(f"{num} ", end="")
            num+=1
        print()
pyramid(val)