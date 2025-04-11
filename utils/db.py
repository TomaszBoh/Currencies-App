from sqlalchemy import create_engine, text
from datetime import datetime, timedelta


def make_connection_string(config):
    if config["db_type"] == "sqlite":
        conn_str = f"sqlite:///{config['sqlite_database_file']}"

    else:
        conn_str=""
    
    return conn_str

def open_db(config):
    connection_str = make_connection_string(config)
    db_engine = create_engine(connection_str)
    db_conn = db_engine.connect()
    return db_conn

def close_db(db):
    db.close()

def make_db_table(db_conn):
    query = """CREATE TABLE IF NOT EXISTS rates (
                    date DATE NOT NULL,
                    currency_code VARCHAR NOT NULL,
                    exchange_rate FLOAT NOT NULL,
                    PRIMARY KEY (date, currency_code)
                    );"""
    
    db_conn.execute(text(query))
    db_conn.commit()

def save_data_to_db(currency, db_conn):
    insert_query = f"""INSERT INTO rates (date, currency_code, exchange_rate) VALUES (:date, :code, :mid)"""
    try:
        db_conn.execute(text(insert_query),currency)
        db_conn.commit()
    except Exception as e:
        print(f"Blad przy INSERT:\n{e}")


def load_data_from_db(db_conn, currency, start_date, end_date):
    params = {
        "currency": currency.upper(),
        "start_date": start_date,
        "end_date": end_date,
              }
    
    #SQL query
    query = f"""SELECT date, exchange_rate
                FROM rates
                WHERE currency_code = '{currency.upper()}' AND date >= '{start_date}' AND date <= '{end_date}'
                ORDER BY date ASC;"""
    
    try:
        db_results = db_conn.execute(text(query), params)
    except Exception as e:
        print(f"Error durining downloading: \n {e}")
        return []
    
    results = []
    for r in db_results:
        results.append({"date": r[0], "rate": r[1]})

    return results
    
def currency_list(db_conn):
    query_2 = f"""SELECT DISTINCT currency_code FROM rates"""

    try:
        db_results = db_conn.execute(text(query_2))
    except Exception as e:
        print(f"Error durining downloading: \n {e}")
        return []
    
    cur_list = [r[0] for r in db_results]

    return cur_list