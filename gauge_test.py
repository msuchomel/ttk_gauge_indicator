import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random

app = ttk.Window()
style = ttk.Style('litera')

def count_down():
    meter.step(1)
    meter.after(1000, count_down)

def start_up():
    meter.amountusedvar.set(random.randint(0,100))

def button_click():
    meter.configure(amountused=random.randint(0,100))

meter = ttk.Meter(
    master=app,
    metersize=180,
    padding=5,
    amountused=60,
    amounttotal=100,
    stripethickness=2,
    metertype='full',
    subtext='Counted Things',
    interactive=False
)
meter.pack(side=LEFT)

btn = ttk.Button(master=app, text='Test', command=button_click)
btn.pack(side=RIGHT)

#count_down()
#meter.step(1)
start_up()

#style.master.mainloop()
app.mainloop()