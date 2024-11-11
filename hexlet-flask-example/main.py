from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Flask!'

@app.get('/users')
def users_get():
    return 'GET /users'

@app.post('/users')
def users():
    return 'Users', 302

@app.route('/courses/')
def courses_list():
    query = request.args.get('query')
    courses = [
        {'id': 1, 'name': 'Python Programming'},
        {'id': 2, 'name': 'Web Development'},
        {'id': 3, 'name': 'Data Science'},
    ]
    
    if query:
        filtered_courses = [course for course in courses if query.lower() in course['name'].lower()]
    else:
        filtered_courses = courses

    return render_template(
        'courses/index.html',
        courses=filtered_courses,
        search=query,
    )

@app.route('/courses/<id>')
def courses(id):
    course = {
        "id": id,
        "name": f"course-{id}",
        "description": "Описание курса"
    }
    return render_template(
        'courses/show.html',
        course=course,
    )

@app.route('/users/<id>')
def show_user(id):
    user = {
        "id": id,
        "name": f"user-{id}"
    }
    return render_template(
        'users/show.html',
        user=user,
    )

# Словарь пользователей
users = [
    {'id': 1, 'name': 'mike'},
    {'id': 2, 'name': 'mishel'},
    {'id': 3, 'name': 'adel'},
    {'id': 4, 'name': 'keks'},
    {'id': 5, 'name': 'kamila'}
]