import sqlite3

def get_db_connection():
    conn = sqlite3.connect('Users.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        country TEXT NOT NULL
    );
    ''')
    conn.commit()
    conn.close()

def get_users():
    users = []
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        users = [dict(row) for row in rows]
    except Exception as e:
        print(f"Error getting users: {e}")
    finally:
        conn.close()
    return users

def insert_user(user):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)",
                    (user['name'], user['email'], user['phone'], user['address'], user['country']))
        conn.commit()
        return get_user_by_id(cur.lastrowid)
    except Exception as e:
        print(f"Error inserting user: {e}")
        conn.rollback()
    finally:
        conn.close()

def get_user_by_id(user_id):
    user = {}
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        user = dict(cur.fetchone())
    except Exception as e:
        print(f"Error getting user by id: {e}")
    finally:
        conn.close()
    return user

def update_user(user):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?",
                    (user["name"], user["email"], user["phone"], user["address"], user["country"], user["user_id"]))
        conn.commit()
        return get_user_by_id(user["user_id"])
    except Exception as e:
        print(f"Error updating user: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_user(user_id):
    message = {}
    try:
        conn = get_db_connection()
        conn.execute("DELETE from users WHERE user_id = ?", (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except Exception as e:
        print(f"Error deleting user: {e}")
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()
    return message