import tkinter as tk
from tkinter.constants import ACTIVE, DISABLED, END
from random import randrange

root = tk.Tk()
root.title("vaccination data")

#To create 4 digit randam number
def rand ():
    tokan = ''
    for i in range(4):
        tokan = tokan + str(randrange(1,10))
    return tokan

def isnotint(test):
    for i in test:
        try:
            int(i)
        except ValueError :
            return True
    return False

#for button next 
def next_check():
    global entry, data, tokan, time_slot_list
    tokan = rand()
    aadhar = aadhar_no.get()
    phone = phone_no.get()

    if len(aadhar) == 0:
        check_i.config(text="please enter your aadhar card number")
    elif len(aadhar) != 12 :
        check_i.config(text="please check your aadhar card number")
    elif isnotint(aadhar) :
        check_i.config(text="aadhar number should only contain numbers")
    elif len(aadhar) == 0:
        check_i.config(text="please enter your phone number")
    elif len(phone) != 10 :
        check_i.config(text="please check your phone number")
    elif isnotint(phone) :
        check_i.config(text="phone number should only contain numbers")
    else:
        check_i.config(text=" ")
        j = round(entry/people_per_slot) if entry%people_per_slot == 0 else entry//people_per_slot+1
        time_slot_list = " to ".join(time[j:j+2])
        give_tokan.config(text=tokan)
        time_slot.config(text=time_slot_list)
        submit_button.config(state=ACTIVE)
        next_button.config(state=DISABLED)


#for button submit
def submit_check ():
    aadhar = aadhar_no.get()
    phone = phone_no.get()
    global entry
    data.append([entry,aadhar,phone,tokan,time_slot_list])
    entry += 1
    entry_no.config(text=f"Entry number: {entry}")
    aadhar_no.delete(0,END)
    phone_no.delete(0,END)
    give_tokan.config(text=" ")
    time_slot.config(text=" ")
    next_button.config(state=ACTIVE)
    submit_button.config(state=DISABLED)



time = [0,'06:00','06:30','07:00','07:30','08:00','08:30','09:00']
people_per_slot = 5
entry = 1
data = []

#creating the labals and buttons
ask_aadhar_t = "Enter your Aadhar card no: "
ask_phone_t = "Enter your Phone no: "
aadhar_no = tk.Entry(root,width=25)
phone_no = tk.Entry(root,width=25)
ask_aadhar = tk.Label(root,text=ask_aadhar_t,width=30)
ask_phone = tk.Label(root,text=ask_phone_t,width=30)
tokan_text = tk.Label(root,text="your tokan number is: ")
give_tokan = tk.Label(root,text=" ",width=20)
entry_no = tk.Label(root,text=f"Entry number: {entry}")
next_button = tk.Button(root,text="Next",command=next_check)
submit_button = tk.Button(root,text="submit",command=submit_check,state=DISABLED)
check_i = tk.Label(root,text=" ",width=35)
time_slot_text = tk.Label(root,text="your time slot is from ")
time_slot = tk.Label(root,text=" ")

#placing the labals and buttons
entry_no.grid(row=0,column=0)
ask_aadhar.grid(row=1,column=0,columnspan=2)
ask_phone.grid(row=2,column=0,columnspan=2)
aadhar_no.grid(row=1,column=2,columnspan=2)
phone_no.grid(row=2,column=2,columnspan=2)
tokan_text.grid(row=3,column=0,columnspan=2)
give_tokan.grid(row=3,column=2,columnspan=2)
time_slot_text.grid(row=4,column=0,columnspan=2)
time_slot.grid(row=4,column=2,columnspan=2)
next_button.grid(row=5,column=2)
submit_button.grid(row=5,column=3)
check_i.grid(row=5,column=0,columnspan=2)

#ending the loop
tk.mainloop()

for i in data:
    print(i)

import datetime
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days = 1)

import xlsxwriter
workbook = xlsxwriter.Workbook('{}-{}-{}.xlsx'.format(tomorrow.day,tomorrow.month,tomorrow.year))
worksheet = workbook.add_worksheet("Vaccination data")
bottom_line = workbook.add_format({'bold':True,'bottom':6,'right':1})
full_border = workbook.add_format({'border':1})

#To add " " in aadhar card number
def aad(a):
    b = ''
    for i in range(len(a)):
        if i%4 == 0:b+=" "
        b+=a[i]
    return(b)

#To create 4 digit randam number
import random
def rand ():
    inttokan = 0
    tokan = ''
    ran = ''
    for i in range(4):
        ran = str(random.randrange(1,10)) 
        tokan = tokan + ran
        i += 1
    print("your tokan number is", tokan)
    inttokan = int(tokan)
    return(inttokan)

row = 0
col = 0

worksheet.write(row, col, "no.", bottom_line)
worksheet.set_column(col,col,5)
col += 1
worksheet.write(row, col, "Aadhar card no.", bottom_line)
worksheet.set_column(col,col,15)
col += 1
worksheet.write(row, col, "Phone number", bottom_line)
worksheet.set_column(col,col,15)
col += 1
worksheet.write(row, col, "tokan number", bottom_line)
worksheet.set_column(col,col,15)
col += 1
worksheet.write(row, col, "allotted time slot", bottom_line)
worksheet.set_column(col,col,20)
col += 1
worksheet.write(row, col, "Vaccination status", bottom_line)
worksheet.set_column(col,col,20)
row += 1

for i in data:
    col = 0
    worksheet.write(row, col, i[0], full_border)
    worksheet.set_column(col,col,5)
    col += 1
    worksheet.write(row, col, aad(i[1]), full_border)
    worksheet.set_column(col,col,15)
    col += 1
    worksheet.write(row, col, i[2], full_border)
    worksheet.set_column(col,col,15)
    col += 1
    worksheet.write(row, col, i[3], full_border)
    worksheet.set_column(col,col,15)
    col += 1
    worksheet.write(row, col, i[4], full_border)
    worksheet.set_column(col,col,20)
    col += 1
    worksheet.write(row, col, " ",full_border)
    worksheet.set_column(col,col,20)
    row += 1

try:
    workbook.close()
    input("all data is exported in excel")
except:
    import json
    input("something went wrong, can't export data in excel file\nall data is stored into text file, named as 'Vdata'")
    Vdata = open("Vdata.txt", "w")
    json.dump(data,Vdata,indent=2)
    Vdata.close()