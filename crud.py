from main import db, employee

# Creating a new employee
employee1 = employee("John", 35)
db.session.add(employee1)
db.session.commit()

# Read the records
allRecords = employee.query.all(); # List all meployees in the table
print(allRecords)

# Select by ID
idNum = 1
getInformation = employee.query.get(idNum)
print(getInformation)


# Filter with name
nameFilter = employee.query.filter_by(name="Alice")
print(nameFilter.all())

# Update the records
updateRecord = employee.query.get(1)
updateRecord.age = 28
db.session.add(updateRecord)
db.session.commit()

# Delete record
deleteRecord = employee.query.get(2)
db.session.delete(deleteRecord)
db.session.commit()

# Print all records
allRecords = employee.query.all()
print(allRecords)
