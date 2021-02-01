from influxdb import InfluxDBClient as db_cli

INFLUXDB_SCHEMAS = {
    
}

db_conn = db_cli('localhost', '8086', 'finance-io', 'finance-io', 'finance')

def flush_tables(conn=db_conn, schemas=INFLUXDB_SCHEMAS):
    pass

if __name__ == "__main__":
    print(db_conn.get_list_database())