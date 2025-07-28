import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='livewire',
    database='saranya'
)

try:
    with connection.cursor() as cursor:
       
        create_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            phoneno VARCHAR(20),
            platform VARCHAR(50)  -- Added this column to store platform info
        )
        """
        cursor.execute(create_table)

       
        cursor.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]
        if count == 0:
            insert_query = "INSERT INTO users (name, email, phoneno) VALUES (%s, %s, %s)"
            data_to_insert = [
                ('John Doe', 'john@gmail.com', '1234567890'),
                ('Jane Smith', 'smith@gmail.com', '5556781234'),
                ('Alice Johnson', 'alice@gmail.com', '4441112222'),
                ('Bob Brown', 'bob@gmail.com', '3332221111'),
                ('Carol White', 'carol@gmail.com', '7778889999'),
                ('Dan Black', 'black@gmail.com', '1113335555'),
                ('Eve Green', 'eve@gmail.com', '9990001111'),
                ('Frank Moore', 'frank@gmail.com', '2224446666'),
                ('Grace Hill', 'grace@gamil.com', '6667778888'),
                ('Henry King', 'hendry@gmail.com', '8889990000')
            ]
            cursor.executemany(insert_query, data_to_insert)
            connection.commit() 

        
        update_query = "UPDATE users SET platform = %s WHERE id = %s"
        update_data = [
            ('facebook', 1),
            ('instagram', 2),
            ('github', 3),
            ('facebook', 4),
            ('linkedIn', 5),
            ('linkedIn', 6),
            ('facebook', 7),
            ('instagram', 8),
            ('github', 9),
            ('linkedIn', 10)
        ]

        for platform, user_id in update_data:
            cursor.execute(update_query, (platform, user_id))

        connection.commit()

        
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        print("All users:")
        for row in result:
            print(row) 
        # ... after updating users and committing

        cursor.execute("""
        SELECT platform
        FROM users
        GROUP BY platform
        ORDER BY COUNT(*) DESC
        LIMIT 1
        """)
        most_common_platform = cursor.fetchone()
        print("Most common platform:", most_common_platform[0] if most_common_platform else "None")


finally:
    connection.close()
