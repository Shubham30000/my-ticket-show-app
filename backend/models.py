from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


#First Entity
class User_Info(db.Model):
    __tablename__ = "user_info"
    id=db.Column(db.Integer,primary_key = True)
    email=db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    role = db.Column(db.String,default = 1)
    full_name = db.Column(db.String,nullable=False)
    address = db.Column(db.String,nullable=False)
    pincode = db.Column(db.Integer,nullable=False)
    #relations later
    tickets = db.relationship("Ticket",cascade="all,delete",backref="user_info",lazy = True)

#Second Entity
class Theatre(db.Model):
    __tablename__ = "theatre"
    id=db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String,nullable=False)
    location = db.Column(db.String,nullable=False)
    pincode = db.Column(db.Integer,nullable=False)
    capacity = db.Column(db.Integer,nullable=False)
    show = db.relationship("Shows",cascade="all,delete",backref="theatre",lazy = True)


#Third entity
class Shows(db.Model):
    __tablename__ = "shows"
    id=db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String,nullable=False)
    tags = db.Column(db.String,nullable=False)
    tkt_price = db.Column(db.Float,nullable=False)
    rating = db.Column(db.Integer,default = 0)
    date_time = db.Column(db.DateTime,nullable = False)
    theatre_id = db.Column(db.Integer,db.ForeignKey("theatre.id"),nullable = False)
    tickets = db.relationship("Ticket",cascade="all,delete",backref="user_info",lazy = True)



#Fourth entity
class Ticket(db.Model):
    __tablename__ = "ticket"
    id=db.Column(db.Integer,primary_key = True)
    no_of_tickets = db.Column(db.Integer,nullable=False)
    sl_nos = db.Column(db.String,nullable=False)
    user_rating = db.Column(db.Integer,default = 0)
    user_id = db.Column(db.Integer,db.ForeignKey("user_info.id"),nullable = False)
    shows_id = db.Column(db.Integer,db.ForeignKey("shows.id"),nullable = False)



