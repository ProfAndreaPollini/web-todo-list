-- todos(pk: id, content, done)
CREATE TABLE IF NOT EXISTS todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  content TEXT NOT NULL,
  done INTEGER NOT NULL DEFAULT 0
);

-- tags(pk:id, name)
CREATE TABLE IF NOT EXISTS tags (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

-- tags_todos(pk:id,fk:todo_id,tag_id)
CREATE TABLE IF NOT EXISTS tags_todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  todo_id INTEGER NOT NULL,
  tag_id INTEGER NOT NULL,
  FOREIGN KEY (todo_id) REFERENCES todos (id),
  FOREIGN KEY (tag_id) REFERENCES tags (id)
);
