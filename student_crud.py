import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres.xdaepowfmrngtymlkmel"
DB_PASS = "pNC6u8qHsMgtJySg"
DB_HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
DB_PORT = "5432"


def db_connection():
    try:
        conn = psycopg2.connect(dbname = DB_NAME, user = DB_USER, password = DB_PASS, host = DB_HOST, port = DB_PORT)
        return conn
    except Exception as e:
        print("Error connecting to the database")
        return None

#FOR TEACHER TABLE
def create_table():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id SERIAL PRIMARY KEY,
            teacher_name VARCHAR(100) NOT NULL,
            teacher_age INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_teacher(name,age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers (teacher_name, teacher_age) VALUES (%s, %s) RETURNING teacher_id", (name, age))
    conn.commit()
    cursor.close()
    conn.close()

def update_teacher(id, name, age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE teachers SET teacher_name = %s, teacher_age = %s WHERE id = %s", (name, age, id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_teacher(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teachers WHERE teacher_id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()


# FOR COURSE TABLE
def create_table_course():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS course (
           course_id SERIAL PRIMARY KEY,
           course_name VARCHAR(100) NOT NULL,
           teacher_id int,
           FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    
def insert_course(course_name, teacher_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO course (course_name,teacher_id) VALUES (%s, %s) RETURNING course_id", (course_name,teacher_id))
    conn.commit()
    cursor.close()
    conn.close()

def update_course(id, name):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE course SET course_name = %s WHERE course_id = %s", (name, id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_course(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM course WHERE course_id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

#FOR STUDENT TABLE
def create_table_student():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
           student_id SERIAL PRIMARY KEY,
           student_name VARCHAR(100) NOT NULL,
           student_age INT NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_student(student_name, student_age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (student_name,student_age) VALUES (%s, %s) RETURNING student_id", (student_name,student_age))
    conn.commit()
    cursor.close()
    conn.close()

def update_student(id, name, age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET student_name = %s, student_age = %s WHERE student_id = %s", (name, age, id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_student(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = %s", (id,))
    conn.commit()

#FOR ENROLLMENT
def create_table_enrollment():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollment (
           enrollment_id SERIAL PRIMARY KEY,
           student_id int,
           course_id int,
           FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
           FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_enrollment(student_id, course_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO enrollment (student_id,course_id) VALUES (%s, %s) RETURNING enrollment_id", (student_id,course_id))
    conn.commit()
    cursor.close()
    conn.close()

def update_enrollment(id, student_id, course_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE enrollment SET student_id = %s, course_id = %s WHERE enrollment_id = %s", (student_id, course_id, id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_enrollment(id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM enrollment WHERE enrollment_id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    # create_table()
    # insert_teacher("Shailaj", 20) #name and age
    # update_teacher(1, "Sarthak", 35) #id, name and age
    # delete_teacher(2) #id

    # create_table_course()
    # insert_course("Computer", 3) #course_name and teacher_id
    # update_course(2, "Physics") #course_id and course_name
    # delete_course(2) #course_id

    # create_table_student()
    # insert_student("Ram", 10) #name and age
    # update_student(1, "Shyam", 12) #id, name and age
    # delete_student(2) #id


    # create_table_enrollment()
    # insert_enrollment(1, 1) #student_id and course_id
    # update_enrollment(1, 2, 2) #enrollment_id, student_id and course_id
    # delete_enrollment(2) #enrollment_id

    