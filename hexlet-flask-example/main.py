from flask import Flask, render_template, request

app = Flask(__name__)

# Словарь пользователей
users = [
    {'id': 1, 'name': 'mike'},
    {'id': 2, 'name': 'mishel'},
    {'id': 3, 'name': 'adel'},
    {'id': 4, 'name': 'keks'},
    {'id': 5, 'name': 'kamila'}
]

@app.route('/')
def hello_world():
    return 'Welcome to Flask!'

@app.get('/users/')
def get_users():
    query = request.args.get('query')
    if query:
        filtered_users = [user for user in users if query.lower() in user['name'].lower()]
    else:
        filtered_users = users
        query = ''

    return render_template(
        'users/index.html',
        users=filtered_users,
        search=query,
    )

@app.post('/users/')
def post_user():
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
        'courses/view.html',
        course=course,
    )

@app.route('/users/<id>')
def show_user(id):
    user = next((user for user in users if user['id'] == int(id)), None)
    if user is None:
        return 'User not found', 404
    return render_template(
        'users/show.html',
        user=user,
    )
