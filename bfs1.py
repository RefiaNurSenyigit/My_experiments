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
}

start=[]
stop=[]

def bfs1(start,graph,node):
    start.append(node)
    stop.append(node)
    while stop:
        x=stop.pop(0)
        print(x,end=" ")

        for child in graph[x]:
            if child not in start:
                start.append(child)
                stop.append(child)

print("this is the queue of Breadth-First Search of a given graph")
bfs1(start,graph,"r")