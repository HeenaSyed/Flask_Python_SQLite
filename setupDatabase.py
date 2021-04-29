from main import db, employee

# Creates all the tables
# Converting class employee to a database
db.create_all()

Alice = employee('Alice', 25)
Bob = employee('Bob', 25)

print(Alice.id, Bob.id)

# To add all objects
db.session.add_all([Alice, Bob])

# To add objects sequentially
# db.session.add(Alice)
# db.session.add(Bob)

# Save the records
db.session.commit()

print(Alice.id, Bob.id)