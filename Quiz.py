
print("Welcome to my Computer Quiz Game!")



play=input("Do you want to play? ")

if play.lower() == "no":
    print("Thankyou!")
    quit()
else:
    print("Okay Lets Play....!  :) ")
    score=0

answer=input("CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("GPU stands for? ")
if answer == "graphical processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer=input("PSU stands for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


print("You got "+str(score)+" questions correct")
print("You got "+str((score/5)*100)+"%")
print("Thankyou for participating in the QUIZ!")

end =input("End Quiz? ")
if end.lower == "yes":
    print("END")

