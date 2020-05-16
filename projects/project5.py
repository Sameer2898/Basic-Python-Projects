def next_palindrome(n):
    n+=1
    while not is_palindrome(n):
        n+=1
    return n
def is_palindrome(n):
    return str(n)==str(n)[::-1]
if __name__ == "__main__":
    size=int(input("Enter the size of list:"))
    num_list=[]
    for i in range(size):
        number=int(input("Enter the number of the list:"))
        num_list.append(number)
    print(f"You entered {num_list}.")
    print(f"Output list:{[num_list[i] if num_list[i]<10 else next_palindrome(num_list[i]) for i in range(size)]}.")