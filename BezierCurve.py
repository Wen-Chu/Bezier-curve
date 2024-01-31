import tkinter as tk

def BezierCurve(t, point, xu, yu): # Calculate Bezier Curve
    if round(xu, 5) == point[3][0] and round(yu, 5) == point[3][1]:
       Beziercanvas.create_line(bezierCurve, tag='line', width=2)
    else:
        xu = pow(1 - t, 3) * point[0][0] + 3 * t * pow(1 - t, 2) * point[1][0] + 3 * pow(t, 2) * (1 - t) * point[2][0] + pow(t, 3) * point[3][0]
        yu = pow(1 - t, 3) * point[0][1] + 3 * t * pow(1 - t, 2) * point[1][1] + 3 * pow(t, 2) * (1 - t) * point[2][1] + pow(t, 3) * point[3][1]
        bezierCurve.append((xu, yu))
        BezierCurve(t+0.002, point, xu, yu)

def moveFunc(event, rec): # when any point is moved, recalculate the Bezier Curve
    if len(rectangle) < 4:
        return
    bezierCurve.clear()
    Beziercanvas.delete("line")
    Beziercanvas.coords(rectangle[rec-1], [event.x-5, event.y-5, event.x+5, event.y+5])
    pointList[rec-1][0] = event.x
    pointList[rec-1][1] = event.y
    bezierCurve.append((pointList[0][0], pointList[0][1]))
    BezierCurve(0.0, pointList, pointList[0][0], pointList[0][1])

def createRectangle(event): # When click the canvas, create a point (most 4 points)
    if len(rectangle) < 4:
        item = Beziercanvas.create_rectangle(event.x-5, event.y-5, event.x+5, event.y+5, fill='white')
        rectangle.append(item)
        pointList.append([event.x, event.y])
        Beziercanvas.tag_bind(item, "<B1-Motion>", lambda event: moveFunc(event, item))
        if len(rectangle) == 4:
            BezierCurve(0.0, pointList, pointList[0][0], pointList[0][1])
if __name__ == '__main__':
    win = tk.Tk()
    win.title('Bezier Curve')
    win.geometry('600x600')
    Beziercanvas = tk.Canvas(win, width=600, height=600)
    Beziercanvas.pack()
    rectangle = []
    pointList = []
    bezierCurve = []
    Beziercanvas.bind("<Button-1>", createRectangle)
    win.mainloop()