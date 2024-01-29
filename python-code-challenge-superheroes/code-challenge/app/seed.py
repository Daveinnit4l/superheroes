from app import app, db
from models import Hero, Power, HeroPower

def seed_heroes(heroes_data):
    print(":female_superhero: Seeding heroes...")
    for hero_data in heroes_data:
        hero = Hero(**hero_data)
        db.session.add(hero)
        db.session.commit()
    print("Hero seeding completed.")

def seed_powers(powers_data):
    print(":female_superhero: Seeding powers...")
    for power_data in powers_data:
        power = Power(**power_data)
        db.session.add(power)
    db.session.commit()
    print("Power seeding completed.")

def seed_hero_powers(hero_power_data ):
    print(":female_superhero: Seeding hero_powers...")
    for hero_power_data in heroes_power_data:
        hero_power_data = HeroPower(**hero_power_data)
        db.session.add(hero_power_data)
        db.session.commit()
        print("HeroPower seeding completed.")

if __name__ == '_main_':
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Jessica Jones", "super_name": "Jewel"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Natasha Romanoff", "super_name": "Black Widow"},
        {"name": "Peter Parker", "super_name": "Spider-Man"},
        {"name": "Bruce Wayne", "super_name": "Batman"},
        {"name": "Clark Kent", "super_name": "Superman"},
        {"name": "Barry Allen", "super_name": "The Flash"},
        {"name": "Diana Prince", "super_name": "Wonder Woman"},
        {"name": "Wade Wilson", "super_name": "Deadpool"},
        {"name": "Tony Stark", "super_name": "Iron Man"},
        {"name": "Scott Summers", "super_name": "Cyclops"},
        {"name": "Jean Grey", "super_name": "Phoenix"},
        {"name": "Hank Pym", "super_name": "Ant-Man"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Matt Murdock", "super_name": "Daredevil"},
        {"name": "Remy LeBeau", "super_name": "Gambit"},
        {"name": "Bruce Banner", "super_name": "The Hulk"}
    
    ]

    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"},
        {"name": "telepathy", "description": "can read minds"},
        {"name": "telekinesis", "description": "can move objects with the mind"},
        {"name": "regeneration", "description": "ability to heal rapidly from any physical injury"},
        {"name": "shape-shifting", "description": "can change physical form at will"},
        {"name": "invisibility", "description": "ability to become unseen"},
        {"name": "teleportation", "description": "instantaneous transportation of oneself"},
        {"name": "time manipulation", "description": "control over the flow of time"},
        {"name": "mind control", "description": "ability to control the thoughts and actions of others"},
        {"name": "intangibility", "description": "ability to pass through solid matter"},
        {"name": "energy projection", "description": "release of energy beams or blasts"},
        {"name": "force field generation", "description": "creation of protective barriers"},
        {"name": "super speed", "description": "ability to move at extraordinary speeds"},
        {"name": "weather manipulation", "description": "control over weather patterns"},
        {"name": "sonic scream", "description": "emit powerful vocalizations"},
        {"name": "precognition", "description": "ability to perceive future events"},
        {"name": "super agility", "description": "exceptional agility and reflexes"}
    
    ]

    heroes_power_data = [
        {'strength': 'Average', 'hero_id': 1, 'power_id': 1},
        {'strength': 'Strong', 'hero_id': 2, 'power_id': 2},
        {'strength': 'Weak', 'hero_id': 3, 'power_id': 3},
        {'strength': 'Average', 'hero_id': 4, 'power_id': 4},
        {'strength': 'Strong', 'hero_id': 5, 'power_id': 5},
        {'strength': 'Weak', 'hero_id': 6, 'power_id': 6},
        {'strength': 'Average', 'hero_id': 7, 'power_id': 7},
        {'strength': 'Strong', 'hero_id': 8, 'power_id': 8},
        {'strength': 'Weak', 'hero_id': 9, 'power_id': 9},
        {'strength': 'Average', 'hero_id': 10, 'power_id': 10},
        {'strength': 'Strong', 'hero_id': 11, 'power_id': 11},
        {'strength': 'Weak', 'hero_id': 12, 'power_id': 12},
        {'strength': 'Average', 'hero_id': 13, 'power_id': 13},
        {'strength': 'Strong', 'hero_id': 14, 'power_id': 14},
        {'strength': 'Weak', 'hero_id': 15, 'power_id': 15},
        {'strength': 'Average', 'hero_id': 16, 'power_id': 16},
        {'strength': 'Strong', 'hero_id': 17, 'power_id': 17},
        {'strength': 'Weak', 'hero_id': 18, 'power_id': 18},
        {'strength': 'Average', 'hero_id': 19, 'power_id': 19},
        {'strength': 'Strong', 'hero_id': 20, 'power_id': 20}

    ]
with app.app_context():
    seed_heroes(heroes_data)
    seed_powers(powers_data)
    seed_hero_powers(heroes_power_data)