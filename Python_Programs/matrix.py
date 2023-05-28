## program to
#  1. get the input from user to decide the dimension of the matrix
# 2. Based on Input ask user to provide those many number of values
# 3. Display those values as Matrix
#4. change the rows into columns

## create one array
First_Array = []

# user to decide the dimention of the Matrix
n = int(input ("Enter the dimension of the matrix : [Less than 10] - "))
if n > 10 :
    print("Matrix value  is more than 10 .. Exiting.... ")
    exit(1)

## ask user to Input n*n values
i = n*n
print(f"enter {i} values now")

for j in range(0,i) :
    tmp =  int(input())
    First_Array.append (tmp)

## Print all values
print("Entered values are - ")
print(First_Array)

## Print in Matrix format
print("Matrix form - ")
k=0
dimension = n
while k < i :
    print(First_Array[k:dimension])
    k= k+n
    dimension =  dimension + n

## Change the row into columns
print("Change rows into columns - ")
k=0
dimension = n
while k < n :
    TEMP = k
    m = 0
    while m < n :
        print(First_Array[TEMP] , end = ' ')
        TEMP += n
        m = m+1
    print("")
    k = k + 1