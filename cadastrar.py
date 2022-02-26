import os
import cadastro
from cadastro import *

name_arq = "users.txt"
register_user = 's'
name_corp = " "
space = "-"*len(name_corp)
header = space + "\n"+name_corp + "\n" + space

if not os.path.exists(name_arq):
    arq = open (name_arq, 'w+t', encoding="utf-8")
    arq.write(header)
    arq.close()

def save_arq(funcs):
    arq = open(name_arq, "r", encoding= "utf-8")
    pos_funcs = arq.read().count("Usuario")+1
    arq.close()

    arq = open (name_arq, 'a+t', encoding="utf-8")
    arq.write("\nUsuário "+str(pos_funcs)+"\n")

    for key in funcs:
        arq.write( "- " +key + ": " + funcs[key] + "\n" )

    arq.write(space)
    arq.close()

while register_user == 's':
    funcs = {
        "Nome": "",
        "CPF": "",
        "Moeda Favorita": ""
    }
    funcs["Nome"] = input("Digite o seu  nome: ")
    funcs["CPF"] = input ("Digite seu CPF: ")
    funcs["Moeda Favorita"] = input("Digite a sua moeda favorita: ")

    save_arq(funcs)

    register_user = input("Dejesa realizar outro cadastro? (s/n)").lower()

