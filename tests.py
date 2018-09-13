#this is a test
import A_Star

connection_file = open("connections.txt", "r")  # open file for reading only
location_file = open("locations.txt", "r")

connections_data = connection_file.readlines()  # save file into list
location_data = location_file.readlines()

connection_file.close()  # close file
location_file.close()


def main():

    Adj_List = A_Star.Construct_data_array(connections_data)
    sorted_adj_list = A_Star.Sort_Adjency_List(Adj_List)

    for item in sorted_adj_list:
        print(item)

    print("------------------------------------------")

    def Delete_Node(node, adj_list):
        for i in range(0, len(adj_list)):
            if adj_list[i][0] == node:
                del adj_list[i]
                break
        for i in range(0, len(adj_list)):
            row = adj_list[i]
            for j in range(0,len(row)):
                if row[j] == node:
                    del row[j]
                    break

    Delete_Node("A2", sorted_adj_list)

    for item in sorted_adj_list:
        print(item)


if __name__ == "__main__":
     main()