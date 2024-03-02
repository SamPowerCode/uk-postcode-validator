import re

def format_uk_postcode():
    # last 3 characters are are always a digit followed two letters
    pass

def verify_uk_postcode():
    # verify with Code-Point Open https://api.os.uk/downloads/v1/products/CodePointOpen/downloads?area=GB&format=CSV&redirect
    pass

def validate_uk_postcode(postcode):
    # regex from https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    regex = r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
    if re.match(regex, postcode, re.IGNORECASE):
        print(f"'{postcode}': is a valid UK postcode")
    else:
        print(f"'{postcode}': is not a valid UK postcode")
    
    # should return something like:
    # {
    #     "valid_uk_postcode": boolean,
    #     "verified_exists_on_uk_mainland": boolean,
    #     "input": user inputed postcode,
    #     "formatted": pretified input
    # }

if __name__ == "__main__":
    postcodes = ["SW1W 0NY2ER", "M1 1AA", "M60 1NW", "CR2 6XH", "DN55 1PT", "W1P 1HQ", "EC1A 1BB", "SW12 2ER", "sw12 2ER", "sdfgsd"]
    for pc in postcodes:
        validate_uk_postcode(pc)

# Formatting too!!!
