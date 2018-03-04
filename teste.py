#INTERFACE GRÁFICA#
print("------------------------------")
print("CRISTAL DATABASES")
print("Taking Care Of Your Business!")
print("Sistema desenvolvido por Petrus Rennan.")
print("------------------------------")
print("")
print("------------------------------------------------------")
print("Digite 'helpme' para exibir as tags da linguagem HARMONY")
print("------------------------------------------------------")
print("")
#FIM DA INTERFACE GRÁFICA#

#TAGS DA LINGUAGEM DE PROGRAMAÇÃO HARMONY#
keylogger="badscan"
redef="redefinir"
helpme="helpme"
lista="hist_entry"
tent="tent"
#FIM DAS TAGS#

#SISTEMA#
senha="HISTÓRICO DE ENTRADA DE DADOS"
rangex=0
password="tacos"
listagem=[senha]
tentativas=0
senha=input('Digite a senha: ')
while(senha!=password):
        rangex=rangex+1
        listagem+=[senha]
        if(senha==redef):
                #CONSOLE DE TENTATIVAS# 
                tentativas=tentativas-1
                if(tentativas<=0):
                        tentativas+=1
                #FIM DO CONSOLE#
                oldpass=input("Digite a antiga senha:")                
                if(oldpass==password):
                        rasc=input("Digite a nova senha: ")
                        passwordconfirm=input("Confirme a nova senha:")   
                        if(passwordconfirm==rasc):
                                print("Senha alterada com sucesso!")
                                password=rasc
                        else:
                                print("As senhas não conferem!")
                else:
                        print("Essa não é a antiga senha!")
                        
        if(senha==keylogger):
                #CONSOLE DE TENTATIVAS# 
                tentativas=tentativas-1
                if(tentativas<=0):
                        tentativas+=1
                #FIM DO CONSOLE#
                print("Analisando senhas impróprias...")
                if(password=="babaca"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                elif(password=="trouxa"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                elif(password=="escroto"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                elif(password=="PCC"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                elif(password=="CV"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                elif(password=="GDR"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                elif(password=="bandido"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                elif(password=="criminoso"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                else:
                        print("Nenhuma senha imprópria foi detectada!")
        if(senha==helpme):
                #CONSOLE DE TENTATIVAS# 
                tentativas=tentativas-1
                if(tentativas<=0):
                        tentativas+=1
                #FIM DO CONSOLE# 
                print("")

                print("-----------------------------------------")
                print("ENCICLOPÉDIA DE TAGS DA LINGUAGEM HARMONY")
                print("-----------------------------------------")
                print("")
                print("redefinir: redefine uma senha.")
                print("badscan: escaneia palavras proibidas nas senhas.")
                print("helpme: Abre a enciclopédia da linguagem HARMONY.")
                print("tent: mostra o número de tentativas de introdução da senha.")
                print("hist_entry: Exibe o histórico de entrada de dados.")
                print("")
                repeat=input("repetir?(s/n): ")
                while(repeat!="n"):
                        print("")
                        print("redef: redefine uma senha.")
                        print("keylogger: escaneia palavras proibidas nas senhas.")
                        print("helpme: Abre a enciclopédia da linguagem HARMONY.")
                        print("")
                        repeat=input("repetir?(s/n): ")
                byebye=input("ATÉ LOGO! (PRESSIONE QUALQUER TECLA PRA SAIR...)")
        if(senha==tent):

               #CONSOLE DE TENTATIVAS# 
                tentativas=tentativas-1
                if(tentativas<=0):
                        tentativas+=1
               #FIM DO CONSOLE# 
                print("Número de tentativas:",tentativas)
                
        if(senha==lista):
                #CONSOLE DE TENTATIVAS# 
                tentativas=tentativas-1
                if(tentativas<=0):
                        tentativas+=1       
                for trials in range(rangex):
                        print(listagem[trials])

                        
        #DIRETRIZ DE SEGURANÇA#
        if(tentativas>=3):
                error=input("DIRETRIZ DE SEGURANÇA ACIONADA! DESLIGANDO SISTEMAS!")
                break
        #FIM DA DIRETRIZ#

                
                
                

                
                
                
        print("")
        senha=input('Digite a senha: ')
        tentativas=tentativas+1
        
        
                
        
if senha == password:
	print('Acesso Liberado!')
	print('A senha para os 5 milhões de dólares é: HTXTORF589')
	
	
#FIM DO SISTEMA#
