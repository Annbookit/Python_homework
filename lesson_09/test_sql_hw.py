from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:51093@localhost:5432/DZ1"
db = create_engine(db_connection_string)
connection = db.connect()

def test_add_new():
    transaction = connection.begin()
    sql = text("INSERT INTO users(\"user_id\") VALUES (:new_user_id)")
    connection.execute(sql, {"new_user_id":"121212"})
    users = text("SELECT * FROM users WHERE user_id = :user_id")
    res = connection.execute(users, {"user_id":"121212"})
    rows = res.mappings().all()
    assert rows[0].user_id == 121212
    
    transaction.commit()

def test_update():
    transaction = connection.begin()
    sql = text("UPDATE users SET user_email = :user_email WHERE user_id = :user_id")
    connection.execute(sql, {"user_email": 'ans@mail.ru', "user_id": 121212})
    users = text("SELECT * FROM users WHERE user_id = :user_id")
    res = connection.execute(users, {"user_id":"121212"})
    rows = res.mappings().all()
    assert rows[0].user_email == "ans@mail.ru"

    transaction.commit()


def test_delete():
    transaction = connection.begin()
    sql = text("DELETE FROM users WHERE user_id = :user_id")
    connection.execute(sql, {"user_id": 121212})
    users = text("SELECT * FROM users WHERE user_id = :user_id")
    res = connection.execute(users, {"user_id":"121212"})
    rows = res.mappings().all()
    assert len(rows) == 0   

    transaction.commit()
    connection.close()
