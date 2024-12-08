import tkinter as tk
import random
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) * 2 + (y2 - y1) * 2)

def show_result(nearest_point, nearest_distance, second_point_distance):
    result_window = tk.Toplevel()
    result_window.title("Результат")
    
    nearest_label = tk.Label(result_window, text=f"Ең жақын нүкте: {nearest_point} (қашықтық: {nearest_distance:.2f})")
    nearest_label.pack()

    second_point_label = tk.Label(result_window, text=f"Екінші нүктеге дейінгі қашықтық: {second_point_distance:.2f}")
    second_point_label.pack()

def calculate_distance():
    global main_point_index, points
    
    main_point = points[main_point_index]
    
    distances = []
    for i, point in enumerate(points):
        if i != main_point_index:
            dist = euclidean_distance(main_point[0], main_point[1], point[0], point[1])
            distances.append((i, dist)) 
    
    nearest_point_index, nearest_distance = min(distances, key=lambda x: x[1])
    
    second_point_index, second_point_distance = [x for x in distances if x[0] != nearest_point_index][0]
    
    show_result(f"Нүкте {nearest_point_index+1}", nearest_distance, second_point_distance)

def generate_random_points():
    global points, main_point_index
    points = [(random.randint(50, 450), random.randint(50, 450)) for _ in range(3)]
    
    for i, (x, y) in enumerate(points):
        canvas.create_oval(x-3, y-3, x+3, y+3, fill="red")
        canvas.create_text(x+10, y-10, text=f"Нүкте {i+1}", font=('Arial', 8))
    
    generate_button.config(state=tk.DISABLED)
    
    main_point_label = tk.Label(window2, text="Бас нүктені таңдау")
    main_point_label.pack()

    button_frame = tk.Frame(window2)
    button_frame.pack()
    for i, (x, y) in enumerate(points):
        button = tk.Button(button_frame, text=f"Нүкте {i+1}", command=lambda i=i: set_main_point(i))
        button.grid(row=0, column=i)

def set_main_point(index):
    global main_point_index
    main_point_index = index
    select_point_button.config(state=tk.NORMAL)

def start():
    global window2, canvas, generate_button, select_point_button, main_point_index, points
    points = []
    main_point_index = None
    
    window2 = tk.Toplevel()
    window2.title("Жақын көршіні іздеу")
    
    canvas = tk.Canvas(window2, width=500, height=500)
    canvas.pack()

    canvas.create_line(250, 0, 250, 500, arrow=tk.LAST) 
    canvas.create_line(0, 250, 500, 250, arrow=tk.LAST)

    button_frame = tk.Frame(window2)
    button_frame.pack()

    generate_button = tk.Button(button_frame, text="Нүктелерді енгізу", command=generate_random_points)
    generate_button.grid(row=0, column=0)

    select_point_button = tk.Button(button_frame, text="Есептеу", command=calculate_distance, state=tk.DISABLED)
    select_point_button.grid(row=0, column=1)

root = tk.Tk()
root.title("Жақын көршіні іздеу")

start_button = tk.Button(root, text="Бастау", command=start)
start_button.pack(pady=20)

exit_button = tk.Button(root, text="Аяқтау", command=root.quit)
exit_button.pack(pady=20)

root.mainloop()
