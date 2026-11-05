from api.fetch_data import fetchAndStore
from data_protection import anonymize_and_mask
from data_analysis import analyze_data

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.db.models import DataProtectedUser
from configuration import DATABASE_URL

def main():
    # 1. Hakee käyttäjät API:sta ja tallentaa ne tietokantaan
    users = fetchAndStore()

    # 2. Uusi muuttuja käsitellyille käyttäjille.
    hiddenUsers = anonymize_and_mask(users)

    # Lisätään suojatut käyttäjät toiseen tietokantataulukkoon
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    try:
        for u in hiddenUsers:
            dataprotecteduser = DataProtectedUser(  
                id=u["id"],
                    name=u["name"],
                    username=u["username"],
                    email=u["email"],
                    phone=u["phone"],
                    website=u["website"],
                    address=u["address"],
                    company=u["company"]
            )
            session.merge(dataprotecteduser)
        session.commit()
    except Exception as e:
        print(e)
    finally:
        session.close()


    # 3. Datan analysointi ja tulostus
    data = analyze_data(users)
    print(f"Shape = {data['shape']}")
    print(f"First two: \n{data['first']['name']}")
    print(f"Last two: \n{data['last']['name']}")
    

if __name__ == "__main__":
    main()