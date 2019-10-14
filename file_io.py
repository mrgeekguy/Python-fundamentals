new_file = open("./file_io_hub/testing.txt", "x")

new_file.write("Hello world!")

new_file.close()

# Challenge
# Create Python file that itself modifies the testing.txt file to say
# I'm sorry, I cannot do that

python_file = open("./file_io_hub/change_text.py", "x")

valid_code = """

to_change = open("./testing.txt", "w")
to_change.write("I'm sorry I cannot do that")
to_change.close()

"""

python_file.write(valid_code)

# better way

# with open("with_statement.py", "w") as f:
#    f.write("# I'm a comment\nprint("Hello World")")

