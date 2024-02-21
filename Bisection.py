import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Fungsi untuk menghitung koefisien regresi linier
def calculate_coefficients(x, y):
    n = len(x)
    sum_x, sum_y, sum_x2, sum_xy = 0, 0, 0, 0
    for i in range(n):
        sum_x += x[i]
        sum_y += y[i]
        sum_x2 += x[i]**2
        sum_xy += x[i]*y[i]
    a = (sum_y*sum_x2 - sum_x*sum_xy) / (n*sum_x2 - sum_x**2)
    b = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
    return a, b

# Fungsi untuk membuat grafik
def create_plot(x, y, a, b):
    fig = plt.Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.scatter(x, y, color='red')
    ax.plot(x, [a + b*i for i in x], color='blue')
    return fig

# Fungsi untuk menangani klik tombol
def on_button_click():
    x = list(map(float, entry_x.get().split(',')))
    y = list(map(float, entry_y.get().split(',')))
    a, b = calculate_coefficients(x, y)
    fig = create_plot(x, y, a, b)
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    label_result = tk.Label(root, text=f"Koefisien a: {a}, Koefisien b: {b}")
    label_result.pack()

# Membuat antarmuka pengguna
root = tk.Tk()
root.title("Least Squares Polynomial Degree 2")

frame = tk.Frame(root)
frame.pack()

label_judul = tk.Label(frame, text="LEAST SQUARES POLYNOMIAL DEGREE 2", font= ("Comic n Sans", 30, "bold"), fg="maroon")
label_judul.pack()

label_anggota = tk.Label(frame, text="ANGGOTA KELOMPOK : ", font= ("Arial", 10 , "bold"), fg="Black")
label_anggota.pack()

label_nama1 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama1.pack()
label_nama2 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama2.pack()
label_nama3 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama3.pack()
label_nama4 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama4.pack()
label_nama5 = tk.Label(frame, text="Nama: Muthia Zhafira , NIM: 24060122130071", font= ("Arial", 10), fg="Black")
label_nama5.pack()

label_x = tk.Label(root, text="Masukkan nilai x (pisahkan dengan koma):")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()
label_y = tk.Label(root, text="Masukkan nilai y (pisahkan dengan koma):")
label_y.pack()
entry_y = tk.Entry(root)
entry_y.pack()
button = tk.Button(root, text="Hitung Koefisien dan Buat Grafik", command=on_button_click)
button.pack()
root.mainloop()
