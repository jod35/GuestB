from flask import Flask,render_template,url_for,request,redirect
from forms import SignForm
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['SECRET_KEY']='9a0a8080e3f9bcff09d1bfd8ce5a6e2964ecedc6'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(45),nullable=False)
    Comment=db.Column(db.String(1000))

    

@app.route('/')
def index():
    comments=User.query.all()
    return render_template('guestbook.html',title="Comments",comments=comments)

@app.route('/signin',methods=['POST','GET'])
def SignIn():
    form=SignForm()
    return render_template('signin.html',title='Sign The Guest Book',form=form)

@app.route('/sign-submit',methods=['POST'])
def Submit():
    form=SignForm()
    name=request.form.get('name')
    comment=request.form.get('comment')
    new_comment=User(name=name,Comment=comment)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)