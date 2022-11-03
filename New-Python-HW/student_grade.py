sub_1 = int(input("Enter mark 1: "))
sub_2 = int(input("Enter mark 2: "))
sub_3 = int(input("Enter mark 3: "))

def result(sub_1,sub_2,sub_3):
    if (sub_1 > 90 and sub_2 > 90 and sub_3 > 90):
        return "Distinction"
    elif (sub_1 > 80 and sub_2 > 80 and sub_3 > 80):
        return "First Class"
    elif (sub_1 < 40 or sub_2 < 40 or sub_3 < 40):
        return "Fail"
    else:
        return "Second Class"
print(result(sub_1,sub_2,sub_3))