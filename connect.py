import sqlite3

try:
    with sqlite3.connect("sudoku_grids.db") as conn:
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

except sqlite3.OperationalError as e:
    print("Failed to open database:", e)

cursor_obj = conn.cursor() 

cursor_obj.execute("DROP TABLE IF EXISTS SUDOKU_GRIDS")

table_creation_query = """
    CREATE TABLE SUDOKU_GRIDS (
        Id INTEGER PRIMARY KEY,
        Grid TEXT NOT NULL,
        Difficulty TEXT NOT NULL
    );
"""

# Execute the table creation query
cursor_obj.execute(table_creation_query)

# Confirm that the table has been created
print("Table is Ready")

# Close the connection to the database
conn.close()