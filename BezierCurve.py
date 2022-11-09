from asyncio import events
from tkinter import *
import math
import os



def moveAction(event, num):
    pointList = []
    x = event.x
    y = event.y

    x0 = x - 5
    y0 = y - 5
    x1 = x + 5
    y1 = y + 5
    canvas.coords(f"rectangle{num}", (x0, y0, x1, y1))  #update the point's position
    input_points[num - 1] = [x, y]  # update the point's coordinate

    canvas.delete("line")
    canvas.create_line(Bezier(0, pointList, input_points), width=2, tags="line")


def Bezier(t, pointList, input_points):
    if t > 1:
        return
    else:
        x = formula(0, t)
        y = formula(1, t)
        pointList.append((x, y))
        Bezier(round(t + 0.002, 5), pointList, input_points)
        return pointList

def formula(point, t):
    return input_points[0][point] * math.pow(1 - t, 3) + \
            3 * input_points[1][point] * t * math.pow((1 - t), 2) + \
            3 * input_points[2][point] * math.pow(t, 2) * (1 - t) + \
            input_points[3][point] * math.pow(t, 3)

#point's function
def create_rectangle(x, y, number):
    x0 = x - 5
    y0 = y - 5
    x1 = x + 5
    y1 = y + 5
    return canvas.create_rectangle(x0, y0, x1, y1, fill='white', tags=f"rectangle{number}")


def main(event):
    if len(input_points) == 4: #input four points
        return
    num = create_rectangle(event.x, event.y, len(input_points) + 1)
    input_points.append([event.x, event.y])

    canvas.tag_bind(f"rectangle{num}", "<B1-Motion>", lambda event: moveAction(event, num))
    
    if len(input_points) == 4:
        canvas.create_line(Bezier(0, pointList, input_points), width=2, tags="line")


if __name__ == '__main__':
    #Setting parameters
    input_points, bezierCurve, pointList = [], [], []
    width, height = 400, 400
    windows = Tk()
    windows.title('Bezier Curve')
    windows.geometry(f'{width}x{height}')
    windows.resizable(False, False) 
    #Create Canvas
    canvas = Canvas(windows, width=width, height=height)
    canvas.pack()
    canvas.bind("<Button-1>", main) # Bind click event

    windows.mainloop()# run

