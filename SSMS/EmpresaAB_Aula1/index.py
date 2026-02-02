import os
import pyodbc

conexao = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=localhost;"
    "DATABASE=EmpresaAB;"
    "UID=Seu User;"
    "PWD=Sua Senha;"
)


cursor = conexao.cursor()

while(True):
    print("----- Empresa AB -----")
    print("""
    1. Cadastrar usuario
    2. Atualizar Usuario
    3. Listar Usuarios
    4. Excluir Usuario
    9. Sair      
    """)
    opcao = input("Digite sua opção: ")
   

    match opcao:

        case "1":
            os.system("cls")
            
            Nome = input("Crie um nome: ")
            Email = input("Crie um Email: ")
            sql = "INSERT INTO USUARIOS (Nome, Email) VALUES (?, ?)"
            print("Sucesso!")
            cursor.execute(sql, Nome, Email)
            conexao.commit()
        
        
        case "2":
            os.system("cls")
                 
            sql = "SELECT * FROM USUARIOS"
            cursor.execute(sql)
            for linha in cursor.fetchall():
                print(linha)
            
            AcheId = int(input("Digite o ID do usuario que deseja atualizar: "))
            print("Oque ira atualizar \n 1. Nome \n 2. Email")
            opcao = input("Digite sua opção: ")
            
            if opcao == "1":
                Nome = input("Digite o novo Nome: ")
                sql = "UPDATE USUARIOS SET NOME = ? WHERE Id = ?"
                cursor.execute(sql, Nome, AcheId)
                   
            if opcao == "2":
                Email = input("Digite o novo Email: ")
                sql = "UPDATE USUARIOS SET Email = ? WHERE Id = ?" 
                cursor.execute(sql, Email, AcheId)
            conexao.commit()
            os.system("cls")

        
        case "3":
            sql = "SELECT * FROM USUARIOS"
            cursor.execute(sql)
            for linha in cursor.fetchall():
                print(linha)
            input("Deseja fechar lista?: ")
            os.system("cls")

            
        case "4":
            sql = "SELECT * FROM USUARIOS"
            cursor.execute(sql)
            for linha in cursor.fetchall():
                print(linha)
            Deleta = int(input("Digite o id do usuario que deseja deletar: "))        

            sql = "DELETE FROM USUARIOS WHERE ID= ?"
            cursor.execute(sql, Deleta)
            conexao.commit()
            os.system("cls")
        
        
        case "9":
            break;
        
        
        case _: 
            input("Digite algo valido...")


    


