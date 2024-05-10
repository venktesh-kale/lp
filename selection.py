def sort(arr):
    for i in range(0, size):
        c = i
        for j in range(i+1, size):
            if(arr[j] < arr[c]):
                arr[c],arr[j] = arr[j],arr[c] 

size = int(input("Enter the size of array :"))
arr = []

for i in range (0, size):
    n = input()
    arr.append(n)

print("Array before sorting : ", arr)
sort(arr)
print("Array after sorting : ", arr)