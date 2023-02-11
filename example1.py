from faker import Faker

print('Hello World')
dir(Faker())
fake = Faker()
print(fake.name())
print(fake.email())
print(fake.country())

print(fake.profile())
