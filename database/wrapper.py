from typing import List, Tuple, Union

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import Item, PotionEffect, PotionItem, Requirement, Recipe, CraftingIngredient

class Database:
    def __init__(self, url):
        self.engine = create_engine(url)
        Item.metadata.create_all(self.engine)
        PotionEffect.metadata.create_all(self.engine)
        PotionItem.metadata.create_all(self.engine)
        Recipe.metadata.create_all(self.engine)
        CraftingIngredient.metadata.create_all(self.engine)

        self.NewSession = sessionmaker(bind=self.engine)
        self.session = None

    def new_session(self, commit=False):
        if self.session is not None and commit:
            self.session.commit()
        self.session = self.NewSession()

    def have_session(self):
        if self.session is None:
            self.session = self.NewSession()

    def commit(self):
        return self.session.commit()

    def rollback(self):
        return self.session.rollback()

    def close_session(self):
        self.session.close()
        self.session = None

    def new_item(
        self,
        name: str,
        value: int,
        weight: float,
        id: int = None
    ) -> Item:
        self.have_session()
        newitem = Item(
            name=name,
            value=value,
            weight=weight,
        )

        if id is not None:
            newitem.id = id

        self.session.add(newitem)
        return newitem

    def get_item_by_ID(self, ID: Union[int, str]) -> Item:
        self.have_session()
        if isinstance(ID, str):
            ID = int(ID, 16)
        return self.session.query(Item).filter_by(id=ID).first()

    def get_items_by_name(self, name: str) -> List[Item]:
        self.have_session()
        return self.session.query(Item).filter_by(name=name).all()

    def new_potion_effect(
        self,
        name: str,
        desc: str,
        cost: float,
        mag: int,
        dur: int,
        value: int,
        is_negative: bool,
        vary_duration: bool,
        id: int = None,
    ) -> PotionEffect:
        self.have_session()
        neweffect = PotionEffect(
            name=name,
            is_negative=is_negative,
            description=desc,
            base_cost=cost,
            base_mag=mag,
            base_dur=dur,
            value=value,
            vary_duration=vary_duration,
        )

        if id is not None:
            neweffect.id = id

        self.session.add(neweffect)
        return neweffect

    def get_effect_by_ID(self, ID: int) -> PotionEffect:
        self.have_session()
        return self.session.query(PotionEffect).filter_by(id=ID
                                                          ).first()

    def get_effects_by_name(self, name: str) -> List[PotionEffect]:
        self.have_session()
        return self.session.query(PotionEffect).filter_by(name=name
                                                          ).all()

    def get_effects_by_item(self, item: Item) -> List[PotionItem]:
        self.have_session()
        assert item.id is not None
        potionitems = self.session.query(PotionItem).filter_by(
            item_id=item.id,
        ).all()
        return potionitems

    def add_effect_to_ingredient(
        self,
        effect: PotionEffect,
        item: PotionEffect,
        mag_mult: float = 1,
        dur_mult: float = 1,
        val_mult: float = 1
    ):
        self.have_session()
        assert item.id is not None
        assert effect.id is not None
        new = PotionItem(
            item_id=item.id,
            effect_id=effect.id,
            mag_multiplier=mag_mult,
            dur_multiplier=dur_mult,
            val_multiplier=val_mult
        )
        return self.session.add(new)

    def get_items_by_effect(self,
                            effect: PotionEffect) -> List[PotionItem]:
        self.have_session()
        assert PotionEffect.id is not None
        potion_items = self.session.query(PotionItem).filter_by(
            effect_id=effect.id
        ).all()
        return potion_items

    def add_requirement(self, name: str, desc: str) -> Requirement:
        self.have_session()
        requirement = Requirement(name=name, desc=desc)
        self.session.add(requirement)
        return requirement

    def get_requirements_by_name(self, name: str) -> List[Requirement]:
        self.have_session()
        reqs = self.session.query(Requirement).filter_by(name=name
                                                         ).all()
        return reqs

    def add_recipe(
        self,
        result: Item,
        quantity: int,
        requirement: Requirement = None
    ) -> Recipe:
        self.have_session()
        assert result.id is not None
        recipe = Recipe(result_id=result.id, quantity=quantity)

        if requirement is not None:
            assert requirement.id is not None
            recipe.requirement_id = requirement.id

        self.session.add(recipe)
        return recipe

    def add_ingredient_to_recipe(
        self, recipe: Recipe, ingredient: Item, quantity: int = 1
    ):
        self.have_session()
        assert recipe.id is not None
        assert ingredient.id is not None
        self.session.add(
            CraftingIngredient(
                recipe_id=recipe.id,
                ingredient_id=ingredient.id,
                quantity=quantity,
            )
        )

    def get_ingredients_for_recipe(
        self, recipe: Recipe
    ) -> List[CraftingIngredient]:
        self.have_session()
        assert recipe.id is not None
        crafting_ingredients = self.session.query(
            CraftingIngredient
        ).filter_by(
            recipe_id=recipe.id,
        ).all()
        return crafting_ingredients

    def get_recipes_for_item(
        self, item: Item, requirements: List[Requirement] = None
    ):
        """Get all available Recipes that produce a given item. Requirements can be used to restrict the available recipes. A list of Requirements should be given as requirements. requirements=[] will list all recipes with no prerequisites, whilst requirements=None will list all recipes regardless of requirements."""
        self.have_session()
        assert item.id is not None
        query = self.session.query(Recipe).filter_by(result_id=item.id)

        if requirements is not None:
            reqs = [None]
            for req in requirements:
                assert req.id is not None
                reqs.append(req.id)
            query.filter(Recipe.requirement_id.in_(reqs))

        return query.all()
