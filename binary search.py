def binary_search(arr,target):
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[]
n=int(input('enter the number of elements in the array:'))

for i in range(n):
    num=int(input(f'enter the {i+1} element:'))
    arr.append(num)
arr.sort()

print(arr)

target=int(input('enter the number to be searched:'))
result=binary_search(arr,target)

if result !=-1:
    print(f'the element is at index {result}')
else:
    print('element not found')

