import re

# TODO update README.md

def format_uk_postcode(postcode):
    postcode = ''.join(character for character in postcode if character.isalnum())
    postcode = f'{postcode[:-3]} {postcode[-3:]}'

    return postcode.upper()

def validate_uk_postcode(postcode):
    # regex taken from https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    regex = r'^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$'
    
    if re.match(regex, postcode, re.IGNORECASE):
        return True
    else:
        return False

if __name__ == '__main__':
    postcode = 'aa9a9aa'
    print(f'{postcode} formated to {format_uk_postcode(postcode)}')
    print(f'{postcode} returned {validate_uk_postcode(postcode)} as a valid postcode')
    print(f'foobar returned {validate_uk_postcode("foobar")} as a valid postcode')
