graph= {
    "r":["e","u","s"],
    "e":["f","i"],
    "f":[],
    "i":["n","a"],
    "n":[],
    "a":[],
    "u":[],
    "s":["y","m","d"],
    "y":["g","t"],
    "g":[],
    "t":[],
    "m":["h"],
    "h":[],
    "d":[]
} #that is the graph given before

start=[]  #searching list
stop=[]  #resulting list

def bfs1(start,graph,node):  #defined function for bread-first search
    start.append(node)   #adding the first vertex to the search list
    stop.append(node)   #than putting it to the resulting list
    while stop:
        x=stop.pop(0)   #taking the every x from resulting list by order
        print(x,end=" ")  #then showing us side by side. (without (end=" ") it -
                          # -would be written with a vertical order.)

        for child in graph[x]: #searching the vertex'es childs from resulting list
            if child not in start: 
                start.append(child) #adding them also in the searching list
                stop.append(child)  #then looking for a results.

print("this is the queue of Breadth-First Search of a given graph")
bfs1(start,graph,"r")