import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *

# ===== URLS ===== #
CASE_TIME_SERIES = "https://api.covid19india.org/csv/latest/case_time_series.csv"
STATE_WISE = "https://api.covid19india.org/csv/latest/state_wise.csv"
DIST_WISE = "https://api.covid19india.org/csv/latest/district_wise.csv"

# # # # # DATA EXTRACTION # # # # #
# ===== CASE-TIME-SERIES ===== #
cts_cols = ['Total Confirmed', 'Total Recovered', 'Total Deceased']
cts = pd.read_csv(CASE_TIME_SERIES, usecols=cts_cols)
cts_total = cts.iloc[-1]

# ===== STATE-WISE ===== #
sw_cols = ['Confirmed', 'Recovered', 'Deaths', 'Active']
state_wise = pd.read_csv(STATE_WISE, usecols=sw_cols)
sw_ka = state_wise.loc[3]

# ===== DISTRICT-WISE ===== #
dist_cols = ['Confirmed', 'Recovered', 'Deceased', 'Active']
dist = pd.read_csv(DIST_WISE, usecols=dist_cols)
dist_mys = dist.loc[302]

# ===== MAIN APP ===== #
root = Tk()
root.title('Extraction & Visualization of COVID-19 DB')
root.resizable(False, False)

# ===== FIRST FRAME ===== #
frame1 = LabelFrame(root, padx=10, pady=10)
frame1.grid(row=0, column=0, padx=5, pady=5, sticky='NSEW')

# ===== SECOND FRAME ===== #
frame2 = LabelFrame(root, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=5, pady=5, sticky='NSEW')

# ===== THIRD FRAME ===== #
frame3 = LabelFrame(root, padx=10, pady=10)
frame3.grid(row=1, column=0, padx=5, pady=5, sticky='NSEW')

# ===== FOURTH FRAME ===== #
frame4 = LabelFrame(root, padx=10, pady=10)
frame4.grid(row=1, column=1, padx=5, pady=5, sticky='NSEW')

# ===== LABELS ===== #
l1_f2 = Label(frame2, text="Confirmed", width=20, font=("bold", 12))
l1_f2.grid(row=0, column=0, padx=5, pady=10, sticky=W)
l2_f2 = Label(frame2, text="Recovered", width=20, font=("bold", 12))
l2_f2.grid(row=1, column=0, padx=5, pady=10, sticky=W)
l3_f2 = Label(frame2, text="Deaths", width=20, font=("bold", 12))
l3_f2.grid(row=2, column=0, padx=5, pady=10, sticky=W)
l4_f2 = Label(frame2, text="Active", width=20, font=("bold", 12))
l4_f2.grid(row=3, column=0, padx=5, pady=10, sticky=W)

# ===== ENTRY ===== #
confirmed = Text(frame2, height=1, width=20, borderwidth=2, font=("bold", 12))
confirmed.grid(row=0, column=1)
recovered = Text(frame2, height=1, width=20, borderwidth=2, font=("bold", 12))
recovered.grid(row=1, column=1)
deaths = Text(frame2, height=1, width=20, borderwidth=2, font=("bold", 12))
deaths.grid(row=2, column=1)
active = Text(frame2, height=1, width=20, borderwidth=2, font=("bold", 12))
active.grid(row=3, column=1)


# # # # # DATA VISUALIZATION # # # # #
def plot(key):
    """Plot Graphs: Bar and Pie chart"""
    fig1 = plt.Figure(figsize=(5, 4), dpi=100)
    fig1.suptitle(f'Bar Chart', fontsize=10)
    ax1 = fig1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(fig1, frame3)
    bar1.get_tk_widget().grid(row=0, column=0)

    fig2 = plt.Figure(figsize=(5, 4), dpi=100)
    fig2.suptitle(f'Pie Chart', fontsize=10)
    ax2 = fig2.add_subplot(111)
    pie2 = FigureCanvasTkAgg(fig2, frame4)
    pie2.get_tk_widget().grid(row=0, column=0)

    if key == 1:
        cts_total.plot(kind='bar', color='lightcoral', ax=ax1)
        colors = ['gold', 'yellowgreen', 'lightcoral']
        explode = (0, 0, 0.1)
        cts_total.plot(kind='pie', colors=colors, explode=explode,
                       autopct='%1.1f%%', startangle=100, legend=True, ax=ax2)

    elif key == 2:
        sw_ka.plot(kind='bar', color='lightcoral', ax=ax1)
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0, 0, 0.2, 0.1)
        sw_ka.plot(kind='pie', colors=colors, explode=explode,
                   autopct='%1.1f%%', startangle=100, legend=True, ax=ax2)

    elif key == 3:
        dist_mys.plot(kind='bar', color='lightcoral', ax=ax1)
        colors = ['gold', 'lightskyblue', 'yellowgreen', 'lightcoral']
        explode = (0, 0.1, 0, 0.1)
        dist_mys.plot(kind='pie', colors=colors, explode=explode,
                      autopct='%1.1f%%', startangle=100, legend=True, ax=ax2)


def set_label(txt):
    label_f1 = Label(frame1, text='Total', width=10, font=("bold", 15))
    label_f1.grid(row=0, column=1, padx=10, pady=10)
    label_f2 = Label(frame1, text='Cases', width=10, font=("bold", 15))
    label_f2.grid(row=1, column=1, padx=10, pady=10)
    label_f3 = Label(frame1, text=f'in {txt}', width=10, font=("bold", 15))
    label_f3.grid(row=2, column=1, padx=10, pady=10)


def select(key):
    """Update text widget"""
    global confirmed
    global recovered
    global deaths
    global active

    confirmed.configure(state='normal')
    recovered.configure(state='normal')
    deaths.configure(state='normal')
    active.configure(state='normal')

    confirmed.delete(1.0, END)
    recovered.delete(1.0, END)
    deaths.delete(1.0, END)
    active.delete(1.0, END)

    if key == 1:
        set_label('India')
        confirmed.insert(END, f"{cts_total['Total Confirmed']:,}")
        recovered.insert(END, f"{cts_total['Total Recovered']:,}")
        deaths.insert(END, f"{cts_total['Total Deceased']:,}")
        active.insert(END, '-')
        plot(1)

    elif key == 2:
        set_label('Karnataka')
        confirmed.insert(END, f"{sw_ka['Confirmed']:,}")
        recovered.insert(END, f"{sw_ka['Recovered']:,}")
        deaths.insert(END, f"{sw_ka['Deaths']:,}")
        active.insert(END, f"{sw_ka['Active']:,}")
        plot(2)

    elif key == 3:
        set_label('Mysuru')
        confirmed.insert(END, f"{dist_mys['Confirmed']:,}")
        recovered.insert(END, f"{dist_mys['Recovered']:,}")
        deaths.insert(END, f"{dist_mys['Deceased']:,}")
        active.insert(END, f"{dist_mys['Active']:,}")
        plot(3)

    confirmed.configure(state='disabled')
    recovered.configure(state='disabled')
    deaths.configure(state='disabled')
    active.configure(state='disabled')


# ===== BUTTONS ===== #
ind = Button(frame1, text='India', width=15, bg="black",
             justify=CENTER, fg='white', command=lambda: select(1))
ind.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

kar = Button(frame1, text='Karnataka', width=15, bg="black",
             justify=CENTER, fg='white', command=lambda: select(2))
kar.grid(row=1, column=0, padx=10, pady=10, columnspan=1)

mys = Button(frame1, text='Mysuru', width=15, bg="black",
             justify=CENTER, fg='white', command=lambda: select(3))
mys.grid(row=2, column=0, padx=10, pady=10, columnspan=1)

root.mainloop()
