

from copy import deepcopy
from cell import cell
from PyQt6.QtCore import QObject
from PyQt6 import QtCore
import random
import math

def get_max(arr):
    max = 0
    iter = 0
    for i in arr:
        if i>max and iter>0:
            max = i
    return max


class plane(QObject):
    space = []
    width = 0
    height = 0
    color_counts = [] #holds cell count for every color
    finished = QtCore.pyqtSignal()
    refresh_func = QtCore.pyqtSignal(int)
    
    #def refresh_func(self): pass
    

    def __init__(self, x:int, y:int, color_num:int):
        super(plane, self).__init__()
        self.width = x
        self.height = y
        self.space = [[cell(id=0) for i in range(x)] for j in range(y)]
        self.color_num = color_num+1
        self.color_counts = [0 for i in range(color_num+1)]
        self.color_counts[0] = x*y
        self.refresh_func.emit(1)
        self.neighbourhood_type = 'Random'
        self.boundary_type = 'Moore'

    #checks if this new cell is available and then places it in that spot
    #returns 1 if success, 0 if failure
    def set_new_cell(self, x, y, id): 
        #print("change")
        #print(id)
        if(self.space[x][y].id==0):
            self.space[x][y] = cell(id=id)
            self.color_counts[0]-=1
            self.color_counts[id]+=1
            return 1
        else: return 0



    def generate_space(self, nucleon_count, type, get_points): #generates space with nucleon_count cells
        i = 0
        print("start generating..")
        #print(type)
        match type:
            case 'Random':
                while i<nucleon_count:
                    x = random.randint(0,self.height-1)
                    y = random.randint(0,self.width-1)
                    i += self.set_new_cell(x, y, i)
            case 'Regular':
                while i<nucleon_count:
                    x = int((self.height*i/nucleon_count)**0.5)
                    y = int((self.width*i/nucleon_count)**0.5)
                    self.space[x][y] = cell(id=id)
            case 'Custom':
                while i<nucleon_count:
                    x, y = get_points() #TODO: create function that gets point with mouseclick
                    if x!=-1:
                        i += self.set_new_cell(x, y, i)
        print("end generating..")
    

    def boundaries(self, x, y):
        if self.boundary_type=='Periodic':
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
        return y, x

    #decides which color gets new cell; type (String) - type of neighbourhood;
    #  boundary_type (int) - type of boundary condition
    def get_neighbours_color(self, y, x): 
        neigh_colors = [0 for i in range(self.color_num)]
        
        match self.neighbourhood_type:
            case 'von Neumann':     
                for i in range(-2,3):
                    #print(i)
                    if i==0:
                        continue
                    dx, dy = self.boundaries(x+(i%2), y+(i//2))
                    if self.space[dx][dy].id!=0: #0 is default cell (not filled with any color)
                        neigh_colors[self.space[dx][dy].id]+=1
            case 'Moore':
                for i in range(-1,2):
                    for j in range(-1,2):
                        dx, dy = self.boundaries(x+i, y+j)
                        if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                            neigh_colors[self.space[dx][dy].id]+=1
            case 'Pentagonal':
                pent_type = random.randint(0,3)
                
                match pent_type:
                    case 0: #right side is off
                        for i in range(-1,1):
                            for j in range(-1,2):
                                dx, dy = self.boundaries(x+i, y+j)
                                if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                                    neigh_colors[self.space[dx][dy].id]+=1
                    case 1: #left side is off
                        for i in range(0,2):
                            for j in range(-1,2):
                                dx, dy = self.boundaries(x+i, y+j)
                                if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                                    neigh_colors[self.space[dx][dy].id]+=1
                    case 2: #upper side is off
                        for i in range(-1,2):
                            for j in range(0,2):
                                dx, dy = self.boundaries(x+i, y+j)
                                if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                                    neigh_colors[self.space[dx][dy].id]+=1
                    case 3: #lower side is off
                        for i in range(-1,2):
                            for j in range(-1,1):
                                dx, dy = self.boundaries(x+i, y+j)
                                if i!=0 and j!=0 and self.space[dx][dy].id!=0:
                                    neigh_colors[self.space[dx][dy].id]+=1

            case 'Hexagonal':
                hex_type = math.floor(random.random()*2)

                if hex_type==0:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            dx, dy = self.boundaries(x+i, y+j)
                            if i!=0 and j!=0 and (i!=1 and j!=-1) and self.space[dx][dy].id!=0 :
                                neigh_colors[self.space[dx][dy].id]+=1
                else:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            dx, dy = self.boundaries(x+i, y+j)
                            if i!=0 and j!=0 and (i!=-1 and j!=1) and self.space[dx][dy].id!=0 :
                                neigh_colors[self.space[dx][dy].id]+=1

        neigh_colors = [[i, neigh_colors[i]] for i in range(len(neigh_colors))]
        neigh_colors.sort(key=lambda d:d[1],reverse=True)
        
        chosen_color = 0
        if neigh_colors[0][1]!=0:
            #print(neigh_colors)
            if neigh_colors[0][1] == neigh_colors[1][1]:
                chosen_color = get_max(self.color_counts)
            else:
                chosen_color = neigh_colors[0][0]
        self.space[y][x].change_color(chosen_color)
        #print(f"{self.color_counts} {chosen_color}")
        self.color_counts[chosen_color] += 1
        self.color_counts[0] -=1
        
    def run(self):
        iters = 0
        print("start main loop...")
        while True:
            for i in range(self.height):
                for j in range(self.width):
                    self.get_neighbours_color(i, j)
            if(iters%20==0):
                print("refreshing...")
                self.refresh_func.emit(1)                
            iters+=1
            if self.color_counts[0]<=0: #stop criterium - when there's no more white "tiles"
                break
        print("finished...")
        self.finished.emit()

    def send_args(self, type, boundaries_type, refresh):
        self.neighbourhood_type = type
        self.boundary_type = boundaries_type
        self.refresh_func = refresh
        print("args_sent")
