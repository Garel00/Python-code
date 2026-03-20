with open('pi.txt') as file_object:
    contents = file_object.read()
    print(contents)
    pi_string = contents.rstrip()

print(pi_string)
print(len(pi_string))
