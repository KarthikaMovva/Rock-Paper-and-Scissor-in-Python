print("Welcome Players!!")
print("Game Introduction: Enter R/r for rock or Enter P/p for paper or Enter S/s for scissor.")
Inputofuser1=input("Enter R/r or P/p or S/s").upper()
Inputofuser2=input("Enter R/r or P/p or S/s").upper()
if len(Inputofuser1)==1 and len(Inputofuser2)==1:
    if Inputofuser1==Inputofuser2:
        print("It's a tie!")
    elif Inputofuser1=="P" and Inputofuser2=="R":
        print("Player1 won!")
    elif Inputofuser1=="R" and Inputofuser2=="P":
        print("Player2 won!")
    elif Inputofuser1=="S" and Inputofuser2=="P":
        print("Player1 won!")
    elif Inputofuser1=="P" and Inputofuser2=="S":
        print("Player2 won!")
    elif Inputofuser1=="R" and Inputofuser2=="S":
        print("Player1 won!")
    elif Inputofuser1=="S" and Inputofuser2=="R":
        print("Player2 won!")
else:
    print("Invalid Input")
print("Thank you")