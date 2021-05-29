import tkinter

import Sorting_Visualiser



def selectionSort():
    Sorting_Visualiser.visualise(3)

def bubbleSort():
    Sorting_Visualiser.visualise(1)

def insertionSort():
    Sorting_Visualiser.visualise(4)

def quickSort():
    Sorting_Visualiser.visualise(5)

def mergeSort():
    Sorting_Visualiser.visualise(2)

def quickSortImplace():
    Sorting_Visualiser.visualise(6)



window = tkinter.Tk()
window.title("Sorting Visualiser!")

window.minsize(width = 500 ,height = 300)

my_label = tkinter.Label(text = "Sorting Visualiser!",font=("Arial",34,"bold"))
my_label.pack()


button1 = tkinter.Button(text = "Selection Sort",command = selectionSort)
button1.pack()

button2 = tkinter.Button(text = "Bubble Sort",command = bubbleSort)
button2.pack()

button3 = tkinter.Button(text = "Insertion Sort",command = insertionSort)
button3.pack()

button4 = tkinter.Button(text = "Merge Sort",command = mergeSort)
button4.pack()

button5 = tkinter.Button(text = "Quick Sort",command = quickSort)
button5.pack()


button6 = tkinter.Button(text = "Quick Sort Implace",command = quickSortImplace)
button6.pack()





window.mainloop()