#def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
#    five = Dollar(amount=5)
#    five.times(multiplier=2)
#    assert 10 == five.amount
def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Dollar(5)
    ten = five.times(2)
    assert Dollar(10) == ten 
    fifteen = five.times(3)
    assert Dollar(15) == fifteen

def test_equality():
    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

# If we rewrite the 10 as 5 * 2, the duplication becomes more evident.
class Dollar:
    def __init__(self, amount):
        self.amount = amount
    
    def times(self, multiplier):
        return Dollar(self.amount * multiplier)
    
    def __eq__(self, other):
        return self.amount == other.amount