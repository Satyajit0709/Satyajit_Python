## this contains number of programs on list
## 1.  find out the biggest  number in the list
"""
Final_List = []

print("Enter the List separated by comma - ")

Final_List = input()
print("Display the list")
i=0
print(Final_List[i])

List_Length = len(Final_List)
print(f"length of the List {List_Length}")
i=0
max_Number=Final_List[0]
for ele in Final_List :
    if ele > max_Number :
        max_Number =  ele
print(f" So max number in the list is  -  {max_Number}")

"""

# 2.  Write a program to replace a number with the SUM of all numbers present before that
Final_List = []
print("Enter the number in the list  - ")
Final_List = input()
print(" entered List is ")
print(Final_List)

Length_of_list = len(Final_List)

i=0
j=0
New_list= []
for ele in Final_List :
    i=0
    k=Final_List.index(ele)
    Temp=0
    while i <= k:
        Temp =  Temp+ int(Final_List[i])
        i= i+1
    New_list.insert(j, Temp)
    j= j+1

print("old List")
print(Final_List)

print("new List")
print(New_list)




