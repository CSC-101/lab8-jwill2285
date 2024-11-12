'''This function takes the list that is given of values and will run through that list in
groups of 3. It will then add the three values in that break to the new_list as a list. This is done with
the append function where it takes values i all the way to i+3 and adds them which is three values. After that
 It will check if each of the lists is length of 3, if they are not it will remove them It then returns the list
 of lists'''
def groups_of_3(values : list[int])->list[list[int]]:
    new_list = []
    for i in range(0,len(values),3):
        new_list.append(values[i:i+3])
    for i in range(len(new_list)):
        if len(new_list[i]) != 3:
            new_list.remove(new_list[i])
    return new_list






