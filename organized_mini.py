import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Canvas
from tkinter import *

#create window
window = tk.Tk()
frame = Frame(window)
frame.pack()
window.title("Mini-project")

#window dimensions
window.configure(width=1500, height=800)
window.configure(bg='lightgray')

# move window to the center of the screen
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

#create canvas to draw and bind it to the window
canvas = Canvas(window, height=windowHeight-100, width=windowWidth-100)
canvas.pack()

global x, y
global radius
radius = 10

vertex_centers = []
circles = []
edge_vertices = []
lines = []

graph = {} 
# represent the graph as a dictionary where the vertices are keys and the value of each vertex is its adjacency list
# vertices are circle objects (tags included
# each circle has a tag that stores its center as a 3-tuple (center.x, center.y, color, visited_flag)

color_dict = {} # a dicionary used to keep track of colors used

def place_vertex(event):

    if (vertex_bool.get() == 1 and edge_bool.get() == 0):
        # x increases from left to right
        # y increases from up to down
        x0 = event.x - radius
        y0 = event.y - radius
        x1 = event.x + radius
        y1 = event.y + radius
        center = ((x0+x1)/2.0, (y0+y1)/2.0)
        vertex_centers.append(center)

        tag = (center[0], center[1], "black", False) #the tag for each circle is its center

        #fill the circle black
        circle = canvas.create_oval(x0, y0, x1, y1, fill = "black", tags = tag)

        if ("black" not in color_dict):
            color_dict["black"] = 1
        else:
            color_dict["black"] += 1

        circles.append(circle)

        graph[circle] = []

        return 0

#helper function to determine if the user clicked on a vertex already drawn on the screen
def click_on_vert(click_x, click_y):
    for circle in circles:
        #bounding box for a given vertex
        tag = canvas.gettags(circle)
        
        left = int(float(tag[0]))-radius
        right = int(float(tag[0]))+radius
        top = int(float(tag[1]))-radius
        bottom = int(float(tag[1]))+radius

        if (left <= click_x and click_x <= right and top <= click_y and click_y <= bottom):
            return circle

    #if vertex not found, no vertex was clicked on so return 0         
    return 0
    

def draw_edge(event):  
    if (vertex_bool.get() == 0 and edge_bool.get() == 1):
        circle_clicked_on = click_on_vert(event.x, event.y)
        if (circle_clicked_on != 0):
            edge_vertices.append(circle_clicked_on)

        if (len(edge_vertices) > 0 and len(edge_vertices)%2 == 0):
            last = edge_vertices.pop() # a circle object
            second_to_last = edge_vertices.pop()

            last_tags = canvas.gettags(last)
            second_to_last_tags = canvas.gettags(second_to_last)

            if (last_tags[2] == second_to_last_tags[2] and no_edge_bt_same_color_vertices.get() == 1):
                #CANNOT CREATE AN EDGE BETWEEN TWO VERTICES LABELED THE SAME COLOR WHEN IN color_mode
                edge_vertices.append(second_to_last)
                edge_vertices.append(last)
            else:
                graph[last].append(second_to_last)
                graph[second_to_last].append(last)

                tag = (last_tags[0], last_tags[1], second_to_last_tags[0], second_to_last_tags[1])
                line = canvas.create_line(last_tags[0], last_tags[1], second_to_last_tags[0], second_to_last_tags[1], tags = tag)
                lines.append(line)

#CHANGE THE COLORS OF CIRCLES
def color_vertex_red(event):
    if (vertex_bool.get() == 0 and edge_bool.get() == 0 and blue_bool.get() == 0 and red_bool.get() == 1 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 0):
        circle_clicked_on = click_on_vert(event.x, event.y) #use circle objects
        if (circle_clicked_on != 0):
            circle_clicked_on_tags = canvas.gettags(circle_clicked_on)
            for circle in circles:
                tag = canvas.gettags(circle)
                if ((abs(float(circle_clicked_on_tags[0]) - float(tag[0]))) < .0001 and (abs(float(circle_clicked_on_tags[1]) - float(tag[1]))) < .0001):
                    canvas.itemconfig(circle, fill = "red")
                    new_tag = (circle_clicked_on_tags[0], circle_clicked_on_tags[1], "red")
                    canvas.itemconfig(circle, tags = new_tag)

                    if (tag[2] in color_dict):
                        color_dict[tag[2]] -= 1

                    if ("red" not in color_dict):
                        color_dict["red"] = 1
                    else:
                        color_dict["red"] += 1

def color_vertex_blue(event):
    if (vertex_bool.get() == 0 and edge_bool.get() == 0 and blue_bool.get() == 1 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 0):
        circle_clicked_on = click_on_vert(event.x, event.y)
        if (circle_clicked_on != 0):
            circle_clicked_on_tags = canvas.gettags(circle_clicked_on)
            for circle in circles:
                tag = canvas.gettags(circle)
                if ((abs(float(circle_clicked_on_tags[0]) - float(tag[0]))) < .0001 and (abs(float(circle_clicked_on_tags[1]) - float(tag[1]))) < .0001):
                    canvas.itemconfig(circle, fill = "blue")
                    new_tag = (circle_clicked_on_tags[0], circle_clicked_on_tags[1], "blue")
                    canvas.itemconfig(circle, tags = new_tag)

                    if (tag[2] in color_dict):
                        color_dict[tag[2]] -= 1

                    if ("blue" not in color_dict):
                        color_dict["blue"] = 1
                    else:
                        color_dict["blue"] += 1

def color_vertex_green(event):
    if (vertex_bool.get() == 0 and edge_bool.get() == 0 and blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 1 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 0):
        circle_clicked_on = click_on_vert(event.x, event.y)
        if (circle_clicked_on != 0):
            circle_clicked_on_tags = canvas.gettags(circle_clicked_on)
            for circle in circles:
                tag = canvas.gettags(circle)
                if ((abs(float(circle_clicked_on_tags[0]) - float(tag[0]))) < .0001 and (abs(float(circle_clicked_on_tags[1]) - float(tag[1]))) < .0001):
                    canvas.itemconfig(circle, fill = "green")
                    new_tag = (circle_clicked_on_tags[0], circle_clicked_on_tags[1], "green")
                    canvas.itemconfig(circle, tags = new_tag)

                    if (tag[2] in color_dict):
                        color_dict[tag[2]] -= 1

                    if ("green" not in color_dict):
                        color_dict["green"] = 1
                    else:
                        color_dict["green"] += 1

def color_vertex_yellow(event):
    if (vertex_bool.get() == 0 and edge_bool.get() == 0 and blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 1 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 0):
        circle_clicked_on = click_on_vert(event.x, event.y)
        if (circle_clicked_on != 0):
            circle_clicked_on_tags = canvas.gettags(circle_clicked_on)
            for circle in circles:
                tag = canvas.gettags(circle)
                if ((abs(float(circle_clicked_on_tags[0]) - float(tag[0]))) < .0001 and (abs(float(circle_clicked_on_tags[1]) - float(tag[1]))) < .0001):
                    canvas.itemconfig(circle, fill = "yellow")
                    new_tag = (circle_clicked_on_tags[0], circle_clicked_on_tags[1], "yellow")
                    canvas.itemconfig(circle, tags = new_tag)

                    if (tag[2] in color_dict):
                        color_dict[tag[2]] -= 1

                    if ("yellow" not in color_dict):
                        color_dict["yellow"] = 1
                    else:
                        color_dict["yellow"] += 1

def color_vertex_black(event):
    if (vertex_bool.get() == 0 and edge_bool.get() == 0 and blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 1 and purple_bool.get() == 0 and pink_bool.get() == 0):
        circle_clicked_on = click_on_vert(event.x, event.y)
        if (circle_clicked_on != 0):
            circle_clicked_on_tags = canvas.gettags(circle_clicked_on)
            for circle in circles:
                tag = canvas.gettags(circle)
                if ((abs(float(circle_clicked_on_tags[0]) - float(tag[0]))) < .0001 and (abs(float(circle_clicked_on_tags[1]) - float(tag[1]))) < .0001):
                    canvas.itemconfig(circle, fill = "black")
                    new_tag = (circle_clicked_on_tags[0], circle_clicked_on_tags[1], "black")
                    canvas.itemconfig(circle, tags = new_tag)

                    if (tag[2] in color_dict):
                        color_dict[tag[2]] -= 1

                    if ("black" not in color_dict):
                        color_dict["black"] = 1
                    else:
                        color_dict["black"] += 1

def color_vertex_purple(event):
    if (vertex_bool.get() == 0 and edge_bool.get() == 0 and blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 1 and pink_bool.get() == 0):
        circle_clicked_on = click_on_vert(event.x, event.y)
        if (circle_clicked_on != 0):
            circle_clicked_on_tags = canvas.gettags(circle_clicked_on)
            for circle in circles:
                tag = canvas.gettags(circle)
                if ((abs(float(circle_clicked_on_tags[0]) - float(tag[0]))) < .0001 and (abs(float(circle_clicked_on_tags[1]) - float(tag[1]))) < .0001):
                    canvas.itemconfig(circle, fill = "purple")
                    new_tag = (circle_clicked_on_tags[0], circle_clicked_on_tags[1], "purple")
                    canvas.itemconfig(circle, tags = new_tag)

                    if (tag[2] in color_dict):
                        color_dict[tag[2]] -= 1

                    if ("purple" not in color_dict):
                        color_dict["purple"] = 1
                    else:
                        color_dict["purple"] += 1

def color_vertex_pink(event):
    if (vertex_bool.get() == 0 and edge_bool.get() == 0 and blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 1):
        circle_clicked_on = click_on_vert(event.x, event.y)
        if (circle_clicked_on != 0):
            circle_clicked_on_tags = canvas.gettags(circle_clicked_on)
            for circle in circles:
                tag = canvas.gettags(circle)
                if ((abs(float(circle_clicked_on_tags[0]) - float(tag[0]))) < .0001 and (abs(float(circle_clicked_on_tags[1]) - float(tag[1]))) < .0001):
                    canvas.itemconfig(circle, fill = "pink")
                    new_tag = (circle_clicked_on_tags[0], circle_clicked_on_tags[1], "pink")
                    canvas.itemconfig(circle, tags = new_tag)

                    if (tag[2] in color_dict):
                        color_dict[tag[2]] -= 1

                    if ("pink" not in color_dict):
                        color_dict["pink"] = 1
                    else:
                        color_dict["pink"] += 1

#variables
vertex_bool = tk.IntVar()
edge_bool = tk.IntVar()
no_edge_bt_same_color_vertices = tk.IntVar() #when on cannot create an edge between vertices colored the same color

blue_bool = tk.IntVar()
red_bool = tk.IntVar()
green_bool = tk.IntVar()
yellow_bool = tk.IntVar()
black_bool = tk.IntVar()
purple_bool = tk.IntVar()
pink_bool = tk.IntVar()

check_coloring_bool = tk.IntVar()
count_colors_bool = tk.IntVar()
is_bipartite_bool = tk.IntVar()

def count_colors():
    if (count_colors_bool.get() == 1):
        print("test")
        num_colors = str(len(color_dict))
        total =  "The number of colors used is: " + num_colors

        if "red" not in color_dict:
            total += "\n There are 0 red vertices"
        else:
            total += "\n There are " + str(color_dict["red"])+ " red vertices"
        
        if "blue" not in color_dict:
            total += "\n There are 0 blue vertices"
        else:
            total += "\n There are " + str(color_dict["blue"])+ " blue vertices"
        
        if "green" not in color_dict:
            total += "\n There are 0 green vertices"
        else:
            total += "\n There are " + str(color_dict["green"])+ " green vertices"
        
        if "yellow" not in color_dict:
            total += "\n There are 0 yellow vertices"
        else:
            total += "\n There are " + str(color_dict["yellow"])+ " yellow vertices"
        
        if "black" not in color_dict:
            total += "\n There are 0 black vertices"
        else:
            total += "\n There are " + str(color_dict["black"])+ " black vertices"
        
        if "purple" not in color_dict:
            total += "\n There are 0 purple vertices"
        else:
            total += "\n There are " + str(color_dict["purple"])+ " purple vertices"

        if "pink" not in color_dict:
            total += "\n There are 0 pink vertices"
        else:
            total += "\n There are " + str(color_dict["pink"])+ " pink vertices"
        
        top1 = Toplevel(window)
        top1.geometry("300x200")
        top1.title("Color Breakdown")
        Label(top1, text = total).place(x=50, y=20)

def check_coloring():
    if (check_coloring_bool.get() == 1):
        find = False
        for circle_key in graph.keys():
            tag1 = canvas.gettags(circle_key)
            color1 = tag1[2]
            for adjacent_circle in graph[circle_key]:
                tag2 = canvas.gettags(adjacent_circle)
                color2 = tag2[2]
                if (color1 == color2):
                    find = True
                    top = Toplevel(window)
                    top.geometry("300x200")
                    top.title("INVALID VERTEX COLORING")
                    Label(top, text = "THE VERTEX COLORING IS NOT VALID").place(x=50, y=80)
                    break 
            if find:
                break
        
        if not find: 
            top = Toplevel(window)
            top.geometry("300x200")
            top.title("VALID VERTEX COLORING")
            Label(top, text = "THE VERTEX COLORING IS VALID").place(x=50, y=80)

def place_vertex_or_edge():
    if (vertex_bool.get() == 1 and edge_bool.get() == 0):
        #vertex mode
        window.bind('<Control-Button-1>', place_vertex)
        
    if (vertex_bool.get() == 0 and edge_bool.get() == 1):
        #edge mode
        window.bind('<Control-Button-1>', draw_edge)

def color_mode():
    if (vertex_bool.get() == 0 and edge_bool.get() == 0): 
        if (blue_bool.get() == 0 and red_bool.get() == 1 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 0):
            #color red
            window.bind('<Button-1>', color_vertex_red)

        if (blue_bool.get() == 1 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 0):
            #color blue
            window.bind('<Button-1>', color_vertex_blue)

        if (blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 1 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 0):
            #color green
            window.bind('<Button-1>', color_vertex_green)

        if (blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 1 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 0):
            #color yellow
            window.bind('<Button-1>', color_vertex_yellow)
        
        if (blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 1 and purple_bool.get() == 0 and pink_bool.get() == 0):
            #color black
            window.bind('<Button-1>', color_vertex_black)

        if (blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 1 and pink_bool.get() == 0):
            #color purple
            window.bind('<Button-1>', color_vertex_purple)
            
        if (blue_bool.get() == 0 and red_bool.get() == 0 and green_bool.get() == 0 and yellow_bool.get() == 0 and black_bool.get() == 0 and purple_bool.get() == 0 and pink_bool.get() == 1):
            #color pink
            window.bind('<Button-1>', color_vertex_pink)
        
def is_bipartite():
    if (is_bipartite_bool):
        if (len(color_dict) == 0 or len(color_dict) == 1):
            top = Toplevel(window)
            top.geometry("300x200")
            top.title("NOT BIPARTITE")
            Label(top, text = "The graph is not bipartite because a bipartite graph \n must have at least 2 vertices according to the textbook").place(x=50, y=80)
        else:
            top = Toplevel(window)
            top.geometry("300x200")
            top.title("The graph is not bipartite because it is empty")
            Label(top, text = "The graph is not bipartite because it is empty").place(x=50, y=80)
        #run BFS
        start_circle = 


vertexCheckButton = Checkbutton(frame, text='Vertex mode: hold control (on mac) and left click to place a vertex', command=place_vertex_or_edge, variable=vertex_bool)
vertexCheckButton.pack(side = BOTTOM)

edgeCheckButton = Checkbutton(frame, text='Edge mode: hold control (on mac) and left click on two vertices to place an edge between them', command=place_vertex_or_edge, variable=edge_bool)
edgeCheckButton.pack(side = BOTTOM)

colorCheckButton = Checkbutton(frame, text='Turn on to not allow edges between vertices that are the same color', command=color_mode, variable=no_edge_bt_same_color_vertices)
colorCheckButton.pack(side = BOTTOM)

redCheckbutton = Checkbutton(frame, text='Red: left click a vertex to color it red', command=color_mode, variable=red_bool, fg = "red")
redCheckbutton.pack(side = BOTTOM)

blueCheckbutton = Checkbutton(frame, text='Blue: left click a vertex to color it blue', command=color_mode, variable=blue_bool, fg = "blue")
blueCheckbutton.pack(side = BOTTOM)

greenCheckbutton = Checkbutton(frame, text='Green: left click a vertex to color it green', command=color_mode, variable=green_bool, fg = "green")
greenCheckbutton.pack(side = BOTTOM)

yellowCheckbutton = Checkbutton(frame, text='Yellow: left click a vertex to color it yellow', command=color_mode, variable=yellow_bool, fg = "yellow")
yellowCheckbutton.pack(side = BOTTOM)

blackCheckbutton = Checkbutton(frame, text='Black: left click a vertex to color it black', command=color_mode, variable=black_bool, fg = "black")
blackCheckbutton.pack(side = BOTTOM)

purpleCheckbutton = Checkbutton(frame, text='Purple: left click a vertex to color it purple', command=color_mode, variable=purple_bool, fg = "purple")
purpleCheckbutton.pack(side = BOTTOM)

pinkCheckbutton = Checkbutton(frame, text='Pink: left click a vertex to color it pink', command=color_mode, variable=pink_bool, fg = "pink")
pinkCheckbutton.pack(side = BOTTOM)

check_vertex_coloring_button = Checkbutton(frame, text='Click to check if the vertex coloring is valid', command=check_coloring, variable=check_coloring_bool)
check_vertex_coloring_button.pack(side = BOTTOM)

count_colors_button = Checkbutton(frame, text='Click to get the number of colors used', command=count_colors, variable=count_colors_bool)
count_colors_button.pack(side = BOTTOM)

is_bipartite_button = Checkbutton(frame, text='Click to check if the graph is bipartite', command=is_bipartite, variable=is_bipartite_bool)
is_bipartite_button.pack(side = BOTTOM)


window.bind(place_vertex_or_edge)

window.mainloop()