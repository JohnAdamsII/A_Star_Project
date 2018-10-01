from Map import Map

def main():

    #initialize a new map
    my_map = Map("connections.txt", "locations.txt")

    while True: 
        start = input("Enter the start node: ")
        if start not in my_map.connections_dictionary.keys():
            print("Invalid selection. Please try again...\n")
        else:
            break
    while True:
        end = input("\nEnter destination node: ")
        if end not in my_map.connections_dictionary.keys():
            print("Invalid selection. Please try again...")
        else:
            break

    while True:
        exclude_choice = input("\nWould you like to exclude any cities from the search?(y/n): ")
        exclude_choice = exclude_choice.lower()
        if exclude_choice not in 'yn':
            print("Invalid input. Please try again...")
        else:
            break

    if exclude_choice == 'y':
        exclude_string = input("\nEnter the cities you wish to exclude in a space-separated list: ")
        excluded_nodes = exclude_string.split()

        for node in excluded_nodes:
            my_map.exclude_node(node)
    
    while True:
        h_type = input("\nWhat type of heuristic do you want (enter 0 for shortest distance or 1 for fewest cities): ")
        if h_type not in '01':
            print("Invalid input. Please try again...")
        else:
            h_type = int(h_type)
            break

    while True:
        step_by_step = input("\nWould you like a step-by-step solution?(y/n): ")
        step_by_step = step_by_step.lower()
        if step_by_step not in 'yn':
            print("Invalid input. Please try again...")
        else:
            if step_by_step == 'y':
                step_by_step = True
            else:
                step_by_step = False
            break

    print('\n')

    path = my_map.a_star(start, end, h_type, step_by_step)

    print('\n')

    my_map.PrintPathStack(path, h_type)
    

if __name__ == "__main__":
    main()
