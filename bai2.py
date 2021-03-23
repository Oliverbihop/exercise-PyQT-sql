import sqlite3
a= sqlite3.connect("MSSV")

b=a.cursor()
with a:
    b.execute("DROP TABLE IF EXISTS ThongtinSV")
    b.execute("CREATE TABLE ThongtinSV( ID text, Name text, Phone text, Village text)")
    b.execute("INSERT INTO ThongtinSV VALUES (18119214,'Phan Thanh Danh',09354778824,'TPHCM')")
    b.execute("INSERT INTO ThongtinSV VALUES(18119001, 'Phan Thanh Danh1',09354778824,'TPHCM')")
    b.execute("INSERT INTO ThongtinSV VALUES(18119002,'Phan Thanh Danh2',09354778824,'TPHCM')")

    b.execute("DROP TABLE IF EXISTS DiemSo")
    b.execute("CREATE TABLE DiemSo ( ID text, Math int, Physic int, Chemistry int)")
    b.execute("INSERT INTO DiemSo VALUES(18119214, 3,5,5)")
    b.execute("INSERT INTO DiemSo VALUES(18119001, 5,5,5)")
    b.execute("INSERT INTO DiemSo VALUES(18119002,6,4,5)")
with a:
    b.execute("DELETE FROM ThongtinSV WHERE ID=18119214")
    b.execute("DELETE FROM DiemSo WHERE ID = 18119001")
    b.execute("SELECT * FROM ThongtinSV")
    for row in b.fetchall():
        print (row)
    b.execute("SELECT * FROM DiemSo")
    for row in b.fetchall():
        print (row)
with a:
    b.execute("SELECT * FROM DiemSo WHERE ID=18119214")
    for row in b.fetchall():
        print (row)

