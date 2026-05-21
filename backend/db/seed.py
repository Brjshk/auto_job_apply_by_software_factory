from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.job import Job
from models.application import Application

DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_db():
    db = SessionLocal()
    # Add sample users
    user = User(username='testuser', password='hashed_password', resume='resume.pdf')
    db.add(user)
    # Add sample jobs
    job = Job(id='1', title='Software Engineer', company='Tech Co', location='Remote', description='Develop software.')
    db.add(job)
    db.commit()
    db.close()

if __name__ == '__main__':
    seed_db()
