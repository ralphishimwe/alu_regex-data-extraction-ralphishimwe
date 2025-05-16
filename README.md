## Regex Data Extraction "alu_regex-data-extraction-ralphishimwe"

This project demonstrates the use of Python's Regular Expressions module to extract structured data from raw text. The script extracts: Email
addresses, phone numbers, hashtags and time formats in 12 hour and 24 hour format.


## File Structure

regex_extractor.py 
README.md 


## How to Run the Script

1. Clone this repository or download the files.

git clone https://github.com/ralphishimwe/alu_regex-data-extraction-ralphishimwe
cd alu_regex-data-extraction-ralphishimwe
Run the Python script:

python3 regex_extractor.py

## Sample Input & Output
Input:

Email me at ralph@mail.com or anyexmample@industry.co.rw
My numbers are (567) 456-7890, 078-234-3344 and 123.999.7890
Meet me at 14:30, or maybe at 2:30 PM or 11:45 am.
Trending hashtags: #Goat #RegexRocks #Gunna

## Output - Extracted Data Types
1. Email Addresses
Matches standard emails like:
- `user@example.com` - `anyone@domain.co.rw`
2. Phone Numbers
Handles multiple formats:
- `(123) 456-7890` - `078-234-3344` - `123.999.7890`
3. Hashtags
Captures social-style hashtags:
- `#RegexRocks` - `#Gunna`
4. Time Formats
Detects time in:
- `14:30` (24-hour) - `2:30 PM` / `11:45 am` (12-hour, case-insensitive)
