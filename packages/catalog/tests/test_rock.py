# write test to test rock class
from catalog import RockType

def test_rock_type():
    assert RockType.igneous.name == "igneous"
    assert RockType.sedimentary.name == "sedimentary"
    assert RockType.metamorphic.name == "metamorphic"

from catalog import Rock

def test_rock():
    rock = Rock("granite", RockType.igneous)
    assert rock.name == "granite"
    assert rock.rock_type == RockType.igneous
    assert str(rock) == "granite is a igneous rock"
    