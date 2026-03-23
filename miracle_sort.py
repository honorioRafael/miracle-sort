def miracle_sort(array):    
    while True:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                is_sorted = False
                break
        
        if is_sorted:
            return array
        else:
            # Wait for a miracle
            pass