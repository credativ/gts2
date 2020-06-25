import psycopg2
import psycopg2.extras
import psycopg2.pool

MINPOOL = 15
MAXPOOL = 30
APPNAME = 'GTS'

pool = psycopg2.pool.ThreadedConnectionPool( MINPOOL, MAXPOOL,' application_name=%s dbname=gts ' % (APPNAME,) )


#conn = pool.getconn()
