class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ") #don't fully understand this line
        print()
        
class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"]) #don't fully undersatnd how this works

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Boom","Splash","Bop"])
        
    def countoff(self):
        for i in range(1,5):
            print(i, end=" ")
            print("and uh")
            
drummer = Drummer()
guitar = Guitarist()
bass = Bassist()
            
class Band(Musician):
    def __init__(self):
        super().__init__(["Yea!!","Yea!!!","Yea!!"])
        
    def group_solo(self):
        drummer.countoff()
        guitar.solo(5)
        
            
            
            
          
        

rockers = Band()
nigel = Guitarist()
Jo = Drummer()


nigel.solo(4)
rockers.group_solo()

