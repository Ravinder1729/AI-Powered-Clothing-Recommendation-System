from vanna.openai import OpenAI_Chat
from vanna.chromadb import ChromaDB_VectorStore
import sqlite3
import vanna
import chromadb
def load_secret_key(file_path):
    with open(file_path, 'r') as file:
        secret_key = file.readline().strip().split('=')[0]  # Splitting on '=' to get the key part
    return secret_key

secret_key = load_secret_key(r'D:\vannai\key\secret_key.txt')

class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)

vn = MyVanna(config={'api_key': secret_key, 'model': 'gpt-3.5-turbo'})
conn = sqlite3.connect(r"D:\vanna\clothing.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

# Iterate over each table and populate the INFORMATION_SCHEMA_COLUMNS table
for table in tables:
    table_name = table[0]
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()

    for col in columns:
        col_id, col_name, col_type, not_null, default_value, primary_key = col
        is_nullable = 'NO' if not_null else 'YES'
        
        # Insert the column information into INFORMATION_SCHEMA_COLUMNS
        cursor.execute('''
        INSERT INTO INFORMATION_SCHEMA_COLUMNS (table_name, column_name, data_type, is_nullable, column_default)
        VALUES (?, ?, ?, ?, ?)
        ''', (table_name, col_name, col_type, is_nullable, default_value))

# Commit and close the connection
conn.commit()

cursor = conn.cursor()
#print('cursor',cursor)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print table names
#print("Tables in the database:")
#for table in tables:
    #print(table[0])
# Connect to the SQLite database (replace 'clothing_store.sqlite' with your actual database file)
conn = sqlite3.connect(r"D:\vanna\clothing.sqlite")
cursor = conn.cursor()

# Define the SQL query to convert the specified columns to lowercase
query = """
UPDATE clothing
SET
    color = LOWER(color),
    size = LOWER(size),
    category = LOWER(category),
    material = LOWER(material),
    gender = LOWER(gender),
    occasion = LOWER(occasion),
    brand = LOWER(brand);
"""

# Execute the query
cursor.execute(query)

# Commit the changes to the database
conn.commit()

# Close the connection
#conn.close()

vn.connect_to_sqlite(r"D:\vanna\clothing.sqlite")

df_ddl = vn.run_sql("SELECT type, sql FROM sqlite_master WHERE sql is not null")

for ddl in df_ddl['sql'].to_list():
  vn.train(ddl=ddl)
training_data = vn.get_training_data()
while True:
    prompt = input("Enter Query (or type 'exit' to quit): ")
    if prompt.lower() == "exit":
        print("Exiting...")
        break
    else:
        response = vn.ask(question=prompt)
        #print("Response:", response)
        #cursor = conn.cursor()

        # Define the SQL query
        query = response[0]

        # Execute the query
        cursor.execute(query)

        # Fetch all results
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

        # Close the connection
        #conn.close()
