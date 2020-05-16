try:
    apple=int(input("Please enter the number of apples you have:"))
    child=int(input(f"In how many childrens you want to distribute {apple} apples:"))
    print(f"You have {apple} apples and {child} childrens.")
    mn=int(input("Please enter the minimum number:"))#mn for minimum.
    mx=int(input("Please enter the maximum number:"))#mx for maximum.
except ValueError:
        print("Please enter integers only.")
        exit()
if mn==mx:
    print("minimum is equal to maximum.")
for i in range(mn,mx+1):
    if apple%i==0:
        print(f"{i} is divisor of {apple}.")
    else:
        print(f"{i} is not a divisor of {apple}.")