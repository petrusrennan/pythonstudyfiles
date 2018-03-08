# -*- coding: utf-8 -*-
#TAGS GLOBAIS#
helpme="helpme"
fire="fire"
adicionar="adicionar"
gerenciar="gerenciar"
lista="lista"
back="back"
#FIM DAS TAGS#
#SISTEMA#

diciofuncio={
    1001: "Fladson dos Santos",
    1002: "Ribas Iniras",
    1003: "Dorgival Dantas",
    1004: "Matheus Camarada"
    }
#CONVERSOR DE DICIONÁRIO PARA LISTAS#

while True:
    print("")
    menu=input("Digite o procedimento:")
    if(menu==lista):
        listafunc=diciofuncio.values()
        tamanho=len(listafunc)
        for c in range(tamanho):
            print(listafunc[c])
    if(menu==gerenciar):
        while True:
            print("")
            IDfuncionario=int(input("Digite o ID do funcionário:"))
            if(IDfuncionario==0):
                break
            fun=diciofuncio[IDfuncionario]
            def busca():
                print(fun)
            busca()
            fire="off"
            while True:
                #CURSOR#
                print("")
                print("DIGITE 'helpme' PARA SABER AS INSTRUÇÕES DISPONÍVEIS")
                proced=input("O que deseja fazer com o funcionário?: ")
                #FUNÇÃO HELPME#
                if(proced==helpme):
                    print("###INSTRUÇÕES PERMITIDAS###")
                    print("")
                    print("helpme: Exibe as instruções que o usuário pode ordenar.")
                    print("fire: Demitir o funcionário.")
                #FIRE#
                if(proced==fire):
                    s="s"
                    n="n"
                    while True:
                        certeza=input("Tem certeza?(s/n):")
                        if(certeza==s):
                            del(diciofuncio[IDfuncionario])
                            print("O funcionário foi demitido.")
                            fire="confirmed"
                            break
                        elif(certeza==n):
                            break
                        else:
                            print("Digite um valor válido!")
                if(fire=="confirmed"):
                    break
            
            

                
            
        
    

    
                
#FIM DO SISTEMA#

