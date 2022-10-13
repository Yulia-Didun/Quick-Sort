'''
    Quick Sort algorithm
    Last element of array as pivot
    Input: text file, the first element is the number of N array elements; 
                      the next N lines of the file correspond to the elements of the input array.
    Output: number of comparisons used in Partition
'''


count=0

#функція записує значення з файлу, і формує їх у масив цілих чисел
def incoming_data(): 
    my_file = open("text_file.txt", "r")
    data = my_file.read()
    data_into_list = data.split("\n")

    #видаляю елемент з індексом 0 (кількість чисел)
    data_into_list.pop(0)
    
    data_into_list = [int(i) for i in data_into_list]
    
    my_file.close()
    return data_into_list



#функція призначена для обміну елементів місцями
def SwapPositions(list, index_1, index_2):
     
    list[index_1], list[index_2] = list[index_2], list[index_1]
    return list



# бере на вхід масив А, індекси першого та останнього елементів цього масиву.
# перевіряється чи p < z
# і тоді викликається функція розбиття, після неї знову викликається QuickSort вже для правої та лівої розбитих частин масиву 
def QuickSort(A, p, z):
    if p < z:
        q = Partition(A, p, z)
        QuickSort(A, p, q - 1)
        QuickSort(A, q + 1, z)



def Partition(A, p, z):
    pivot = A[z] #встановити останній елемент опорним
    i = p - 1
    for j in range(p, z):
        global count
        count+=1
        if A[j] <= pivot:
            i += 1
            SwapPositions(A, i, j)
    
    SwapPositions(A, z, i + 1)
    return i + 1         


A = incoming_data()
QuickSort(A, 0, len(A) - 1)
print(count)