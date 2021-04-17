square = [1, 4,9, 16, 26, 50]
print(square)
print(square[0]) # indexing returns the item
print(square[-1])
print(square[-3:]) # Slicing returns anew list
print(square[:]) # copy of the list
print(square + [37, 89, 76, 0, 15]) # concatenation operation
cubes = [1, 8, 27,64,125]
print(4**3)
cubes.append(216) # to add the cube of 6
cubes.append(7**3) # add the cube of 7
print(cubes)
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(letters)
letters[2:4] = ['C', 'D', 'E'] # replaces the first letters with the second
print(letters)
letters[2:4] = [] # clears the elements by replacing the elemnts in the list with an empty list

print(letters)
letters[:] = []
print(letters)
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(len(letters)) # len function is used to count the number of literals in a string

a = ['a', 'b', 'c', 'e']
n = [1, 2, 3]
x = [a,n]
print(x)
print(x[0]) # The value in the fisrt place of x
print(x[0][1]) # THe value in the second place of x[0]





