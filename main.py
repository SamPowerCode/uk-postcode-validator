import re
import json
import requests
from io import BytesIO, TextIOWrapper
import zipfile
import csv

# TODO remove print statments
# TODO check if postcode is NI
# TODO update README.md
# TODO sort imports
# TODO make requirments.txt
# TODO add tests

def format_uk_postcode():
    # TODO remove any non alpha numeric charactors
    
    # last 3 characters are are always a digit followed two letters
    pass

def verify_uk_postcode(postcode='SW1W 0NY'):
    # TODO move request to it's own method
    # TODO add try expect for request
    url = "https://api.os.uk/downloads/v1/products/CodePointOpen/downloads"
    response = requests.get(url)

    if response.status_code == 200:
        for item in json.loads(response.content.decode('utf-8')):
            if item['format'] == 'CSV':
                csv_url = item['url']
    else:
        print("blah blah blah")

    response = requests.get(csv_url)
    # check if the request was successful
    if response.status_code == 200:
        # read the content of the response into a BytesIO object
        zip_data = BytesIO(response.content)
        
        # create a ZipFile object using the BytesIO object
        with zipfile.ZipFile(zip_data, 'r') as zip_ref:
            # gets a list of all files in the zip
            file_list = zip_ref.namelist()
            # find area code in postcode
            area_code = postcode[:2].lower()
            # find the csv with the area code we're looking for
            csv_file_path = [x for x in file_list if f'{area_code}.csv' in x.lower()]
            
            # open the CSV file within the zip file
            with zip_ref.open(csv_file_path[0]) as csv_file:
                # covnert from binary to text do we can parse it easily
                csv_file_text = TextIOWrapper(csv_file, encoding='utf-8')
                # read the CSV file into memory
                csv_data = csv.reader(csv_file_text)
                
                # loop through csv to check if postcode exists 
                for row in csv_data:
                    if postcode in row[0]:
                        return True
    else:
        # TODO add try/except here
        print("Failed to download zip file")
    
    return False

def validate_uk_postcode(postcode):
    # regex from https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
    regex = r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
    if re.match(regex, postcode, re.IGNORECASE):
        print(f"'{postcode}': is a valid UK postcode")
    else:
        print(f"'{postcode}': is not a valid UK postcode")
    
    # TODO should return something like:
    # {
    #     "valid_uk_postcode": boolean,
    #     "verified_exists_on_uk_mainland": boolean,
    #     "input": user inputed postcode,
    #     "formatted": pretified input
    # }

if __name__ == "__main__":
    postcodes = ["SW1W 0NY2ER", "M1 1AA", "M60 1NW", "CR2 6XH", "DN55 1PT", "W1P 1HQ", "EC1A 1BB", "SW1W 0NY", "sw12 2ER", "sdfgsd"]
    # for pc in postcodes:
    #     validate_uk_postcode(pc)
    print(verify_uk_postcode(postcode='SW1W 0NsY'))
