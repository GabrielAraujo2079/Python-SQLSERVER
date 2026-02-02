#Todas as libs usadas
import mysql.connector
import bcrypt
import os

#String de conexão
conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2079",
    database = "EmpresaXY"
)

cursor = conexao.cursor()

def menu_admin(nome):
    while True:
        print(f"""
        ==========================
          MENU ADMIN - {nome}
        ==========================
        1. Listar usuários
        2. Criar usuário
        3. Remover usuário
        4. Voltar
        """)

        opcao = input("Escolha: ")

        
        match opcao:
            
            
            case "1":
                sql = "SELECT * FROM Usuarios WHERE ID > 1;"
                cursor.execute(sql)
                for users in cursor.fetchall(): 
                    print(users)
                input("Clique enter fechar a lista:")
                os.system("cls")
            
            
            case "2":
          
                nome = input("Digte o nome de usuarios: ")
                senha = input("Digite sua senha: ")
                email = input("Digite seu email: ")

                hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
                sql = "INSERT INTO Usuarios (Nome, Senha, Email) VALUES (%s, %s, %s )"    
                valores = (nome , hash_senha, email)
                cursor.execute(sql, valores)
                conexao.commit()
                os.system("cls")
            
            
            case "3":
                sql = "SELECT * FROM Usuarios WHERE ID > 1;"
                cursor.execute(sql)
                
                for users in cursor.fetchall(): 
                    print(users)
                
                while resultado is None or user == "0":
                    excluir = input("Digite o ID do usuario que deseja excluir: ")
                
                    sql = "DELETE FROM USUARIOS WHERE ID = %s"
                    valores(sql, excluir)
                    cursor.execute(valores)
                
                    resultado = cursor.fetchone()
                
                    user = input("Usuarios não encontrado aperte enter pra tentar novamente ou digite 0 pra sair")
                
                
                if resultado is not None:
                    senha = input("Usuarios exluido com sucesso! ")             
               
            
            case "4":
                break