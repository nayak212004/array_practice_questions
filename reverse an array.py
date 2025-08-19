# reverse an array

def reverse(array):
    reversed_array=[]
    for i in array:
        reversed_array=[i] + reversed_array
    return reversed_array

arr=[]
n=int(input('enter the no of elements:'))
for i in range(n):
    num=int(input(f'enter the {i+1} element:'))
    arr.append(num)

result=reverse(arr)
print(f'reversed array is {result}')
