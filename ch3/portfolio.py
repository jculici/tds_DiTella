#def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
#    five = Dollar(amount=5)
#    five.times(multiplier=2)
#    assert 10 == five.amount
def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3) 

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)
    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)
    assert Dollar(5) != Franc(5)

def test_franc_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)

class Money:
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

    def dollar(amount):
        return Dollar(amount)

class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)
    
class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)