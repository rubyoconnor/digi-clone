

def get_string(m):
    my_string=input(m)
    return my_string


def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def add_to_fruit(L):
    for i in range(0, len(L)):
        output= "{} {} {}".format(i, L[i][0], L[i][1])
        print(output)
    # add more fruit to a fruit already in the list
    which_index = get_integer("Which number fruit would you like to add to?")
    quantity = get_integer("How many would you like to add?")
    L[which_index][1] += quantity
    output = "You now have {} {} in the fruit bowl".format(L[which_index][1], L[which_index][0])
    print(output)



def remove_fruit(L):
    for i in range(0, len(L)):
        output= "{} {} {}".format(i, L[i][0], L[i][1])
        print(output)
    # add more fruit to a fruit already in the list
    which_index = get_integer("Which number fruit would you like to remove from?")
    quantity = get_integer("How many would you like to remove?")
    L[which_index][1] -= quantity
    output = "You now have {} {} in the fruit bowl".format(L[which_index][1], L[which_index][0])
    print(output)



def add_new_fruit(L):
    for i in range(0, len(L)):
        output = "{} {} {}".format(i, L[i][0], L[i][1])
        print(output)

    new_fruit = get_string("please enter the new fruit: -->")
    fruit_quantity = get_integer("please enter the quantity-->")

    L.append([new_fruit, fruit_quantity])
    print(L)

    output = "You now have added {} {} in the fruit bowl".format(fruit_quantity, new_fruit)
    print(output)





def print_fruit(L):
    for x in L:
        output = "{} {}".format(x[0], x[1])
        print(output)

def main():
    fruit_list = [
        ["Apple", 10],
        ["Grapes", 500],
        ["Lemons", 2]
    ]
    menu_list = [
        ["p", "Print Fruit"],
        ["a", "Add Fruit"],
        ["r", "Remove Fruit"],
        ["n", "new fruit"],
        ["q", "Quit"]]

    run_program = True
    while run_program:
        for x in menu_list:
            output = "{} {}".format(x[0], x[1])
            print(output)
        user_input = input("Press enter an option ->")
        if user_input == "p":
            print_fruit(fruit_list)
        elif user_input == "a":
            add_to_fruit(fruit_list)
        elif user_input == "r":
            remove_fruit(fruit_list)
        elif user_input == "n":
            add_new_fruit(fruit_list)
        elif user_input == "q":
            run_program = False
            print("You have quit")