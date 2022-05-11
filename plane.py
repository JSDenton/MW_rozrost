

from turtle import width
from sklearn.decomposition import SparseCoder
import cell
import random
import math

def get_max(arr):
    max = 0
    for i in arr:
        if i>max:
            max = i
    return max
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
    color_counts = [] #holds cell count for every color

    #checks if this new cell is available and then places it in that spot
    #returns 1 if success, 0 if failure
    def set_new_cell(self, x, y, id): 
        if(self.space[x][y].id==0):
            self.space[x][y] = cell(id)
            return 1
        else: return 0


    def generate(self, nucleon_count, type): #generates space with nucleon_count cells
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
    

    def boundaries(self, x, y, boundary_type):
        if boundary_type==0:
            x=x%self.width
            y=y%self.height
        else:
            if x<0:
                x=0
            elif x>=self.width:
                x = self.width-1
            elif y<0:
                y=0
            elif y>=self.height:
                y = self.height - 1
        return x, y

    #decides which color gets new cell; type (String) - type of neighbourhood;
    #  boundary_type (int) - type of boundary condition (0 - periodic, 1 - absolute)
    def get_neighbours_color(self, x, y, type, boundary_type): 
        neigh_colors = [0 for i in range(self.color_num)]
        match type:
            case 'von Neumann':                
                for i in range(-2,3):
                    if i==0:
                        continue
                    dx, dy = self.boundaries(x+i%2, y+i//2, boundary_type)
                    if self.space[dx][dy].id!=0: #0 is default cell (not filled with any color)
                        neigh_colors[self.space[dx][dy].id]+=1
            case 'Moore':
                for i in range(-1,2):
                    for j in range(-1,2):
                        dx, dy = self.boundaries(x+i, y+j, boundary_type)
                        if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                            neigh_colors[self.space[dx][dy].id]+=1
            case 'Pentagonal':
                pent_type = math.floor(random.random()*4)
                
                match pent_type:
                    case 0: #right side is off
                        for i in range(-1,1):
                            for j in range(-1,2):
                                dx, dy = self.boundaries(x+i, y+j, boundary_type)
                                if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                                    neigh_colors[self.space[dx][dy].id]+=1
                    case 1: #left side is off
                        for i in range(0,2):
                            for j in range(-1,2):
                                dx, dy = self.boundaries(x+i, y+j, boundary_type)
                                if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                                    neigh_colors[self.space[dx][dy].id]+=1
                    case 2: #upper side is off
                        for i in range(-1,2):
                            for j in range(0,2):
                                dx, dy = self.boundaries(x+i, y+j, boundary_type)
                                if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                                    neigh_colors[self.space[dx][dy].id]+=1
                    case 3: #lower side is off
                        for i in range(-1,2):
                            for j in range(-1,1):
                                dx, dy = self.boundaries(x+i, y+j, boundary_type)
                                if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                                    neigh_colors[self.space[dx][dy].id]+=1

            case 'Hexagonal':
                hex_type = math.floor(random.random()*2)

                if hex_type==0:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            dx, dy = self.boundaries(x+i, y+j, boundary_type)
                            if i!=0 and j!=0 and (i!=1 and j!=-1) and self.space[dx][dy].id!=0 :
                                neigh_colors[self.space[dx][dy].id]+=1
                else:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            dx, dy = self.boundaries(x+i, y+j, boundary_type)
                            if i!=0 and j!=0 and (i!=-1 and j!=1) and self.space[dx][dy].id!=0 :
                                neigh_colors[self.space[dx][dy].id]+=1

                
        neigh_colors.sort()
        chosen_color = 0
        if neigh_colors[0]!=0:
            if neigh_colors[0] == neigh_colors[1]:
                #TODO: co jak sąsiedzi mają remis i trzeba wyłonić "zwycięzcę"
                chosen_color = get_max(self.color_counts)
            else:
                chosen_color = neigh_colors[0]
        self.space[x][y] = cell(chosen_color)
        self.color_counts[chosen_color] += 1