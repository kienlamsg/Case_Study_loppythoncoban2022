
from tkinter import *
from tkinter import ttk
from datetime import date


tkWindow = Tk()
tkWindow.geometry('1000x900')  
tkWindow.title('Expense management app homepage')

Label(tkWindow, text="Welcome to expense management app!").pack(side='top')

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

# def update_exp_type_option(*args):
#     exp_category_selection = exp_dict[exp_category.get()]
#     exp_type.set(exp_category_selection[0])
    
#     new_exp_type = exp_type_Entry_widget['exp_type']
#     new_exp_type.delete(0, 'end')
#     for el in exp_category_selection:
#         new_exp_type.add_command(command=lambda type = el : exp_type.set(type))

def update_exp_type_option(*args):
    exp_category_selection = exp_dict[exp_category.get()]
    exp_type.set('')
    exp_type_option['menu'].delete(0, 'end')
    for el in exp_category_selection:
        exp_type_option['menu'].add_command(label=el, command= lambda: exp_type.set(el))
    exp_type.set(exp_category_selection[0])


exp_dict = {'food & drink': ['restaurant', 'snacks', 'coffee'],
            'transportation':['taxi', 'bus', 'train mrt'], 
            'essentials':['groceries', 'bill', 'household'],
            'entertainment':['movies','shopping','party'],
            'others':['shopping','study','others']}



#exp category label + expense type label & optionmenu
exp_category_lbl = Label(expense_input_frame, text="Expense Category").grid(row=0, column=0)
exp_type_lbl = Label(expense_input_frame,text="Expense Type").grid(row=1, column=0)  

exp_category = StringVar()
exp_type = StringVar()

exp_category.trace('w', update_exp_type_option)

exp_category_option = OptionMenu(expense_input_frame, exp_category, *exp_dict.keys())
exp_category_option.grid(row=0, column=1,sticky = 'ew')  

exp_type_option = OptionMenu(expense_input_frame, exp_type, '')
exp_type_option.grid(row=1, column=1, sticky = 'ew')   


#price label and price entry box
price_lbl = Label(expense_input_frame,text="Price").grid(row=2, column=0)  
price= IntVar()
price_Entry_widget = Entry(expense_input_frame, name = 'price', textvariable= price).grid(row=2, column=1)  

#date label and date entry box
exp_date_lbl = Label(expense_input_frame,text="Expense Date").grid(row=3, column=0)  
exp_date = StringVar()
exp_date_Entry_widget = Entry(expense_input_frame, name = 'exp_date', textvariable= exp_date)
exp_date_Entry_widget.grid(row=3, column=1)


def add_current_date_btn_f():
    exp_date_Entry_widget.delete(0,END)
    exp_date_Entry_widget.insert(0,date.today())
    return
    
    
add_current_date_btn = Button(expense_input_frame, text = 'Add Current Date',command= lambda: add_current_date_btn_f())
add_current_date_btn.grid(row=3, column = 3)

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
