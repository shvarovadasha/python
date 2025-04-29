import time
import random
def bubble_sort(nums):  
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
# Verify it works
if __name__ == "__main__":
    import time, random
    a = []
    for j in range(1,5):
        x = [random.random() for i in range(0, 10**j)]
        start = time.time()
        bubble_sort(x)
        a.append(time.time()-start)
        print('1', '0'*j,' - ', a[j-1], sep = '')

##for j in range(1,11):
##    x = [random.random() for i in range(0, 1000)]
##    start = time.time()
##    bubble_sort(x)
##    a.append(time.time()-start)
##for k in range(0,10):
##    print(a[k])
##print(q for q in a)
