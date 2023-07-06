from tkinter import *

def bouton(num):
    global equation_text
    equation_text= equation_text + str(num)
    equation_label.set(equation_text)

def egal():
    global equation_text

    try:
        total= str(eval(equation_text))
        equation_label.set(total)
        equation_text= total
    except ZeroDivisionError:
        equation_label.set("erreur arithmétique")
        equation_text= ""
    except SyntaxError:
        equation_label.set("erreur de syntax")
        equation_text= ""


def effacer():
    global equation_text
    equation_label.set("")
    equation_text= ""

def touche_press(event):
    touche= event.keysym
    print(event)

    match touche:
        case '1':
            bouton('1')
        case '2':
            bouton('2')
        case '3':
            bouton('3')
        case '4':
            bouton('4')
        case '5':
            bouton('5')
        case '6':
            bouton('6')
        case '7':
            bouton('7')
        case '8':
            bouton('8')
        case '9':
            bouton('9')
        case '0':
            bouton('0')
        case 'plus':
            bouton('+')
        case 'minus':
            bouton('-')
        case 'asterisk':
            bouton('*')
        case 'slash':
            bouton('/')
        case 'comma':
            bouton(',')
        case 'Return':
            egal()
        case 'BackSpace' :
            effacer()
            
        
windows= Tk()
windows.title("calculatrice")
windows.geometry("500x650")
windows.configure(bg='black') #background
windows.bind('1', touche_press)
windows.bind('2', touche_press)
windows.bind('3', touche_press)
windows.bind('4', touche_press)
windows.bind('5', touche_press)
windows.bind('6', touche_press)
windows.bind('7', touche_press)
windows.bind('8', touche_press)
windows.bind('9', touche_press)
windows.bind('0', touche_press)
windows.bind('+', touche_press)
windows.bind('-', touche_press)
windows.bind('*', touche_press)
windows.bind('<Return>', touche_press)
windows.bind('/', touche_press)
windows.bind(',', touche_press)
windows.bind('<BackSpace>', touche_press)

equation_text = ""

equation_label = StringVar()

var_label = StringVar()
label = Label(windows, textvariable= equation_label, font=('consolas',20), background="black", width=31, height=2, borderwidth=3, relief="ridge", fg='orange')
label.pack()

frame= Frame(windows)
frame.pack()

bouton1 = Button(frame, text=1, height=4, width=9,font=35, command= lambda: bouton(1), fg='orange', bg='black')
bouton1.grid(row=0, column=0)


bouton2 = Button(frame, text=2, height=4, width=9,font=35, command= lambda: bouton(2), fg='orange', bg='black')
bouton2.grid(row=0, column=1)

bouton3 = Button(frame, text=3, height=4, width=9,font=35, command= lambda: bouton(3), fg='orange', bg='black')
bouton3.grid(row=0, column=2)

bouton4 = Button(frame, text=4, height=4, width=9,font=35, command= lambda: bouton(4), fg='orange', bg='black')
bouton4.grid(row=1, column=0)

bouton5 = Button(frame, text=5, height=4, width=9,font=35, command= lambda: bouton(5),fg='orange', bg='black')
bouton5.grid(row=1, column=1)

bouton6=Button(frame, text=6,height=4,width=9,font=35, command= lambda: bouton(6), fg='orange', bg='black' )
bouton6.grid(row=1, column=2)

bouton7=Button(frame, text=7,height=4,width=9,font=35, command= lambda: bouton(7), fg='orange', bg='black' )
bouton7.grid(row=2, column=0)

bouton8=Button(frame, text=8,height=4,width=9,font=35, command= lambda: bouton(8), fg='orange', bg='black' )
bouton8.grid(row=2, column=1)

bouton9=Button(frame, text=9,height=4,width=9,font=35, command= lambda: bouton(9), fg='orange', bg='black' )
bouton9.grid(row=2, column=2)

bouton0=Button(frame, text=0,height=4,width=9,font=35, command= lambda: bouton(0), fg='orange', bg='black' )
bouton0.grid(row=3, column=1)

plus=Button(frame, text='+',height=4,width=9,font=35, command= lambda: bouton('+'), fg='orange', bg='black')
plus.grid(row=0, column=3)

soustraction=Button(frame, text='-',height=4,width=9,font=35, command= lambda: bouton('-'), fg='orange', bg='black' )
soustraction.grid(row=1, column=3)

multiplication=Button(frame, text='x',height=4,width=9,font=35, command= lambda: bouton('*'),fg='orange', bg='black' )
multiplication.grid(row=2, column=3)

division=Button(frame, text='/',height=4,width=9,font=35, command= lambda: bouton('/'), fg='orange', bg='black' )
division.grid(row=3, column=3)

égal=Button(frame, text='=',height=4,width=9,font=35, command=egal, fg='orange', bg='black' )
égal.grid(row=3, column=2)

virgule=Button(frame, text='.',height=4,width=9,font=35, command= lambda: bouton('.'), fg='orange', bg='black' )
virgule.grid(row=3, column=0)

clear=Button(windows, text='effacer',height=4,width=12,font=35, command=effacer, fg='orange', bg='black')
clear.pack()

windows.mainloop()