# WAP  in  python to display all the common elements of two list which are inputted by the user.

list1 = input("ENTER LIST1 : ").split()
list2 = input("ENTER LIST2 : ").split()
common_elements = []
for num in list1:
    if num in list2 and num not in common_elements:
        common_elements.append(num) 
print( "COMMON ELEMENTS :" , common_elements)

