import file

list = file.nouvelle_file()

file.enfiler(list, 10)
file.enfiler(list, 11)
file.enfiler(list, 12)
file.enfiler(list, 13)

file.defiler(list)

print(list)