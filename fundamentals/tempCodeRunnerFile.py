#------------ Nested List : 3D Array -----------------------------------------------------------------------------------------------------------------#
"""
In Python, you can represent a 3D array using nested lists. A 3D array is essentially a list of lists of lists. Here's an example to illustrate:
Imagine you want to represent a 3x3x3 3D array, where each element can be identified by three indices: [i][j][k].

"""

array_3d = [
    [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ],       # First 2D array
    [ [10, 11, 12], [13, 14, 15], [16, 17, 18] ], # Second 2D array
    [ [19, 20, 21], [22, 23, 24], [25, 26, 27] ]  # Third 2D array
]

print(array_3d[2][1][0] ) #prints 22 

"""

In this array_3d:

array_3d[0] would give you the first 2D array.
array_3d[1][2] would access the third row of the second 2D array.
array_3d[2][1][0] would access the first element of the second row of the third 2D array (which is 22).

This is a simple representation, and you can access and manipulate elements just like you would with any nested list structure. 
Keep in mind that while this is a conceptually straightforward way to represent a 3D array in Python, it may not be the most efficient for large datasets or complex operations. 
For more advanced numerical computations, you might want to use libraries like NumPy, which provide optimized and more feature-rich array types.


"""