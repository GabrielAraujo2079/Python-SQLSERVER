CREATE DATABASE EmpresaAB;
GO

USE EmpresaAB;
GO

CREATE TABLE USUARIOS (
	ID INT PRIMARY KEY IDENTITY(1,1),
	Nome VARCHAR(100),
	Email VARCHAR(20),
);
GO

INSERT INTO USUARIOS (Nome, Email)
VALUES
	('Gabriel Araujo', 'Araujo@gmail.com'),
	('João Pedro Araujo', 'Teta@email.com');
GO

SELECT * FROM USUARIOS

