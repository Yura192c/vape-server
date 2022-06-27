from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:@localhost/test'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    phone_num = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(35), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
    	return "<{}:{},{}>".format(self.id,  self.name[:35], self.phone_number[:15])



@app.route("/")
def index():
    return "Hello World! http://127.0.0.1:5000/homepage"


@app.route('/user/id/<int:id>/')
def show_user_profile(id):
    # показать профиль данного пользователя
    return "User id:" + str(id)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # вывести сообщение с данным id, id - целое число
    return 'Post %d' % post_id

if __name__ == "__main__":
    app.run()
   # "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"