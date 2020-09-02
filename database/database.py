from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Item, PotionEffect, PotionItem, Recipe, CraftingIngredient

class Database:
    def __init__(self, url):
        self.engine = create_engine(url)
        Item.metadata.create_all(self.engine)
        PotionEffect.metadata.create_all(self.engine)
        PotionItem.metadata.create_all(self.engine)
        Recipe.metadata.create_all(self.engine)
        CraftingIngredient.metadata.create_all(self.engine)

        self.SessionMaker = sessionmaker(bind=self.engine)
