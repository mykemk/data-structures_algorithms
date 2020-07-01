# Practicing hash tables

#New hash table
item1 = {'Key1':'Value1', 'key2':'Value2', 'Key3':'Value3'}
print(item1)
#Adding items to the hash table
item1['key4'] = 'Value4'
item1['Key5'] = 'Value5'
print(item1)

#Replacing an item
item1['key1'] = 'Myke'

print(item1)

#Accessing items in a Hash table
for key,value in items(item1):
    print(f'key: {key} value: {value}')
    