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

import os
import statistics

import matplotlib
matplotlib.use("Agg")  # no display is available when this script runs headlessly
import matplotlib.pyplot as plt


# ============================================================================
# Setup: Fetch Sample Texts
# ============================================================================
#
# NOTE FOR INSTRUCTORS: the code below expects real excerpts in a texts/
# folder: texts/dewey.txt (English), texts/montessori.txt (Italian), and
# texts/freire.txt (Portuguese). This repository does not ship that folder,
# and it has been left that way on purpose rather than guessed at: Dewey's
# "Democracy and Education" is public domain and available from Project
# Gutenberg, and a public-domain Montessori text in Italian would work well
# too, but Freire's major works are still under copyright (published 1968 and
# later), so pasting an excerpt here would not be appropriate. Please choose
# and supply your own copyright-appropriate excerpts for texts/dewey.txt,
# texts/montessori.txt and texts/freire.txt so the exercise runs against real
# source material.
#
# Until a texts/ folder is supplied, the three short synthetic strings below
# (written for this script, not quoted from any real author) let the rest of
# the file run and be inspected out of the box. They are only there to keep
# the statistics and classifier logic exercised; they are not a substitute
# for real source texts.
#
# ============================================================================

FALLBACK_ENGLISH_TEXT = """
Learning happens best when a student feels safe enough to ask a real question
and patient enough to sit with an answer that is not yet complete. A good
teacher builds routines that make room for both quiet practice and open
exploration, so that skills and curiosity grow together rather than apart.

A classroom is a small community before it is anything else. Rules matter
less than trust, and trust is built slowly, through small consistent acts:
showing up, listening well, admitting a mistake, trying again. Over time,
these habits shape how a person learns for the rest of their life, far past
any single course or exam.

None of this happens by accident. It takes careful planning, honest
reflection, and a willingness to change course when something is clearly not
working for the people in the room.
"""

FALLBACK_ITALIAN_TEXT = """
L'educazione non e qualcosa che un insegnante fa a uno studente; nasce da
un'esperienza condivisa e da un'attenzione sincera verso cio che una persona
porta gia dentro l'aula. Una buona scuola costruisce spazio per la curiosita
insieme alla struttura, cosicche i bambini possano mettere alla prova le
proprie idee nel mondo reale invece di memorizzare semplici risposte.

Una classe e prima di tutto una piccola comunita. Le regole contano meno
della fiducia, e la fiducia si costruisce lentamente, attraverso piccole
azioni costanti: essere presenti, ascoltare con attenzione, riconoscere un
errore, riprovare ancora. Con il tempo, queste abitudini formano il modo in
cui una persona impara per il resto della propria vita.

Niente di tutto questo accade per caso. Richiede una pianificazione attenta,
una riflessione onesta e la volonta di cambiare strada quando qualcosa
evidentemente non funziona per le persone presenti nella stanza.
"""

FALLBACK_PORTUGUESE_TEXT = """
A educacao nao e algo que um professor faz a um estudante; ela nasce de uma
experiencia partilhada e de uma atencao verdadeira aquilo que uma pessoa ja
traz para a sala. Uma boa escola cria espaco para a curiosidade junto com a
estrutura, para que as criancas possam testar as suas proprias ideias no
mundo real, em vez de memorizar respostas simples.

Uma sala de aula e, antes de mais nada, uma pequena comunidade. As regras
importam menos do que a confianca, e a confianca constroi-se devagar, atraves
de pequenas acoes constantes: estar presente, escutar com atencao, reconhecer
um erro, tentar outra vez. Com o tempo, esses habitos moldam a forma como uma
pessoa aprende para o resto da vida.

Nada disto acontece por acaso. Exige um planeamento cuidadoso, uma reflexao
honesta e a vontade de mudar de rumo quando algo claramente nao esta a
funcionar para as pessoas presentes na sala.
"""


def _load_text_with_fallback(filepath, fallback_text, label):
    """Load a text file if it exists; otherwise fall back to a short synthetic
    demo string so the rest of the script can still run without a texts/
    folder present. See the note above for what real file belongs here."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()[:100000]
    except FileNotFoundError:
        print(
            f"NOTE: '{filepath}' not found -- using a short synthetic {label} "
            f"demo string instead. See the note near the top of this file for "
            f"what real file an instructor should supply here."
        )
        return fallback_text.strip()


# Load texts from files, or fall back to the synthetic strings above
dewey_text = _load_text_with_fallback("texts/dewey.txt", FALLBACK_ENGLISH_TEXT, "English")
montessori_text = _load_text_with_fallback("texts/montessori.txt", FALLBACK_ITALIAN_TEXT, "Italian")
freire_text = _load_text_with_fallback("texts/freire.txt", FALLBACK_PORTUGUESE_TEXT, "Portuguese")


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

1. Split the text into individual words, treating anything that is not a
   letter (spaces, punctuation, newlines) as a separator between words.
2. For each word, measure its length in characters.
3. Return the lengths as a list, in the same order the words appeared in
   the text, since later exercises rely on words and lengths lining up.
"""

def get_word_lengths(text):
    """
    Extract the length of each word in a text.

    Args:
        text: String containing the text to analyze

    Returns:
        List of integers representing word lengths
    """
    # A "word" here is a run of letters (accented letters included, since our
    # texts may be in Italian or Portuguese) or apostrophes, e.g. "don't".
    # Anything else -- spaces, newlines, punctuation, digits -- separates words.
    words = []
    current_word = ""
    for character in text:
        if character.isalpha() or character == "'":
            current_word += character
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
    if current_word:
        words.append(current_word)

    return [len(word) for word in words]


# Write your own tests here (at least three test cases)
assert get_word_lengths("This is a really great sample sentence!") == [4, 2, 1, 6, 5, 6, 8]
assert get_word_lengths("") == []
assert get_word_lengths("One, two, three!") == [3, 3, 5]
assert get_word_lengths("Don't stop") == [5, 4]
print("\nExercise 1 tests passed.")


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

1. Get the list of word lengths for the text (reusing Exercise 1).
2. Start with an empty dictionary mapping length -> count.
3. For each length in the list, add one to that length's count, starting
   the count at zero the first time a length is seen.
4. Return the dictionary.
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
    lengths = get_word_lengths(text)
    distribution = {}
    for length in lengths:
        distribution[length] = distribution.get(length, 0) + 1
    return distribution


# Write your own tests here (at least three test cases)
assert word_length_distribution("This is a really great sample sentence!") == {
    4: 1, 2: 1, 1: 1, 6: 2, 5: 1, 8: 1
}
assert word_length_distribution("") == {}
assert word_length_distribution("cat bat hat") == {3: 3}
print("Exercise 2 tests passed.")


# ============================================================================
# EXERCISE 3: Create Histograms / Bar Charts
# ============================================================================
#
# Your task: Visualize the word length distribution as a histogram/bar chart.
# Label your charts and axes and give your plots suitable names.
#
# ------------------------------------------------------------------------------

PLOTS_DIR = "plots"
os.makedirs(PLOTS_DIR, exist_ok=True)


def plot_histogram(distribution, title):
    """Create a bar chart of word lengths."""
    lengths = sorted(distribution.keys())
    counts = [distribution[length] for length in lengths]

    plt.figure(figsize=(8, 5))
    plt.bar(lengths, counts, color="steelblue")
    plt.xlabel("Word length (characters)")
    plt.ylabel("Number of words")
    plt.title(title)
    plt.xticks(lengths)
    plt.tight_layout()

    filename = os.path.join(PLOTS_DIR, title.lower().replace(" ", "_") + ".png")
    plt.savefig(filename)
    plt.close()
    print(f"Saved histogram to {filename}")


# Create histogram for Dewey (English)
plot_histogram(word_length_distribution(dewey_text), "Dewey (English) Word Lengths")

# Create histogram for Montessori (Italian)
plot_histogram(word_length_distribution(montessori_text), "Montessori (Italian) Word Lengths")

# Create histogram for Freire (Portuguese)
plot_histogram(word_length_distribution(freire_text), "Freire (Portuguese) Word Lengths")


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

1. Get the raw word length distribution (reusing Exercise 2).
2. Add up all the counts to find the total number of words.
3. For each length, divide its count by the total and multiply by 100.
4. Return the percentages. If the text has no words at all, return an empty
   result rather than dividing by zero.
"""

def percentage_distribution(text):
    """
    Calculate percentage of words at each length.

    Returns:
        Dictionary or list where values are percentages (0-100)
        Example: if result[4] = 15.5, then 15.5% of words have length 4
    """
    distribution = word_length_distribution(text)
    total_words = sum(distribution.values())
    if total_words == 0:
        return {}
    return {length: (count / total_words) * 100 for length, count in distribution.items()}


# Write your own tests here (hint: what should the percentages sum to?
# Note it might not be exact due to rounding...)
sample_percentages = percentage_distribution("cat bat hat")
assert sample_percentages == {3: 100.0}

mixed_percentages = percentage_distribution("a bb ccc dddd")
assert abs(sum(mixed_percentages.values()) - 100.0) < 0.001  # percentages should sum to ~100%
assert percentage_distribution("") == {}
print("Exercise 4 tests passed.")


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

1. Get the word lengths for both texts (reusing Exercise 1).
2. Calculate the mean word length for each text, and the absolute
   difference between the two means.
3. Calculate the median word length for each text, and the absolute
   difference between the two medians.
4. Add the two differences together and return that as the distance.
   A smaller number means the texts are more similar.
"""

def compare_statistics(text1, text2):
    """
    Calculate distance between two texts using average and median.

    Returns:
        Float representing distance (smaller = more similar)
    """
    lengths1 = get_word_lengths(text1)
    lengths2 = get_word_lengths(text2)

    mean_diff = abs(statistics.mean(lengths1) - statistics.mean(lengths2))
    median_diff = abs(statistics.median(lengths1) - statistics.median(lengths2))

    return mean_diff + median_diff


# Write your own tests
assert compare_statistics("cat bat hat", "cat bat hat") == 0  # identical texts, zero distance
assert compare_statistics("a bb ccc", "a a a") > 0            # different texts, positive distance
print("Exercise 5 tests passed.")


# Optional extension: Incorporate the mode into your distance calculation.
def compare_statistics_with_mode(text1, text2):
    """Same idea as compare_statistics, but also factors in the most common
    word length (the mode) for each text."""
    lengths1 = get_word_lengths(text1)
    lengths2 = get_word_lengths(text2)

    mean_diff = abs(statistics.mean(lengths1) - statistics.mean(lengths2))
    median_diff = abs(statistics.median(lengths1) - statistics.median(lengths2))
    mode_diff = abs(statistics.mode(lengths1) - statistics.mode(lengths2))

    return mean_diff + median_diff + mode_diff


assert compare_statistics_with_mode("cat bat hat", "cat bat hat") == 0
print("Optional mode extension tests passed.")


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
    dist1 = percentage_distribution(text1)
    dist2 = percentage_distribution(text2)

    # A length that only appears in one of the two texts still needs to count
    # in the comparison, just with a percentage of 0 on the other side.
    all_lengths = set(dist1.keys()) | set(dist2.keys())
    if not all_lengths:
        return 0.0

    squared_diffs = [
        (dist1.get(length, 0.0) - dist2.get(length, 0.0)) ** 2
        for length in all_lengths
    ]
    return sum(squared_diffs) / len(all_lengths)


# Write your own tests
assert mean_squared_error("cat bat hat", "cat bat hat") == 0  # identical texts, zero error
assert mean_squared_error("a bb ccc", "a a a") > 0
print("Exercise 6 tests passed.")


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
    distances = {
        "English": mean_squared_error(sample_text, english_ref),
        "Italian": mean_squared_error(sample_text, italian_ref),
        "Portuguese": mean_squared_error(sample_text, portuguese_ref),
    }
    return min(distances, key=distances.get)


# A quick sanity check: each reference text should be closest to itself
assert predict_language(dewey_text, dewey_text, montessori_text, freire_text) == "English"
assert predict_language(montessori_text, dewey_text, montessori_text, freire_text) == "Italian"
assert predict_language(freire_text, dewey_text, montessori_text, freire_text) == "Portuguese"
print("Exercise 7 tests passed.")


# ============================================================================
# EXERCISE 8: Group Evaluation Tasks
# ============================================================================


# --------------------------------------------------------------------------
# 1. Test your predictor with sample texts in each language. Does it work?
# --------------------------------------------------------------------------

# Test with sample texts in each language, you are welcome to take a small
# section of each text as a sample, or use new texts entirely.
print("\n" + "=" * 50)
print("Exercise 8, Task 1: predictor sanity check")
print("=" * 50)
print("English reference predicted as:", predict_language(dewey_text, dewey_text, montessori_text, freire_text))
print("Italian reference predicted as:", predict_language(montessori_text, dewey_text, montessori_text, freire_text))
print("Portuguese reference predicted as:", predict_language(freire_text, dewey_text, montessori_text, freire_text))

# Feel free to use the secret text provided (secret_text.txt) to test your
# language prediction function. For this you will need the following code
# to load the text into the variable secret_text. As with the three
# reference texts above, this repository does not ship a real texts/secret.txt
# (an instructor would supply a genuine mystery excerpt), so we fall back to
# one of the synthetic demo strings just so this section still runs.
secret_text = _load_text_with_fallback("texts/secret.txt", FALLBACK_ITALIAN_TEXT, "mystery")

print("\nsecret_text predicted as:", predict_language(secret_text, dewey_text, montessori_text, freire_text))


# --------------------------------------------------------------------------
# 2. How many words does a sample need for accurate prediction?
#    Test with different sizes: 10 words, 50 words, 100 words, 500 words,
#    1000 words, 5000 words.
# --------------------------------------------------------------------------

def _first_n_words(text, n_words):
    """Return the first n_words words of text, joined back into a string.
    If the text has fewer words than that, this just returns the whole text."""
    words = text.split()
    return " ".join(words[:n_words])


print("\n" + "=" * 50)
print("Exercise 8, Task 2: does sample size change the prediction?")
print("=" * 50)
print("(Our synthetic demo texts are short, so very large sample sizes below")
print(" just fall back to using the whole text -- with real, longer source")
print(" texts in texts/, the larger sizes would be more meaningful.)")
for size in [10, 50, 100, 500, 1000, 5000]:
    sample = _first_n_words(secret_text, size)
    prediction = predict_language(sample, dewey_text, montessori_text, freire_text)
    print(f"  {size} words -> predicted {prediction}")


# --------------------------------------------------------------------------
# 3. Based on your tests what language is this text in?
#
#    Note, the point is not to guess correctly, the point is to evaluate
#    what your tests give you... how large a sample do you need to be sure
#    your test is accurate? What might cause it to fail?
# --------------------------------------------------------------------------

print("\n" + "=" * 50)
print("Exercise 8, Task 3: reading the results above")
print("=" * 50)
print("Look at the predictions printed in Task 2: once the predicted language")
print("stops changing as the sample size grows, that's a reasonable point to")
print("trust the result. If it keeps flipping between languages even at larger")
print("sample sizes, that's a sign the sample is too short, or that this")
print("particular text's word-length statistics sit awkwardly between two")
print("of the reference languages.")


# --------------------------------------------------------------------------
# 4. Which pair of languages is hardest to distinguish? Which is easiest?
# --------------------------------------------------------------------------

print("\n" + "=" * 50)
print("Exercise 8, Task 4: pairwise distances between reference texts")
print("=" * 50)
language_pairs = [
    ("English vs Italian", dewey_text, montessori_text),
    ("English vs Portuguese", dewey_text, freire_text),
    ("Italian vs Portuguese", montessori_text, freire_text),
]
for label, text_a, text_b in language_pairs:
    print(f"  {label}: MSE = {mean_squared_error(text_a, text_b):.4f}")
print("The pair with the smallest MSE above is the hardest to tell apart by")
print("word length alone; the pair with the largest MSE is the easiest.")


# --------------------------------------------------------------------------
# 5. Compare the basic method (Exercise 5) with MSE (Exercise 6).
#    Which performs better?
# --------------------------------------------------------------------------

print("\n" + "=" * 50)
print("Exercise 8, Task 5: basic method vs MSE")
print("=" * 50)
for label, text_a, text_b in language_pairs:
    basic = compare_statistics(text_a, text_b)
    mse = mean_squared_error(text_a, text_b)
    print(f"  {label}: basic={basic:.4f}, mse={mse:.4f}")
print("The basic method only looks at two summary numbers (mean and median),")
print("so two texts with very different shapes of distribution can still end")
print("up looking similar to it. MSE compares the whole distribution shape,")
print("length by length, so it tends to be the more sensitive of the two.")


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
# Sample response (not the only right way to answer this, and worth writing
# your own once you have run this against real reference texts): word length
# on its own turned out to carry a surprising amount of signal for
# distinguishing these three languages, mostly because Italian and Portuguese
# tend to run longer average word lengths than English due to their heavier
# use of inflectional endings. The most important design decision was
# comparing full percentage distributions with MSE rather than only comparing
# a couple of summary statistics, since two languages can share a similar
# mean word length while still differing a great deal in their spread.
#
# The biggest limitation is that word length says nothing about grammar,
# vocabulary, or meaning, so a short or unusual sample can easily be
# misclassified, and the reference texts themselves need to be reasonably
# representative of each language rather than one author's unusual style. A
# useful next step would be to combine word length with something like
# common short "function words" (the, di, de, and so on), which tend to be
# very language-specific and would likely make the predictor more reliable on
# short samples.
#
# ============================================================================


# ============================================================================
# End of Skills Demo
# ============================================================================
