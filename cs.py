#!/usr/bin/python
#-*- coding: utf-8 -*-

from tkinter import*
from subprocess import call

def evaluer(event):
	matr=matricule.get()
	s="\\PassOptionsToPackage{arabic,francais}{babel}\
\\documentclass[a4paper,12pt]{article}\
\\usepackage{tikz}\
\\usepackage{pst-barcode}\
\\usepackage{geometry}\
\\geometry{letterpaper}\
\\usepackage{setspace}\
\\usepackage{fontspec}\
\\usepackage{tabto}\
\\usepackage{polyglossia}\
\\setmainlanguage{francais}\
\\setotherlanguage{arabic}\
\\newfontfamily\\arabicfont[Script = Arabic]{DejaVu Sans Mono}\
\\setotherlanguage{arabic}\
\\usepackage{lmodern}\
\\usepackage{graphicx}\
\\geometry{vmargin=0cm,hmargin=2cm}\
\\begin{document}\
\\begin{tikzpicture}[remember picture,overlay]\
\\draw[very thick]\
([yshift=-25pt,xshift=25pt]current page.north west)--\
([yshift=-25pt,xshift=-25pt]current page.north east)--\
([yshift=25pt,xshift=-25pt]current page.south east)--\
([yshift=25pt,xshift=25pt]current page.south west)--cycle;\
\end{tikzpicture}\
\\pagestyle{empty}\
\\begin{center}\
\\begin{otherlanguage}{arabic}الجمهورية الجزائرية الديمقراطية الشعبية\\\\\
\\end{otherlanguage}République Algérienne Démocratique et Populaire\\\\\
\\begin{otherlanguage}{arabic}وزارة التعليم العالي والبحث العلمي\\\\\
\\end{otherlanguage}\
Ministère de l'Enseignement Supérieur et de la Recherche Scientifique\\\\\
\\includegraphics[width=4.8cm]{Logo_Univ_Bejaia}\\\\\
\\textbf{CERTIFICAT DE SCOLARITÉ}\\\\\
\\vline\
\\end{center}Le Doyen de la Faculté des \\textbf{Sciences Éxactes}\\\\\
\n\\\\%\n\
certifie que l'étudiant(e):\\\\\
\n\\\\%\n\
Nom: \\textbf{"+nom.get()+"}\\\\\
\n\\\\%\n\
Prénom : \\textbf{"+prenom.get()+"}\\\\\
\n\\\\%\n\
Né(e) le : \\textbf{"+date_nais.get()+"}   à : \\textbf{"+ville_nais.get()+"}\\\\\
\n\\\\%\n\
est inscrit(e)  en \\textbf{Deuxième année.}\\\\\
\n\\\\%\n\
Matricule : \\textbf{"+matr+"}\\\\\
\n\\\\%\n\
Domaine : \\textbf{Mathématiques et Informatique}\\\\\
\n\\\\%\n\
Filière : \\textbf{Informatique}\\\\\
\n\\\\%\n\
Spécialité : \\textbf{Génie Logiciel}\\\\\
\n\\\\%\n\
Diplôme préparé : \\textbf{Master}\\\\\
\n\\\\%\n\
\\textbf{Année universitaire : 2015/2016}\
\n\\\\%\n\
\\begin{flushright}\
\\begin{pspicture}(4,0in)\
\\psbarcode{"+matr+"}{includecheck height=0.4}{code128}\
\\end{pspicture}\\\
\n\\\\%\n\
Béjaia, le 25/11/2015\\\\P/Le Doyen\
\\end{flushright}\
\\vfill \
\\scriptsize\\textbf{\\underline{NB:}} Ce document n'est delivré qu'en un seul exemplaire, \
il appartient à l'étudiant (e) d'en faire des copies certifiées conformes.\
\\vspace{1.5cm}\
\\end{document}"
	certificat = open(r''+matr+'.tex' , 'w')
	certificat.write(s)
	certificat.close()
	call(["xelatex", matr+".tex"])
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
