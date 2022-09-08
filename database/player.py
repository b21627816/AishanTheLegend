from re import X
from sqlalchemy import Column, String, Integer, ARRAY, JSON, BigInteger
from .base import Base


class Player(Base):
    __tablename__ = "player"

    id = Column(Integer, primary_key=True)
    health = Column(Integer)
    xp = Column(BigInteger)
    level = Column(Integer)
    weapon = Column(String)
    inventory = Column(ARRAY(JSON))

    def __init__(self, health, xp, level, weapon, inventory):
        self.health = health
        self.xp = xp
        self.level = level
        self.weapon = weapon
        self.inventory = inventory

    def __repr__(self) -> str:
        return f"Player(id={self.id!r}, health={self.health!r}, level={self.level!r}, weapon={self.weapon!r}, inventory={self.inventory!r})"
