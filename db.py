from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

    workouts = relationship("Workout", back_populates="user")


class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    type = Column(String)
    duration = Column(Integer)  # minutes
    calories = Column(Float)
    date = Column(Date)

    user = relationship("User", back_populates="workouts")


engine = create_engine('sqlite:///fitness.db', echo=True)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

class Data:
    def __init__(self):
        self.session = Session()

    def user_register(self,name:str,age:int) -> str:
        try:
            user = User(name=name, age=age)
            self.session.add(user)
            self.session.commit()
            return "User added successfully"
        except Exception as e:
            self.session.rollback()
            print("Error: ", e)
            raise

    def get_users(self):
        return self.session.query(User).all()

