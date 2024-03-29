# courses_service.py
from app import mysql

def get_all_courses():
    connection = mysql.connection
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM course")
    courses_data = cursor.fetchall()

    cursor.close()

    return courses_data


def add_course(course_code, course_name, college):
    connection = mysql.connection
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO course (courseCode, courseName, college) VALUES (%s, %s, %s)",
            (course_code, course_name, college)
        )
        
        connection.commit()
        cursor.close()
        return True
    
    except Exception as e:
        print(f"Error adding course: {e}")
        return False
    
    finally:
        if connection:
            connection.close()

            
            
def delete_course(courseCode):
    connection = mysql.connection
    cursor = connection.cursor()
    cursor.execute("DELETE FROM course WHERE courseCode = %s" , (courseCode,))
    
    connection.commit()







def update_course(course_code, course_name, college):
    connection = mysql.connection
    cursor = connection.cursor()

    try:
        print('Updating course:', course_code, course_name, college)
        query = "UPDATE course SET courseCode = %s WHERE courseName = %s AND college = %s"
        print('Query:', query)
        cursor.execute(query, (course_code, course_name, college))
        connection.commit()
        return True
    
    except Exception as e:
        print(f"Error updating course: {str(e)}")
        connection.rollback()
        return False
    
    finally:
        cursor.close()

    