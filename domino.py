from tkinter import *
import random
import time

root = Tk()
root.geometry('1600x800+0+0')
root.title("Domino's Pizza")

text_Input = StringVar()
operator = ""

frame = Frame(root, width = 1600, height = 50,bg = 'blue', relief = SUNKEN)
frame.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700, relief = SUNKEN)
f1.pack(side = LEFT)

f2 = Frame(root, width = 300, height = 700, relief = SUNKEN)
f2.pack(side = RIGHT)
#time
localtime = time.asctime(time.localtime(time.time()))
#display
lblInfo = Label(frame, font = ('arial', 50, 'bold'), text = "Domino's Pizza", fg = 'Steel Blue', bd = 10, anchor = 'w')
lblInfo.grid(row = 0, column = 0)
lblInfo = Label(frame, font = ('arial', 20, 'bold'), text = localtime, fg = 'Steel Blue', bd = 10, anchor = 'w')
lblInfo.grid(row = 1, column = 0)
#calci
def bClick(numbers):
    global operator
    operator += str(numbers)
    text_Input.set(operator)

def bClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def bEqualsInput():
    global operator
    ans = str(eval(operator))
    text_Input.set(ans)
    operator = ""

def Ref():
    x = random.randint(10000, 50000)
    randomRef = str(x)
    rand.set(randomRef)

    if(pp.get() != ""):
        PP = float(pp.get())
    else:
        PP = 0

    if(mgw.get() != ""):
        MGW = float(mgw.get())
    else:
        MGW = 0

    if(dv.get() != ""):
        DV = float(dv.get())
    else:
        DV = 0

    if(ve.get() != ""):
        VE = float(ve.get())
    else:
        VE = 0

    if(m.get() != ""):
        M = float(m.get())
    else:
        M = 0

    if(fh.get() != ""):
        FH = float(fh.get())
    else:
        FH = 0

    if(coke.get() != ""):
        C = float(coke.get())
    else:
        C = 0

    cpp = PP * 199
    cmgw = MGW * 299
    cdv = DV * 249
    cve = VE * 299
    cm = M * 199
    cfh = FH * 349
    cc = C * 99

    CostofMeal = "Rs", str('%.2f' % (cpp + cmgw + cdv + cve + cm + cfh + cc))

    Tax = (cpp + cmgw + cdv + cve + cm + cfh + cc) * 0.05

    Total = (cpp + cmgw + cdv + cve + cm + cfh + cc)

    svc = (cpp + cmgw + cdv + cve + cm + cfh + cc) * 0.01

    service = "Rs", str('%.2f' % svc)

    OverAllCost = "Rs", str('%.0f' % (Tax + Total + svc))

    gst = "Rs", str('%.2f' % Tax)

    sc.set(service)
    cost.set(CostofMeal)
    tax.set(gst)
    subTotal.set(CostofMeal)
    total.set(OverAllCost)
    
    
def qExit():
    root.destroy()

def Reset():
    rand.set("")
    pp.set("")
    mgw.set("")
    dv.set("")
    ve.set("")
    m.set("")
    fh.set("")
    coke.set("")
    subTotal.set("")
    total.set("")
    tax.set("")
    cost.set("")
    sc.set("")

    

txtDisplay = Entry(f2, font = ('arial', 20, 'bold'), textvariable = text_Input, bd = 30, insertwidth = 4, bg = 'powder blue', justify = 'right').grid(columnspan = 4)
b7 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '7', bg = 'powder blue', command = lambda: bClick(7)).grid(row = 2, column = 0)
b8 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '8', bg = 'powder blue', command = lambda: bClick(8)).grid(row = 2, column = 1)
b9 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '9', bg = 'powder blue', command = lambda: bClick(9)).grid(row = 2, column = 2)
Add = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '+', bg = 'powder blue', command = lambda: bClick('+')).grid(row = 2, column = 3)

b4 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '4', bg = 'powder blue', command = lambda: bClick(4)).grid(row = 3, column = 0)
b5 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '5', bg = 'powder blue', command = lambda: bClick(5)).grid(row = 3, column = 1)
b6 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '6', bg = 'powder blue', command = lambda: bClick(6)).grid(row = 3, column = 2)
Sub = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '-', bg = 'powder blue', command = lambda: bClick('-')).grid(row = 3, column = 3)

b1 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '1', bg = 'powder blue', command = lambda: bClick(1)).grid(row = 4, column = 0)
b2 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '2', bg = 'powder blue', command = lambda: bClick(2)).grid(row = 4, column = 1)
b3 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '3', bg = 'powder blue', command = lambda: bClick(3)).grid(row = 4, column = 2)
Mul = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '*', bg = 'powder blue', command = lambda: bClick('*')).grid(row = 4, column = 3)

b0 = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '0', bg = 'powder blue', command = lambda: bClick(0)).grid(row = 5, column = 0)
bc = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = 'C', bg = 'powder blue', command = bClearDisplay).grid(row = 5, column = 1)
be = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '=', bg = 'powder blue', command = bEqualsInput).grid(row = 5, column = 2)
Div = Button(f2, padx = 16, pady = 16, bd = 8, fg = 'black', font = ('arial', 20, 'bold'), text = '/', bg = 'powder blue', command = lambda: bClick('/')).grid(row = 5, column = 3)

#endcalci

rand = StringVar()
pp = StringVar()
mgw = StringVar()
dv = StringVar()
ve = StringVar()
m = StringVar()
fh = StringVar()
coke = StringVar()
subTotal = StringVar()
total = StringVar()
tax = StringVar()
cost = StringVar()
sc = StringVar()


lblRef = Label(f1, font = ('arial', 16, 'bold'), text = 'Reference', bd = 16, anchor = 'w').grid(row = 0, column = 0)
txtRef = Entry(f1, font = ('arial', 16, 'bold'), textvariable = rand, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 0, column = 1)

lblPP = Label(f1, font = ('arial', 16, 'bold'), text = 'Peppy Paneer', bd = 16, anchor = 'w').grid(row = 1, column = 0)
txtPP = Entry(f1, font = ('arial', 16, 'bold'), textvariable = pp, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 1, column = 1)

lblmgw = Label(f1, font = ('arial', 16, 'bold'), text = 'Mexican Green Wave', bd = 16, anchor = 'w').grid(row = 2, column = 0)
txtmgw = Entry(f1, font = ('arial', 16, 'bold'), textvariable = mgw, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 2, column = 1)

lbldv = Label(f1, font = ('arial', 16, 'bold'), text = 'Deluxe Veggie', bd = 16, anchor = 'w').grid(row = 3, column = 0)
txtdv = Entry(f1, font = ('arial', 16, 'bold'), textvariable = dv, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 3, column = 1)

lblve = Label(f1, font = ('arial', 16, 'bold'), text = 'Veg Extravanganza', bd = 16, anchor = 'w').grid(row = 4, column = 0)
txtve = Entry(f1, font = ('arial', 16, 'bold'), textvariable = ve, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 4, column = 1)

lblm = Label(f1, font = ('arial', 16, 'bold'), text = 'Margherita', bd = 16, anchor = 'w').grid(row = 5, column = 0)
txtm = Entry(f1, font = ('arial', 16, 'bold'), textvariable = m, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 5, column = 1)

lblfh = Label(f1, font = ('arial', 16, 'bold'), text = 'Farm House', bd = 16, anchor = 'w').grid(row = 6, column = 0)
txtfh = Entry(f1, font = ('arial', 16, 'bold'), textvariable = fh, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 6, column = 1)

#----------------------------------------------------------

lblc = Label(f1, font = ('arial', 16, 'bold'), text = 'Coke', bd = 16, anchor = 'w').grid(row = 0, column = 2)
txtc = Entry(f1, font = ('arial', 16, 'bold'), textvariable = coke, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 0, column = 3)

lblcost = Label(f1, font = ('arial', 16, 'bold'), text = 'Cost', bd = 16, anchor = 'w').grid(row = 1, column = 2)
txtcost = Entry(f1, font = ('arial', 16, 'bold'), textvariable = cost, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 1, column = 3)

lblsc = Label(f1, font = ('arial', 16, 'bold'), text = 'Service Charge', bd = 16, anchor = 'w').grid(row = 2, column = 2)
txtsc = Entry(f1, font = ('arial', 16, 'bold'), textvariable = sc, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 2, column = 3)

lblt = Label(f1, font = ('arial', 16, 'bold'), text = 'GST', bd = 16, anchor = 'w').grid(row = 3, column = 2)
txtt = Entry(f1, font = ('arial', 16, 'bold'), textvariable = tax, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 3, column = 3)

lblst = Label(f1, font = ('arial', 16, 'bold'), text = 'Sub Total', bd = 16, anchor = 'w').grid(row = 4, column = 2)
txtst = Entry(f1, font = ('arial', 16, 'bold'), textvariable = subTotal, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 4, column = 3)

lblto = Label(f1, font = ('arial', 16, 'bold'), text = 'Total', bd = 16, anchor = 'w').grid(row = 5, column = 2)
txtto = Entry(f1, font = ('arial', 16, 'bold'), textvariable = total, bd = 10, insertwidth = 4, bg = 'blue', justify = 'right').grid(row = 5, column = 3)

#----------------------------------------------------------

bTotal = Button(f1, padx = 16, pady = 8, fg = 'black', font = ('arial', 16, 'bold'), width = 10, text = 'Total', bg = 'red', command = Ref).grid(row = 7, column = 1)
bReset = Button(f1, padx = 16, pady = 8, fg = 'black', font = ('arial', 16, 'bold'), width = 10, text = 'Reset', bg = 'red', command = Reset).grid(row = 7, column = 2)
bquit = Button(f1, padx = 16, pady = 8, fg = 'black', font = ('arial', 16, 'bold'), width = 10, text = 'Exit', bg = 'red', command = qExit).grid(row = 7, column = 3)

root.mainloop()
