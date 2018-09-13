import DFS

connection_file = open("connections.txt", "r")  # open file for reading only
location_file = open("locations.txt", "r")

connections_data = connection_file.readlines()  # save file into list
location_data = location_file.readlines()

connection_file.close()  # close file
location_file.close()

#path = DFS.DFS("G4b", "G2b", sorted_adj_list, Get_Connections)
#path = DFS.DFS("B1", "C1", sorted_adj_list, Get_Connections)
#path = DFS.DFS("C1", "B1", sorted_adj_list, Get_Connections)

def main():

    Adj_List = DFS.Construct_data_array(connections_data)
    Cordinate_List = DFS.Construct_data_array(location_data)

    sorted_adj_list = DFS.Sort_Adjency_List(Adj_List)

    """ 
    print("Adjency List:")
    for item in Adj_List:
        print(item)

    print("Sorted Adjency List")

    for item in sorted_adj_list:
         print(item) """

    """     print("TESTS")
    print(DFS.Get_Connections("A1",sorted_adj_list))
    print(DFS.Get_Locations("A1",Cordinate_List))
    print(DFS.Get_Index("A1", sorted_adj_list))
    print(DFS.distance_calc("A1", "A2",Cordinate_List)) """

    """  print("Cordinate List:")

    for item in Cordinate_List:
        print(item) """

    path = DFS.DFS("C1", "B1", sorted_adj_list, DFS.Get_Connections)

    if path == False:
        print("Path not found")
    else:
        print("\n")
        DFS.PrintPathStack(path, Cordinate_List)
    

if __name__ == "__main__": main()