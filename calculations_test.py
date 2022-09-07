# Egy teszteset az egy függvény
# Egy teszteset mindig csak egy dolgot tesztel
#Teszteset neve konvenció szerint a test szóval kezdődik




from calculations import absolute


def test_absolute_with_positive():
    # BDD = Behaviour Driven Development
    # 3 részből áll:givel-when-then
    #given
    input = 5
        #when
    result = absolute(input)
    expected = 5
    assert result == expected

def test_absolute_with_negtive():
    assert absolute(-5) == 5

def test_absolute_with_zero():
    assert absolute(0) == 0