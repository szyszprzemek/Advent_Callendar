def check(arg):
    ''' Checking conditions '''
    a_old = 0
    flag = False

    for a_str in str(arg):
        a = int(a_str)
        if (a < a_old):
            return False
        if (a == a_old):
            flag = True       
        a_old = a

    return flag

if __name__ == "__main__":
    start = 353096
    end = 843212
    counter = 0
    
    for i in range(start, end):
        if (check(i)):
            counter += 1

    print("Counter: ", counter)

