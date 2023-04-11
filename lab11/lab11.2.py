import tkinter as tk

# Создаем окно с холстом
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()

# Нарисуем буквы имени Abylaikhan
canvas.create_text(100, 100, text="A", font=("Arial", 72))
canvas.create_text(200, 100, text="b", font=("Arial", 72))
canvas.create_text(300, 100, text="y", font=("Arial", 72))
canvas.create_text(400, 100, text="l", font=("Arial", 72))
canvas.create_text(500, 100, text="a", font=("Arial", 72))
canvas.create_text(600, 100, text="i", font=("Arial", 72))

# Запускаем основной цикл окна
root.mainloop()
