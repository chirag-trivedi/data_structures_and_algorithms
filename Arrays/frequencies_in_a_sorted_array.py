from collections import Counter
def frequencies(arr):
    length = len(arr)
    
    if length == 1:
        print(arr[0],"-->",1)
        
    counter = Counter(arr)
    return counter    
    

arr = [10,10,10,20,30,30]
print(frequencies(arr))