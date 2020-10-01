from database.models import Item
from database.wrapper import Database

def setup_db(url):
    db = Database(url)

    items = {
        "Mudcrab Chitin":
            db.new_item(
                "Mudcrab Chitin", value=2, weight=0.25, id=0x0006bc00
            ),
        "Vampire Dust":
            db.new_item(
                "Vampire Dust", value=25, weight=0.2, id=0x0003ad76
            ),
        "Charred Skeever Hide":
            db.new_item(
                "Charred Skeever Hide",
                value=1,
                weight=0.5,
                id=0x00052695
            ),
        "Hawk Feathers":
            db.new_item(
                "Hawk Feathers", value=15, weight=0.1, id=0x000e7ed0
            ),
        "Jarrin Root":
            db.new_item(
                "Jarrin Root", value=10, weight=0.5, id=0x0001bcbc
            ),
        "River Betty":
            db.new_item(
                "River Betty", value=15, weight=0.25, id=0x00106e1a
            ),
        "Nirnroot":
            db.new_item(
                "Nirnroot", value=10, weight=0.2, id=0x00059b86
            ),
        "Crimson Nirnroot":
            db.new_item(
                "Crimson Nirnroot",
                value=10,
                weight=0.2,
                id=0x000b701a
            ),
        "Deathbell":
            db.new_item(
                "Deathbell", value=4, weight=0.1, id=0x000516c8
            ),
        "Ectoplasm":
            db.new_item(
                "Ectoplasm", value=25, weight=0.1, id=0x0003ad63
            ),
        "Falmer Ear":
            db.new_item(
                "Falmer Ear", value=10, weight=0.2, id=0x0003ad5d
            ),
        "Human Flesh":
            db.new_item(
                "Human Flesh", value=1, weight=0.25, id=0x001016b3
            ),
        "Human Heart":
            db.new_item(
                "Human Heart", value=0, weight=1, id=0x000b18cd
            ),
        "Imp Stool":
            db.new_item(
                "Imp Stool", value=0, weight=0.3, id=0x0004da23
            ),
        "Nightshade":
            db.new_item(
                "Nightshade", value=8, weight=0.1, id=0x0002f44c
            ),
        "Red Mountain Flower":
            db.new_item(
                "Red Mountain Flower",
                value=2,
                weight=0.1,
                id=0x00077e1d
            ),
        "Skeever Tail":
            db.new_item(
                "Skeever Tail", value=3, weight=0.2, id=0x0003ad6f
            ),
        "Small Antlers":
            db.new_item(
                "Small Antlers", value=2, weight=0.1, id=0x0006bc0b
            ),
        "Troll Fat":
            db.new_item(
                "Troll Fat", value=15, weight=1, id=0x0003ad72
            ),
        "Void Salts":
            db.new_item(
                "Void Salts", value=125, weight=0.2, id=0x0003ad60
            ),
        "Butterfly Wing":
            db.new_item(
                "Butterfly Wing", value=3, weight=0.1, id=0x000727e0
            ),
        "Chaurus Eggs":
            db.new_item(
                "Chaurus Eggs", value=10, weight=0.2, id=0x0003ad56
            ),
        "Daedra Heart":
            db.new_item(
                "Daedra Heart", value=250, weight=0.5, id=0x0003ad5b
            ),
        "Eye of Sabre Cat":
            db.new_item(
                "Eye of Sabre Cat", value=2, weight=0.1, id=0x0006bc07
            ),
        "Glow Dust":
            db.new_item(
                "Glow Dust", value=20, weight=0.5, id=0x0003ad73
            ),
        "Hagraven Feathers":
            db.new_item(
                "Hagraven Feathers",
                value=20,
                weight=0.1,
                id=0x0003ad66
            ),
        "Hanging Moss":
            db.new_item(
                "Hanging Moss", value=1, weight=0.25, id=0x00057f91
            ),
        "Luna Moth Wing":
            db.new_item(
                "Luna Moth Wing", value=5, weight=0.1, id=0x000727df
            ),
        "Namira's Rot":
            db.new_item(
                "Namira's Rot", value=0, weight=0.25, id=0x0004da24
            ),
        "Nordic Barnacle":
            db.new_item(
                "Nordic Barnacle", value=5, weight=0.2, id=0x0007edf5
            ),
        "Bear Claws":
            db.new_item(
                "Bear Claws", value=2, weight=0.1, id=0x0006bc02
            ),
        "Blue Butterfly Wing":
            db.new_item(
                "Blue Butterfly Wing",
                value=2,
                weight=0.1,
                id=0x000727de
            ),
        "Blue Mountain Flower":
            db.new_item(
                "Blue Mountain Flower",
                value=2,
                weight=0.1,
                id=0x00077e1c
            ),
        "Chicken's Egg":
            db.new_item(
                "Chicken's Egg", value=2, weight=0.5, id=0x00023d77
            ),
        "Spider Egg":
            db.new_item(
                "Spider Egg", value=5, weight=0.2, id=0x0009151b
            ),
        "Spriggan Sap":
            db.new_item(
                "Spriggan Sap", value=15, weight=0.2, id=0x00063b5f
            ),
        "Berit's Ashes":
            db.new_item(
                "Berit's Ashes", value=5, weight=0.2, id=0x000705b7
            ),
        "Blisterwort":
            db.new_item(
                "Blisterwort", value=12, weight=0.2, id=0x0004da25
            ),
        "Bone Meal":
            db.new_item(
                "Bone Meal", value=5, weight=0.5, id=0x00034cdd
            ),
        "Canis Root":
            db.new_item(
                "Canis Root", value=5, weight=0.1, id=0x0006abcb
            ),
        "Cyrodilic Spadetail":
            db.new_item(
                "Cyrodilic Spadetail",
                value=15,
                weight=0.25,
                id=0x00106e19
            ),
        "Giant's Toe":
            db.new_item(
                "Giant's Toe", value=20, weight=1, id=0x0003ad64
            ),
        "Rock Warbler Egg":
            db.new_item(
                "Rock Warbler Egg", value=2, weight=0.5, id=0x0007e8c8
            ),
        "Creep Cluster":
            db.new_item(
                "Creep Cluster", value=1, weight=0.2, id=0x000b2183
            ),
        "Frost Mirriam":
            db.new_item(
                "Frost Mirriam", value=1, weight=0.1, id=0x00034d32
            ),
        "Histcarp":
            db.new_item(
                "Histcarp", value=6, weight=0.25, id=0x00106e18
            ),
        "Juniper Berries":
            db.new_item(
                "Juniper Berries", value=1, weight=0.1, id=0x0005076e
            ),
        "Large Antlers":
            db.new_item(
                "Large Antlers", value=2, weight=0.1, id=0x0006bc0a
            ),
        "Silverside Perch":
            db.new_item(
                "Silverside Perch",
                value=15,
                weight=0.25,
                id=0x00106e1c
            ),
        "Wheat":
            db.new_item("Wheat", value=5, weight=0.1, id=0x0004b0ba),
        "Blue Dartwing":
            db.new_item(
                "Blue Dartwing", value=1, weight=0.1, id=0x000e4f0c
            ),
        "Powdered Mammoth Tusk":
            db.new_item(
                "Powdered Mammoth Tusk",
                value=2,
                weight=0.1,
                id=0x0006bc10
            ),
        "Grass Pod":
            db.new_item(
                "Grass Pod", value=1, weight=0.1, id=0x00083e64
            ),
        "Dragon's Tongue":
            db.new_item(
                "Dragon's Tongue", value=5, weight=0.1, id=0x000889a2
            ),
        "Hagraven Claw":
            db.new_item(
                "Hagraven Claw", value=20, weight=0.25, id=0x0006b689
            ),
        "Tundra Cotton":
            db.new_item(
                "Tundra Cotton", value=1, weight=0.1, id=0x0003f7f8
            ),
        "Bleeding Crown":
            db.new_item(
                "Bleeding Crown", value=10, weight=0.3, id=0x0004da20
            ),
        "Pearl":
            db.new_item("Pearl", value=2, weight=0.1, id=0x000854fe),
        "Slaughterfish Scales":
            db.new_item(
                "Slaughterfish Scales",
                value=3,
                weight=0.1,
                id=0x0003ad70
            ),
        "Briar Heart":
            db.new_item(
                "Briar Heart", value=20, weight=0.5, id=0x0003ad61
            ),
        "Honeycomb":
            db.new_item("Honeycomb", value=5, weight=1, id=0x000b08c5),
        "Hawk Beak":
            db.new_item(
                "Hawk Beak", value=15, weight=0.25, id=0x000e7ebc
            ),
        "Scaly Pholiota":
            db.new_item(
                "Scaly Pholiota", value=4, weight=0.25, id=0x0006f950
            ),
        "Wisp Wrappings":
            db.new_item(
                "Wisp Wrappings", value=2, weight=0.1, id=0x0006bc0e
            ),
        "Frost Salts":
            db.new_item(
                "Frost Salts", value=100, weight=0.25, id=0x0003ad5f
            ),
        "Lavender":
            db.new_item(
                "Lavender", value=1, weight=0.1, id=0x00045c28
            ),
        "Beehive Husk":
            db.new_item(
                "Beehive Husk", value=5, weight=1, id=0x000a9191
            ),
        "Glowing Mushroom":
            db.new_item(
                "Glowing Mushroom", value=5, weight=0.2, id=0x0007ee01
            ),
        "Snowberries":
            db.new_item(
                "Snowberries", value=4, weight=0.1, id=0x0001b3bd
            ),
        "Ice Wraith Teeth":
            db.new_item(
                "Ice Wraith Teeth",
                value=30,
                weight=0.25,
                id=0x0003ad6a
            ),
        "Sabre Cat Tooth":
            db.new_item(
                "Sabre Cat Tooth", value=2, weight=0.1, id=0x0006bc04
            ),
        "Thistle Branch":
            db.new_item(
                "Thistle Branch", value=1, weight=0.1, id=0x000134aa
            ),
        "White Cap":
            db.new_item(
                "White Cap", value=0, weight=0.3, id=0x0004da22
            ),
        "Dwarven Oil":
            db.new_item(
                "Dwarven Oil", value=15, weight=0.25, id=0x000f11c0
            ),
        "Mora Tapinella":
            db.new_item(
                "Mora Tapinella", value=4, weight=0.25, id=0x000ec870
            ),
        "Taproot":
            db.new_item(
                "Taproot", value=15, weight=0.5, id=0x0003ad71
            ),
        "Pine Thrush Egg":
            db.new_item(
                "Pine Thrush Egg", value=2, weight=0.5, id=0x00023d6f
            ),
        "Jazbay Grapes":
            db.new_item(
                "Jazbay Grapes", value=1, weight=0.2, id=0x0006ac4a
            ),
        "Elves Ear":
            db.new_item(
                "Elves Ear", value=10, weight=0.1, id=0x00034d31
            ),
        "Small Pearl":
            db.new_item(
                "Small Pearl", value=2, weight=0.1, id=0x00085500
            ),
        "Orange Dartwing":
            db.new_item(
                "Orange Dartwing", value=1, weight=0.1, id=0x000bb956
            ),
        "Slaughterfish Egg":
            db.new_item(
                "Slaughterfish Egg",
                value=3,
                weight=0.2,
                id=0x0007e8c5
            ),
        "Abecean Longfin":
            db.new_item(
                "Abecean Longfin", value=15, weight=0.5, id=0x00106e1b
            ),
        "Salt Pile":
            db.new_item(
                "Salt Pile", value=2, weight=0.2, id=0x00034cdf
            ),
        "Purple Mountain Flower":
            db.new_item(
                "Purple Mountain Flower",
                value=2,
                weight=0.1,
                id=0x00077e1e
            ),
        "Garlic":
            db.new_item("Garlic", value=1, weight=0.25, id=0x00034d22),
        "Torchbug Thorax":
            db.new_item(
                "Torchbug Thorax", value=1, weight=0.1, id=0x0004da73
            ),
        "Fly Amanita":
            db.new_item(
                "Fly Amanita", value=2, weight=0.1, id=0x0004da00
            ),
        "Swamp Fungal Pod":
            db.new_item(
                "Swamp Fungal Pod",
                value=5,
                weight=0.25,
                id=0x0007e8b7
            ),
        "Giant Lichen":
            db.new_item(
                "Giant Lichen", value=5, weight=0.25, id=0x0007e8c1
            ),
        "Bee":
            db.new_item("Bee", value=3, weight=0.1, id=0x000a9195),
        "Fire Salts":
            db.new_item(
                "Fire Salts", value=50, weight=0.25, id=0x0003ad5e
            ),
        "Moon Sugar":
            db.new_item(
                "Moon Sugar", value=50, weight=0.25, id=0x000d8e3f
            ),
    }

    potion_effects = {
        "Cure Disease":
            db.new_potion_effect(
                "Cure Disease", "Cures all diseases.", 0.5, 5, 0, 21,
                False, False, 0x000AE722
            ),
        "Damage Health":
            db.new_potion_effect(
                "Damage Health",
                "Causes {mag} points of poison damage.", 3, 2, 1, 3,
                True, False, 0x0003EB42
            ),
        "Damage Magicka":
            db.new_potion_effect(
                "Damage Magicka",
                "Drains the target's Magicka by {mag} points.", 2.2, 3,
                0, 52, True, False, 0x0003A2B6
            ),
        "Damage Magicka Regen":
            db.new_potion_effect(
                "Damage Magicka Regen",
                "Decrease the target's Magicka regeneration by {mag}% for {dur} seconds.",
                0.5, 100, 5, 265, True, True, 0x00073F2B
            )
    }

    db.commit()
