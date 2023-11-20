from calendar import c
from bottle import get,run,static_file,post,request
import sqlite3 as sq

@get('/')
def index():
    return static_file('index.html', root='public')

@get("/api/todos")
def get_all_todos():
    #connect to database
    conn = sq.connect('data.db')
    #select from database
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    todos = c.fetchall()
    conn.close()

    data = {"todos": []}

    for todo in todos:
        data["todos"].append({"id": todo[0], "content": todo[1],"done": todo[2]})
    return data

    # return {"todos": [{"id": 1, "content": "Todo 1","done": 0}, {"id": 2, "content": "Todo 2","done":1}]}

@post("/api/todos")
def create_todo():
    print(request.json)
    content = request.json.get("content")
    #connect to database
    conn = sq.connect('data.db')
    #insert into database
    c = conn.cursor()
    c.execute("INSERT INTO todos (content,done) VALUES (?,?)",(content,0))
    conn.commit()   
    conn.close()

    return {}

run(host='localhost', port=8080, debug=True,reloader=True)