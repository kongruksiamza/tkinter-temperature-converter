from tkinter import *
from tkinter import ttk
root=Tk()
root.title("โปรแกรมแปลงอุณหภูมิ")
root.iconbitmap("icon/tempicon.ico")
root.resizable(0,0)

def reset():
    output_txt.delete(0,END)
    input_txt.delete(0,END)
    temp_combo.set("เคลวิน")

def convert():
    output_txt.delete(0,END)
    #ตัวเลขที่ผู้ใช้ป้อน
    celcius_value = float(input_txt.get())
    #หน่วยที่ผู้ใช้เลือก
    unit_value = temp_combo.get()
    #คำนวณ
    if unit_value=="เคลวิน":
        kelvin=celcius_value+273
        output_txt.insert(0,kelvin)
    else:
        fahrenheit=celcius_value*1.8+32
        output_txt.insert(0,fahrenheit)

#settings
font = ("Arial",15,"bold")
color="orange"

#input widget
input_label=Label(root,text="อุณหภูมิ(เซลเซียส)",font=font)
input_txt=Entry(root,width=20,font=font)
input_label.grid(row=0,column=0,sticky=W)
input_txt.grid(row=0,column=1)

#combobox widget
unit_label=Label(root,text="แปลงเป็นหน่วย",font=font)
unit_list = ["ฟาเรนไฮน์","เคลวิน"]
temp_combo=ttk.Combobox(root,value=unit_list,font=font,width=18)
temp_combo.set("เคลวิน")
unit_label.grid(row=1,column=0,sticky=W)
temp_combo.grid(row=1,column=1)

#output widget
output_label=Label(root,text="ผลลัพธ์",font=font)
output_txt=Entry(root,width=20,font=font)
output_label.grid(row=2,column=0,sticky=W)
output_txt.grid(row=2,column=1)

#button widget
convertBtn=Button(root,text="แปลง",font=font,width=10,bg=color,command=convert)
resetBtn=Button(root,text="ล้าง",font=font,width=7,bg=color,command=reset)
convertBtn.grid(row=3,column=1,sticky=W,padx=5,pady=5)
resetBtn.grid(row=3,column=1,sticky=E,padx=5,pady=5)

root.mainloop()