def second_max_min(array):
    array.sort()
    min=array[1]
    max=array[n-2]
    return min, max

n=int(input('enter the number of elements in the array:'))
arr=[]
for i in range(n):
    num=int(input(f'enter the {i+1} element:'))
    arr.append(num)
result=second_max_min(arr)
print(f'the max and min element of the array are:\n{result}')