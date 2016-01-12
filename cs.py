#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import*
from subprocess import call

def evaluer(event):
	matr=matricule.get()
	s="\\documentclass[french,12pt]{article}\\usepackage[T1]{fontenc}\\usepackage[utf8]{inputenc}\\usepackage{lmodern}\\usepackage[a4paper]{geometry}\\usepackage[arabic,francais]{babel}\\usepackage{graphicx}\\geometry{vmargin=1cm,hmargin=1cm}\\begin{document}\\pagestyle{empty}\\begin{center}\\begin{otherlanguage}{arabic}الجمهورية الجزائرية الديمقراطية الشعبية\\\\\\end{otherlanguage}République Algérienne Démocratique et Populaire\\\\\\begin{otherlanguage}{arabic}وزارة التعليم العالي والبحث العلمي\\\\\\end{otherlanguage}Ministère de l'Enseignement Supérieur et de la Recherche Scientifique\\\\\includegraphics[width=4.8cm]{Logo_Univ_Bejaia}\\\\\\textbf{CERTIFICAT DE SCOLARITÉ}\\\\\\vline\\end{center}Le Doyen de la Faculté des \\textbf{Sciences Éxactes}\\\\certifie que l'étudiant(e):\\\\Nom: \\textbf{"+nom.get()+"}\\\\Prénom : \\textbf{"+prenom.get()+"}\\\\Né(e) le : \\textbf{"+date_nais.get()+"}   à : \\textbf{"+ville_nais.get()+"}\\\\est inscrit(e)  en \\textbf{Deuxième année.}\\\\Matricule : \\textbf{"+matr+"}\\\\Domaine : \\textbf{Mathématiques et Informatique}\\\\Filière : \\textbf{Informatique}\\\\Spécialité : \\textbf{Génie Logiciel}\\\\Diplôme préparé : \\textbf{Master}\\\\\\textbf{Année universitaire : 2015/2016}\\\\\\begin{flushright}Béjaia, le 25/11/2015\\\\P/Le Doyen\\end{flushright}\\textbf{\\underline{NB:}} Ce document n'est délivre qu'en un seul exemplaire, il appartient à l'étudiant (e) d'en faire des copies certifiées conformes.\\end{document}"
	certificat = open(r''+matr+'.tex' , 'w')
	certificat.write(s)
	certificat.close()
	call(["pdflatex", matr+".tex"])
	call(["evince", matr+".pdf"])

fenetre=Tk()
fenetre.pack_propagate(0)
nom=Entry(fenetre, background='white')
prenom=Entry(fenetre, background='white')
date_nais=Entry(fenetre, background='white')
ville_nais=Entry(fenetre, background='white')
matricule=Entry(fenetre, background='white')
matricule.bind("<Return>",evaluer)

certificat = Label(text = 'Certificats de Scolarité')
certificat.grid(row=0)

labelNom = Label(text = 'Nom :')
labelPrenom = Label(text = 'Prenom :')
labelDate_nais = Label(text = 'Date de naissance :')
labelVille_nais = Label(text = 'ville de naissance :')
labelMatricule = Label(text = 'Matricule :')

labelNom.grid(row=1)
labelPrenom.grid(row=2)
labelDate_nais.grid(row=3)
labelVille_nais.grid(row=4)
labelMatricule.grid(row=5)

nom.grid(row=1,column=1)
prenom.grid(row=2,column=1)
date_nais.grid(row=3,column=1)
ville_nais.grid(row=4,column=1)
matricule.grid(row=5,column=1)

generer=Button(fenetre, text="Générer", fg="black")
generer.bind("<Button-1>",evaluer)
quitter=Button(fenetre, text="Quitter", fg="red",command=fenetre.destroy)
generer.grid(row=6,column=0)
quitter.grid(row=6,column=1)

fenetre.mainloop()






