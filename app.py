from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,country_id,phone,email) values (:username,:country_id,:phone,:email)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_gossip", methods=["GET","POST"])
def add_one_gossip():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into gossip (content,user_id) values (:content,:user_id)",request.form)
        user = query_db('select * from gossip')
        return render_template("gossipform.html", gossips=user, one_user=one_user, the_title="add new gossip")
    user = query_db('select * from gossip')
    one_user = query_db("select * from gossip limit 1", one=True)
    return render_template("gossipform.html", gossips=user, one_user=one_user, the_title="add new gossip")

@app.route("/add_one_ooh_ad", methods=["GET","POST"])
def add_one_ooh_ad():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into ooh_ad (text_content,pic_description,user_id) values (:text_content,:pic_description,:user_id)",request.form)
        user = query_db('select * from ooh_ad')
        return render_template("ooh_adform.html", ooh_ads=user, one_user=one_user, the_title="add new ooh_ad")
    user = query_db('select * from ooh_ad')
    one_user = query_db("select * from ooh_ad limit 1", one=True)
    return render_template("ooh_adform.html", ooh_ads=user, one_user=one_user, the_title="add new ooh_ad")

@app.route("/add_one_own_cybersecurity", methods=["GET","POST"])
def add_one_own_cybersecurity():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into own_cybersecurity (content,user_id) values (:content,:user_id)",request.form)
        user = query_db('select * from own_cybersecurity')
        return render_template("own_cybersecurityform.html", own_cybersecuritys=user, one_user=one_user, the_title="add new own_cybersecurity")
    user = query_db('select * from own_cybersecurity')
    one_user = query_db("select * from own_cybersecurity limit 1", one=True)
    return render_template("own_cybersecurityform.html", own_cybersecuritys=user, one_user=one_user, the_title="add new own_cybersecurity")

