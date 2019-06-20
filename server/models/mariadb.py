from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)

    # name by language
    name_ko = db.Column(db.String(45))
    name_en = db.Column(db.String(45))
    name_ja = db.Column(db.String(45))

    # tag by language
    tag_ko = db.Column(db.String(45))
    tag_en = db.Column(db.String(45))
    tag_ja = db.Column(db.String(45))

