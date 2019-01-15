from sqlite3 import connect
from contextlib import contextmanager


@contextmanager
def temptable(cur):
    cur.execute("create table points(x int, y int)")
    try:
        yield
    finally:
        cur.execute("drop table points")


with connect("test.db") as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute("insert into points (x, y) values(1, 1)")
        cur.execute("insert into points (x, y) values(1, 2)")
        cur.execute("insert into points (x, y) values(2, 1)")
        for row in cur.execute("select x, y from points"):
            print(row)
        for row in cur.execute("select sum(x * y) from points"):
            print(row)
