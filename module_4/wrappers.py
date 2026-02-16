money = int(input("How much money do you have: "))
candies = money / 4
wrappers = candies

while wrappers >= 3:
    wrappers-=2
    candies+=1

print(f"You can purchase {candies:.0f} candy bars!")