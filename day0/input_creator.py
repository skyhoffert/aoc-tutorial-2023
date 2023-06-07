
# Let's use python's random library for this problem. It provides an easy way to generate random-ish numbers.
import random

# Start by opening a file with python's built-in "open" function.
# "open" takes 2 arguments, first is a file name, second is how it should be opened.
# In this case, we want to open the file "input.txt".
# "w" means "write mode" which allows us to write to the file.
# Sometimes you want to read a file - for that you would use "r" instead of "w".
# This function returns a "file" object that has some useful functions.
fout = open("input.txt", "w")

# Let's keep track of how many lines we've written to the file.
number_written = 0

# The most straightforward way to do this is with a loop. Let's start with a while loop for now.
# A good condition for this loop would be to check the number of lines written until we reach some value.
# I'm feeling.... 10,000 lines.... sounds good! The condition "number_written < 10000" will test that.
# But we have to remember to add to the "numeber_written" variable every time.
while number_written < 10000:

    # Write takes a string argument. To keep this simple, let's build a string first.
    # Start with an empty string.
    out_string = ""

    # Now, let's append a random integer to this string. We can use the "random.randint" function.
    # random.randint takes 2 arguments, first is the lowest possible value, second is the highest possible value.
    out_string = out_string + random.randint(-100,100)

    # That's great, but the list format should have one value per line.
    out_string = out_string + "\n"

    # On second thought, I think this would be more clear on a single line. Let's try like this:
    out_string = "" + random.randint(-100,100) + "\n"

    # To write to a file opened with "w", we can use the "write" function of the "fout" object.
    # Simple provide write the string we wish to write.
    fout.write(out_string)

    # Oh, don't forget to keep track of how many lines were written!
    number_written = number_written + 1

# And good practice is to close a file that was opened previously.
fout.close()
