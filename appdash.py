import tkinter as tk
from tkinter import ttk
import pandas as panda
import os.path
import tkinter.messagebox
import tkinter.simpledialog
import matplotlib as plt

i = 0
y = 0

diretorio = 'C:\\Users\\felip\\Desktop\\Treinamento Python\\'

def ler_df():
    if(os.path.exists('dataframe.csv')==True):
        return panda.read_csv('dataframe.csv', encoding='latin-1')

window = tk.Tk() # Criando a Janela
window['bg']='#008de4' #Definindo cor de fundo App
window.title('Dash DataFrame')# Definindo o título App
window.iconbitmap('C:\\Users\\felip\\Desktop\\Treinamento Python\\icon.ico') # Definindo o Ícone App

colunas = {}

colunas['Coluna_1'] = tk.Entry(window, textvariable='')
colunas['Coluna_2'] = tk.Entry(window, textvariable='')
colunas['Coluna_3'] = tk.Entry(window, textvariable='')
colunas['Coluna_4'] = tk.Entry(window, textvariable='')
colunas['Coluna_5'] = tk.Entry(window, textvariable='')
colunas['Coluna_6'] = tk.Entry(window, textvariable='')
colunas['Coluna_7'] = tk.Entry(window, textvariable='')
colunas['Coluna_8'] = tk.Entry(window, textvariable='')
colunas['Coluna_9'] = tk.Entry(window, textvariable='')
colunas['Coluna_10'] = tk.Entry(window, textvariable='')
colunas['Coluna_11'] = tk.Entry(window, textvariable='')
colunas['Coluna_12'] = tk.Entry(window, textvariable='')
colunas['Coluna_13'] = tk.Entry(window, textvariable='')
colunas['Coluna_14'] = tk.Entry(window, textvariable='')
colunas['Coluna_15'] = tk.Entry(window, textvariable='')

entrys = {}

entrys['Entry_1'] = tk.Entry(window, textvariable='')
entrys['Entry_2'] = tk.Entry(window, textvariable='')
entrys['Entry_3'] = tk.Entry(window, textvariable='')
entrys['Entry_4'] = tk.Entry(window, textvariable='')
entrys['Entry_5'] = tk.Entry(window, textvariable='')
entrys['Entry_6'] = tk.Entry(window, textvariable='')
entrys['Entry_7'] = tk.Entry(window, textvariable='')
entrys['Entry_8'] = tk.Entry(window, textvariable='')
entrys['Entry_9'] = tk.Entry(window, textvariable='')
entrys['Entry_10'] = tk.Entry(window, textvariable='')
entrys['Entry_11'] = tk.Entry(window, textvariable='')
entrys['Entry_12'] = tk.Entry(window, textvariable='')
entrys['Entry_13'] = tk.Entry(window, textvariable='')
entrys['Entry_14'] = tk.Entry(window, textvariable='')
entrys['Entry_15'] = tk.Entry(window, textvariable='')

def messageBox(mensagem):
    return tk.messagebox.showinfo('Aviso',mensagem)

def alertBox(mensagem):
    return tk.messagebox.showwarning('Alerta',mensagem)

def criaColuna(frame):
    global i
    global y
    
    if (i==0):
        btn_criardf = tk.Button(frame, text='Criar Dataframe', command=lambda: criaDataFrame(frame,colunas['Coluna_1'].get(),colunas['Coluna_2'].get(),colunas['Coluna_3'].get(),colunas['Coluna_4'].get(),colunas['Coluna_5'].get(),colunas['Coluna_6'].get(),colunas['Coluna_7'].get(),colunas['Coluna_8'].get(),colunas['Coluna_9'].get(),colunas['Coluna_10'].get(),colunas['Coluna_11'].get(),colunas['Coluna_12'].get(),colunas['Coluna_13'].get(),colunas['Coluna_14'].get(),colunas['Coluna_15'].get()),bg='#ffffff', fg='#008de4', font='Arial 12',padx=12,bd=0)
        btn_criardf.place(relx=0.5,rely=0.93,anchor='center')
    
    if (i<15):
        i+=1
        y+=1
        label = tk.Label(frame, bd=0, text='Coluna '+str(i),bg='#008de4',fg='#ffffff', font='Arial 11 bold',width=16)
        colunas['Coluna_'+str(i)] = tk.Entry(frame, bd=0, name='e'+str(i),bg='#ffffff',fg='#008de4', font='Arial 12 bold', justify='center',width=16)
        val_coluna = colunas['Coluna_'+str(i)].get()
        colunas['Coluna_'+str(i)].insert(0, val_coluna)
        colunas['Coluna_'+str(i)].focus_set()
        if(i==6 or i==11):
            y=1
        
        if(i<=5):
            label.place(relx=0.2,rely=(y+0.2)/7,anchor='center')
            colunas['Coluna_'+str(i)].place(relx=0.2,rely=(y+0.2)/7+0.05,anchor='center')
        elif(i>=6 and i<=10):
            label.place(relx=0.5,rely=(y+0.2)/7,anchor='center')
            colunas['Coluna_'+str(i)].place(relx=0.5,rely=(y+0.2)/7+0.05,anchor='center')
        elif(i>10):
            label.place(relx=0.8,rely=(y+0.2)/7,anchor='center')
            colunas['Coluna_'+str(i)].place(relx=0.8,rely=(y+0.2)/7+0.05,anchor='center')

def janelaCriaDf():
    global i
    global y
    i = 0
    y = 0
    if(os.path.exists('dataframe.csv')==False):
        j_x = 500
        j_y = 450
        
        window_criaDf = tk.Toplevel()
        window_criaDf.title('Criar DataFrame')
        window_criaDf['bg']='#008de4'
        window_criaDf.iconbitmap(diretorio+'icon.ico')
        window_criaDf.resizable(False, False)
        p_x = int(largura_window/2) - int(j_x/2)
        p_y = int(altura_window/2) - int(j_y/2)
        geometry = str(j_x)+'x'+str(j_y)+'+'+str(p_x)+'+'+str(p_y)
        window_criaDf.geometry(geometry)
    
        btn_criacoluna = tk.Button(window_criaDf, text='Criar Coluna', command=lambda: criaColuna(window_criaDf),bg='#ffffff', fg='#008de4', font='Arial 13',padx=12,bd=0)
        btn_criacoluna.place(relx=0.5,rely=0.07,anchor='center')
    else:
        messageBox('Já existe um DataFrame criado!')        

def criaDataFrame(root, *col):
    global i
    global y
    i = 0
    y = 0
    writeString = ''
    for coluna in col:
        if (coluna!=''):
            writeString+='"'+coluna.strip()+'",'
    writeString = writeString[0:len(writeString)-1]
    if (writeString!=''):
        if (os.path.exists('dataframe.csv')==False):
            with open('dataframe.csv', 'x') as pd:
                pd.write(writeString)
                messageBox('Seu dataframe foi salvo com sucesso!')
                root.destroy()
    else:
        alertBox('Insira corretamente os dados!')
        
def janelaAdiconaRegistro():
    if(os.path.exists('dataframe.csv')==True):
        j_x = 500
        j_y = 450
        
        window_addRegistro = tk.Toplevel()
        window_addRegistro.title('Adicionar Registro')
        window_addRegistro['bg']='#008de4'
        window_addRegistro.iconbitmap(diretorio+'icon.ico')
        window_addRegistro.resizable(False, False)
        p_x = int(largura_window/2) - int(j_x/2)
        p_y = int(altura_window/2) - int(j_y/2)
        geometry = str(j_x)+'x'+str(j_y)+'+'+str(p_x)+'+'+str(p_y)
        window_addRegistro.geometry(geometry)
    
        btn_criaregistro = tk.Button(window_addRegistro, text='Registrar', command=lambda: criaRegistro(window_addRegistro,entrys['Entry_1'].get(),entrys['Entry_2'].get(),entrys['Entry_3'].get(),entrys['Entry_4'].get(),entrys['Entry_5'].get(),entrys['Entry_6'].get(),entrys['Entry_7'].get(),entrys['Entry_8'].get(),entrys['Entry_9'].get(),entrys['Entry_10'].get(),entrys['Entry_11'].get(),entrys['Entry_12'].get(),entrys['Entry_13'].get(),entrys['Entry_14'].get(),entrys['Entry_15'].get()),bg='#ffffff', fg='#008de4', font='Arial 13',padx=12,bd=0)
        btn_criaregistro.place(relx=0.5,rely=0.07,anchor='center')
        
        global i
        global y
        i=0
        y=0
        
        df = ler_df()
        for coluna in df.columns:
            if (i<15):
                i+=1
                y+=1
                label = tk.Label(window_addRegistro, bd=0, text=coluna,bg='#008de4',fg='#ffffff', font='Arial 11 bold',width=14)
                entrys['Entry_'+str(i)] = tk.Entry(window_addRegistro, bd=0, name='e'+str(i),bg='#ffffff',fg='#008de4', font='Arial 12 bold', justify='center',width=16)
                val_entry = entrys['Entry_'+str(i)].get()
                entrys['Entry_'+str(i)].insert(0, val_entry)
                
                if(i==6 or i==11):
                    y=1
                
                if(i<=5):
                    label.place(relx=0.2,rely=(y+0.2)/7,anchor='center')
                    entrys['Entry_'+str(i)].place(relx=0.2,rely=(y+0.2)/7+0.05,anchor='center')
                elif(i>=6 and i<=10):
                    label.place(relx=0.5,rely=(y+0.2)/7,anchor='center')
                    entrys['Entry_'+str(i)].place(relx=0.5,rely=(y+0.2)/7+0.05,anchor='center')
                elif(i>10):
                    label.place(relx=0.8,rely=(y+0.2)/7,anchor='center')
                    entrys['Entry_'+str(i)].place(relx=0.8,rely=(y+0.2)/7+0.05,anchor='center')
                
                entrys['Entry_1'].focus_set()
    else:
        alertBox('Não há dataframe criado!')        

def criaRegistro(root, *ent):
    i = 0
    writeString = ''
    df = ler_df()
    for entry in ent:
        if (entry=='' and i<len(df.columns)):
            writeString+='"'+'",'
            i+=1
        elif (entry!='' and i<len(df.columns)):
            writeString+='"'+entry.strip()+'",'
            i+=1
    writeString = '\n'+writeString[0:len(writeString)-1]
    if (writeString!=''):
        if (os.path.exists('dataframe.csv')==True):
            with open('dataframe.csv', 'a') as pd:
                pd.write(writeString)
                messageBox('Registro Adicionado!')
                root.destroy()
    else:
        alertBox('Insira corretamente os dados!')        

def geraGrafico():
    if(os.path.exists('dataframe.csv')==True):
        
        coluna = tk.simpledialog.askstring('Coluna do Gráfico', 'Digite a Coluna de Base')
        df = ler_df()
        
        df[coluna].value_counts().plot.pie(title='Gráfico por '+coluna, autopct="%.1f%%")
        plt.pyplot.savefig('grafico1.png', dpi=138)
        j_x = 540
        j_y = 520
        window_geraGrafico = tk.Toplevel()
        window_geraGrafico.title('Gráfico Gerado')
        window_geraGrafico['bg']='#ffffff'
        window_geraGrafico.iconbitmap(diretorio+'icon.ico')
        window_geraGrafico.resizable(True, True)
        p_x = int(largura_window/2) - int(j_x/2)
        p_y = int(altura_window/2) - int(j_y/2)
        geometry = str(j_x)+'x'+str(j_y)+'+'+str(p_x)+'+'+str(p_y)
        window_geraGrafico.geometry(geometry)
        grafico = tk.PhotoImage(file=diretorio+'grafico1.png')
        label_grafico = tk.Label(window_geraGrafico, image=grafico)
        label_grafico.place(relx=0.5,rely=0.5,anchor='center')
        
    else:
        alertBox('Não há dataframe criado!')        


def mostraDf():
    if(os.path.exists('dataframe.csv')==True):
        j_x = 920
        j_y = 480
        i = 0
        n = 0
        df = ler_df()
        window_mostraDf = tk.Toplevel()
        window_mostraDf.title('TableFrame')
        window_mostraDf['bg']='#ffffff'
        window_mostraDf.iconbitmap(diretorio+'icon.ico')
        window_mostraDf.resizable(True, True)
        p_x = int(largura_window/2) - int(j_x/2)
        p_y = int(altura_window/2) - int(j_y/2)
        geometry = str(j_x)+'x'+str(j_y)+'+'+str(p_x)+'+'+str(p_y)
        window_mostraDf.geometry(geometry)
        list_columns = []
        for col in df.columns:
            n+=1
            list_columns.append(n)
        tree_view = ttk.Treeview(window_mostraDf, show='headings', height='6')
        tree_view['columns']=list_columns
        for coluna in df.columns:
            i+=1
            tree_view.heading(i, text=coluna)
        i=0
        for df.loc[i].tolist in range(0,df.shape[0]):
            tree_view.insert('', 'end',values=df.loc[i].tolist())
            i+=1
        tree_view.pack()
    else:
        alertBox('Não há dataframe criado!')

def sair():
    window.destroy()

#primary color: #008de4
#secondary color: #ffffff

largura_window = window.winfo_screenwidth()
altura_window = window.winfo_screenheight()

janela_x = 700
janela_y = 520

posx = int(largura_window/2) - int(janela_x/2)
posy = int(altura_window/2) - int(janela_y/2)

geometria = str(janela_x)+'x'+str(janela_y)+'+'+str(posx)+'+'+str(posy)

window.geometry(geometria) #Definindo o Tamanho da Janela App
window.resizable(True, True) # Definindo janela não redimensionável

label_title = tk.Label(window,text = window.title(),bg='#008de4',fg='#ffffff', font='Arial 16',bd=0)
img = tk.PhotoImage(file=diretorio+'icon2.png')
label_img = tk.Label(window, image=img, bd=0)
FrameButtons = tk.LabelFrame(bd=0,bg='#ffffff')

#buttons
bt_criaDf = tk.Button(FrameButtons, text='Criar Base de Dados', bg='#ffffff', fg='#008de4', font='Arial 14',padx=150,bd=0, command=janelaCriaDf)
bt_mostraDf = tk.Button(FrameButtons, text='Mostrar Dados', bg='#ffffff', fg='#008de4', font='Arial 14',padx=150,bd=0, command=mostraDf)
bt_addDados = tk.Button(FrameButtons, text='Adicionar Dados', bg='#ffffff', fg='#008de4', font='Arial 14',padx=150,bd=0, command=janelaAdiconaRegistro)
bt_geraGrafico = tk.Button(FrameButtons, text='Gerar Gráfico', bg='#ffffff', fg='#008de4', font='Arial 14',padx=150,bd=0, command=geraGrafico)
bt_sair = tk.Button(FrameButtons, text='Sair', bg='#ffffff', fg='#008de4', font='Arial 14',padx=150,bd=0, command=sair)
#positions buttons
bt_criaDf.grid(row=0,column=0)
bt_mostraDf.grid(row=1,column=0)
bt_addDados.grid(row=2,column=0)
bt_geraGrafico.grid(row=3,column=0)
bt_sair.grid(row=4,column=0)


label_title.place(relx = 0.5,rely = 0.35,anchor = 'center')
label_img.place(relx = 0.5,rely = 0.2,anchor = 'center')
FrameButtons.place(relx = 0.5,rely = 0.7,anchor = 'center')


window.mainloop() # Manter a janela sem fechar