def add_username_to_file(username):
    file = open('data.txt', 'a')
    file.write(username + '\n')
    file.close()
    print("filewite")