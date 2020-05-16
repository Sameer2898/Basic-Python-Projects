print("Enter the number of list one by one:")
size=int(input("Enter the size of the list:"))
mylist=[]
for i in range(size):
    mylist.append(int(input("Enter the list element:")))
print(f"The list is {mylist}")
reverse1=mylist[:]
reverse1.reverse()
reverse2=mylist[::-1]
print(f"My First reversed list of {mylist} is {reverse2}.")
print(f"My Second reversed list of {mylist} is {reverse2}.")
reverse3=mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i],reverse3[len(reverse3)-i-1]=reverse3[len(reverse3)-i-1],reverse3[i]
print(f"My Third reversed list of {mylist} is {reverse3}.")
if reverse1==reverse2==reverse3:
    print("All list are same.")