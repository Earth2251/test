import customtkinter

app = customtkinter.CTk()
app.title('niggaaaaa')
app.geometry('500x500')

label = customtkinter.CTkLabel(app, text="nigaaaaa", fg_color="transparent",text_color="grey21",font=('Aria', 40))
label.pack(pady=(20, 0))
#แสดงคำตอบ---------------------------------------------------------------------------------------
answer_text = customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable=answer_text, font=('Aria', 50))
answer_label.pack(pady=(20, 0))
#รับค่าinput----------------------------------------------------------------------------------------
entry = customtkinter.CTkEntry(app, placeholder_text="enter radius")
entry.pack(pady=(15, 0))
#ปุ่ม-----------------------------------------------------------------------------------------------
import math

def button_event():
    user_input = entry.get()
    radius = float(user_input)
    area = math.pi * radius**2
    answer_text.set(area)
    print("Radius:", user_input)
    print("Area:", area)




buttom = customtkinter.CTkButton(app, text="press it", command=button_event)
buttom.pack(pady=(20, 0))
app.mainloop()