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
# each circle has a tag that stores its center as a 5-tuple (center.x, center.y, color, visited_flag, blue or red)
# 0 = not visisted
# tag[4] is 3 by default

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

        tag = (center[0], center[1], "black", 0, 3) #the tag for each circle is its center

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
            elif (second_to_last not in graph[last] and last not in graph[second_to_last]):
                #prevent multiple edges between the same pair of vertices
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
draw_bipartite_bool = tk.IntVar()

def count_colors():
    if (count_colors_bool.get() == 1):
        print("test")

        num_colors = 0
        for col in color_dict.keys():
            if color_dict[col] != 0:
                num_colors += 1
        
        total =  "The number of colors used is: " + str(num_colors)

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
        if (len(circles) == 0 or len(circles) == 1):
            top = Toplevel(window)
            top.geometry("400x200")
            top.title("NOT BIPARTITE")
            Label(top, text = "The graph is not bipartite because a bipartite graph \n must have at least 2 vertices according to the textbook").place(x=50, y=80)
        else:

            num_degree_0 = 0
            #set all vertices of degree 1 to visited
            for circle in circles:
                if len(graph[circle]) == 0:
                    #1 is for visited
                    #-1 for degree 0 
                    circle_tags = canvas.gettags(circle)
                    new_tag = (circle_tags[0], circle_tags[1], circle_tags[3], 1, -1)
                    num_degree_0 += 1
                else:
                    #set all visited flags (tag[3]) to false for any node with degree > 0
                    #set all tag[4] to 3
                    for neighbor in graph[circle]:
                        neighbor_tags = canvas.gettags(neighbor)
                        new_tag_all = (neighbor_tags[0], neighbor_tags[1], neighbor_tags[2], 0, 3)
                        canvas.itemconfig(neighbor, tag = new_tag_all)
                    

            #run a BFS at each connected component
            num_visited = 0
            unsuccessful = 0

            while num_visited < len(circles)-num_degree_0: 
                start_circle = circles[0] # placeholder 
                
                found = 0
                for circle in circles:
                    start_circle_tags = canvas.gettags(circle)
                    if (len(graph[circle]) != 0 and int(start_circle_tags[3]) != 1):
                        # if has no neighbors and has not been visited yet
                        start_circle = circle
                        new_tag = (start_circle_tags[0], start_circle_tags[1], start_circle_tags[2], 1, 0) #start is colored 0 by default
                        canvas.itemconfig(start_circle, tag = new_tag)
                        num_visited += 1
                        found = 1
                        break

                if found == 1:
                    #makes it here
                    """        
                    #run BFS at an arbitary vertex
                    start_circle = circles[0]
                    start_circle_tags = canvas.gettags(start_circle)
                    new_tag = (start_circle_tags[0], start_circle_tags[1], start_circle_tags[2], 1, 0) #start is colored 0 by default
                    canvas.itemconfig(start_circle, tag = new_tag)
                    """       
                    layer_arr = [[]]

                    #current_layer = [start_circle]
                    layer_arr[0].append(start_circle)

                    layer_counter = 0
                    
                    while layer_counter < len(layer_arr) and len(layer_arr[layer_counter]) != 0:
                        for node in layer_arr[layer_counter]:
                            current_node_tags = canvas.gettags(node)
                            current_color = current_node_tags[4]

                            first = 0
                            if (len(graph[node]) != 0):
                                for neighbor in graph[node]:
                                    neighbor_tags = canvas.gettags(neighbor)
                                    neighbor_visited = int(neighbor_tags[3])
                                    neighbor_color = neighbor_tags[4]

                                    if (neighbor_visited == 0):
                                        num_visited += 1 
                                        new_neighbor_tag = (neighbor_tags[0], neighbor_tags[1], neighbor_tags[2], 1, (layer_counter+1)%2)
                                        canvas.itemconfig(neighbor, tag = new_neighbor_tag)
                                        if (first == 0):
                                            layer_arr.append([])
                                            first == 1
                                        layer_arr[layer_counter+1].append(neighbor)
                                    else:
                                        if (neighbor_color == current_color):
                                            unsuccessful = 1
                                            break        
                            if unsuccessful:
                                break

                        layer_counter += 1

                        if unsuccessful:
                            break

                if unsuccessful: 
                    break              
            
            if unsuccessful:            
                top = Toplevel(window)
                top.geometry("400x200")
                top.title("NOT BIPARTITE")
                Label(top, text = "The graph is not bipartite because BFS cannot \n be used to assign colors to its vertices").place(x=50, y=80)
                return -1
            else:
                top = Toplevel(window)
                top.geometry("400x200")
                top.title("BIPARTITE")
                Label(top, text = "The graph is bipartite because BFS can \n be used to assign colors to its vertices").place(x=50, y=80)
        
def draw_bipartite():
    if (draw_bipartite_bool):
        if (is_bipartite() != -1):
            for circle in circles:
                for neighbor in graph[circle]:
                    neighbor_tags = canvas.gettags(neighbor)
                    #0 is not visisted
                    #tag[4] is 3 by default
                    new_tag_all = (neighbor_tags[0], neighbor_tags[1], "black", 0, 3)
                    canvas.itemconfig(neighbor, fill = "black", tag = new_tag_all)

            #adjust counts
            color_dict["black"] = 0
            color_dict["red"] = 0
            color_dict["blue"] = 0

            #nodes with degree 0 get colored red by default
            num_degree_0 = 0

            for circle in circles:
                if len(graph[circle]) == 0:
                    #1 is for visited
                    #-1 for degree 0 
                    circle_tags = canvas.gettags(circle)
                    new_tag = (circle_tags[0], circle_tags[1], "red", 1, -1)
                    canvas.itemconfig(circle, fill = "red", tag = new_tag)
                    color_dict["red"] += 1
                    num_degree_0 += 1

            #"""
            #run a BFS at each connected component
            num_visited = 0

            while num_visited < len(circles)-num_degree_0: 
                start_circle = circles[0] # placeholder 
                
                found = 0
                for circle in circles:
                    start_circle_tags = canvas.gettags(circle)
                    if (len(graph[circle]) != 0 and int(start_circle_tags[3]) != 1):
                        # if has no neighbors and has not been visited yet
                        start_circle = circle
                        new_tag = (start_circle_tags[0], start_circle_tags[1], "red", 1, 0) #start is colored 0 by default
                        canvas.itemconfig(start_circle, fill = "red", tag = new_tag)
                        color_dict["red"] += 1
                        num_visited += 1
                        found = 1
                        break

                if found == 1:

                    layer_arr = [[]]

                    #current_layer = [start_circle]
                    layer_arr[0].append(start_circle)

                    layer_counter = 0

                    while layer_counter < len(layer_arr) and len(layer_arr[layer_counter]) != 0:
                        for node in layer_arr[layer_counter]:
                            
                            #this version of BFS is used just for 2-coloring, 
                            # so it does not have checks because the check for the graph being 
                            # bipartite was done at the beginning of draw_bipartite()
                            first = 0
                            if (len(graph[node]) != 0):
                                for neighbor in graph[node]:
                                    neighbor_tags = canvas.gettags(neighbor)
                                    neighbor_visited = int(neighbor_tags[3])

                                    if (neighbor_visited == 0): 
                                        num_visited += 1
                                        if layer_counter % 2 == 0:
                                            new_color = "blue"
                                            color_dict["blue"] += 1
                                        else:
                                            new_color = "red"
                                            color_dict["red"] += 1

                                        new_neighbor_tag = (neighbor_tags[0], neighbor_tags[1], new_color, 1, (layer_counter+1)%2)
                                        canvas.itemconfig(neighbor, fill = new_color, tag = new_neighbor_tag)
                                        if (first == 0):
                                            layer_arr.append([])
                                            first == 1
                                        layer_arr[layer_counter+1].append(neighbor)
                        
                        layer_counter += 1
            #"""


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

is_bipartite_button = Checkbutton(frame, text='Click to see the bipartite coloring for the bipartite graph drawn', command=draw_bipartite, variable=draw_bipartite_bool)
is_bipartite_button.pack(side = BOTTOM)

window.bind(place_vertex_or_edge)

window.mainloop()