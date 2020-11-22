def calc(argv):
    operation = 0
    suma = 0
    mult = 1
    counter = 0

    for arg in argv:

        # counter control the flow
        if (counter == 0):

            # determine operation
            if (arg == 1):
                operation = 1
                counter = 3
                suma = 0
                
            elif (arg == 2):
                operation = 2
                counter = 3
                mult = 1

            elif (arg == 99):
                #print("Exit")
                return argv

        else:
            # adding
            if (operation == 1):
                if (counter >= 2):
                    suma += argv[arg]
                elif (counter == 1):
                    argv[arg] = suma
                counter -= 1

            # multiplication
            elif (operation == 2):
                if (counter >= 2):
                    mult *= argv[arg]
                elif (counter == 1):
                    argv[arg] = mult
                counter -= 1
    
    return argv


if __name__ == "__main__":

    first = [1,0,0,0,99]
    print(calc(first))
    
    second = [2,3,0,3,99]
    print(calc(second))

    third = [2,4,4,5,99,0]
    print(calc(third))

    fourth = [1,1,1,4,99,5,6,0,99]
    print(calc(fourth))

    #noun = 12
    #verb = 2
    result_exp = 19690720

    for noun in range(0, 99):
        for verb in range(0, 99):
            fifth = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,1,13,23,27,1,6,27,31,2,31,13,35,1,9,35,39,2,39,13,43,1,43,10,47,1,47,13,51,2,13,51,55,1,55,9,59,1,59,5,63,1,6,63,67,1,13,67,71,2,71,10,75,1,6,75,79,1,79,10,83,1,5,83,87,2,10,87,91,1,6,91,95,1,9,95,99,1,99,9,103,2,103,10,107,1,5,107,111,1,9,111,115,2,13,115,119,1,119,10,123,1,123,10,127,2,127,10,131,1,5,131,135,1,10,135,139,1,139,2,143,1,6,143,0,99,2,14,0,0]
            result = calc(fifth)[0]
            if (result == result_exp):
                print(noun)
                print(verb)
