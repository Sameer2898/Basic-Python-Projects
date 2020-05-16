def game():
    import random
    def guess_game(a,b,actual):
        user=int(input(f"Please guess the number between {a} and {b}:"))
        guess=1
        while user !=actual:
            if user<actual:
                user=int(input("The number is too low:"))
                guess+=1
            else:
                user=int(input("The number is too high:"))
                guess+=1
        print(f"You guess the number in {guess} times.")
        return guess
    if __name__ == "__main__":
        player1=input(r"Enter player 1's name:")
        player2=input(r"Enter player 2's name:")
        a=int(input("Enter the value of first number:"))
        b=int(input("Enter the value of second nunmber:"))
        actual1=random.randint(a,b)
        print(f"{player1} turn's")
        g1=guess_game(a,b,actual1)
        actual2=random.randint(a,b)
        print(f"{player2} turn's.")
        g2=guess_game(a,b,actual2)
        if g1<g2:
            print(f"{player1}wins.")
        elif g1>g2:
            print(f"{player2} wins.")
        else:
            print("The match is draw.")
        print(f"The number for {player1} is {actual1} and for {player2} is {actual2}.")
        again()
def again():
    user1=input("Do you want to play again?")
    if user1=="Y" or user1=="y":
        game()
    elif user1=="N" or user1=="n":
        print("BYE.....")
    else: 
        again()
game()