from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Item, Category

engine = create_engine('postgresql://catalog:grader@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


first_user = User(
    name='Butrint',
    email='butrint993@gmail.com',
    picture="""https://1.bp.blogspot.com/-DgTeH3DApts/
            TqnPUuWTy3I/AAAAAAAAAbo/2Jn3lMDQ_dk/s1600/
            anonymous.jpg"""
)

session.add(first_user)
session.commit()

first_category = Category(
    name='Soccer',
    user=first_user
)

second_category = Category(
    name='Basketball',
    user=first_user
)

third_category = Category(
    name='Tennis',
    user=first_user
)

fourth_category = Category(
    name='MMA',
    user=first_user
)

session.add(first_category)
session.add(second_category)
session.add(third_category)
session.add(fourth_category)
session.commit()

# Soccer Items
first_item = Item(
    name='Nike Mercurial Vapor 13 Elite Tech Craft FG',
    description="""The Nike Mercurial Vapor 13 Elite Tech
                Craft FG is engineered for a fast-paced,
                leather-based game.""",
    category=first_category,
    user=first_user
)

session.add(first_item)
session.commit()


second_item = Item(
    name='Nike Phantom Vision Elite Dynamic Fit FG',
    description="""The Nike Phantom Vision Elite FG
                Dynamic Fit brings the precision of
                street games to the football field.""",
    category=first_category,
    user=first_user
)

session.add(second_item)
session.commit()

# Basketball Items
third_item = Item(
    name='Jordan Mars 270',
    description="""Drawing inspiration from four classic Air Jordans,
                the Jordan Mars 270 is a modern-day remix
                that offers a heavy dose of heritage.""",
    category=second_category,
    user=first_user
)

session.add(third_item)
session.commit()

fourth_item = Item(
    name='Air Jordan Legacy 312 Low',
    description="""The Air Jordan Legacy 312 Low celebrates Michael Jordans
                legacy with this shout-out to Chicagos 312 area code.""",
    category=second_category,
    user=first_user
)

session.add(fourth_item)
session.commit()

# Tennis Items
fifth_item = Item(
    name='NikeCourt Zoom Cage 3',
    description="""The NikeCourt Zoom Cage 3 delivers
                responsive performance with an iridescent finish.""",
    category=third_category,
    user=first_user
)

session.add(fifth_item)
session.commit()

sixth_item = Item(
    name='NikeCourt Air Max Wildcard',
    description="""The NikeCourt Air Max Wildcard delivers
                the comfort you need to hit hard
                and move fast on the court.""",
    category=third_category,
    user=first_user
)

session.add(sixth_item)
session.commit()

# MMA Items
seventh_item = Item(
    name='Ringside Undefeated Boxing Shoes 8 Black',
    description="""The Ringside Diablo Boxing Shoes usher
                in a new generation of high
                performance ring footwear.""",
    category=fourth_category,
    user=first_user
)

session.add(seventh_item)
session.commit()

eightth_item = Item(
    name='Adidas Combat Speed 5 Wrestling',
    description="""The Adidas Combat Speed shoes
                offer the right comfort one needs to move fast.""",
    category=fourth_category,
    user=first_user
)

session.add(eightth_item)
session.commit()

print("added menu items!")
