# UK Postcode Validator
A simple script that validates and formats a UK postcode

An example of how you could run the code might be:

```python
from main import format_uk_postcode, validate_uk_postcode
postcode = 'aa9a9aa'
print(f'{postcode} formated to {format_uk_postcode(postcode)}')
print(f'{postcode} returned {validate_uk_postcode(postcode)} as a valid postcode')
print(f'foobar returned {validate_uk_postcode("foobar")} as a valid postcode')
```
Returns the following:
```
aa9a9aa formated to AA9A 9AA
aa9a9aa returned True as a valid postcode
foobar returned False as a valid postcode
```

Tests can be run with following in a terminal window:

```bash
python test_main.py
```
