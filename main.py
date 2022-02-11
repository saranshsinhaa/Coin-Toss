from tkinter import *
from random import randint

#---------------------------------------------------------------------------------

root=Tk()
root.title("Heads or Tails")
root.geometry("700x500")
root.config(bg="white")

#---------------------------------------------------------------------------------

home=PhotoImage(file='images/home.png')
head=PhotoImage(file='images/head.png')
tail=PhotoImage(file='images/tail.png')

#---------------------------------------------------------------------------------

image_label=Label(root, image=home)
image_label.pack(padx=10, pady=10)

#---------------------------------------------------------------------------------

choice_list=[head,tail]
toss_choice=randint(0,1)

#---------------------------------------------------------------------------------

def toss():
    toss_choice=randint(0,1)
    image_label.config(image=choice_list[toss_choice],bd=0)

#---------------------------------------------------------------------------------

toss_button=Button(root, font=('showcard gothic',15 ,'bold'),bg='#52B4F9',
                   width=20, height=20,text="Toss!", bd=4, command=toss)

toss_button.pack(padx=10, pady=10)

#---------------------------------------------------------------------------------

root.mainloop()

