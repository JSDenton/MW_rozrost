

from turtle import width
from sklearn.decomposition import SparseCoder
import cell
import random

class plane:
    def __init__(self, x, y, color_num):
        self.width = x
        self.height = y
        self.space = [[cell(0) for i in range(x)] for j in range(y)]
        self.color_num = color_num
        self.color_counts = [0 for i in range(color_num)]
        self.color_counts[0] = x*y
    space = []
    width = 0
    height = 0
    color_counts = []

    #checks if this new cell is available and then places it in that spot
    #returns 1 if success, 0 if failure
    def set_new_cell(self, x, y, id): 
        if(self.space[x][y].id==0):
            self.space[x][y] = cell(id)
            return 1
        else: return 0


    def generate(self, nucleon_count, type):
        i = 0
        match type:
            case 'Random':
                while i<nucleon_count:
                    x = random.random() * self.width
                    y = random.random() * self.height
                    i += self.set_new_cell(x, y, i)
            case 'Regular':
                while i<nucleon_count:
                    x = self.width*i/nucleon_count**0.5
                    y = self.height*i/nucleon_count**0.5
                    self.space[x][y] = cell(id)
            case 'Custom':
                while i<nucleon_count:
                    x, y = get_point() #TODO: create function that gets point with mouseclick
                    if x!=-1:
                        i += self.set_new_cell(x, y, i)
    
    def get_neighbours_color(self, x, y, type, boundary_type):
        neigh_colors = [0 for i in range(self.color_num)]
        match type:
            case 'von Neumann':                
                for i in range(-1, 2, 2):
                    for j in range(-1, 2, 2):
                        if self.space[x+i][y+i].id!=0:
                            neigh_colors[self.space[x+i][y+i].id]+=1
                
        neigh_colors.sort()
        chosen_color = 0
        if neigh_colors[0] == neigh_colors[1]:
            #TODO: co jak sąsiedzi mają remis i trzeba wyłonić "zwycięzcę"
        else:
            chosen_color = neigh_colors[0]
        self.space[x][y] = cell()
