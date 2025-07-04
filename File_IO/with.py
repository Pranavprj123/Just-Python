with open("pran.txt", "r") as f:  #contet manager 
    content = f.read()
    print(content)

    # No need to write f.close() it automatically closes the file after the block