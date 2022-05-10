#To get started with basic Psycopg2 usage, write a function called select_all which queries either our Star or Planet table in PostgreSQL and returns all the rows using the following query:

#SELECT * FROM Star;



import psycopg2

def select_all(table):
  conn = psycopg2.connect(dbname = 'db', user = 'grok')
  cur = conn.cursor()

  query = 'SELECT * FROM ' + table + ';'        #query to be executed in PostgreSQL
  cur.execute(query)                            #execute query
  result = cur.fetchall()

  return(result)
