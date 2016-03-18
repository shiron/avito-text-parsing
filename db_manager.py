#coding=utf-8
import sqlite3


def write_to_db(path_db, file, is_fraud, ac):
    """Write results to db"""
    try:
        conn = sqlite3.connect(path_db)
        c = conn.cursor()
        c.execute("""INSERT INTO result VALUES (?,?,?)""", (file, str(ac), str(is_fraud) ))
        conn.commit()
        conn.close()
    except Exception as inst:
        print inst.args[0]


def create_db(path_db):
    """Create DB if it doesn't exists"""
    try:
        con = sqlite3.connect(path_db)
        cur = con.cursor()
        cur.executescript("""
            create table if not exists result(
                filename text,
                academic_sickness real,
                is_fraud bool
            );
            """)
        con.commit()
        con.close()
    except Exception as inst:
        print inst.args[0]