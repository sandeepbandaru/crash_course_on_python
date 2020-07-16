"""
Conditionals Cheat Sheet
In earlier videos, we took a look at some of the built-in Python operators that allow us to compare values, and some logical operators we can use to combine values. We also learned how to use operators in if-else-elif blocks. 

It’s a lot to learn but, with practice, it gets easier to remember it all. In the meantime, this handy cheat sheet gives you all the information you need at a glance. 

Comparison operators
a == b: a is equal to b
a != b: a is different than b
a < b: a is smaller than b
a <= b: a is smaller or equal to b
a > b: a is bigger than b
a >= b: a is bigger or equal to b
Logical operators
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True. False if both are False.
not a: True if a is False, False if a is True.
"""

#------------------------------------------------------	
#Practice Quiz: Conditionals

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

#------------------------------------------------------
#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size//filesize
   
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = block_size%filesize

    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 8192
    else:    
       return 4096

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

