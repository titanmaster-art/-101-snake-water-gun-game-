 ##project 1 foor github
import random
def check(comp,user):
    if comp == user:
        return 0#if both choose the same option

    if(comp ==0 and user ==1) or(comp ==1 and user == 2) or (comp == 2 and user  == 0):#conditiomns for the computer to win
        return -1
    return 1#if else  conditoon rather than the computer condition for win happen happens themn the human would win it

comp = random.randint(0,2)
user = int(input("enter 0 for snake , 1 for water  ,2 for gun:"))
score = check(comp,user)

print(f"you choose{user}")
print(f"computer chose{comp}")

if score == 0:
    print("it is a draw")
elif score == -1:
    print("you lose")
else:
    print("you won")
