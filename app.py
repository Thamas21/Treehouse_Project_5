from flask import (render_template, url_for,
                   request, redirect)
from models import (app, Project, db)
from datetime import datetime


def date_strptime(date_str):
    date_str = date_str.replace('-', ' ')
    date_obj = datetime.strptime(date_str, '%Y %m')
    return date_obj


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projectform', methods=['GET', 'POST'])
def projectform():
    if request.form:
        print(request.form['title'])
        print(type(request.form['date']))
        date_obj = date_strptime(request.form['date'])
        print(type(date_obj))
        new_project = Project(title=request.form['title'],
                              date=date_obj,
                              description=request.form['description'],
                              skills_list=request.form['skills'],
                              github=request.form['github'])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('projectform.html')


@app.route('/edit_project/<id>', methods=['GET', 'POST'])
def edit_project(id):
    project = Project.query.get_or_404(id)
    if request.form:
        date_obj = date_strptime(request.form['date'])
        project.title = request.form['title']
        project.date = date_obj
        project.description = request.form['description']
        project.skills_list = request.form['skills']
        project.github = request.form['github']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_project.html', project=project)


@app.route('/delete_project/<id>')
def delete_project(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/detail/<id>')
def detail(id):
    project = Project.query.get_or_404(id)
    return render_template('detail.html', project=project)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
