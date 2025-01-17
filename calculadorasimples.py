from tkinter import*
from tkinter import ttk

#Cores
cor1 = '#2b2b2a' #Preta
cor2 = '#feffff' #Branca
cor3 = '#38576b' #Azul
cor4 = '#eceff1' #Cinza
cor5 = '#ffab40' #Laranja


janela =Tk()
janela.title('Calculadora Simples')
janela.geometry('235x318')
janela.config(bg=cor1)

#Frames de display e botões
frame_screen = Frame(janela, width=235, height=50, bg=cor3)
frame_screen.grid(row=0, column=0)    

frame_body = Frame(janela, width=235, height=268)
frame_body.grid(row=1, column=0)


#criando botões


b_1 = Button(frame_body, text='C', width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #bg=blackground=cor de fundo, fg==foreground=cor da letra, font=fonte, relief=tipo de borda, overrelief=efeito de borda
b_1.place(x=0, y=0)

b_2 = Button(frame_body, text='%', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #height, width = tamanho do botão
b_2.place(x=118, y=0)

b_3 = Button(frame_body, text='/', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=176, y=0)

b_4 = Button(frame_body, text='7', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=50)

b_5 = Button(frame_body, text='8', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=50)

b_6 = Button(frame_body, text='9', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=50)

b_7 = Button(frame_body, text='*', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=176, y=50)

b_8 = Button(frame_body, text='4', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=100)

b_9 = Button(frame_body, text='5', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=100)

b_10 = Button(frame_body, text='6', width=5, height=2, bg=cor4,font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=100)

b_11 = Button(frame_body, text='-', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=176, y=100)

b_10 = Button(frame_body, text='1', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=0, y=150)

b_11 = Button(frame_body, text='2', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=59, y=150)

b_12 = Button(frame_body, text='3', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=118, y=150)

b_13 = Button(frame_body, text='+', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=176, y=150)

b_14 = Button(frame_body, text='0', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=0, y=200)

b_15 = Button(frame_body, text='.', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=59, y=200)

b_16 = Button(frame_body, text='=', width=16, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=118, y=200)




b_11 = Button(frame_body, text='2', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=59, y=150)

b_12 = Button(frame_body, text='3', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=118, y=150)

b_13 = Button(frame_body, text='+', width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=176, y=150)

b_14 = Button(frame_body, text='0', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=0, y=200)

b_15 = Button(frame_body, text='.', width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=59, y=200)

b_16 = Button(frame_body, text='=', width=16, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=118, y=200)







janela.mainloop()

