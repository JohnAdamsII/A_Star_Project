from math import sqrt
import heapq   

class Map():
    """Maps are undirected graphs whose nodes have locations and connections"""

    def __init__(self, connections_file_string, locations_file_string):
        """Set up the map created by the passed in connections and locations files"""

        self.connections_dictionary = {}
        self.locations_dictionary = {}

        # construct a dictionary mapping a node to its connections list
        connections_file = open(connections_file_string, 'r')
        for line in connections_file:
            stripped_line = line.rstrip('\n')
            split_line = stripped_line.split()
            self.connections_dictionary[split_line[0]] = split_line[2:]
        del self.connections_dictionary["END"]

        # construct a dictionary mapping a node to its location
        locations_file = open(locations_file_string, 'r')
        for line in locations_file:
            stripped_line = line.rstrip('\n')
            split_line = stripped_line.split()
            self.locations_dictionary[split_line[0]] = split_line[1:]
        del self.locations_dictionary["END"]

    def print_connections(self):
        """Prints all nodes and their connections"""
        for key, value in self.connections_dictionary.items():
            print("Node: " + key + "\tConnections: %s" % value)

    def print_locations(self):
        """Prints all nodes and their locations"""
        for key, value in self.locations_dictionary.items():
            print("Node: " + key + "\tLocation: %s" % value)

    def print_all(self):
        """Prints all nodes' locations and connections"""
        for key, value in self.locations_dictionary.items():
            connections = self.connections_dictionary[key]
            print("Node:" + key + " \t\tLocation:" + str(value) +
                  "\t\tConnections:" + str(connections))

    def exclude_node(self, excluded_node):
        """Excludes the passed node from connections and locations"""
        excluded_connections = self.connections_dictionary[excluded_node]
        del self.connections_dictionary[excluded_node]
        del self.locations_dictionary[excluded_node]

        for node in excluded_connections:
            target_list = self.connections_dictionary[node]
            target_list.remove(excluded_node)

    def distance_calc(self, node, goal):
        node_location = self.locations_dictionary[node]
        X1 = float(node_location[0])
        Y1 = float(node_location[1])

        goal_location = self.locations_dictionary[goal]
        X2 = float(goal_location[0])
        Y2 = float(goal_location[1])

        return sqrt((Y2-Y1)**2+(X2-X1)**2)

    def calculate_estimate(self, node, goal, type):
        if type == False:
            estimate = self.distance_calc(node, goal)
        else:
            estimate = 1
    
        return estimate

    def A_Star(self, start_node, end_node):
        PriorityQueue = []
        ClosedNodes = []

        PredArray = {}

        current = start_node

        current_connections = self.connections_dictionary[current]

        for node in current_connections:
            estimate = self.calculate_estimate(node, end_node, False)
            distance_travelled = self.distance_calc(start_node, node)
            total_distance = distance_travelled + estimate

            print("Node: " + node + "\tDistance: " + str(total_distance))

            node_struct = (total_distance, node)
            heapq.heappush(PriorityQueue, node_struct)

        while len(PriorityQueue) != 0:

            node_selected = heapq.heappop(PriorityQueue)

            PredArray[node_selected[1]] = current 

            print("City selected: " + node_selected[1] + "\tTotal: " + str(node_selected[0]))

            options = self.connections_dictionary[node_selected[1]]

            options.remove(PredArray[node_selected[1]])

            print("Where to travel: %s\n" % self.connections_dictionary[node_selected[1]])
            if node_selected[1] == end_node:
                break

            print("Possible cities where to travel: %s\n" % options)

            




           

def main():

    my_map = Map("connections.txt", "locations.txt")
    
    my_map.A_Star("A1", "A2")


if __name__ == "__main__":
    main()
