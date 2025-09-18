def practice_4a_beginner():
    """
    Beginner: Format personal information
    """
    print("\n" + "="*50)
    print("EXERCISE 4A: Info Formatter (Beginner)")
    print("="*50)
    # Personal information
    name = "John Doe"
    age = 25
    height = 5.9 # feet
    weight = 170.5 # pounds
    # TODO 1: Create f-string with name and age
    # Format: "Name: John Doe, Age: 25"
    info1 = f"Name: {name}, Age: {age}" # Replace with f"Name: {name}, Age: {age}"
    # TODO 2: Format height to 1 decimal place
    # Format: "Height: 5.9 feet"
    info2 = f"Height: {height:.1f}" # Replace with f"Height: {height:.1f} feet"
    # TODO 3: Format weight to no decimal places
    # Format: "Weight: 171 lbs"
    info3 = f"Weight: {weight:.0f}" # Replace with f"Weight: {weight:.0f} lbs"
    print(info1)
    print(info2)
    print(info3)
# Run the exercise
practice_4a_beginner()
def practice_5a_beginner():
    """
    Beginner: Extract parts of strings
    """
    print("\n" + "="*50)
    print("EXERCISE 5A: String Extraction (Beginner)")
    print("="*50)
    # Full name
    full_name = "John Michael Smith"
    print(f"Full name: {full_name}")
    # TODO 1: Get the first name (first 4 characters)
    # Use: full_name[:4]
    first_name = full_name[:4] # Replace None
    # TODO 2: Get the last name (last 5 characters)
    # Use: full_name[-5:]
    last_name = full_name[-5:] # Replace None
    # Email address
    email = "user@example.com"
    print(f"\nEmail: {email}")
    # TODO 3: Get username (everything before @)
    # Find @ position first
    at_position = email.find("@")
    username = email[:at_position] # Replace with email[:at_position]
    # TODO 4: Get domain (everything after @)
    domain = email[at_position+1:] # Replace with email[at_position+1:]
    print(f"\nExtracted from name:")
    print(f" First name: {first_name}")
    print(f" Last name: {last_name}")
    print(f"\nExtracted from email:")
    print(f" Username: {username}")
    print(f" Domain: {domain}")
# Run the exercise
practice_5a_beginner()