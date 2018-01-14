
def person(name, age, **kw):
	print('name: %s age: %s other: %s' % (name, age, kw))

extra = {'city': 'Beijing', 'job': 'Engineer'}

person('Michael', 30, **extra)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

def person(name, age, *, city, job):
	print(name, age, city, job)
	
person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *args, city="Beijing", job):
	print(name, age, args, city, job)
	
person('Jack', 24, job='Engineer')
