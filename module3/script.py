from code import interact
from enum import unique

a_list=list([3,4,6,5,3])
xyz=[24,234,234,134]

my_set={1,2,3}
if isinstance(my_set,set):
    print('This is a set')

other_set=set(xyz)

union_result=other_set.union(my_set) #{1, 2, 3, 134, 24.234, 234}
union_result_2=my_set | other_set    #{1, 2, 3, 134, 24.234, 234}
print(f"Union function: {union_result_2 | union_result}")

interact_result = other_set.intersection(my_set)
interact_result_sign = other_set & my_set
print(f"interact function: {interact_result}")

set_difference=union_result.difference(my_set)
print(f"difference between {union_result} and {my_set} is: {set_difference}")
sign_difference=union_result - my_set
print(sign_difference==set_difference)

list1=["red","green", "blue","black"]
list2=["orange","black", "white","yellow"]

set1=set(list1)
set2=set(list2)
unique_set = set1 | set2
print(unique_set)
