
from sqlalchemy import Column, Integer, String
from .base import Base


class Monster(Base):
    __tablename__ = "monster"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    health = Column(Integer)
    power = Column(Integer)
    xp = Column(Integer)

    def __init__(self, name, health, power, xp):
        self.name = name
        self.health = health
        self.power = power
        self.xp = xp

    def __repr__(self) -> str:
        return f"Monster(id={self.id!r}, name={self.name!r}, health={self.health!r}, power={self.power!r}, xp={self.xp!r})"
