def bubble_sort(some_data):
    dat = list(some_data)
    len_string = len(dat) - 1

    for i in range(len_string):

        for j in range(len_string - i):
            if dat[j] > dat[j + 1]:
                dat[j], dat[j + 1] = dat[j + 1], dat[j]

    return dat


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
