"""
===============================================================================
PROGRAMMING AND DESIGN PRINCIPLES
Skills Demo 2: Word Length Analysis
===============================================================================

Module Codes: 5N2927 Programming Design Principles

Dundrum College of Further Education

===============================================================================

Introduction

In this skills demo, you'll build a language predictor based on word length
statistics. You'll analyze texts from three educational theorists - Dewey
(English), Montessori (Italian), and Freire (Portuguese) - to discover how
word length patterns can reveal a text's language.

What you will work on:
    - Extract and analyze word lengths from text
    - Calculate statistical measures (mean, median, distribution)
    - Visualize data with histograms
    - Create methods for measuring the distance between two texts
    - Build a language classifier

===============================================================================

Assessment Breakdown (Skills Demonstration 2 - 40%)

Your work will be assessed according to the following criteria:

    Criterion               Marks   What to Submit
    ---------               -----   --------------
    Algorithm                 8     Top-level algorithm (pseudocode/flowchart)
                                    with detailed breakdown for each task.
                                    Complete data dictionary listing all
                                    variables and their purposes.

    Accurate Programming     16     Working code that compiles. Appropriate
                                    data types. Correct use of functions with
                                    local/global variables. Parameter passing
                                    between functions. At least one function
                                    returning a value. Use of at least one
                                    system-defined function (e.g., len(),
                                    sum(), sorted()).

    Appropriate Testing       6     Test data table with expected outputs.
                                    Screenshots showing actual results match
                                    expected results.

    Industry Standards        5     Logical program structure. Meaningful
                                    comments. Consistent indentation. Clear
                                    input prompts and output labels.

    Team Participation        5     Evidence of each team member's contribution
                                    (who wrote which functions, meeting notes,
                                    Git commits, etc.).

    Total                    40

Team Structure

From Exercise 8 onwards, you will work in teams of 2-3 learners. Each team
member should:
    - Be responsible for at least one complete function
    - Participate in testing and debugging
    - Contribute to the final reflection

===============================================================================
"""


# ============================================================================
# Setup: Fetch Sample Texts
# ============================================================================
#
# NOTE: Make sure that the texts are in the /texts folder when you run this!
# You should expect one text called dewey, one text called montessori and
# one text called freire... later you will also have a text called secret.
#
# ============================================================================

# Load texts from files
with open('texts/dewey.txt', 'r', encoding='utf-8') as f:
    dewey_text = f.read()[:100000]

with open('texts/montessori.txt', 'r', encoding='utf-8') as f:
    montessori_text = f.read()[:100000]

with open('texts/freire.txt', 'r', encoding='utf-8') as f:
    freire_text = f.read()[:100000]


# Verify all texts loaded
print("=" * 50)
print("Sample Texts Loaded Successfully!")
print("=" * 50)
print(f"\nDewey (English):     {len(dewey_text):,} characters")
print(f"Montessori (Italian): {len(montessori_text):,} characters")
print(f"Freire (Portuguese):  {len(freire_text):,} characters")
print("\nFirst 200 characters of each:")
print(f"\nDewey: {dewey_text[0:200]}...")
print(f"\nMontessori: {montessori_text[0:200]}...")
print(f"\nFreire: {freire_text[0:200]}...")


# ============================================================================
# EXERCISE 1: Extract Word Lengths
# ============================================================================
#
# Your task: Write a function that takes text and returns a list of word
# lengths.
#
# The n-th entry in the list should be the length of the n-th word
# (starting from index 0).
#
# Example:
#     get_word_lengths("This is a really great sample sentence!")
#     -> returns: [4, 2, 1, 6, 5, 6, 8]
#
# ------------------------------------------------------------------------------

"""
Write your pseudocode here (you are welcome to also describe your steps in sentences)


"""

def get_word_lengths(text):
    """
    Extract the length of each word in a text.
    
    Args:
        text: String containing the text to analyze
        
    Returns:
        List of integers representing word lengths
    """
    # Your code here
    pass


# Write your own tests here (at least three test cases)



# ============================================================================
# EXERCISE 2: Word Length Distribution
# ============================================================================
#
# Your task: Count how many words have each length (1, 2, 3, etc.).
#
# You are welcome to return either a dictionary or a list.
#
# ------------------------------------------------------------------------------

"""
Write your pseudocode here (you are welcome to describe the steps in sentences)


"""

def word_length_distribution(text):
    """
    Count how many words have each length.
    
    Args:
        text: String containing the text to analyze
    
    Returns:
        You decide:
        Dictionary mapping length to count, e.g. {1: 3, 2: 5, 3: 8, ...}
        OR a list where index represents word length
    """
    # Your code here
    pass


# Write your own tests here (at least three test cases)



# ============================================================================
# EXERCISE 3: Create Histograms / Bar Charts
# ============================================================================
#
# Your task: Visualize the word length distribution as a histogram/bar chart.
# Label your charts and axes and give your plots suitable names.
#
# ------------------------------------------------------------------------------

def plot_histogram(distribution, title):
    """Create a bar chart of word lengths."""
    # Your code here
    pass


# Create histogram for Dewey (English)



# Create histogram for Montessori (Italian)



# Create histogram for Freire (Portuguese)



# ============================================================================
# EXERCISE 4: Percentage Distribution
# ============================================================================
#
# Your task: Convert raw counts to percentages. This makes texts of different
# lengths comparable.
#
# ------------------------------------------------------------------------------

"""
Write a description of your process here (you are welcome to describe your steps in sentences)


"""

def percentage_distribution(text):
    """
    Calculate percentage of words at each length.
    
    Returns:
        Dictionary or list where values are percentages (0-100)
        Example: if result[4] = 15.5, then 15.5% of words have length 4
    """
    # Your code here
    pass


# Write your own tests here (hint: what should the percentages sum to?
# Note it might not be exact due to rounding...)



# ============================================================================
# END OF DAY 1
# ============================================================================
#
# Please submit what you have up to this point on Moodle by 1pm today.
# You are welcome to continue if you have time, after you submit.
# Tomorrow we will continue on to Day 2 and you will be allocated into groups.
#
# ============================================================================


# ============================================================================
# DAY 2: Comparing Texts
# ============================================================================
#
# Having built tools to analyze individual texts, we now turn to comparison:
# how can we measure whether two texts are similar?
#
# For the remainder of this skills demo, you will work in groups of 2 or 3.
#
# ============================================================================


# ============================================================================
# EXERCISE 5: Compare Statistics (Basic Method)
# ============================================================================
#
# Your task: Calculate how "similar" two texts are based on their statistics.
# Feel free to use the statistics library or list functions to help you.
#
# Core Idea:
#     1. Find the difference in averages
#     2. Find the difference in medians
#     3. Add the absolute values of these differences
#     4. Return total distance
#
# ------------------------------------------------------------------------------

"""
Write your pseudocode here



"""

def compare_statistics(text1, text2):
    """
    Calculate distance between two texts using average and median.
    
    Returns:
        Float representing distance (smaller = more similar)
    """
    # Your code here
    pass


# Write your own tests



# Optional extension: Incorporate the mode into your distance calculation.



# ============================================================================
# EXERCISE 6: Mean Squared Error Distance (Advanced Method)
# ============================================================================
#
# Your task: Create a function that calculates the Mean Squared Error between
# the percentage distributions of two texts.
#
# Formula:
#     MSE = (1/n) * sum of (p_i - q_i)^2
#
# Where:
#     p_i is the percentage of words with length i in text 1
#     q_i is the percentage of words with length i in text 2
#     n is the number of different word lengths being compared
#
# Pseudocode:
#     1. Get percentage distribution for text 1
#     2. Get percentage distribution for text 2
#     3. For each word length, calculate (percentage1 - percentage2)^2
#     4. Sum all squared differences
#     5. Divide by the number of word lengths compared
#     6. Return MSE
#
# ------------------------------------------------------------------------------

def mean_squared_error(text1, text2):
    """
    Calculate MSE between percentage distributions of two texts.
    
    Returns:
        Float representing MSE (smaller = more similar)
    """
    # Your code here
    pass


# Write your own tests



# ============================================================================
# EXERCISE 7: Build and Evaluate Language Predictor
# ============================================================================
#
# Your task: Predict the language of a sample text, then evaluate how well
# your predictor works.
#
# Pseudocode:
#     1. Calculate distance from sample to English reference
#     2. Calculate distance from Italian reference
#     3. Calculate distance from Portuguese reference
#     4. Return language with smallest distance
#
# ------------------------------------------------------------------------------

def predict_language(sample_text, english_ref, italian_ref, portuguese_ref):
    """
    Predict the language of a sample text.
    
    Args:
        sample_text: Text to classify
        english_ref: Reference text in English
        italian_ref: Reference text in Italian
        portuguese_ref: Reference text in Portuguese
        
    Returns:
        String: "English", "Italian", or "Portuguese"
    """
    # Your code here
    pass


# ============================================================================
# EXERCISE 8: Group Evaluation Tasks
# ============================================================================


# --------------------------------------------------------------------------
# 1. Test your predictor with sample texts in each language. Does it work?
# --------------------------------------------------------------------------

# Test with sample texts in each language, you are welcome to take a small
# section of each text as a sample, or use new texts entirely.



# Feel free to use the secret text provided (secret_text.txt) to test your
# language prediction function. For this you will need the following code
# to load the text into the variable secret_text:

# with open('texts/secret.txt', 'r', encoding='utf-8') as f:
#     secret_text = f.read()[:100000]



# --------------------------------------------------------------------------
# 2. How many words does a sample need for accurate prediction?
#    Test with different sizes: 10 words, 50 words, 100 words, 500 words,
#    1000 words, 5000 words.
# --------------------------------------------------------------------------

# Test with different sample sizes



# --------------------------------------------------------------------------
# 3. Based on your tests what language is this text in?
#
#    Note, the point is not to guess correctly, the point is to evaluate
#    what your tests give you... how large a sample do you need to be sure
#    your test is accurate? What might cause it to fail?
# --------------------------------------------------------------------------




# --------------------------------------------------------------------------
# 4. Which pair of languages is hardest to distinguish? Which is easiest?
# --------------------------------------------------------------------------

# Compare distances between language pairs



# --------------------------------------------------------------------------
# 5. Compare the basic method (Exercise 5) with MSE (Exercise 6).
#    Which performs better?
# --------------------------------------------------------------------------

# Compare basic vs MSE methods



# ============================================================================
# FINAL REFLECTION
# ============================================================================
#
# 6. Write two brief paragraphs reflecting on:
#
#    1. Surprising findings: What surprised you about word length patterns?
#    2. Design decisions: What was your most important design decision?
#    3. Limitations: What are the limitations of this approach?
#    4. Improvements: How would you improve the predictor?
#    5. Statistics: Did the distributions between languages look very
#       different? What sample size proved to be necessary? What assumptions
#       did we make about our sample text.
#
# Write your reflection here:
#
#
#
#
# ============================================================================


# ============================================================================
# End of Skills Demo
# ============================================================================
