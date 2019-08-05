def heapify(input, n, i):
    largest = i
    l = 2*i+1
    r = 2*i+2

    if l < n and input[largest] < input[l]:
        largest = l
    if r < n and input[largest] < input[r]:
        largest = r
    if largest != i:
        input[i], input[largest] = input[largest], input[i]
        heapify(input, n, largest)

def heap_sort(input):
    n = len(input)

    for i in range(n, -1, -1):
        heapify(input, n, i)

    for i in range(n-1, 0, -1):
        input[i], input[0] = input[0], input[i]
        heapify(input, i, 0)

input = [8,5,3,1,9,6,0,7,4,2,5]
heap_sort(input) 
n = len(input) 
print ("Sorted inputay is") 
for i in range(n): 
    print ("%d" %input[i]), 
