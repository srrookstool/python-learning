import re

def format_receipt(items, prices, quantities):
    print("=" * 40)
    print(f"{"Item":<20} {"Qty":^5} {"Price":>8}")
    print("="*40)
    for item,price,quantity in zip(items, prices, quantities):
        print(f"{item:<20} {quantity:^5} {"$":>4} {price:>4.2f}")
    print("=" * 40)
    print(f"{"TOTAL":<20} {"$":>10} {sum(prices):>4.2f}")
    print("=" * 40)
items = ["Coffee", "Sandwich", "Cookie"]
prices = [3.50, 8.99, 2.00]
quantities = [2, 1, 3]
print(format_receipt(items, prices, quantities))

def process_user_data(raw_data):
    cleaned_name = raw_data['name'].strip().title()
    cleaned_email= raw_data['email'].lower().replace(" ","")
    cleaned_phone= ""
    for x in raw_data['phone']:
        if x.isnumeric():
            cleaned_phone += x
    cleaned_address="".join(raw_data['address'].split()).title()
    namelist = cleaned_name.lower().split()
    username= namelist[0] + "_" + namelist[1]
    return {'name':cleaned_name,'email':cleaned_email,'phone':cleaned_phone,'address':cleaned_address,'username':username}

data = {
    'name': ' john DOE ',
    'email': ' JOHN.DOE @EXAMPLE.COM ',
    'phone': '(555) 123-4567',
    'address': '123 main street, apt 5'
    }
result = process_user_data(data)
print(result['name'],result['email'],result['phone'],result['username'])

def analyze_text(text):
    """
    Perform comprehensive text analysis using string methods.
    Args:
    text: Multi-line string of text
    Returns:
    dict: Analysis results containing:
    - 'total_chars': Total character count
    - 'total_words': Total word count
    - 'total_lines': Number of lines
    - 'avg_word_length': Average word length (rounded to 2 decimal)
    - 'most_common_word': Most frequently used word (case-insensitive)
    - 'longest_line': The longest line in the text
    - 'words_per_line': List of word counts per line
    - 'capitalized_sentences': Number of sentences starting with capital
    - 'questions': Number of sentences ending with '?'
    - 'exclamations': Number of sentences ending with '!'
    Example:
    >>> text = '''Hello world! How are you?
    ... This is a test. Another line here!'''
    >>> result = analyze_text(text)
    >>> result['total_words']
    11
    >>> result['questions']
    1
    """
    
def find_patterns(text):
    """
    Find basic patterns in text using regex.
    Args:
    text: String to search
    Returns:
    dict: Found patterns:
    - 'integers': List of all integers
    - 'decimals': List of all decimal numbers
    - 'words_with_digits': Words containing digits
    - 'capitalized_words': Words starting with capital letter
    - 'all_caps_words': Words in all capitals (min 2 chars)
    - 'repeated_chars': Words with repeated characters (aa, ll, etc.)
    Example:
    >>> text = "I have 25 apples and 3.14 pies. HELLO W0RLD!"
    >>> result = find_patterns(text)
    >>> result['integers']
    ['25']
    >>> result['decimals']
    ['3.14']
    >>> result['all_caps_words']
    ['HELLO']
    >>> result['words_with_digits']
    ['W0RLD']
    """
    patterns = {
    'integers': r'\d+', # Fill in pattern
    'decimals': r'\d\.\d', # Fill in pattern
    'words_with_digits': r'\w*\d\w*', # Fill in pattern
    'capitalized_words': r'^[A-Z][a-z]+', # Fill in pattern
    'all_caps_words': r'[A-Z]+', # Fill in pattern
    'repeated_chars': r'(\w)\1+' # Fill in pattern
    }
    # Your code here