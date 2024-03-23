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

def test_franc_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
class Money:
    pass 
class Dollar(Money):
    def __init__(self, amount):
        self._amount = amount
    
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)
    
    def __eq__(self, other):
        return self._amount == other._amount

class Franc:
    def __init__(self, amount):
        self._amount = amount
    
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
    
    def __eq__(self, other):
        return self._amount == other._amount