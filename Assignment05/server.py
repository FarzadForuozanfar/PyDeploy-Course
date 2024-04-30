from fastapi import FastAPI, HTTPException, Form
from datetime import datetime
import sqlite3

app = FastAPI()

conn = sqlite3.connect('todo.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

async def check_db_exist(cursor):
    try:
        # Check if the todos table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='todos'")
        table_exists = cursor.fetchone()

        # If the todos table does not exist, create it
        if not table_exists:
            cursor.execute("""
            CREATE TABLE "todos" (
                "id"    INTEGER,
                "title" TEXT NOT NULL,
                "description"   TEXT NOT NULL,
                "time"  TEXT,
                "status"    INTEGER DEFAULT 0,
                PRIMARY KEY("id" AUTOINCREMENT)
            )
            """)
            conn.commit()
            print("Table 'todos' created successfully")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Create a new todo
@app.post("/todos/")
async def create_todo(title: str = Form(), description: str = Form()):
    check_db_exist(cursor=cursor)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO todos (title, description, time) VALUES (?, ?, ?)", (title, description, current_time))
    conn.commit()
   
    return {"id": cursor.lastrowid, "title": title, "description": description, "time": current_time}

# Get all todos
@app.get("/todos/")
async def get_todos():
    check_db_exist(cursor=cursor)
    cursor.execute("SELECT * FROM todos")
    todos = cursor.fetchall()
    return {"todos": todos}

# Get a specific todo by ID
@app.get("/todos/{id}")
async def get_todo(id: int):
    cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
    todo = cursor.fetchone()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"todo": todo}

# Update a todo by ID
@app.put("/todos/{id}")
async def update_todo(id: int, title: str = Form(None), description: str = Form(None), status: int = Form(None)):
    update_fields = []
    
    if title:
        update_fields.append(f"title='{title}'")
    
    if description:
        update_fields.append(f"description='{description}'")
        
    if status:
        update_fields.append(f"status='{status}'")
        
    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update provided")
    
    query = f"UPDATE todos SET {', '.join(update_fields)} WHERE id={id}"
    
    cursor.execute(query)
    conn.commit()
    
    cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
    todo = cursor.fetchone()
    
    return {"message": "Todo updated successfully", "todo" : todo}

# Delete a todo by ID
@app.delete("/todos/{id}")
async def delete_todo(id: int):
    cursor.execute("SELECT id FROM todos WHERE id=?", (id,))
    todo = cursor.fetchone()
    
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    cursor.execute("DELETE FROM todos WHERE id=?", (id,))
    conn.commit()
    
    return {"message": "Todo deleted successfully"}
