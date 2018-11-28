#coding:utf-8

import tkinter
def inscription():
	"""
		ce function permet de creer le formulaire d'inscription
	"""
	inscrip=tkinter.Label(app,text="veilleu  sesire des bones information ")
	nom_label=tkinter.Label(app,text="nom")
	prenom_label=tkinter.Label(app,text="prenom")
	tel_label=tkinter.Label(app,text="telephone")
	nom_bt_label=tkinter.Label(app,text="nom boutique")
	style_lable=tkinter.Label(app,text="Style")

	nom_entry=tkinter.Entry(app)
	prenom_entry=tkinter.Entry(app)
	tel_entry=tkinter.Entry(app)
	nom_bt_entry=tkinter.Entry(app)
	style_h=tkinter.Radiobutton(app,value=1,text="H")
	style_f=tkinter.Radiobutton(app,value=0,text="F")
	#les positionnement 
	inscrip.grid(row=0, column=1, columnspan=2)

	nom_label.grid(row=1, column=0)
	nom_entry.grid(row=1,column=2)
	prenom_label.grid(row=2, column=0)
	prenom_entry.grid(row=2, column=2)
	tel_label.grid(row=3, column=0)
	tel_entry.grid(row=3, column=2)
	nom_bt_label.grid(row=4, column=0)
	nom_bt_entry.grid(row=4, column=2)
	style_lable.grid(row=5,column=0,rowspan=2)
	style_h.grid(row=5,column=2)
	style_f.grid(row=6, column=2)


app=tkinter.Tk()
app.geometry("500x400")
app.title("marsa")

mainmenu=tkinter.Menu(app)
mainmenu.add_command(label="inscription",command=inscription)


app.config(menu=mainmenu)
app.mainloop()