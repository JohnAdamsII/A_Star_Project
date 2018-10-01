import PriorityQueue as pq
from math import sqrt

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
        connections_file.close()

        # construct a dictionary mapping a node to its location
        locations_file = open(locations_file_string, 'r')
        for line in locations_file:
            stripped_line = line.rstrip('\n')
            split_line = stripped_line.split()
            self.locations_dictionary[split_line[0]] = split_line[1:]
        del self.locations_dictionary["END"]
        locations_file.close()

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
            #print("Node:" + key + " \t\tLocation:" + str(value) +
                  #"\t\tConnections:" + str(connections))
            print('Node: {} \t\tLocation: {}\t\tConnections: {}'.format(key, value, connections))

    def exclude_node(self, excluded_node):
        if excluded_node not in self.connections_dictionary.keys():
            print(excluded_node + " does not exist.")
            return -1
        excluded_connections = self.connections_dictionary[excluded_node]
        del self.connections_dictionary[excluded_node]
        del self.locations_dictionary[excluded_node]

        for node in excluded_connections:
            target_list = self.connections_dictionary[node]
            target_list.remove(excluded_node)

    def calc_sld(self, node1, node2):
        """Calculates the straight line distance between node1 and node2"""
        location1 = self.locations_dictionary[node1]
        x1 = int(location1[0])
        y1 = int(location1[1])

        location2 = self.locations_dictionary[node2]
        x2 = int(location2[0])
        y2 = int(location2[1])
        
        return sqrt((x2-x1)**2 + (y2-y1)**2)

    def calculate_heuristic(self, node, end, h_type):
        """Returns the heuristic cost estimate to go from start to end.
        If h_type is 0, straight line distance is used, else number of cities is used"""
        if h_type:
            return 1
        else:
            return self.calc_sld(node, end)

    def construct_predecessor_path(self, pred_map, current):
        path = [current]

        while current in pred_map.keys():
            current = pred_map[current]
            path.append(current)
        return path


    def a_star(self, start, end, h_type, step_by_step):
        """Returns the shortest path from start to end based on the heuristic type"""

        #map from a node to the node it came from
        pred_map = {}

        #priority queue of open nodes
        open_nodes = pq.PriorityQueue()

        #list of closed nodes
        closed_nodes = []

        #map from a node to the cost of getting to that node from the start node
        g_cost = {}
        g_cost[start] = 0 #the cost of getting from start to start is 0

        #map from a node to its total cost estimate aka its priority in the queue
        total_cost = {}

        #initialize the start node's cost and heuristic estimate
        cost_estimate = self.calculate_heuristic(start, end, h_type)

        #push the start node onto the queue
        open_nodes.push_with_priority(start, cost_estimate)
        total_cost[start] = cost_estimate #the total cost of the start node is entirely heuristic

        #loop while open_nodes is not empty
        while open_nodes.entry_map:
            
            #pop the lowest cost node off the queue and add it to the list of closed nodes
            current = open_nodes.pop()
            current_node = current[1]

            if step_by_step:
                print("City selected: " + current_node)

            if current_node == end:
                return self.construct_predecessor_path(pred_map, current_node)

            closed_nodes.append(current_node)

            #neighbors is a list of all the connections from the current node
            neighbors = self.connections_dictionary[current_node]

            if step_by_step:
                print("Possible cities to where to travel: %s" % neighbors)
                

            for neighbor in neighbors:

                #check to see if neighbor has already been visited
                if neighbor in closed_nodes:
                    continue

                #calculate cost from current to neighbor
                if h_type:
                    g_cost_neighbor = 1 + g_cost[current_node]
                else:
                    g_cost_neighbor = self.calc_sld(current_node, neighbor) + g_cost[current_node]

                #calculate heuristic cost estimate from neighbor to end
                cost_estimate = self.calculate_heuristic(neighbor, end, h_type)

                total_cost_neighbor = cost_estimate + g_cost_neighbor

                #is neighbor already an open node?
                if neighbor in open_nodes.entry_map.keys():
                    #if so, have we found a better path
                    if total_cost_neighbor >= total_cost[neighbor]:
                        #if not, continue
                        continue

                #otherwise, add neighbor to the queue or update its values
                g_cost[neighbor] = g_cost_neighbor
                open_nodes.push_with_priority(neighbor, total_cost_neighbor)
                total_cost[neighbor] = total_cost_neighbor

                #add neighbor to the predecessor map
                pred_map[neighbor] = current_node

            if step_by_step:
                print("Cities at the end of possible paths: ")
                for city in open_nodes.queue:
                    if city[1] != "removed":
                        print(city[1] + "(%.2f)," % city[0], end = ' ')
                print("\n")
                input("Press enter to continue...")

        return [] #indicates that no path existed

        #end a_star

    def PrintPathStack(self, path, h_type):

        if path == []:
            print("Path not found.")
        else:
            path.reverse()
            total_dist = 0

            for x in range(0, len(path)-1):
                if h_type:
                    total_dist += 1
                    print(path[x] + " to " + path[x+1] + " length 1")
                else:
                    dist = self.calc_sld(path[x], path[x+1])
                    total_dist += dist
                    print(path[x] + " to " + path[x+1] + " length %.2f" % dist)
            print("Total path length: %.2f" % total_dist)
         

def main():

    my_map = Map("connections.txt", "locations.txt")

    my_map.print_all()

    excluded_nodes = ["G4", "D1", "B2", "B1"]

    for node in excluded_nodes:
        my_map.exclude_node(node)

    my_map.print_all()

    path = my_map.a_star("A1", "D3", False, False)

    print('\n')

    print(path)

    my_map.PrintPathStack(path, False)


if __name__ == "__main__":
    main()
