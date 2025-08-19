#max and min element

def max_min(array):
    array.sort()
    min=array[0]
    max=array[n-1]
    return

n=int(input('enter the number of elements in the array:'))
arr=[]
for i in range(n):
    num=int(input(f'enter the {i+1} element:'))
    arr.append(num)

print(f'the max and min element of the array are\n min:{min(arr)}\n max:{max(arr)}')