from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)
    weight = Column(Float)

    def __repr__(self):
        return "<{base}.Item(ID={id}, name={name}, value={value}, weight={weight})>".format(
            base=__name__,
            name=self.name,
            id=self.id,
            value=self.value,
            weight=self.weight,
        )

class PotionEffect(Base):
    __tablename__ = "potion_effects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_negative = Column(Boolean)
    description = Column(String)
    base_cost = Column(Float)
    base_mag = Column(Integer)
    base_dur = Column(Integer)
    value = Column(Integer) # value at 100 skill

    def __repr__(self):
        return "<{base}.PotionEffect(id={id}, name={name}, is_negative={neg}, description={desc}, base_cost={cost}, base_mag={mag}, base_dur={dur}, value={value})>".format(
            base=__name__,
            id=self.id,
            name=self.name,
            neg=self.is_negative,
            desc=self.description,
            cost=self.base_cost,
            mag=self.base_mag,
            dur=self.base_dur,
            value=self.value
        )

class PotionItem(Base):
    __tablename__ = "potion_items"

    item_id = Column(
        Integer,
        ForeignKey("{table}.id".format(table=Item.__tablename__)),
        primary_key=True
    )
    effect_id = Column(
        Integer,
        ForeignKey(
            "{table}.id".format(table=PotionEffect.__tablename__)
        ),
        primary_key=True
    )
    mag_multiplier = Column(Float)
    dur_multiplier = Column(Float)
    val_multiplier = Column(Float)

    def __repr__(self):
        return "<{base}.PotionItem(item={item}, effect={effect}, mag_multiplier=x{mag}, dur_multiplier=x{dur}, val_multiplier=x{val})>".format(
            base=__name__,
            item=self.item_id,
            effect=self.effect_id,
            mag=self.mag_multiplier,
            dur=self.dur_multiplier,
            val=self.val_multiplier
        )

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    result_id = Column(
        Integer,
        ForeignKey("{table}.id".format(table=Item.__tablename__)),
    )
    quantity = Column(Integer)

    def __repr__(self):
        return "<{base}.Recipe(id={id}, result={result}, quantity={quantity})>".format(
            base=__name__,
            id=self.id,
            result=self.result_id,
            quantity=self.quantity
        )

class CraftingIngredient(Base):
    __tablename__ = "crafting_ingredients"

    recipe_id = Column(
        Integer,
        ForeignKey("{table}.id".format(table=Recipe.__tablename__)),
        primary_key=True
    )
    ingredient_id = Column(
        Integer,
        ForeignKey("{table}.id".format(table=Item.__tablename__)),
        primary_key=True
    )
    quantity = Column(Integer)

    def __repr__(self):
        return "<{base}.CraftingIngredient(recipe={recipe}, ingredient={ingredient}, quantity={quantity})>".format(
            base=__name__,
            recipe=self.recipe_id,
            ingredient=self.ingredient_id,
            quantity=self.quantity
        )
