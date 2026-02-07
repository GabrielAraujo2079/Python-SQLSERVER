#Todas as libs usadas
import mysql.connector
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()
#String de conexão
conexao = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conexao.cursor()

def menu_admin(nome):
    while True:
        print(f"""
        ____________________________________________________________________
                              MENU ADMIN - {nome}
        ____________________________________________________________________
        1. Listar usuários
        2. Criar usuário
        3. Remover usuário
        4. Atualizar
        9. Sair
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
                users = cursor.fetchall()
                
                if not users:
                    input("Nenhum usuário encontrado.")
                    break

                for user in users:
                    print(user)

                excluir = input("\nDigite o ID do usuário que deseja excluir (0 para cancelar): ")

                if excluir == "0":
                    break

                # Verificar se existe
                sql = "SELECT Id FROM Usuarios WHERE Id = %s"
                cursor.execute(sql, (excluir,))
                resultado = cursor.fetchone()

                if resultado is None:
                    input("Usuário não encontrado.")
                    break

                # Excluir
                sql = "DELETE FROM Usuarios WHERE Id = %s"
                cursor.execute(sql, (excluir,))
                conexao.commit()
                input("Usuário excluído com sucesso!")
                os.system("cls")       
               
            
            case "4":
                sql = "SELECT * FROM Usuarios WHERE ID > 1;"
                cursor.execute(sql)
                for users in cursor.fetchall(): 
                    print(users)

                idSelecionado = input("Digite o ID de quem você quer atualizar: ")
                os.system("cls")
                
                print(f"""
                ____________________________________________________________________
                
                                    !Atualizar Usuarios!
                ____________________________________________________________________
                1. Nome
                2. Email
                3. Senha
                """)
                
                escolha = input(" Oque deseja atualizar?: ")
                
                match escolha:
                    case "1":
                        nomeNovo = input("Escolha o novo nome: ")
                        sql = "UPDATE Usuarios SET Nome = %s WHERE ID = %s"
                        valores = (sql, nomeNovo, idSelecionado )
                        cursor.execute(valores)
                        conexao.commit()
                        print("Sucesso")
                        
                    
                 
                 
                break
            case "9":
                os.system("cls")
                break