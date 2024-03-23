def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Dollar(amount=5)
    five.times(multiplier=2)
    assert 10 == five.amount
def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount

# If we rewrite the 10 as 5 * 2, the duplication becomes more evident.
def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount

# If we rewrite the 10 as 5 * 2, the duplication becomes more evident.
def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount

# If we rewrite the 10 as 5 * 2, the duplication becomes more evident.
def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Dollar(5)
    five.times(2)
    assert 10 == five.amount

# If we rewrite the 10 as 5 * 2, the duplication becomes more evident.
class Dollar:
    def __init__(self, amount):
        self.amount = amount
    
    def times(self, multiplier):
        self.amount *= multiplier