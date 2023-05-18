#1
def Countdown(num):
    arr=[]
    while num>=0:
        arr.append(num)
        num-=1
    return arr
print(Countdown(20))
#2
def Print_Return(arr):
    print(arr[0])
    return arr[1]
print(Print_Return([6,2]))
#3
def first_plus_length(arr):
    sum = arr[0] +len(arr)
    return sum
print(first_plus_length([15,8,9,7,4]))
#4
def Values_Greater_than_Second(arr):
     arr1 = []
     if len(arr) < 2:
        return False
     else:
        for i in range(len(arr)):
            if arr[i] > arr[1]:
                arr1.append(arr[i])
        return arr1, len(arr1)

print(Values_Greater_than_Second([5,2,3,2,1,4]))
print(Values_Greater_than_Second([3]))
#5
def Length_Value(Length, value):
    arr = []
    while Length > 0:
        arr.append(value)
        Length-=1
    return arr

print(Length_Value(4,7))
print(Length_Value(6,2))