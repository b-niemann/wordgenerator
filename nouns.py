with open('fileutf-8.txt', 'r') as file:
    with open('nouns10000.txt', 'w') as outputfile:

    count = 0
    for line in file:
        word = line.split()[0]
        if word != '#' and word[0].isupper() and not word.isupper() and count < 10000:
            print(str(count) + word)
            outputfile.write(word + '\n')
            count += 1
