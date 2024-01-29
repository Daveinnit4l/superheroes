from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Enum, ForeignKey

db = SQLAlchemy()

class Hero(db.Model):
    _tablename_ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    super_name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime) 

    powers = relationship('Power', secondary='hero_powers')
 

class Power(db.Model):
    _tablename_ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime) 

    heroes = relationship('Hero', secondary='hero_powers')


class HeroPower(db.Model):
    _tablename_ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255))
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime) 

    hero = relationship('Hero', backref='hero_powers')
    power = relationship('Power', backref='hero_powers')

    _table_args_ = (
        db.UniqueConstraint('hero_id', 'power_id', name='uq_hero_power'),
    )