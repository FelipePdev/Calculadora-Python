from tkinter import *
from tkinter import ttk

cor1 = '#34e5eb' #azulbb
cor2 = '#0c0d0c' #preto
cor3 = '#f77a36' #laranja
cor4 = '#ffffff' #banco

#criando container da calculadora
janela = Tk()
janela.title('Calculadora')

#tamanho da calculadora
janela.geometry('240x310')
janela.config(bg=cor2)

frame_tela = Frame(janela, width=240, height=50, )
frame_tela.grid(row=0, column=0)
frame_tela.config(bg=cor2)


frame_corpo = Frame(janela, width= 240, height=270)
frame_corpo.grid(row=1, column=0)

digitos = ''
valor_texto = StringVar()

#função
def entrada(digito):
    
    global digitos
    digitos = digitos + str(digito)
    
    
    #passando valor par a tela
    valor_texto.set(digitos)
    
def calcular():
    resultado = eval(digitos)  
    valor_texto.set(str(resultado))
    
    
#clean
def clean():
    global digitos
    digitos = ''   
    valor_texto.set('') 
    

#criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=15, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Times 20'), bg=cor2, fg=cor4)
app_label.place(x=0, y=0)



#criando botoes

b_1 = Button(frame_corpo, command= clean, text='C',  width=11,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE,)
b_1.place(x= 0 , y=0)
b_2 = Button(frame_corpo, command = lambda:entrada('%'), text='%',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_2.place(x=120, y=0)
b_3 = Button(frame_corpo, command = lambda:entrada('/'), text='/',  width=5,  height=2, bg=cor3, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)

b_5 = Button(frame_corpo, command = lambda:entrada('7'), text='7',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=52)
b_6 = Button(frame_corpo, command = lambda:entrada('8'), text='8',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_6.place(x=60, y=52)
b_7 = Button(frame_corpo, command = lambda:entrada('9'), text='9',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_7.place(x=120, y=52)
b_8 = Button(frame_corpo, command = lambda:entrada('*'), text='*',  width=5,  height=2,bg=cor3, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_8.place(x=180, y=52)

b_9 = Button(frame_corpo, command = lambda:entrada('4'), text='4',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=104)
b_10 = Button(frame_corpo, command = lambda:entrada('5'), text='5',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_10.place(x=60, y=104)
b_11 = Button(frame_corpo, command = lambda:entrada('6'), text='6',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_11.place(x=120, y=104)
b_12 = Button(frame_corpo, command = lambda:entrada('-'), text='-',  width=5,  height=2,bg=cor3, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_12.place(x=180, y=104)

b_13 = Button(frame_corpo, command = lambda:entrada('1'), text='1',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=156)
b_14 = Button(frame_corpo, command = lambda:entrada('2'), text='2',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_14.place(x=60, y=156)
b_15 = Button(frame_corpo, command = lambda:entrada('3'), text='3',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_15.place(x=120, y=156)
b_16 = Button(frame_corpo, command = lambda:entrada('+'), text='+',  width=5,  height=2,bg=cor3, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_16.place(x=180, y=156)

b_17 = Button(frame_corpo, command = lambda:entrada('0'), text='0',  width=11,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_17.place(x= 0 , y=208)
b_18 = Button(frame_corpo, command = lambda:entrada('.'), text='.',  width=5,  height=2, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_18.place(x=120, y=208)
b_19 = Button(frame_corpo, command = calcular, text='=',  width=5,  height=2,bg=cor3, font=('Times 13 bold'), fg=cor2, relief=RAISED, overrelief=RIDGE)
b_19.place(x=180, y=208)




janela.mainloop()