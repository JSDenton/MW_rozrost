import random
class cell:
    def __init__(self, id=0):
        self.id = id
        
        
    id = 0
    red = 0
    blue = 0
    green = 0
    color = 0 #is defined by mix_color() method, which mixes the 

    def change_color(self, id):
        self.id = id

    def mix_color(self):
        self.color = self.red*256*256 + self.green*256 + self.blue

    def rand_color(self):
        self.red = random.randint(0,255)
        self.blue = random.randint(0,255)
        self.green = random.randint(0,255)
        self.mix_color()
    