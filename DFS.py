import math
    
connection_file = open("connections.txt", "r")  # open file for reading only
location_file = open("locations.txt", "r")

connections_data = connection_file.readlines()  # save file into list
location_data = location_file.readlines()

connection_file.close()  # close file
location_file.close()

# formats raw data read from file

def Construct_data_array(raw_data):
    Formatted_List = raw_data

    for i in range(len(raw_data)):
        Formatted_List[i] = Formatted_List[i].rstrip("\n")  # remove new line character
        Formatted_List[i] = Formatted_List[i].split()       # split strings into list

    Formatted_List.pop()  # remove END
    return Formatted_List



# sorts Adjency list and appends bool to last element
def Sort_Adjency_List(array):
    new_array = array

    for i in range(0, len(new_array)):
        temp = new_array[i][0]
        del new_array[i][0]
        del new_array[i][0]
        new_array[i].sort()
        new_array[i].insert(0, temp)
        new_array[i].append(False)

    return new_array


def Get_Connections(node, l):
    for x in range(0, len(l)):
        if l[x][0] == node:
            return l[x]
    else:
        return "location not found"


def Get_Locations(node, l):
    for x in range(0, len(l)):
        if l[x][0] == node:
            return l[x]
    else:
        return "location not found"


def Get_Index(node, l):
    for x in range(0, len(l)):
        if l[x][0] == node:
            return x
    else:
        print("starting or destination node not found")
        exit(0)


def distance_calc(node1, node2, l):
    loc1 = Get_Index(node1, l)
    X1 = float(l[loc1][1])
    Y1 = float(l[loc1][2])

    loc2 = Get_Index(node2, l)
    X2 = float(l[loc2][1])
    Y2 = float(l[loc2][2])

    distance = math.sqrt((Y2-Y1)**2+(X2-X1)**2)
    return math.ceil(distance*100)/100


def DFS(start, end, adj_list, get_adj):
    path_stack = []

    adj_list[Get_Index(start, adj_list)][-1] = True

    path_stack.append(start)

    while len(path_stack) != 0:
        current = path_stack[-1]
        if current == end:
            break
        else:
            current_adj = get_adj(current, adj_list)
            i = 1
            while i < len(current_adj) - 1:
                y = get_adj(current_adj[i], adj_list)
                if y[-1] == False:
                    x = Get_Index(y[0], adj_list)
                    adj_list[x][-1] = True
                    path_stack.append(y[0])
                    break
                else:
                    i += 1
            if i == len(current_adj) - 1:
                path_stack.pop()

    if len(path_stack) == 0:
        return False

    return path_stack


def PrintPathStack(path, l):
    total_dist = 0
    for x in range(0, len(path)-1):
        dist = distance_calc(path[x], path[x+1], l)
        total_dist += dist
        print(path[x] + " to " + path[x+1] + " length " + str(dist))
    print("Total path length: " + str(total_dist))


def main():

    Adj_List = Construct_data_array(connections_data)
    Cordinate_List = Construct_data_array(location_data)

    sorted_adj_list = Sort_Adjency_List(Adj_List)

    start = input("Enter starting location: ")
    end = input("Enter ending location: ")

    path = DFS(start, end, sorted_adj_list, Get_Connections)

    if path == False:
        print("Path not found")
    else:
        print("\n")
        PrintPathStack(path, Cordinate_List)


if __name__ == "__main__":
    main()
