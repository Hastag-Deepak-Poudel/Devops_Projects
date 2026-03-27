def add(a,b):
	return a + b

def test_add():
	assert add(2,3) == 6
	assert add('Space','Ship') == 'SpaceShip'