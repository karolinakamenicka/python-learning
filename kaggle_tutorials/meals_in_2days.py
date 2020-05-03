def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    if len(meals)<=1:
        print('False')
        return False
    meal2 = meals, meals[1:]+ [None]
    print(meal2)
    for day in list(zip(*meal2)):
        print(day)
        if type(day)== list:
            for d in day[0]:
                print(d)
                for d2 in day[1]:
                    print(d2)
                    if d ==d2:
                        print('True')
                        return True
        else:
            if day[0]==day[1]:
                print('True')
                return True
    print('False')
    return False

menu_is_boring([['Spa', 'Spam']])

