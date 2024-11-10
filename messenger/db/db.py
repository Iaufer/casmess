import psycopg2


class Database:
    def __init__(self, dbname, user, password, host="127.0.0.1", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            print("Connection established")
        except Exception as e:
            print(f"Can't establish connection to database: {e}")



    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed")


    def insert_user(self, username, password):
        if self.conn is None:
            print("No connection to the database. Call connect() first.")
            return

        try:
            cursor = self.conn.cursor()
            insert_query = "INSERT INTO users (username, encrypted_password) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, password))
            self.conn.commit()
            print("User inserted successfully")
        except Exception as e:
            print(f"Failed to insert user: {e}")
        finally:
            cursor.close()