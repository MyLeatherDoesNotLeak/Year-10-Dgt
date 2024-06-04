def num_check(question) :
    error = "Please enter a number that is more than zero\n"
    while True:
                
        try:       
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":
    width = num_check("Width: ")
    height = num_check("height: ")
    cost = num_check("Cost: ")

    perimeter = 2 * (width + height)
    cost = perimeter * cost

    print()
    print(f"perimeter: {perimeter} meters")
    print(f"Cost: $ {cost}")

    keep_going = input("Press enter to keep going or any key to quit. \n")
    print("Thank you for using the area / perimeter calculator.")
    print("___________________________________________")
