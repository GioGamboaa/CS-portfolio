'''
Giovani Roliz S. Gamboa 9-Samat
'''

class Glassware :
    def __init__(self,kindofglassware):
        self.kindofglassware =kindofglassware
        print("I have ", self.kindofglassware)
    

class Beaker(Glassware):
    def __init__ (self):
        super().__init__("beaker")
        
class Tray:
    def __init__(self):
        self.beakers = [Beaker() for i in range (5)]
        print("Tray created with ", len(self.beakers), " beakers")
        
    def __del__(self):
        self.beakers.clear()
        print("Tray gone, beakers erased")

       
       
        


tray = Tray()

del tray

print(tray)#to prove its gone
