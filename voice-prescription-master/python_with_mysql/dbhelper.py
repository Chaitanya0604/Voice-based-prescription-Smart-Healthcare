import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='root',
                                     database='pythontest')
        query = 'create table if not exists user(userId int primary key,userName varchar(200), phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    #Insert
    def insert_user(self, userid, username, phone):
        query = "insert into user(userId,userName,phone) values({},'{}','{}')".format(
            userid, username, phone)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    #Fech All
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ", row[0])
            print("User Name :", row[1])
            print("User Phone : ", row[2])
            print()
            print()

    #delete user
    def delete_user(self, userId):
        query = "delete from user where userId= {}".format(userId)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    #update

    def update_user(self, userId, newName, newPhone):
        query = "update user set userName='{}',phone='{}' where userId={}".format(
            newName, newPhone, userId)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
