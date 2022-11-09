import tkinter as tk
import math

def Height(level, val): #get the length of first branch
    global height

    if level <= int(spinBox.get()) and level < 7:
        val += pow(0.75, level-1)
        Height(level + 1, val)
    else:
        height = round(300/val, 5)

def RC_A(level, x1, y1, angle, wid,baseAngle): #dendrite(Fractal branch)
    global height

    if angle-30 >= baseAngle+90 or angle+30 <= baseAngle-90:
        return 

    if level > int(spinBox.get()):
        return

    if level < 7:
        if level % 2 == 0: #even number
            x2 = x1 - int(math.cos(math.radians(angle)) * (1/math.sin(math.radians(60))) * pow(0.75, level - 1) * height)
            y2 = y1 - int(math.sin(math.radians(angle)) * (1/math.sin(math.radians(60))) * pow(0.75, level - 1) * height)
        else: #odd number
            x2 = x1 - int(math.cos(math.radians(angle)) * pow(0.75, level - 1) * height)
            y2 = y1 - int(math.sin(math.radians(angle)) * pow(0.75, level - 1) * height)

        Treecanvas.create_line(x1, y1, x2, y2, fill="#%02x%02x%02x" % (R+20*level, G+10*level, B), width=wid)

        RC_A(level + 1, x2, y2, angle + 30, wid - 2,baseAngle)
        RC_A(level + 1, x2, y2, angle - 30, wid - 2,baseAngle)
    else:
        RC_B_1(level, x1, y1, 15, 4)

def RC_B_1(level, cX, cY, r, wid): #for fractal circle
    if level > int(spinBox.get()):
        return
    if level == 7 :
        Treecanvas.create_oval(cX-r, cY-r, cX+r, cY+r, outline='white', width=wid)
        RC_B_1(level+1, cX, cY, r, wid)
    else : 
        RC_B_2(level,cX,cY,r,30,wid-1,)

def RC_B_2(level,cX,cY,r,angle,wid, baseAngle = 0) :
    if angle>330 : 
        return
    if level > int(spinBox.get()):
        return

    x = cX + math.sin(angle*math.pi/180) *(r)
    y = cY + math.cos(angle*math.pi/180) *(r)

    r=r/2 #下一層
    Treecanvas.create_oval(x-r, y-r, x+r, y+r, outline='white', width=wid)
    RC_B_2(level+1,x,y,r,30,wid-1,) #next layer

    RC_B_2(level,cX,cY,r*2,angle+60,wid,30) #回到同一層

def RC_C(level): #fractal dendrite
    if level >5: 
        return RC_C(5)
    else:
        if level == 1: return 2
        elif level == 2: return 3
        return RC_C(level-1) + RC_C(level-2)

def RC_C_rot(rot, baseAngle): #fractal dendrite's angle
    if baseAngle > 360 + 90: #Because start angle is 90
        return 
    else:
        RC_A(1, 600, 350, baseAngle, 15, baseAngle)
        RC_C_rot(rot, baseAngle+rot)

def Fractal_Pattern():
    Treecanvas.delete(tk.ALL)
    Height(1, 0)
    RC_A(1, 600, 350, 90, 15, 90)
    rot= 360/RC_C(int(spinBox.get())) #calculate the rot
    RC_C_rot(rot,baseAngle = 90)


if __name__ == "__main__":
    win = tk.Tk()
    win.title('Fractal Pattern')
    win.geometry('1200x1200')
    Treecanvas = tk.Canvas(win, width=1200, height=1200)
    Treecanvas.pack()
    lable = tk.Label(Treecanvas, text="Level")

    R, G, B = 0, 102, 204

    spinBox = tk.Spinbox(Treecanvas, from_=1, to=9, width=5, command=Fractal_Pattern) #改變層數才會呼叫
    Fractal_Pattern() #第一層

    lable.place(x=10, y=10, anchor='nw')
    spinBox.place(x=45, y=10, anchor='nw')
    win.mainloop()
