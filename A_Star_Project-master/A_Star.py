from map import Map
from math import sqrt
import heapq

def calculate_heuristic(node, goal, amount_traversed, map, type):
    if type == False:
        #get node coordinates
        node_location = map[node]
        x1 = float(node_location[0])
        y1 = float(node_location[1])

        #get goal coordinates
        goal_location = map[goal]
        x2 = float(goal_location[0])
        y2 = float(goal_location[1])

        #calculate straight line distance between node and goal
        estimate = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    else:
        estimate = 1
    
    return estimate + amount_traversed

def main():
    my_map = Map("connections.txt", "locations.txt") #needed dot operator for imported files

if __name__ == "__main__":
    main()
