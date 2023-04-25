#imports
from tkinter import *
import Dot_List
import time
import Direction_Vector as DV
import Canvas_Vars

def init_dots():
    global canvas, goal
    goal = canvas.create_oval(Canvas_Vars.goal_coords, fill="red")
    for i in Dot_List.dot_list:
        i.dot_object = canvas.create_oval(i.dot_coords, fill=i.color)
        canvas.tag_lower(i.dot_object)
    canvas.update()

def reset_dots():
    global canvas
    canvas.delete('all')

def move_dots():
    global canvas
    x = 0
    num_done = 0
    while(x < Dot_List.dot_list[0].brain.direction_length and not Dot_List.all_dots_done()):
        y=0
        for i in Dot_List.dot_list:
            if not i.dead and not i.reached_goal:
                canvas.coords(i.dot_object, i.dot_coords)
                i.updatePosition()
                if i.dot_coords[0] <= Canvas_Vars.sudo_border:
                    i.dead = True
                    i.dot_coords[0] = Canvas_Vars.sudo_border
                    i.dot_coords[2] = Canvas_Vars.sudo_border+2*i.dot_rad
                    canvas.coords(i.dot_object, i.dot_coords)

                if i.dot_coords[2] >= Canvas_Vars.canvas_width-Canvas_Vars.sudo_border:
                    i.dead = True
                    i.dot_coords[2] = Canvas_Vars.canvas_width-Canvas_Vars.sudo_border
                    i.dot_coords[0] = Canvas_Vars.canvas_width-Canvas_Vars.sudo_border-2*i.dot_rad
                    canvas.coords(i.dot_object, i.dot_coords)

                if i.dot_coords[1] <= Canvas_Vars.sudo_border:
                    i.dead = True
                    i.dot_coords[1] = Canvas_Vars.sudo_border
                    i.dot_coords[3] = Canvas_Vars.sudo_border+2*i.dot_rad
                    canvas.coords(i.dot_object, i.dot_coords)

                if i.dot_coords[3] >= Canvas_Vars.canvas_height-Canvas_Vars.sudo_border:
                    i.dead = True
                    i.dot_coords[3] = Canvas_Vars.canvas_height-Canvas_Vars.sudo_border
                    i.dot_coords[1] = Canvas_Vars.canvas_height-Canvas_Vars.sudo_border-2*i.dot_rad
                    canvas.coords(i.dot_object, i.dot_coords)
                dot_centerpoint =  DV.vector(i.pos.x, i.pos.y)
                dot_centerpoint.centerpoint(i.dot_rad)
                if (dot_centerpoint.intersecting_circles(Canvas_Vars.goal_centerpoint, i.dot_rad, Canvas_Vars.goal_rad)):
                    i.reached_goal = True
                canvas.tag_lower(i.dot_object)
            y+=1
        canvas.update()
        x += 1
        time.sleep(0.001)
    
    Dot_List.next_gen()


#window
window = Tk()
window.geometry("500x600")
window.resizable(False,False)

#frame
#frame = Tkinter.Frame(window, height=600, width=500, bg="gray")
  
#canvas
canvas = Canvas(window, height=Canvas_Vars.canvas_height, width=Canvas_Vars.canvas_width, bg="white")
canvas.pack()
#frame.pack()

#goal
for i in range(50):
    reset_dots()
    init_dots()
    time.sleep(0.001)
    move_dots()
    time.sleep(0.25)
window.mainloop()