from flask import Flask, render_template, request,session

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
        user=request.form.get('teacher_users')
        if password == 'iam':
            return render_template('teacherpage.html', user=user)
        else:
            return render_template('wrongpage.html')
        

@app.route('/attendance', methods=['POST'])
def attendance():
    user = session.get('user') 
    return render_template('studentpage.html',user=user)


if __name__== "__main__":
    app.run(debug=True)