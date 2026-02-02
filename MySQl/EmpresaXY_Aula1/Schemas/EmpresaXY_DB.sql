CREATE DATABASE EmpresaXY;


CREATE TABLE Usuarios (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Senha VARCHAR(255) NOT NULL,
    Tipo ENUM('User', 'Admin') DEFAULT 'User'
);

SELECT * FROM Usuarios;
SELECT * FROM usuarios
WHERE Email = 'Admin@Email.com' AND Senha = '$2b$12$wsEf5EJDHogmNlxbVqilH.Ssuj8WiWoQkTTAPTjLU.RAMQFBSK62G'

