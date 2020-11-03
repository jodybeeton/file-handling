from tkinter import *

# creating file entry function
def create():

    txt_entry_info = txt_entry.get("1.0" , END)

    print(txt_entry_info)

    file = open("my_weekend_activities_txt", 'w')

    file.write('My weekend activities')

    file.write(txt_entry_info)

    file.close()

# creating the display function
def display():

    reader = open('my_weekend_activities_txt', 'r')

    activities = reader.read()

    txt_entry.insert(END,activities)

    reader.close()

#creating thr append function
def append():

    reader = open('my_weekend_activities_txt', 'w')

    reader.write(txt_entry.get(1.0, END))

#creating the clear function
def clear():

        reader = open('my_weekend_activities_txt','r+')

        reader.truncate(0)

        txt_entry.delete(1.0, END)
# creating the exit function
def exit_():
        window.destroy()

window = Tk()
window.title("Text File")
window.geometry('600x600')
window.configure(bg='red')

weekend_btn = Button(window, text='My weekend activities', font=10, width=20, height=2,)
weekend_btn.pack()
weekend_btn.place(x=50, y=10)

txt_entry = Text(window, width = 50, height = 10)
txt_entry.pack()
txt_entry.place(x = 10 , y = 70)

creat_btn = Button(window, text='Create textfile', command=create)
creat_btn.pack()
creat_btn.place(x= 10, y = 300)

dsp_btn = Button(window, text='Display',command=display)
dsp_btn.pack()
dsp_btn.place(x= 140, y = 300)

appnd_btn = Button(window, text='Append Data',command=append)
appnd_btn.pack()
appnd_btn.place(x = 220 , y = 300)

clear_btn = Button(window, text="Clear", command=clear)
clear_btn.pack()
clear_btn.place(x = 340, y = 300)

exit_btn = Button(window, text = "Exit", command=exit_)
exit_btn.pack()
exit_btn.place(x = 420, y = 300)



window.mainloop()
