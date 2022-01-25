with open("my_file.txt", mode="r") as file:
    # contents = file.read()
    # print(contents)

    # in "w" mode: Deletes all content and writes.
    # in "a" mode: Appends the text.
    file.write("\nNew text.")

    # in "w" mode, if a file doesn't exists,
    # it will create a new file and write to it.


    # Absolute file path: (root)/Documents/workspace/python ...
    # Relative file path: ./lecture-notes.py (look at the current folder) 
    #                     ../../day-24 -> up two levels and in day-24 folder

