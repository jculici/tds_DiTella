def test_multiplication():
    # test that you can multiply a Dollar by a number and get the right amount.
    five = Dollar(amount=5)
    five.times(multiplier=2)
    assert 10 == five.amount
class Dollar:
    pass