from tkinter import ttk
import random
from tkinter import *
from colors import *
import time
import tkinter as tk

# Importing algorithms
from algorithms.bubbleSort import bubble_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.mergeSort import merge_sort
from algorithms.quickSort import quick_sort
from algorithms.heapSort import heap_sort
from algorithms.countingSort import counting_sort


# Main window using the TK widget
window = Tk()
window.title("Sorting Algorithms Visualization using Python")
window.geometry('600x450')
window.config(bg=WHITE)


algorithm_name = StringVar()
speed_name = StringVar()
data = []
algo_list = ['Bubble Sort', 'Insertion Sort', 'Selection Sort',
             'Merge Sort', 'Quick Sort', 'Heap Sort', 'Counting Sort']
speed_list = ['slow', 'Medium', 'Fast']


# Drawing the numerical array as bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


# Randomly generate array
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [LIGHT_GREEN for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)
    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == 'Heap Sort':
        heap_sort(data, drawData, timeTick)
    else:
        counting_sort(data, drawData, timeTick)


# User interface to show the front-end part
frame = Frame(width=900, height=300, bg=LIGHT_GRAY)
frame.grid(row=0, column=0, padx=20, pady=10)

l1 = Label(frame, text="Select the Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(
    frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

b1 = Button(frame, text="Click to generate Array",
            command=generate, bg=LIGHT_GRAY)
b1.grid(row=2, column=0, padx=5, pady=5)

l2 = Label(frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(column=1, row=1, padx=5, pady=5)
speed_menu.current(0)

canvas = Canvas(window, width=1600, height=400, bg=LIGHT_GRAY)
canvas.grid(row=1, column=0, padx=10, pady=5)

b3 = Button(frame, text="visualizer", command=sort, bg=LIGHT_GRAY)
b3.grid(row=2, column=1, padx=5, pady=5)


"""insert = tk.Button(window, text='Insertion Sort', command=insertion_sort)
select = tk.Button(window, text='Selection Sort', command=selection_sort)
bubble = tk.Button(window, text='Bubble Sort', command=bubble_sort)
shuf = tk.Button(window, text='Shuffle', command=generate)
insert.grid(column=1, row=1)
select.grid(column=2, row=1)
bubble.grid(column=3, row=1)
shuf.grid(column=0, row=1)"""


window.mainloop()
