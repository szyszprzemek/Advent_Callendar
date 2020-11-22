def uniqueElements(arg):
    '''Find unique elements in list'''
    b = set(arg)
    return list(b)


def check(arg):
    ''' Checking conditions '''
    a_old = 0
    flag = False
    allNr = []

    for a_str in str(arg):
        a = int(a_str)
        if (a < a_old):
            return False

        if (a == a_old):
            flag = True
            allNr.append(a)
            
        a_old = a
    
    if(flag):
        for element in uniqueElements(allNr):
            if (str(arg).count(str(element)) == 2):
                return True
    
    return False
    

if __name__ == "__main__":
    start = 353096
    end = 843212
    counter = 0
    
    for i in range(start, end):
        if (check(i)):
            print(i)
            counter += 1

    print("Counter: ", counter)


