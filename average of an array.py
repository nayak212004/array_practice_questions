def average(array):
    sum=0
    avg=0

    for i in range(len(array)):
        sum=array[i]+sum

    avg=sum/len(array)
    return avg
arr=[]
n=int(input('enter the no of elements:'))
for i in range(n):
    num=int(input(f'enter the {i+1} element:'))
    arr.append(num)

result=average(arr)
print(f'sum of all the element of an array is {result}')