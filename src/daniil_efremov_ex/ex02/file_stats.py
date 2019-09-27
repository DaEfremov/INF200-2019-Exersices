def char_counts(textfilename):
    with open(textfilename, 'r') as file:
        data = file.read()
    result = []

    for kode in range(256):
        if chr(kode) in data:
            result.append(data.count(chr(kode)))
        else:
            result.append(0)

    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
