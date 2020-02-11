"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
filename = 'src/foo.txt'

with open(filename) as f:
    contents = f.read()
print(contents)

#! IMPORTANT !
"""
I chose not to use close() because of the following reasons:
if a bug in your program prevents the close() method from being executed, the file may never close.
This may seem trivial, but improperly closed files can cause data to be lost or
corrupted. And if you call close() too early in your program, you’ll find
yourself trying to work with a closed file (a file you can’t access), which leads
to more errors. It’s not always easy to know exactly when you should close a
file, but with the structure shown here, Python will figure that out for you.
All you have to do is open the file and work with it as desired, trusting that
Python will close it automatically when the with block finishes execution.

"""

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

new_filename = 'bar.txt'

with open(new_filename, 'w') as f:
    f.write(
        "Sally, take my hand \n Travel south cross land \n Put out the fire \n Don't look past my shoulder \n"
    )
