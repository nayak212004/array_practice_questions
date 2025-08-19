n=5
def sum_of_elements(array):
    sum=0
    for i in range(len(array)):
        sum =array[i]+sum
    return sum
arr=[]
for i in range(n):
    num=int(input(f'enter the {i+1} element:'))
    arr.append(num)

result=sum_of_elements(arr)
print(f'sum of all the element of an array is {result}')
