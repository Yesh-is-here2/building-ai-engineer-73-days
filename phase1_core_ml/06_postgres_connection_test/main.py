import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="phase1db",
    user="yesh",
    password="yeshpass",
)

with conn:
    with conn.cursor() as cur:
        # Create table if it doesn't exist
        cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name TEXT,
            score INT
        );
        """)

        # Insert rows only once (avoid duplicates)
        cur.execute("""
        INSERT INTO students (name, score)
        SELECT 'Alice', 88
        WHERE NOT EXISTS (SELECT 1 FROM students WHERE name='Alice');
        """)

        cur.execute("""
        INSERT INTO students (name, score)
        SELECT 'Bob', 92
        WHERE NOT EXISTS (SELECT 1 FROM students WHERE name='Bob');
        """)

        cur.execute("""
        INSERT INTO students (name, score)
        SELECT 'Charlie', 79
        WHERE NOT EXISTS (SELECT 1 FROM students WHERE name='Charlie');
        """)

        # Query results
        cur.execute("""
        SELECT id, name, score
        FROM students
        ORDER BY score DESC;
        """)

        for row in cur.fetchall():
            print(row)

conn.close()
