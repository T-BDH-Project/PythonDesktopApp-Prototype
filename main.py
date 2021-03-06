from tkinter import *
from tkinter import messagebox
import psutil
import speedtest
from math import *
import prosses
from functools import partial


#=====Parametre de la fenetre=====
fen=Tk()
fen.title("Paramètres")
fen.resizable(width=False,height=False)
fen.geometry("250x280")
fen.iconbitmap('icon.ico')

grille=Canvas(fen,height=400,width=250)
grille.grid(row=0,column=0)







#=====Les fonctions=====
def validateLogin(username, password, log):
	user = username.get()
	passw = password.get()
	print(f"username entré : {user}")
	print(f"password entré : {passw}")
	log.withdraw()
	
	fen.deiconify()




def conf_validate(nbre_core, nbre_ram, nbre_stock, bp, final_per, per):
	prosses.main(nbre_core, nbre_ram, nbre_stock, bp, final_per, per)
	exit()

def appui_btn_validate():
	all_yes = False
	choice_nb_core = spinbox_nb_core.get()
	choice_nb_ram = spinbox_nb_ram.get()
	choice_nb_stockage = spinbox_nb_free_space.get()
	fen.withdraw()
	confirmation(choice_nb_core, choice_nb_ram, choice_nb_stockage, all_yes)

def appui_btn_all():
	all_yes = True
	fen.withdraw()
	confirmation(0, 0, 0, all_yes)

def on_closing():
	if messagebox.askokcancel("Quitter", "Voulez vous vraiment quitter ?"):
		exit()


def avertissement():
	warning = messagebox.showwarning("Test de connexion",'Veuillez attendre un instant, nous testons votre connexion.\nCliquez sur "OK" pour continuer ')

def login():
	log = Tk()  
	log.geometry('400x150')  
	log.title('Login')

	#username label and text entry box
	usernameLabel = Label(log, text="User Name").grid(row=0, column=0)
	username = StringVar()
	usernameEntry = Entry(log, textvariable=username).grid(row=0, column=1)  

	#password label and password entry box
	passwordLabel = Label(log,text="Password").grid(row=1, column=0)  
	password = StringVar()
	passwordEntry = Entry(log, textvariable=password, show='*').grid(row=1, column=1)  
	validatelogin = partial(validateLogin, username, password, log)
	
	#login button
	loginButton = Button(log, text="Login", command=validatelogin).grid(row=4, column=0)  
	log.protocol("WM_DELETE_WINDOW", on_closing)


	log.mainloop()

def confirmation(nbre_core, nbre_ram, nbre_stockage, all_yes):
	conf = Tk()
	conf.title("Confirmation")
	conf.resizable(width=False,height=False)
	conf.geometry("500x250")
	conf.iconbitmap('icon.ico')

	grille_conf = Canvas(conf,height=250,width=500)
	grille_conf.grid(row=0,column=0)

	
	
	avertissement()
	servers = []
	threads = None
			
	s = speedtest.Speedtest(timeout=3)
	s.get_servers(servers)
	s.get_best_server()
	s.download(threads=threads)


	results_dict = s.results.dict()
	bp = round(s.results.download/1000000, 1)
	
	stock = round(psutil.disk_usage('/').free/1073741274)
	commi = 30
	if all_yes == True:
		text = f'Voulez-vous vraiment allouer toutes les ressources de votre pc ?\nA savoir: {psutil.cpu_count()} cœurs, {floor(psutil.virtual_memory().available/1073741274)} GB de RAM,\n {stock} GB de stockage et {bp} Mb/s de bande passante'
		a = 250
		b = 60
		#On calcule le prix et le pourcentage que le proprio aura
		one_pr = round((psutil.cpu_count()*0.65)+(floor(psutil.virtual_memory().available/1073741274)*0.50)+(stock*0.030)+(bp*0.01),2)
		per = (commi * one_pr) / 100.0
		final_per = one_pr - per
		cores_number = float(psutil.cpu_count())
		ram_number = floor(psutil.virtual_memory().available/1073741274)
		stockage_number = stock
		bande_passante = bp

	else:
		text = f'Vous allez allouer:\n {nbre_core} cœurs\n{nbre_ram} GB de RAM\n{nbre_stockage} GB de stockage\net {bp} Mb/s de bande passante'
		a = 250
		b = 90
		#On calcule le prix et le pourcentage que le proprio aura
		cores_number = float(nbre_core)
		ram_number = float(nbre_ram)
		stockage_number = float(nbre_stockage)
		bp_number = float(bp)
		bande_passante = bp
		one_pr = round((cores_number*0.65)+(ram_number*0.50)+(stockage_number*0.030)+(bp_number*0.01),2)
		per = (commi * one_pr) / 100.0
		final_per = one_pr-per

	
	text_conf_global = Label(conf, text=text, font=("Arial", 12), fg="red")
	grille_conf.create_window(a,b, window=text_conf_global)

	
	



	text_prix = Label(conf, text=f"Votre gain:\n{round(final_per, 2)} €", font=("Arial", 10), fg="red")
	grille_conf.create_window(400,190, window=text_prix)


	yeys = False
	btn_conf = Button(conf, text ="Valider", command = lambda: conf_validate(cores_number, ram_number, stockage_number, bande_passante, final_per, per), font=("Arial", 12), bg="#D5D7C9")
	grille_conf.create_window(250,190, window=btn_conf)

	
	
	conf.protocol("WM_DELETE_WINDOW", on_closing)
	conf.mainloop()





#=====Les objets=====
#Objets coeurs
text_nb_core = Label(fen, text='Nombre de cœurs :', font= ("Arial", 9))
grille.create_window(61, 20, window=text_nb_core)

spinbox_nb_core = Spinbox(fen, from_=1, to=psutil.cpu_count(), bd=1, font= ("Serial", 9), bg="#D5D7C9")
grille.create_window(85, 43, window=spinbox_nb_core)


#Objets RAM
text_nb_ram = Label(fen, text='Capacité de ram (GB):', font= ("Arial", 9))
grille.create_window(69,65, window=text_nb_ram)

spinbox_nb_ram = Spinbox(fen, from_=1, to=floor(psutil.virtual_memory().available/1073741274), bd=1, font= ("Serial", 9), bg="#D5D7C9")
grille.create_window(85,88,window=spinbox_nb_ram)


#Objets stockage
text_nb_free_space = Label(fen, text='Capacité de stockage (minimum 30 GB):', font= ("Arial", 9))
grille.create_window(120,110, window=text_nb_free_space)

spinbox_nb_free_space = Spinbox(fen, from_=30, to=round(psutil.disk_usage('/').free/1073741274),bd=1, font= ("Serial", 9), bg="#D5D7C9")
grille.create_window(85,133, window=spinbox_nb_free_space)


#Boutton pour allouer l'entièreté des ressources
btn_all = Button(fen, text ="Tout allouer", command = appui_btn_all, font= ("Arial", 9), bg="#D5D7C9")
grille.create_window(45,220,window=btn_all)

#Boutton de validation
btn_validate = Button(fen, text ="Valider", command = appui_btn_validate, font= ("Arial", 9), bg="#D5D7C9")
grille.create_window(30,260,window=btn_validate)
fen.protocol("WM_DELETE_WINDOW", on_closing)




#=====Lancement=====



if __name__ == "__main__":
	fen.withdraw()
	login()
	
	
