import numpy as np

def practice_1_review():
    """
    Quick Review Exercise: Array Operations
    Warm up with what you know!
    """
    print("\n" + "="*50)
    print("REVIEW EXERCISE: Array Basics")
    print("="*50)
    
    # Given array of temperatures
    temps = np.array([68, 72, 75, 71, 77, 73, 70])    
    print("This week's temperatures:", temps)
    
    # TODO 1: Add 5 degrees to all temperatures (heat wave!)
    heat_wave = temps+5 # Replace with temps + 5

    # TODO 2: Convert to Celsius: C = (F - 32) * 5/9
    celsius = (temps - 32) *5 /9 # Replace with (temps - 32) * 5/9

    # TODO 3: Find temperatures above 72
    warm_days = temps > 72 # Replace with temps > 72

    print(f"Heat wave temps: {heat_wave}")
    print(f"In Celsius: {celsius}")
    print(f"Days above 72°F: {warm_days}")
    print(f"Number of warm days: {np.sum(warm_days) if warm_days is not None else '?'}")

# Run the review
practice_1_review()