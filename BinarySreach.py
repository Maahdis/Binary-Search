#Binary Search
def Find_Num(NumList , Target):
    Findex = 0
    Lindex = len(NumList) - 1
    Middle = int((Findex + Lindex)/2)
    Found_that = True
    while Found_that:
        if Target not in NumList:
            return "The Target is not found !"
        elif Target == NumList[Middle]:
            return f"{Target} in Possition {Middle}"
        elif Target < NumList[Middle]:
            Lindex -= 1
            Middle = int((Findex + Lindex)/2)
            if Target == NumList[Middle]:
                return f"{Target} in Possition {Middle}"
        elif Target > NumList[Middle]:
            Lindex += 1
            Middle = int((Findex + Lindex)/2)
            if Target == NumList[Middle]:
                return f"{Target} in Possition {Middle}"
            
my_list = list(map(int , input("Enter the numbers in the (Sorted) list : ").split()))
target = int(input("Please your target : "))
print(Find_Num(my_list , target ))