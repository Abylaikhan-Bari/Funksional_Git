import tkinter as tk

# Создаем окно с холстом
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=500)
canvas.pack()

# Нарисуем буквы имени Abylaikhan
canvas.create_text(100, 100, text="S", font=("Arial", 72))
canvas.create_text(200, 100, text="t", font=("Arial", 72))
canvas.create_text(300, 100, text="u", font=("Arial", 72))
canvas.create_text(400, 100, text="d", font=("Arial", 72))
canvas.create_text(500, 100, text="e", font=("Arial", 72))
canvas.create_text(600, 100, text="n", font=("Arial", 72))
canvas.create_text(700, 100, text="t", font=("Arial", 72))

# Запускаем основной цикл окна
root.mainloop()
