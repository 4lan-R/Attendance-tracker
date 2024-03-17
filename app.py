from flask import Flask, render_template, request,session

import sqlite3

app=Flask(__name__)
app.secret_key = 'alan'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/student_track', methods=['POST'])
def student_track():
    if request.method == 'POST':
        password = request.form.get('student_password') 
        user=request.form.get('student_users')
        session['user'] = user
        if password == 's8cse':
            return render_template('subject.html',user=user)
        else:
            return render_template('wrongpage.html')
    

@app.route('/teacher_track', methods=['POST'])
def teacher_track():
    if request.method == 'POST':
        password = request.form.get('teacher_password') 
        user = request.form.get('teacher_users')
        conn = sqlite3.connect('attendance.db')
        cursor = conn.cursor()
        if user=='Deep_learning':
            cursor.execute("SELECT * FROM Deep_learning")
            records = cursor.fetchall()
        else:
            cursor.execute("SELECT * FROM Data_mining")
            records = cursor.fetchall()
        if password == 'teacher':
            return render_template('teacherpage.html', user=user, records=records)
        else:
            return render_template('wrongpage.html')
        

@app.route('/attendance', methods=['POST'])
def attendance():
    subject=request.form.get('subject')
    user = session.get('user') 

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    if subject=='Deep_learning':
        cursor.execute("SELECT * FROM Deep_learning WHERE student_name = ?", (user,))
    else:
        cursor.execute("SELECT * FROM Data_mining WHERE student_name = ?", (user,))
    records = cursor.fetchall()

    conn.close()

    # Initialize variables to count present days
    total_days = 0
    present_days = 0

    # Calculate attendance percentage for the user
    for record in records:
        # Skip the first column which is the ID
        for attendance in record[2:]:
            total_days += 1
            if attendance:
                present_days += 1

    attendance_percentage = (present_days / total_days) * 100 if total_days > 0 else 0

    return render_template('studentpage.html', user=user, attendance_percentage=attendance_percentage, subject=subject)


if __name__== "__main__":
    app.run(debug=True)