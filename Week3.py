bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("Original list of Bikes:", bicycles)

print("First bicycle:", bicycles[0].upper())

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Number of cars in the list:", len(cars))

bicycles[0] = 'giant'
print('Updated list of bikes:', bicycles)

motorcycle = ['honda', 'yamaha', 'suzuki']
motorcycle.append('ducati')
print('list after appending', motorcycle)

motorcycle.insert(0, 'harley')
print('list after inserting:', motorcycle)

del motorcycle[0]
print('list after using del:', motorcycle)

popped_motorcycle = motorcycle.pop()
print('Popped Motorcycle', popped_motorcycle)
print('list after popping:', motorcycle)

motorcycle.remove('yamaha')
print('list after removing yamaha', motorcycle)


cars.sort()
print('permanently sorted cars', cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('original list of cars:', cars)
print('temporarily sorted cars:', sorted(cars))
print('original list of after termporary sort:', cars)

cars.sort()
cars.reverse()
print('reversed list of cars:', cars)

sorted_num = [2,3,4,5,7]

sum = 0

for num in sorted_num:
    sum = sum + num
    print(sum)

print(sum)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!") 
    print(f"I cant wait to see your next trick, {magician.title()}\n")

range_of_numbers = range(1, 5)
for value in range_of_numbers:
    print('generated val:', value)

squares = [value** 2 for value in range(1, 6)]
print('list of squares', squares)

dimensions = (200, 50)
print('tuple dimensions:', dimensions)

