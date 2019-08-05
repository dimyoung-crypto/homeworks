import random
import datetime
import prettytable
import matplotlib.pyplot as plt

#Selection Sort
def selection(A):
    for i in range(len(A)):

        # Find the minimum element in remaining
        #     # unsorted array
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

            # Swap the found minimum element with
            # the first element
        A[i], A[min_idx] = A[min_idx], A[i]
    #print("Sorted array: \n")
    #for i in range(len(A)):
    #   print("%d" % A[i])


#Insertion Sort
def insertion(B):
    # Traverse through 1 to len(arr)
    for i in range(1, len(B)):
        key = B[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < B[j]:
            B[j + 1] = B[j]
            j -= 1
        B[j + 1] = key
    print("Sorted array: \n")
    for i in range(len(B)):
        print("%d" % B[i])


    #########################################
#######TABLES VARIABLES######
#########################################

table = prettytable.PrettyTable(["List size", "Selection sorting time", "Insertion sorting time"])
x=[]
y1=[]
y2=[]

for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))
    B=A.copy()
    t1 = datetime.datetime.now()
    selection(A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Selection sorting " + str(N) + " takes " + str((t2 - t1).total_seconds()) + " s")

    t3 = datetime.datetime.now()
    insertion(B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Insertion sorting " + str(N) + " takes " + str((t4 - t3).total_seconds()) + " s")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds())])
print(table)

plt.plot(x,y1,"C0")
plt.plot(x,y2,"C1")
plt.show()
