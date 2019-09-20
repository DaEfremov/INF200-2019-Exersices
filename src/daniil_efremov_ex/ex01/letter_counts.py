def letter_freq(txt):
    txt.lower()
    single_item = [item for item in txt]

    return dict((item, single_item.count(item)) for item in single_item)


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
