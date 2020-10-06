def determine_time_class(numbers, limit):
    numbers = sorted(numbers)
    times = [numbers[0]]
    split_point = None
    for i in numbers[1:]:
        if i <= (sum(times)/len(times))*limit:
            times.append(i)
        else:
            split_point = min(split_point or 9999999, i)

    return split_point

def determine_time_classes(ons, offs):
    ons=sorted(ons)
    offs=sorted(offs)
    dah_limit = determine_time_class(ons, 2)
    letter_separator_limit = determine_time_class(offs, 2)
    word_separator_limit = determine_time_class(offs[offs.index(letter_separator_limit):], 2)
    return dah_limit, letter_separator_limit, word_separator_limit

def lex_sequence(times):
    dah_limit, letter_separator_limit, word_separator_limit = determine_time_classes(times[::2], times[1::2])
    print(dah_limit, letter_separator_limit, word_separator_limit)
    on = True
    tokens = []
    for time in times:
        if on:
            if time >= (dah_limit or 1000000000):
                tokens.append('dah')
            else:
                tokens.append('dit')
        else:
            if time >= (word_separator_limit or 9999999):
                tokens.append('word_separator')
            elif time >= (letter_separator_limit or 9999999):
                tokens.append('letter_separator')
        on = not on
    return tokens

def parse_sequence(times):
    sequence = lex_sequence(times)
    morse = ['']
    for token in sequence:
        if token == 'dah':
            morse[-1] += '-'
        elif token == 'dit':
            morse[-1] += '.'
        elif token == 'letter_separator':
            morse.append('')
        elif token == 'word_separator':
            morse.append('')
            morse.append('')
    while morse[-1] == '':
        morse.pop()
    return morse
