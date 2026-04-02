class People:

    # KNOW THAT THE __init__() function is NOT required
    def __init__(self, age, name): # constructor 
        self.age = age
        self.name = name

# self sometimes not used in special caes but almost alwsyd expcet to use it
# p1 > p2 l(p1,p2)


    def say_hi(self):
        print(f"my name is {self.name}")
    
    def get_older(self):
        #age+= 10

#p = People(19, 'natbat')
#p2 = People(32, 'peeps')

#print(p.age, p2.age)
#p.get_older() #does not take in paramaters if its just self
#print(p.age,p2.age, People.age)


class Air:
    def blow_wind(self):
        print("i am windy")

a = Air()
a.blow_wind()



