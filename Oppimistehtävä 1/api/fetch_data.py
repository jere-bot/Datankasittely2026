import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db.models import User
from configuration import DATABASE_URL, API_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def fetchAndStore():
    response = requests.get(API_URL)
    users = response.json()
    session = SessionLocal()
    try:
        for u in users:
            user = User(
                id=u["id"],
                name=u["name"],
                username=u["username"],
                email=u["email"],
                phone=u["phone"],
                website=u["website"],
                address=u["address"],
                company=u["company"]
         )
            session.merge(user)  # merge avoids duplicate key errors
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close

    print("Users inserted into database.")
    return users