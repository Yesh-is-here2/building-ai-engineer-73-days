import time
import psycopg2
time.sleep(2)
conn = psycopg2.connect(host='db', port=5432, dbname='phase1db', user='yesh', password='yeshpass')
with conn:
    with conn.cursor() as cur:
        cur.execute('SELECT NOW();')
        print('DB time:', cur.fetchone()[0])
conn.close()
