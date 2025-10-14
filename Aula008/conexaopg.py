#pip install psycopg2 *deve ser usado no terminal
import psycopg2

conexao = psycopg2.connect(host="127.0.0.1", database="senai", user="postgres", password="senai", port=5432)
cursor = conexao.cursor()
cons = "INSERT INTO clientes(cliente, estado, sexo, status) VALUES('Silvio Santos', 'RJ', 'M', 'Diamond')"
cursor.execute(cons)
conexao.commit()
consulta = "SELECT * FROM clientes"
cursor.execute(consulta)
registros = cursor.fetchall()
for row in registros:
    print("Nome = ", row[1])
    print("Estado = ", row[2])
    print("Status  = ", row[4], "\n")
cursor.close()
conexao.close()
