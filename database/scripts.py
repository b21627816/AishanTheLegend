import os
from dotenv import load_dotenv, find_dotenv
from database.base import Session
from monster import Monster
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def main():
    load_dotenv(find_dotenv())
    engine = create_engine(
        os.getenv("DB_URL"),
        echo=True, future=True)

    Session = sessionmaker(bind=engine)

    Base = declarative_base()

    session = Session()

    add_monsters(session=session)


def add_monsters(session: Session):
    hound = Monster(
        name="Hound",
        power=7,
        xp=10,
        health=70
    )

    slime = Monster(
        name="Slime",
        power=12,
        xp=10,
        health=30
    )

    session.add_all([hound, slime])

    session.commit()


if __name__ == "__main__":
    main()
