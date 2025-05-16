import re

# 1. Email will extract emails with pattern user@example.com or user@example.com.uk
def extract_email(text):
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(email_pattern, text)

# 2. Phone number will extract phone numbers with pattern (123) 456-7890, 123-456-7890 and 123.456.7890
def extract_phonenbr(text):
    nbr_pattern = r'(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}'
    return re.findall(nbr_pattern, text)
# 3. Hashtag will extract hashtags with pattern #example
def extract_hashtag(text):
    hash_pattern = r'#\w+'
    return re.findall(hash_pattern, text)
    
# 4. Time extracts time in 24-hour and 12-hour format (with optional AM/PM)
def extract_time(text):
    time_pattern = r'\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?:\s?[APap][Mm])?\b'
    return re.findall(time_pattern,text)

if __name__ == "__main__":
    text = """
    Email me at ralph@mail.com or anyexmample@industry.co.rw
    My numbers are (567) 456-7890, 078-234-3344 and 123.999.7890
    Meet me at 14:30, or maybe at 2:30 PM or 11:45 am.
    Trending hashtags: #Goat #RegexRocks #Gunna
    """

    print("1. Extracted Emails ==")
    print(extract_email(text))
    
    print("\n2. Extracted Phone Numbers ==")
    print(extract_phonenbr(text))
    
    print("\n3. Extracted Hashtags ==")
    print(extract_hashtag(text))
    
    print("\n4. Extracted Time Formats ==")
    print(extract_time(text))
