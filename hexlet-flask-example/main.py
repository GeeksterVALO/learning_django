from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
app.secret_key = 'some_secret_key'
users_file = 'users_list.json'  # Обновленный путь к файлу в корневом каталоге проекта

# Загрузка пользователей из файла
def load_users():
    try:
        with open(users_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading users: {e}')
        return []

# Сохранение пользователей в файл
def save_users(users):
    try:
        with open(users_file, 'w') as file:
            json.dump(users, file, indent=4)
        print(f'Saved users: {users}')
    except Exception as e:
        print(f'Error saving users: {e}')

@app.route('/', endpoint='hello_world')
def hello_world():
    return 'Welcome to Flask!'

@app.get('/users/', endpoint='get_users')
def get_users():
    query = request.args.get('query')
    users = load_users()
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

@app.post('/users', endpoint='users_post')
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
    return redirect(url_for('get_users'), code=302)

@app.route('/users/new', endpoint='users_new')
def users_new():
    user = {'name': '', 'email': '', 'password': '', 'passwordConfirmation': '', 'city': ''}
    errors = {}
    return render_template('users/new.html', user=user, errors=errors)

@app.route('/courses/', endpoint='courses_list')
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

@app.route('/courses/<id>', endpoint='courses')
def courses(id):
    course = {
        "id": id,
        "name": f"course-{id}",
        "description": "Описание курса"
    }
    return render_template('courses/view.html', course=course)

@app.route('/users/<id>', endpoint='show_user')
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
