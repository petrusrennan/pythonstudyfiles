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
keylogger="keylogger"
redef="redef"
helpme="helpme"
#FIM DAS TAGS#

#SISTEMA#
senha="pattern"
password="tacos"
while(senha!=password):
        if(senha==redef):
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
                print("Analisando senhas impróprias...")
                if(password=="gay"):
                        print("SENHA IMPRÓPRIA DETECTADA! SENHA PADRÃO REDEFINIDA!")
                        password="tacos"
                else:
                        print("Nenhuma senha imprópria foi detectada!")
        if(senha==helpme):
                print("")

                print("-----------------------------------------")
                print("ENCICLOPÉDIA DE TAGS DA LINGUAGEM HARMONY")
                print("-----------------------------------------")
                print("")
                print("redef: redefine uma senha.")
                print("keylogger: escaneia palavras proibidas nas senhas.")
                print("helpme: Abre a enciclopédia da linguagem HARMONY.")
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

                
                
                
        print("")
        senha=input('Digite a senha: ')
        
        
                
        
        
        
if senha == password:
	print('Acesso Liberado!')
	
#FIM DO SISTEMA#

