print("Welcome to my computer quiz Game ")

playing = input("Do you want to play ")

if playing.lower() != "yes":
    quit()
else:
    print("Okay ! let`s play ")    
score = 0

answer = input("What does Cpu stand for?  ")

if  answer.lower() == "central processing unit":
    print (" Correct !")
    score += 1   

else:
    print(" Incorrect! ")

answer1 = input(" What does OtP stand for?   ")

if  answer1.lower()  == "one time passward":
    print (" Correct !")
    score += 1   
else:
    print(" Incorrect! ")

answer2= input("What does op stand for?   ")

if  answer2.lower()  == "over power":
    print (" Correct !")
    score += 1   
else:
    print(" Incorrect! ")

answer3 = input("What does pc stand for? ")

if  answer3.lower()  == "persnal computer":
    print (" Correct !")
    score += 1   
else:
    print(" Incorrect! ")

print("You Got " + str(score) + " question correct")
print("You Got " + str((score/4)*100 ) + " % " )