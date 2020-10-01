import unittest
from sqlalchemy import MetaData
from database.wrapper import Database
from database.models import Item, PotionEffect, PotionItem, Requirement, Recipe, CraftingIngredient

TEST_ITEM_NAME = "Test"
TEST_ITEM_VALUE = 1
TEST_ITEM_WEIGHT = 0.5
TEST_ITEM_ID = 100

TEST_EFFECT_NAME = "TestEffect"
TEST_EFFECT_DESC = "Description"
TEST_EFFECT_COST = 1
TEST_EFFECT_MAG = 2
TEST_EFFECT_DUR = 3
TEST_EFFECT_VALUE = 4
TEST_EFFECT_NEG = True
TEST_EFFECT_VARYDUR = False
TEST_EFFECT_ID = 200

TEST_REQUIREMENT_NAME = "Requirement"
TEST_REQUIREMENT_DESC = "This is a test"

TEST_RECIPE_QUANTITY = 2

class TestWrappers(unittest.TestCase):
    def setUp(self):
        self.db = Database("sqlite:///:memory:")
        testitem = self.db.new_item(
            TEST_ITEM_NAME, TEST_ITEM_VALUE, TEST_ITEM_WEIGHT,
            TEST_ITEM_ID
        )
        self.db.new_potion_effect(
            TEST_EFFECT_NAME, TEST_EFFECT_DESC, TEST_EFFECT_COST,
            TEST_EFFECT_MAG, TEST_EFFECT_DUR, TEST_EFFECT_VALUE,
            TEST_EFFECT_NEG, TEST_EFFECT_VARYDUR, TEST_EFFECT_ID
        )
        testreq = self.db.add_requirement(
            TEST_REQUIREMENT_NAME, TEST_REQUIREMENT_DESC
        )
        self.db.commit()
        testrecipe = self.db.add_recipe(
            testitem, TEST_RECIPE_QUANTITY, testreq
        )
        self.db.commit()
        self.db.add_ingredient_to_recipe(testrecipe, testitem)
        self.db.commit()

    def tearDown(self):
        self.db.close_session()
        m = MetaData()
        m.reflect(self.db.engine)
        m.drop_all(self.db.engine)
        self.db.engine.dispose()
        self.db = None

    def assertTestItem(self, item):
        self.assertEqual(
            item.name, TEST_ITEM_NAME, "Name does not match"
        )
        self.assertEqual(
            item.value, TEST_ITEM_VALUE, "Value does not match"
        )
        self.assertEqual(
            item.weight, TEST_ITEM_WEIGHT, "Weight does not match"
        )
        self.assertEqual(item.id, TEST_ITEM_ID, "ID does not match")

    def assertTestEffect(self, effect: PotionEffect):
        self.assertEqual(
            effect.name, TEST_EFFECT_NAME, "Name does not match"
        )
        self.assertEqual(
            effect.description, TEST_EFFECT_DESC,
            "Description does not match"
        )
        self.assertEqual(
            effect.base_cost, TEST_EFFECT_COST, "Cost does not match"
        )
        self.assertEqual(
            effect.base_mag, TEST_EFFECT_MAG,
            "Magnitude does not match"
        )
        self.assertEqual(
            effect.base_dur, TEST_EFFECT_DUR, "Duration does not match"
        )
        self.assertEqual(
            effect.value, TEST_EFFECT_VALUE, "Value does not match"
        )
        self.assertEqual(
            effect.is_negative, TEST_EFFECT_NEG,
            "is_negative does not match"
        )
        self.assertEqual(
            effect.vary_duration, TEST_EFFECT_VARYDUR,
            "vary_duration does not match"
        )
        self.assertEqual(
            effect.id, TEST_EFFECT_ID, "ID does not match"
        )

    def assertTestRequirement(self, req: Requirement):
        self.assertEqual(
            req.name, TEST_REQUIREMENT_NAME, "Name does not match"
        )
        self.assertEqual(
            req.desc, TEST_REQUIREMENT_DESC,
            "Description does not match"
        )

    def assertTestRecipe(self, recipe: Recipe):
        self.assertEqual(
            recipe.result_id, TEST_ITEM_ID, "Wrong item ID"
        )
        self.assertEqual(
            recipe.requirement.name, TEST_REQUIREMENT_NAME,
            "Wrong requirement name"
        )
        self.assertEqual(
            recipe.quantity, TEST_RECIPE_QUANTITY, "Wrong quantity"
        )

    def test_new_item(self):
        items = self.db.session.query(Item).filter_by(
            name=TEST_ITEM_NAME
        ).all()
        self.assertEqual(len(items), 1, "Should only be one item")
        self.assertTestItem(items[0])

    def test_get_item_by_id(self):
        item = self.db.get_item_by_ID(TEST_ITEM_ID)
        self.assertTestItem(item)

    def test_get_items_by_name(self):
        items = self.db.get_items_by_name(TEST_ITEM_NAME)
        self.assertEqual(len(items), 1)
        self.assertTestItem(items[0])

    def test_new_potion_effect(self):
        effect = self.db.session.query(PotionEffect).filter_by(
            id=TEST_EFFECT_ID
        ).first()
        self.assertTestEffect(effect)

    def test_get_effect_by_ID(self):
        effect = self.db.get_effect_by_ID(TEST_EFFECT_ID)
        self.assertTestEffect(effect)

    def test_get_effect_by_name(self):
        effects = self.db.get_effects_by_name(TEST_EFFECT_NAME)
        self.assertEqual(len(effects), 1)
        self.assertTestEffect(effects[0])

    def test_effect_association(self):
        item = self.db.get_item_by_ID(TEST_ITEM_ID)
        effect = self.db.get_effect_by_ID(TEST_EFFECT_ID)
        self.db.add_effect_to_ingredient(effect, item, 1, 2, 3)
        self.db.commit()

        potionitems = self.db.get_effects_by_item(item)
        self.assertEqual(len(potionitems), 1)
        self.assertTestEffect(potionitems[0].effect)
        self.assertTestItem(potionitems[0].item)

        potionitems = self.db.get_items_by_effect(effect)
        self.assertEqual(len(potionitems), 1)
        self.assertTestEffect(potionitems[0].effect)
        self.assertTestItem(potionitems[0].item)

    def test_add_requirement(self):
        req = self.db.session.query(Requirement).filter_by(
            name=TEST_REQUIREMENT_NAME
        ).first()
        self.assertTestRequirement(req)

    def test_get_requirements_by_name(self):
        reqs = self.db.get_requirements_by_name(TEST_REQUIREMENT_NAME)
        self.assertEqual(len(reqs), 1)
        self.assertTestRequirement(reqs[0])

    def test_add_recipe(self):
        recipe = self.db.session.query(Recipe).first()
        self.assertTestRecipe(recipe)

    def test_get_ingredients_for_recipe(self):
        recipe = self.db.session.query(Recipe).first()
        ingredients = self.db.get_ingredients_for_recipe(recipe)
        self.assertEqual(len(ingredients), 1)
        self.assertTestItem(ingredients[0].ingredient)
        self.assertTrue(recipe is ingredients[0].recipe)
        self.assertEqual(ingredients[0].quantity, 1)

if __name__ == '__main__':
    unittest.main()
