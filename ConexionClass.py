# -*- coding: utf-8 -*-
from ConexionAbstract import ConexionAbstract;
#!/usr/bin/python

import psycopg2
from config import config


class Conexion(ConexionAbstract):
    
#https://www.postgresqltutorial.com/postgresql-python//
    def create(self):
        print("Create")
        conn = None
        sql = '''CREATE TABLE Clientes_VIP(
                first_name CHAR(20) NOT NULL,
                last_name CHAR(20),
                age INT,
                sex CHAR(1),
                capital FLOAT)'''
        try:
            params = config()
            conn = psycopg2.connect(**params)		    
            cur = conn.cursor()
            cur.execute(sql)   
            print("Table created successfully........")
            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                
            print('Database connection closed.')
    
    def read(self):
        print("Read")
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)		    
            cur = conn.cursor()
            cur.execute('SELECT * from clientes')
            row = cur.fetchone()
            while row is not None:
                print(row)
                row = cur.fetchone()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            print('Database connection closed.')
    
    def update(self):
        print("Update")
        sql = """UPDATE Clientes_VIP
                SET capital = %s
                WHERE first_name = %s"""
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)		    
            cur = conn.cursor()
            cur.execute(sql,('20000000','Elsa'))
            update_rows = cur.rowcount
            
            print("Updating..",update_rows)
            
            conn.commit()
     
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            print('Database connection closed.')
    
    def delete(self):
        print("Delete")
        sql = """DELETE FROM Clientes_VIP WHERE first_name = %s"""
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)		    
            cur = conn.cursor()
            cur.execute(sql,('Elsa',))
            rows_deleted = cur.rowcount
            
            print("Deleting..",rows_deleted)
            
            conn.commit()
     
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
            print('Database connection closed.')
    

    def insert(self):
        print("Insert")
        conn = None
        sql = '''INSERT INTO Clientes_VIP(first_name, last_name ,age,sex,capital)
             VALUES('Elsa','Pato',28,'0',10000000)'''
        sql2 ='''INSERT INTO Clientes_VIP(first_name, last_name ,age,sex,capital)
             VALUES(%s,%s,%s,%s,%s)'''
        try:
            params = config()
            conn = psycopg2.connect(**params)		    
            cur = conn.cursor()
            cur.execute(sql2,('Pedro','Picapiedra','30','1','10000000'))   
            #cur.execute(sql)   
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                
            print('Database connection closed.')
    
    

    

conexion = Conexion()
conexion.read()
conexion.create()
conexion.insert()
conexion.update()
conexion.delete()


