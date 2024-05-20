#intro
name= input("Type your name:  ")
print("Hello" +" "+ name)
print("Welcome to my quiz game !")

#if user want to play or not
playing=input("Do you want to play ? ")
if playing.lower() != "yes":
    print("Ok")
    quit()
print("Lets play")

#Question1
answer1=input("Q.1  What does CPU stand for ? ")
if answer1.lower() == "central processing unit":
    print("Correct answer! ")
else:
    tryagain=input("Your answer is wrong. Want to try again ?  ")
    if  tryagain.lower() =="yes":
        answer1=input("Q.1  What does CPU stand for ? ")
        if answer1.lower() == "central processing unit":
            print("Correct answer! ")
        else:
            print("Your answer is again wrong. Let's go to next question! ")
    else:
        print("Let's go to next question!")
    
#Question2
answer2=input("Q.2  What does GPU stand for ? ")
if answer2.lower() == "graphic processing unit":
    print("Correct answer! Thank you for playing this game!")
else:
    tryagain=input("Your answer is wrong. Want to try again ?  ")
    if  tryagain.lower() =="yes":
        answer2=input("Q.2  What does GPU stand for ? ")
        if answer2.lower() == "graphic processing unit":
            print("Correct answer! Thank you for playing this game!")
        else:
            print("Your answer is again wrong. Thank you for playing this game! ")
    else:
        print("Thank you for playing this game!")

#the program have finished