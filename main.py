from tkinter import *
import psutil
fen=Tk()
fen.title("Paramètre du node")
fen.resizable(width=False,height=False)
fen.geometry("500x250")
fen.iconbitmap('icon.ico')

grille=Canvas(fen,height=250,width=500)
grille.grid(row=0,column=0)



def test():    ###Lancer quand l'utilisateur clique sur les différents objets
	print("touch")

def test_2():
	print("touch2")

def conf_validate():
	print("validate")


def appui_btn():
	choice_nb_cpu= spinbox_nb_cpu.get()
	choice_nb_core= spinbox_nb_core.get()
	confirmation(choice_nb_cpu, choice_nb_core)

def confirmation(nbre_cpu, nbre_core):
	conf = Tk()
	conf.title("Confirmation")
	conf.resizable(width=False,height=False)
	conf.geometry("250x125")
	conf.iconbitmap('icon.ico')


	windowWidth = conf.winfo_reqwidth()
	windowHeight = conf.winfo_reqheight()
	positionRight = int(conf.winfo_screenwidth()/2 - windowWidth/2)
	positionDown = int(conf.winfo_screenheight()/2 - windowHeight/2)
	conf.geometry("+{}+{}".format(positionRight, positionDown))


	grille_conf=Canvas(conf,height=125,width=250)
	grille_conf.grid(row=0,column=0)


	text_conf_cpu=Label(conf,text=f'Vous allez allouer {nbre_cpu} processeurs',font= ("Arial", 9))
	grille_conf.create_window(122,20,window=text_conf_cpu)

	text_conf_core=Label(conf,text=f'et {nbre_core} cores',font= ("Arial", 9))
	grille_conf.create_window(122,40,window=text_conf_core)

	btn_conf = Button(conf, text ="Valider", command = conf_validate, font= ("Arial", 9), bg="#D5D7C9")
	grille_conf.create_window(122,80,window=btn_conf)



	conf.mainloop()




text_nb_cpu = Label(fen,text='Nombre de processeurs :',font= ("Arial", 9))
grille.create_window(80,20,window=text_nb_cpu)

spinbox_nb_cpu = Spinbox(fen, from_=1, to=psutil.cpu_count(),bd=1,command=test,font= ("Serial", 9),bg="#D5D7C9")
grille.create_window(85,43,window=spinbox_nb_cpu)

choice_nb_cpu=spinbox_nb_cpu.get()

text_nb_core = Label(fen,text='Nombre de coeurs par processeurs :',font= ("Arial", 9))
grille.create_window(110,65,window=text_nb_core)

spinbox_nb_core = Spinbox(fen, from_=1, to=10,bd=1,command=test_2,font= ("Serial", 9),bg="#D5D7C9")
grille.create_window(85,88,window=spinbox_nb_core)

choice_nb_core=spinbox_nb_core.get()

btn_validate = Button(fen, text ="Valider", command = appui_btn, font= ("Arial", 9), bg="#D5D7C9")
grille.create_window(30,130,window=btn_validate)






fen.mainloop()
