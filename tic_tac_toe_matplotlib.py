
import tkinter as Tk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, PathPatch
import numpy as np
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.widgets import TextBox
from matplotlib.widgets import Button
import os,signal
import sys
import psutil
import logging
cmap = plt.get_cmap('spring') #define the colors of the plot 
colors = [cmap(i) for i in np.linspace(0.1, 0.9, 5+1)]  

def check_exist(i,j,k):
    if 0<=i<=2 and 0<=j<=2 and 0<=k<=2:
        return True
    else:
        return False

def check_3d_cube(cube_3d,turn):
    exists=list()
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if cube_3d[i][j][k]==turn:
                    if(check_exist(i+1,j,k)):
                        if(cube_3d[i+1][j][k]==turn):
                            if(check_exist(i+2,j,k)):
                                if(cube_3d[i+2][j][k]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,j*3,k*3])
                    if(check_exist(i,j+1,k)):
                        if(cube_3d[i][j+1][k]==turn):
                            if(check_exist(i,j+2,k)):
                                if(cube_3d[i][j+2][k]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([i*3,(j+2)*3,k*3])
                    if(check_exist(i,j,k+1)):
                        if(cube_3d[i][j][k+1]==turn):
                            if(check_exist(i,j,k+2)):
                                if(cube_3d[i][j][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([i*3,j*3,(k+2)*3])
                    if(check_exist(i+1,j+1,k)):
                        if(cube_3d[i+1][j+1][k]==turn):
                            if(check_exist(i+2,j+2,k)):
                                if(cube_3d[i+2][j+2][k]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j+2)*3,k*3])
                    if(check_exist(i+1,j,k+1)):
                        if(cube_3d[i+1][j][k+1]==turn):
                            if(check_exist(i+2,j,k+2)):
                                if(cube_3d[i+2][j][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,j*3,(k+2)*3])
                    if(check_exist(i,j+1,k+1)):
                        if(cube_3d[i][j+1][k+1]==turn):
                            if(check_exist(i,j+2,k+2)):
                                if(cube_3d[i][j+2][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([i*3,(j+2)*3,(k+2)*3])
                    if(check_exist(i+1,j-1,k)):
                        if(cube_3d[i+1][j-1][k]==turn):
                            if(check_exist(i+2,j-2,k)):
                                if(cube_3d[i+2][j-2][k]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j-2)*3,k*3])
                    if(check_exist(i+1,j,k-1)):
                        if(cube_3d[i+1][j][k-1]==turn):
                            if(check_exist(i+2,j,k-2)):
                                if(cube_3d[i+2][j][k-2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,j*3,(k-2)*3])
                    if(check_exist(i,j+1,k-1)):
                        if(cube_3d[i][j+1][k-1]==turn):
                            if(check_exist(i,j+2,k-2)):
                                if(cube_3d[i][j+2][k-2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([i*3,(j+2)*3,(k-2)*3])
                    if(check_exist(i+1,j+1,k+1)):
                        if(cube_3d[i+1][j+1][k+1]==turn):
                            if(check_exist(i+2,j+2,k+2)):
                                if(cube_3d[i+2][j+2][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j+2)*3,(k+2)*3])
                    if(check_exist(i+1,j-1,k+1)):
                        if(cube_3d[i+1][j-1][k+1]==turn):
                            if(check_exist(i+2,j-2,k+2)):
                                if(cube_3d[i+2][j-2][k+2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j-2)*3,(k+2)*3])                
                    if(check_exist(i+1,j+1,k-1)):
                        if(cube_3d[i+1][j+1][k-1]==turn):
                            if(check_exist(i+2,j+2,k-2)):
                                if(cube_3d[i+2][j+2][k-2]==turn):
                                    exists.append([i*3,j*3,k*3])
                                    exists.append([(i+2)*3,(j+2)*3,(k-2)*3])  
    return (exists)              
def cube(a,b,c,l,color): #plots a cube of side l at (a,b,c)  
        for ll in [0,l]:
            for i in range(3):
                dire= ["x","y","z"]
                xdire = [b,a,a] 
                ydire = [c,c,b]
                zdire = [a,b,c]
                side = Rectangle((xdire[i],ydire[i]),height=1,width=1,edgecolor='black',facecolor=color,alpha=0.5)
                ax.add_patch(side)
                art3d.pathpatch_2d_to_3d(side, z=zdire[i]+ll, zdir=dire[i])
X=[[0,3,6,0,0,3,3,6,6],[0,3,6,0,0,3,3,6,6],[0,3,6,0,0,3,3,6,6]]
Y=[[0,0,0,3,6,3,6,3,6],[0,0,0,3,6,3,6,3,6],[0,0,0,3,6,3,6,3,6]]
Z=[[0,0,0,0,0,0,0,0,0],[3,3,3,3,3,3,3,3,3],[6,6,6,6,6,6,6,6,6]]
sizes=[1,1,1,1,1,1,1,1,1]

def plotter3D(X,Y,Z,sizes,color): #run cube(a,b,c,l) over the whole data set 
    for iX in range(len(X)):
        x = X[iX]
        y = Y[iX]
        z = Z[iX]
        for ix in range(len(x)): 
            cube(x[ix],y[ix],z[ix],sizes[iX],color)
turn=0
exists=list()
cube_3d=list()
def restart_program():
    """Restarts the current program, with file objects and descriptors
       cleanup
    """
    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except Exception as e:
        logging.error(e)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def playagain(event):
    plt.close()
    restart_program()
def game(user_input):
    global turn,exists
    if(len(exists)<2):
        if(user_input==""):
            return False
        if(user_input=="quit"):
            return False
        if(user_input.isnumeric()==False):
            print("wrong input1")
            return False
        user_input=list(user_input)
        if(len(user_input)<3):
            print("wrong input2")
            return False
        for i in range(0,3):
            user_input[i]=int(user_input[i])
        if(user_input[0]>2 or user_input[1]>2 or user_input [2]>2):
            print("try again wrong input")
            return False
        if(cube_3d[user_input[0]][user_input[1]][user_input[2]]!="-"):
            print("cube already colored")
            return False
        else:
            cube_3d[user_input[0]][user_input[1]][user_input[2]]=turn
        print(cube_3d)
        X=[[(user_input[0])*3]]
        Y=[[(user_input[1])*3]]
        Z=[[(user_input[2])*3]]
        if(turn==0):
            plotter3D(X,Y,Z,sizes,"red")
        else:
            plotter3D(X,Y,Z,sizes,"blue")   
        exists=check_3d_cube(cube_3d,turn)
        print(exists)
        if(len(exists)>=2):
            for i in range(0,len(exists),2):
                ax.plot([exists[i][0]+0.5,exists[i+1][0]+0.5],[exists[i][1]+0.5,exists[i+1][1]+0.5],[exists[i][2]+0.5,exists[i+1][2]+0.5],linewidth=5,color="black")
                ax.text(3,3,10, 'Game over', style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

                
        if(turn==1):
            turn=0
        else:
            turn=1 
        plt.pause(0.05)
        return True

fig = plt.figure() #open a figure 
ax=fig.add_subplot(projection='3d') #make it 3d 
plotter3D(X,Y,Z,sizes,"pink") #generate the cubes from the data set 
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            ax.text(i*3+0.25,j*3+0.25,k*3+1.25,str(i)+str(j)+str(k),fontweight ='extra bold')

ax.set_xlim3d(0, 7) #set the plot ranges 
ax.set_ylim3d(0, 7)
ax.set_zlim3d(0, 7)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
ax.axes.xaxis.set_ticks([])
ax.axes.zaxis.set_ticks([])
try_again=True
for i in range(0,3):
    tempk=[]
    for j in range(0,3):
        tempj=["-","-","-"]
        tempk.append(tempj)
    cube_3d.append(tempk)
print(cube_3d)
exists=check_3d_cube(cube_3d,turn)
graphBox = fig.add_axes([0.1, 0.05, 0.1, 0.075])
txtBox = TextBox(graphBox, "Input: ")
plt.pause(0.05)
try_again=txtBox.on_submit(game)
txtBox.set_val("")  
axButn3 = plt.axes([0.5, 0.05, 0.3, 0.075])
btn3 = Button(axButn3, label="Play Again", color='pink', hovercolor='tomato')
btn3.on_clicked(playagain)
plt.pause(0.05)
plt.show()
