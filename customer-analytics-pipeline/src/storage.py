import sqlite3

def save_to_sqlite(df, db_path="data/customer_data.db", table_name="customers"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
