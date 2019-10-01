import math


def letter_freq(message):
    lower_txt = message.lower()
    single_item = [item for item in lower_txt]

    return dict((item, single_item.count(item)) for item in single_item)


def entropy(message):
    number_of_letters = len(message)

    count_dict = letter_freq(message)
    occurences = dict()
    frequency = dict()
    entro = 0

    for code in range(256):

        if chr(code) in count_dict:
            occurences[code] = count_dict[chr(code)]
            frequency[code] = occurences[code] / number_of_letters
            entro -= frequency[code] * math.log2(frequency[code])

        else:
            frequency[code] = 0

    return entro


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
