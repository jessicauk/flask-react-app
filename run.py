from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config.update(
  SECREY_KEY='jessica22',
  # SQLALCHEMY_DATABASE_URI='<database>://<user_id>:<passwor>@<server>/<database_name>',
  SQLALCHEMY_DATABASE_URI='postgresql://postgres:jessica22@localhost/contact',
  SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello'

# query strings

@app.route('/new/')
def querystring(greeting = "hello"):
    query_val = request.args.get('greeting', greeting)
    return '<h1> the greeting is: {0} </h1>'.format(query_val)

# remove query strings

@app.route('/user')
@app.route('/user/<name>')
def no_query_string(name="Jessica"):
    return '<h1>Hello there {0} </h1>'.format(name)

# strings

@app.route('/text/<string:name>')
def working_with_strings(name='jessica apolinar'):
    return '<h1>here is a string: {0}</h1>'.format(name)

# numbers

@app.route('/numbers/<int:num>')
def worrking_with_numbers(num):
    return '<h1>The number you picked is: {0}</h1>'.format(num)

# numbers add

@app.route('/add/<int:num1>/<int:num2>')
def adding_integers(num1,num2):
    return '<h1>The sum is: {}'.format(num1 + num2) + '</h1>'

# floats add

@app.route('/product/<float:num1>/<float:num2>')
def product_two_numbers(num1,num2):
    return '<h1>The product is: {}'.format(num1 * num2) + '</h1>'

# templates

@app.route('/template')
def using_template():
    return render_template('hello.html', token="hello world")

class Person(db.Model):
  __table_name__ = 'person'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  registerDate = db.Column(db.DateTime, default=datetime.utcnow())

  def __init__(self, id, name, registerDate):
    self.id = id
    self.name = name
    self.registerDate = registerDate


  def __repr__(self):
    return 'The id is {}, Name is {}'.format(self.id, self.name)

class PhoneNumber(db.Model):
    __table_name__ = 'phone'

    idPhoneNumber = db.Column(db.Integer, primary_key=True)
    typePhoneNumber = db.Column(db.Integer, nullable = False)
    phoneNumber = db.Column(db.String(30), nullable= True)

    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self, idPhoneNumber, typePhoneNumber, phoneNumber, person_id):
        self.idPhoneNumber = idPhoneNumber
        self.typePhoneNumber = typePhoneNumber
        self.phoneNumber = phoneNumber
        self.person_id = person_id

    def __repr__(self):
        return '{}, - {}'.format(self.phoneNumber, self.name)
    # relationship
    


if __name__ == '__main__' :
    db.create_all()
    app.run(debug=True)
