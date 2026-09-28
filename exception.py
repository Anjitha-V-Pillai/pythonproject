def file_close():
    f.close()


def file_append():
    filename = input("Enter filename")
    f = open(filename, 'a')
    content = input("Enter the content")
    f.write(content)
    f.close()


def file_search():
    filename = input("Enter filename")
    f = open(filename, 'r')
    s = f.read()

    word = input("Enter the file to be searched")

    if word in s:
        print("Word", word, "is present")
    else:
        print("Word", word, "is not present")

    f.close()


def file_delete():
    import os