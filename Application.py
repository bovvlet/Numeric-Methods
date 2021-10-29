from Methods.Euler import Euler
from Methods.EulerImproved import EulerImproved
from Methods.RungeKutta import RungeKutta
import tkinter as tk


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def plot(x_0, y_0, x_n, _N, N_0, N_max, c1, c2, c3):
    '''cleaning all plots'''
    plt.clf()

    '''converting values from string to int'''
    x0 = int(x_0)
    xn = int(x_n)
    y0 = int(y_0)
    N = int(_N)
    n_0 = int(N_0)
    n_max = int(N_max)

    method = [Euler(x0, y0, xn, N, n_0, n_max),
              EulerImproved(x0, y0, xn, N, n_0,  n_max),
              RungeKutta(x0, y0, xn, N, n_0,  n_max)]
    '''ploting exact solution'''
    x = np.arange(x0, xn, 0.01)
    y = method[0].y_exact(x)
    plt.subplot(2, 2, 1)
    plt.plot(x, y, 'm', label='exact')
    plt.legend()

    for cur in method:
        '''cheching checkboxes'''
        if cur.name == 'Euler' and c1.get() == False:
            continue
        if cur.name == 'Improved_Euler' and c2.get() == False:
            continue
        if cur.name == 'RungeKutta' and c3.get() == False:
            continue

        cur.compute_points(N)
        cur.compute_errors(N)

        '''graphing with usage of method'''
        plt.subplot(2, 2, 1)
        plt.ylabel("Graph of methods")
        plt.xlabel("X")
        plt.plot(cur.get_x_array(), cur.get_y_array(), label=cur.name)
        plt.grid()
        plt.legend()

        '''graph of errors for some N'''
        plt.subplot(2, 2, 2)
        plt.ylabel("Local errors")
        plt.xlabel("X")
        plt.plot(cur.get_x_array(), cur.get_error_array(), label=cur.name)
        plt.grid()
        plt.legend()

        '''graph of errors for some interval for N'''
        cur.compute_global_errors()
        x_euler_global = np.arange(n_0, n_max + 1)
        y_euler_global = cur.get_global_error()
        plt.subplot(2, 1, 2)
        plt.ylabel("Global errors")
        plt.xlabel("N")
        plt.plot(x_euler_global, y_euler_global, label=cur.name)
        plt.grid()
        plt.legend()
    plt.show()

def start():
    '''customizing of out GUI'''
    matplotlib.use("tkAgg")
    win = tk.Tk()
    win.title('Numerical methods')
    win.geometry("400x280+10+10")
    win.resizable(False, False)
    for i in range(9):
        win.rowconfigure(i, minsize=30)
        win.columnconfigure(i, minsize=15)

    '''labels'''
    tk.Label(win, text="calculating numerical methods", font="Arrial").grid(row=0, columnspan=2)
    tk.Label(win, text="enter   x_0", padx=5).grid(row=1)
    tk.Label(win, text="enter   y_0", padx=5).grid(row=2)
    tk.Label(win, text="enter     N", padx=5).grid(row=3)
    tk.Label(win, text="enter     X", padx=5).grid(row=4)
    tk.Label(win, text="calculating error", font="Arrial").grid(row=5, columnspan=2)
    tk.Label(win, text="enter   n_0", padx=5).grid(row=6)
    tk.Label(win, text="enter N_max", padx=5).grid(row=7)

    '''entries'''
    x_0_entry = tk.Entry(win)
    y_0_entry = tk.Entry(win)
    X_entry = tk.Entry(win)
    N_entry = tk.Entry(win)
    n_0_entry = tk.Entry(win)
    n_max_entry = tk.Entry(win)

    '''putting initial values on our entries'''
    x_0_entry.insert(0, "1")
    y_0_entry.insert(0, "-2")
    X_entry.insert(0, "7")
    N_entry.insert(0, "10")
    n_0_entry.insert(0, "5")
    n_max_entry.insert(0, "30")

    '''placement of entries on the GUI'''
    x_0_entry.grid(row=1, column=1)
    y_0_entry.grid(row=2, column=1)
    N_entry.grid(row=3, column=1)
    X_entry.grid(row=4, column=1)
    n_0_entry.grid(row=6, column=1)
    n_max_entry.grid(row=7, column=1)


    '''variable of checkboxes'''
    c1 = tk.BooleanVar()
    c2 = tk.BooleanVar()
    c3 = tk.BooleanVar()
    c1.set(True)
    c2.set(True)
    c3.set(True)

    '''checkbuttons'''
    Eu = tk.Checkbutton(text='Euler', onvalue=1, offvalue=0, variable=c1)
    Imp_Eu = tk.Checkbutton(text='ImprovedEu', onvalue=1, offvalue=0, variable=c2)
    Runge = tk.Checkbutton(text='Runge', onvalue=1, offvalue=0, variable=c3)

    '''placement of checkbuttons on the GUI'''
    Eu.grid(row=0, column=3)
    Imp_Eu.grid(row=1, column=3)
    Runge.grid(row=2, column=3)

    '''button for ploting'''
    tk.Button(text='Plot', command=lambda: plot(x_0_entry.get(),
                                                y_0_entry.get(),
                                                X_entry.get(),
                                                N_entry.get(),
                                                n_0_entry.get(),
                                                n_max_entry.get(), c1, c2, c3)).\
        grid(row=8, columnspan=2, rowspan=2, stick='news')

    win.mainloop()


