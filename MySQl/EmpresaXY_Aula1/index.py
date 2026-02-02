#Todas as libs usadas
import mysql.connector
import bcrypt
import os
from admin import menu_admin

#String de conexão
conexao = mysql.connector.connect(
    host = "localhost",
    user = "Seu user",
    password = "Sua senha",
    database = "Seu DB"
)

#Cursor de conexão
cursor = conexao.cursor()

#Criação do usuario Admin ⬇
nome = "Admin"
senha = "Admin123"
email = "Admin@Email.com"
tipo = "Admin"


#Gerar hash de senha formato 256
hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

#Atribuir valores Ao BD
sql = "INSERT INTO Usuarios (Nome, Senha, Email, Tipo) VALUES (%s, %s, %s, %s ) ON DUPLICATE KEY UPDATE Email = Email;"    
valores = (nome , hash_senha, email, tipo)
cursor.execute(sql, valores)
conexao.commit() 

while True:
    
    print("""
    ____________________________________________________________________

                              Empresa XY
    ____________________________________________________________________
    1. Cadastro
    2. Login
    3. Sair            
    """)
    opcao = input("Digite oque deseja fazer: ")
    os.system("cls")

    match opcao:
        
        #Cadastro sem tratamento de erro
        case "1":
            nome = input("Digte o nome de usuarios: ")
            senha = input("Digite sua senha: ")
            email = input("Digite seu email: ")

            hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
            sql = "INSERT INTO Usuarios (Nome, Senha, Email) VALUES (%s, %s, %s )"    
            valores = (nome , hash_senha, email)
            cursor.execute(sql, valores)
            conexao.commit()
            os.system("cls")
        
        #Login por email e senha hash + checkHashPw
        case "2":
            for i in range(3):
                email = input("Digite o seu email: ").lower()      
            
                sql = "SELECT  * FROM Usuarios WHERE Email = %s "
                valores = email,
                cursor.execute(sql, valores)
                os.system("cls")
           
                resultado = cursor.fetchone()
            
                if resultado is not None:
                    senha = input("Digite sua senha: ")
                
                    hash_senha = resultado[3]
                    
                    if isinstance(hash_senha, str):
                        hash_senha = hash_senha.encode()
                    
                    if bcrypt.checkpw(senha.encode(), hash_senha):
                                  
                        nome = resultado[1]
                        tipo = resultado[4]
                        input(f"Bem vindo! {nome}")
                        
                        if tipo == "Admin":
                            menu_admin(nome)
                        #Volta pro menu principal
                        break
                    else:
                        print("Senha invalida")
                      
            
                          
                else:
                    input("Email invalido!")
                            
        #Sair :)
        case "3":
            break; 







