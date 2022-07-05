from threading import local
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from datetime import date

from numpy import record




tkWindow = Tk()
tkWindow.geometry('1000x800')  
tkWindow.title('Expense management app homepage')

Label(tkWindow, text="Welcome to expense management app!").pack(pady=20)

expense_display_frame = Frame(tkWindow)
expense_display_frame.place(relx=0.5,
    rely=0.2,
    anchor= 'center')


columns = ('expense_category', 'expense_type', 'price', 'date')
tree = ttk.Treeview(expense_display_frame, columns=columns, show='headings')

tree.heading('expense_category', text='Expense Category   ')
tree.heading('expense_type', text='Expense Type   ')
tree.heading('price', text='Price   ')
tree.heading('date', text='Date   ')

exp_list = []
totalexpense = 0

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # showinfo(title= 'Information', message= ','. join(record))
        
tree.bind('<<TreeviewSelect>>', item_selected)

tree.grid(row=0, column=0, sticky='nsew')

scrollbar = Scrollbar(expense_display_frame, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky='nsew')


#update expense button 
def update_expense_btn_f():
    selected = tree.focus()
    tree.item(selected, values= [exp_category.get(), exp_type.get(), price.get(),exp_date.get()])

update_exp_btn = Button(expense_display_frame, text = 'update', command= lambda: update_expense_btn_f())
update_exp_btn.grid(row=8, column = 0)

#delete expense button 
def delete_expense_btn_f():
    x = tree.selection()
    for i in x:
        tree.delete(x)

delete_exp_btn = Button(expense_display_frame, text = 'delete', command = lambda: delete_expense_btn_f())
delete_exp_btn.grid(row=9, column = 0)

#report expense button 
def report_expense_btn_f():
    global exp_list
    global totalexpense
    for i in range (len(exp_list)):
        totalexpense += exp_list[i][2]
        i = i + 1
        
    report_exp_lbl.config(text='Total Expense: ' + str(totalexpense))
    totalexpense = 0

report_exp_btn = Button(expense_display_frame, text = 'report', command =lambda: report_expense_btn_f())
report_exp_btn.grid(row=10, column = 0)

report_exp_lbl = Label(expense_display_frame, text = 'Total Expense: ')
report_exp_lbl.grid(row=11, column = 0)




#input frame
expense_input_frame = Frame(tkWindow)
expense_input_frame.place(rely=0.5)

#exp category label and entry box
exp_category_lbl = Label(expense_input_frame, text="Expense Category").grid(row=0, column=0)
exp_category = StringVar()
exp_category_Entry_widget = Entry(expense_input_frame, name = 'exp_category', textvariable= exp_category).grid(row=0, column=1)  

#expense type label and entry box
exp_type_lbl = Label(expense_input_frame,text="Expense Type").grid(row=1, column=0)  
exp_type = StringVar()
exp_type_Entry_widget = Entry(expense_input_frame, name= 'exp_type', textvariable= exp_type).grid(row=1, column=1)  

#price label and price entry box
price_lbl = Label(expense_input_frame,text="Price").grid(row=2, column=0)  
price= IntVar()
price_Entry_widget = Entry(expense_input_frame, name = 'price', textvariable= price).grid(row=2, column=1)  

#date label and date entry box
exp_date_lbl = Label(expense_input_frame,text="Expense Date").grid(row=3, column=0)  
exp_date = StringVar()
exp_date_Entry_widget = Entry(expense_input_frame, name = 'exp_date', textvariable= exp_date).grid(row=3, column=1)  

#show current date
date_lbl = Label(expense_input_frame, text=date.today()).grid(row=5,column=1)


def add_exp_btn_f():
    global exp_list
    exp_list.append([exp_category.get(), exp_type.get(), price.get(),exp_date.get()])
        
    for item in tree.get_children():
        tree.delete(item)

    for exp in exp_list:
        tree.insert('', END, values=exp)
        

#add expense button 
add_exp_btn = Button(expense_input_frame, text = 'Add',command= lambda: add_exp_btn_f())
add_exp_btn.grid(row=6, column = 1)

 
  
tkWindow.mainloop()
print(exp_list)

