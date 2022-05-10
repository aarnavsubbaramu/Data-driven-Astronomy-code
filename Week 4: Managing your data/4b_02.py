#Write a function called column_stats which calculates the mean and median of a selected column in either Star or Planet table. For this, let your function take two string arguments:

    #the name of the table;
    #the name of the column.

#and have it return the mean and median (in this order) of the selected column.



import psycopg2
import numpy as np

def column_stats(table, col):
  conn = psycopg2.connect(dbname = 'db', user = 'grok')
  cur = conn.cursor()

  query = 'SELECT ' + col + ' FROM ' + table + ';' #query to be executed in PostgreSQL
  cur.execute(query)
  result = cur.fetchall()

  data = np.array(result)                          #arranging query results in a NumPy array
  x = np.mean(data)                                #mean
  y = np.median(data)                              #median
  return(x, y)
