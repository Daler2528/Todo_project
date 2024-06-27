import psycopg2

import os

from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self):
        self.db = psycopg2.connect(
            host="localhost",
            dbname="todo_db",
            password=os.getenv("POSTGRESS_PASSWORD"),
            user=os.getenv("POSTGRESS_USER"),
        )
        self.db.autocommit = True

    def create_userr_table(self):
        cursor = self.db.cursor()
        create_userr_sql = """
            create table users1(
                id serial primary key,
                username varchar(128) unique not null, 
                password varchar(128) not null,
                email varchar(56),
                phone varchar(56)
            );             
        """
        cursor.execute(create_userr_sql)
        self.db.commit()


    def create_todo_table(self):
        cursor = self.db.cursor()
        create_todo_sql = """
            create table todo(
                id serial primary key,
                title varchar(128) unique not null,
                status varchar(128) not null,
                owner_id int references users1(id),
                deadline timestamp default now() + interval '1 day'
                
            );
        
        """
        cursor.execute(create_todo_sql)
        self.db.commit()



    def insert_user(self,username , password, email,phone):
        insert_user_sql = """
        insert into users1(username,password,email,phone) values (%s,%s,%s,%s);
        """

        cursor = self.db.cursor()
        cursor.execute(insert_user_sql , (username , password, email,phone))

    def insert_todo(self, title , status , owner_id):
        insert_todo_sql = """
        insert into todo(title , status , owner_id) values (%s , %s , %s)
        """
        cursor = self.db.cursor()
        cursor.execute(insert_todo_sql,(title , status , owner_id))
        self.db.commit()

    def check_username_unique(self,username):
        search_username_unique_sql = """
            select * from users1 where username=%s;
                """
        cursor = self.db.cursor()
        cursor.execute(search_username_unique_sql, (username,))
        result = cursor.fetchall()
        self.db.commit()
        if result:
            return False
        else:
            return True


    def get_user_by_username(self,username):
        search_username_sql = """
                    select * from users1 where username=%s;
                        """
        cursor = self.db.cursor()
        cursor.execute(search_username_sql, (username,))
        result = cursor.fetchone()
        return result

    def update_todo(self,todo_id , value):
        update__todo_sql = """
            update todo set status=%s where id = %s
    
        """
        cursor = self.db.cursor()
        data = cursor.execute(update__todo_sql ,(value,todo_id))
        self.db.commit()
        return data


    def my_doto(self,user_id):
        my_todo_sql = "select * from todo where owner_id = %s"
        cursor = self.db.cursor()
        cursor.execute(my_todo_sql ,(user_id,))
        data = cursor.fetchall()
        return data
        self.db.commit()


    def delete_todo(self,todo_id):
        delete_todo_sql = """
            delete from todo where id =%s 
        
        """
        cursor = self.db.cursor()
        cursor.execute(delete_todo_sql ,(todo_id, ))
        data = cursor.fetchall()
        self.db.commit()


if __name__ == '__main__':
    db = Database()
    #db.create_userr_table()
    #db.create_todo_table()
    #db.insert_user("Daler" , "Daler2528" , "Daler2528@gmail.com" , "+998999812528")
    #db.insert_todo("Make breakfast" , "To do" , 1)
    #print(db.check_username_unique("Dale"))
    print(db.get_user_by_username("Ali"))