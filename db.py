import sqlite3

conn = sqlite3.connect('mydb')
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

def drop_table(table):
    cursor.execute(
        '''
        DROP TABLE {}
        '''.format(table)
    )
    conn.commit()


def create_users_table():
    try:
        cursor.execute(
            '''
                CREATE TABLE users(
                    username varchar,
                    first varchar,
                    last varchar,
                    password varchar,
                    email varchar
                )  
            '''
        )
    
        conn.commit()
    except sqlite3.OperationalError:
        pass


def create_user(values):
    """
        Takes a dictionary of values. 
        {
            "username": "username"
            "first": "name",
            "last": "name",
            "email": "email",
            "password": "password"
        }
    """
    username = values["username"]
    first = values["first"]
    last = values["last"]
    password = values["password"]
    email =  values["email"]

    cursor.execute(
        '''
            INSERT INTO users(username, first, last, password, email)
            VALUES(?,?,?,?,?)
        ''', 
        (username, first, last, password, email)
    )

    conn.commit()


def get_user_by_email(email):
    cursor.execute(
        '''
            SELECT * FROM users WHERE email = ?
        ''',
        (email,)
    )
    user = cursor.fetchone()

    return dict(user)


# drop_table("users")
create_users_table()
create_user({
    "username": "Rlovell",
    "first": "Rich",
    "last": "Lovell",
    "email": "email@email.com",
    "password": "password"
})
user = get_user_by_email("email@email.com")

print(
    "Found user called {first} {last}, with the email of {email}".format(
        first=user['first'], 
        last=user['last'],
        email=user['email']
    )
)

conn.close()