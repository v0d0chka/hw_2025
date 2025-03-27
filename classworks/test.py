import psycopg2

PGHOST = "ep-floral-dust-a2jf904r-pooler.eu-central-1.aws.neon.tech"
PGDATABASE = "neondb"
PGUSER = "neondb_owner"
PGPASSWORD = "npg_3NHo0suMlikq"
PORT = 5432


with psycopg2.connect(
    dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT
) as connection:
    with connection.cursor() as cursor:
        query = """
            CREATE TABLE brand (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) UNIQUE NOT NULL
            )
        """
        query = """
            CREATE TABLE IF NOT EXISTS customer (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL
            );
            CREATE TABLE IF NOT EXISTS car (
                id SERIAL PRIMARY KEY,
                model VARCHAR(50) NOT NULL,
                cost INTEGER,
                brand_id INTEGER REFERENCES brand(id),
                customer_id INTEGER REFERENCES customer(id)
            );
            """
        cursor.execute(query)

# CREATE
with psycopg2.connect(
    dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT
) as connection:
    with connection.cursor() as cursor:
        # query_insert = 'INSERT INTO brand (name) VALUES (%s)'
        # result1 = cursor.execute(query_insert, ("Bentley",))
        # print(result1)
        #
        # query_insert = 'INSERT INTO brand (name) VALUES (%s) RETURNING id'
        # cursor.execute(query_insert, ('Aston_Martin',))
        # print(cursor.fetchone())

        # query_insert = 'INSERT INTO customer (name) VALUES (%s) RETURNING id, name'
        # owners = [
        #     ('Anton',),
        #     ('Leha',),
        #     ('Fedor',),
        # ]
        # cursor.executemany(query_insert, owners)

        query_insert = "INSERT INTO car (model, cost, brand_id, customer_id) VALUES (%s, %s, %s, %s)"
        cars = [
            ("Alpine", 130000, 1, 4),
            ("Brabus Rocket 900", 125000, 2, 6),
            ("Hennesy", 1250000, 2, 4),
        ]
        cursor.executemany(query_insert, cars)
