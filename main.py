import musicalbeeps
import random

oldList =[]
listOfData = []

# opening the file in read mode
with open('files/dataList.txt', 'r') as f:
    oldList = f.readlines()

# remove \n from the list
for line in oldList:
    if line[-1] == "\n":
        listOfData.append(line[:-1])
    else:
        listOfData.append(line)


# printing the data
print(listOfData)

player = musicalbeeps.Player(volume = 0.8,mute_output = False)


#the slower the sequence, the slower insertion go

def insertionSort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        player.play_note("B", 1)

        # Move elements of arr, that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            player.play_note("D", 1)
            arr[j + 1] = arr[j]

            j -= 1
        arr[j + 1] = key



insertionSort(listOfData)
print(listOfData)