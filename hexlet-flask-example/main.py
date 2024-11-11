from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
app.secret_key = 'some_secret_key'
base_dir = os.path.abspath(os.path.dirname(__file__))
users_file = os.path.join(base_dir, 'users', 'users_list.json')

# Загрузка пользователей из файла
def load_users():
    print(f'Checking if file {users_file} exists.')
    if os.path.exists(users_file):
        with open(users_file, 'r') as file:
            users = json.load(file)
            print(f'Loaded users: {users}')  # Отладочное сообщение
            return users
    print(f'File {users_file} does not exist or is empty.')
    return []

# Сохранение пользователей в файл
def save_users(users):
    with open(users_file, 'w') as file:
        json.dump(users, file)
    print(f'Saved users: {users}')  # Отладочное сообщение

@app.route('/')
def hello_world():
    return 'Welcome to Flask!'

@app.get('/users/')
def get_users():
    query = request.args.get('query')
    users = load_users()
    if query:
        filtered_users = [user for user in users if query.lower() in user['name'].lower()]
    else:
        filtered_users = users
        query = ''

    print(f'Displaying users: {filtered_users}')  # Отладочное сообщение

    return render_template(
        'users/index.html',
        users=filtered_users,
        search=query,
    )

@app.post('/users/')
def users_post():
    user = request.form.to_dict()
    errors = validate(user)
    if errors:
        return render_template(
          'users/new.html',
          user=user,
          errors=errors,
        )
    users = load_users()
    user_id = len(users) + 1
    user['id'] = user_id
    users.append(user)
    save_users(users)
    return redirect('/users', code=302)

@app.route('/users/new')
def users_new():
    user = {'name': '', 'email': '', 'password': '', 'passwordConfirmation': '', 'city': ''}
    errors = {}
    return render_template('users/new.html', user=user, errors=errors)

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

    return render_template('courses/index.html', courses=filtered_courses, search=query)

@app.route('/courses/<id>')
def courses(id):
    course = {
        "id": id,
        "name": f"course-{id}",
        "description": "Описание курса"
    }
    return render_template('courses/view.html', course=course)

@app.route('/users/<id>')
def show_user(id):
    users = load_users()
    user = next((user for user in users if user['id'] == int(id)), None)
    if user is None:
        return 'User not found', 404
    return render_template('users/show.html', user=user)

def validate(user):
    errors = {}
    if not user.get('name'):
        errors['name'] = 'Это поле обязательно для заполнения'
    if not user.get('email'):
        errors['email'] = 'Это поле обязательно для заполнения'
    return errors