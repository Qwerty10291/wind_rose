import sqlalchemy
from db_session import SqlAlchemyBase
from sqlalchemy import orm

class City(SqlAlchemyBase):
    __tablename__ = 'cities'
    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    link = sqlalchemy.Column(sqlalchemy.String)
    winds = orm.relation('Winds', back_populates='city')

class Winds(SqlAlchemyBase):
    __tablename__ = 'winds'
    id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True, autoincrement=True)
    city_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("cities.id"))
    wind = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.DateTime)
    city = orm.relation("City")