def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=[]
n=int(input('enter the number of elements in the array:'))
for i in range(n):
    num=int(input(f'enter the {i+1} element:'))
    arr.append(num)
arr.sort()
print(arr)
target=int(input('enter the element to be searched:'))

result=linear_search(arr,target)

if result!=-1:
    print(f'element is at index {result}')
else:
    print('element not found')