from tkinter import * 
import sqlite3
from tkinter import messagebox
from tkinter import PhotoImage

root=Tk()
root.geometry("800x350")
root.resizable(False,False)
root.title("Virtuālā bibliotēka")
label_programma=Label(text="Virtuālā bibliotēka")
label_programma.pack()
label_programma.config(font=("Bold",20))

#logo
attels=PhotoImage(file="book.png")
attels=attels.subsample(2,2)
label_attels=Label(image=attels)
label_attels.place(x=300,y=100)

#nosaukums
label_nosaukums=Label(text="Grāmatas nosaukums")
label_nosaukums.place(x=10,y=100)
label_nosaukums.config(font=(15))
entry_nosaukums=Entry(width=30)
entry_nosaukums.place(x=10,y=130)
#autors
label_autors=Label(text="Grāmatas autors")
label_autors.place(x=10,y=150)
label_autors.config(font=(15))
entry_autors=Entry(width=30)
entry_autors.place(x=10,y=180)
#gads
label_gads=Label(text="Izdošanas gads")
label_gads.place(x=10,y=200)
label_gads.config(font=(15))
entry_gads=Entry(width=30)
entry_gads.place(x=10,y=230)


#grāmatas reģistrācijas poga un funkcija
def gramatas_registresana():
    nosaukums=entry_nosaukums.get()
    autors=entry_autors.get()
    gads=entry_gads.get()

    conn=sqlite3.connect("biblioteka.db")
    conn.execute("INSERT INTO dati VALUES (?,?,?)",(nosaukums,autors,gads))
    conn.commit()

    #pēc pievienošanas attīram ievades laukus
    entry_nosaukums.delete(0,END)
    entry_autors.delete(0,END)
    entry_gads.delete(0,END)

poga_registret=Button(text="Reģistrēt",command=gramatas_registresana)
poga_registret.place(x=10,y=270)
poga_registret.config(bg="grey",bd=0,width=25,height=3)


#bibliotēkas apskates poga un funkcija

def apskatit_saturu():
    conn=sqlite3.connect("biblioteka.db")
    cursor=conn.cursor()
    cursor.execute(" SELECT * FROM dati ")#izvēlamies visas rindas
    saturs=cursor.fetchall()
    #pārvērš formātā bez iekavām un tt.
    formatted_data = "\n".join("\t".join(str(cell) for cell in row) for row in saturs)
    messagebox.showinfo("Fetched Data", formatted_data)


poga_apskatit=Button(text="Apskatīt saturu",command=apskatit_saturu)
poga_apskatit.place(x=650,y=100)
poga_apskatit.config(bg="grey",bd=0,width=20,height=3)


#grāmatas meklēšanas poga un funkcija

def gramatas_meklesana():
    logs=Toplevel()
    logs.geometry("300x200")
    label_meklejama_gramata=Label(logs,text="Ievadi grāmatas nosaukumu")
    label_meklejama_gramata.pack()
    label_meklejama_gramata.config(font=(15))


    entry_meklejama_gramata=Entry(logs,width=30)
    entry_meklejama_gramata.pack(pady=20)

    #meklēšana db
    def gramatas_izvade():
        gramata=entry_meklejama_gramata.get()
        conn=sqlite3.connect("biblioteka.db")
        cursor=conn.cursor()
        cursor.execute("SELECT nosaukums, autors, gads FROM dati WHERE nosaukums=?", (gramata,))
        rezultats = cursor.fetchall()
        
        if rezultats != []:
            messagebox.showinfo("Atrasts","Tāda grāmata ir bibliotēkā")
        else:
            messagebox.showerror("Nav atrasts","Grāmata nav atrasta bibliotēkā")
        logs.deiconify()
        entry_meklejama_gramata.delete(0,END)
        


    poga_atrast=Button(logs,text="Meklēt grāmatu",command=gramatas_izvade)
    poga_atrast.pack(pady=20)
    poga_atrast.config(bd=0,bg="grey",width=20,height=3)

    logs.mainloop()

poga_meklet=Button(text="Meklēt grāmatu",command=gramatas_meklesana)
poga_meklet.place(x=650,y=185)
poga_meklet.config(bg="grey",bd=0,width=20,height=3)


#dzēst grāmatu poga un funkcija

def gramatas_dzesana():
    logs1=Toplevel()
    logs1.geometry("300x200")
    label_dzesama_gramata=Label(logs1,text="Ievadi grāmatas nosaukumu")
    label_dzesama_gramata.pack()
    label_dzesama_gramata.config(font=(15))


    entry_dzesama_gramata=Entry(logs1,width=30)
    entry_dzesama_gramata.pack(pady=20)

    #meklēšana db
    def gramatas_iznemsana():
        gramata=entry_dzesama_gramata.get()
        conn=sqlite3.connect("biblioteka.db")
        cursor=conn.cursor()
        #dzēšam grāmatu balstoties uz tās nosaukuma (ja vajadz;etu dzēst viena autoa grāmatas balstītos uz autora vārda)
        cursor.execute("DELETE FROM dati WHERE nosaukums=?", (gramata,)) 
        rezultats = cursor.fetchall()
        conn.commit()
        
        if rezultats == []:
            messagebox.showinfo("Paziņojums","Grāmata dzēsta")
            
        else:
            messagebox.showerror("Nav atrasts","Grāmata nav atrasta bibliotēkā")
            
        logs1.deiconify()
        entry_dzesama_gramata.delete(0,END)
        
        


    poga_atrast=Button(logs1,text="Dzēst grāmatu",command=gramatas_iznemsana)
    poga_atrast.pack(pady=20)
    poga_atrast.config(bd=0,bg="grey",width=20,height=3)

    logs1.mainloop()


poga_dzest=Button(text="Izņemt grāmatu",command=gramatas_dzesana)
poga_dzest.place(x=650,y=270)
poga_dzest.config(bg="grey",bd=0,width=20,height=3)

root.mainloop()