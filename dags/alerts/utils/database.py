from airflow.hooks.postgres_hook import PostgresHook
from psycopg2.extras import RealDictCursor


def fetch(conn_id, sql):
    src = PostgresHook(postgres_conn_id=conn_id)
    src_conn = src.get_conn()
    cursor = src_conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(sql)
    return cursor.fetchall()
