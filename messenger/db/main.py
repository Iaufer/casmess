from messenger.db.db import Database


def main():
    db = Database(dbname="postgres", user="postgres", password="2505", host="127.0.0.1", port="5432")

    db.connect()

    db.insert_user("zSDD", "test_paqssword")

    db.close()

if __name__ == "__main__":
    main()
