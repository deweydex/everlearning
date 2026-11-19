# Python Level 5: plan for three tutorial notebooks

This plan sits behind three Jupyter notebooks: variables and data types, input and print, and if/else. The notebooks are built and tested. The plan says why they look the way they do, so that you can change the decisions you disagree with.

## What the repository already covers

I read deweydex/dewlab, including the style guide, the page templates and the Experiments and Exercises module. That module already has seven pages on names and values, text, numbers, input, true and false, and decisions, written in a minimal format with many small experiments and little explanation. Your notebooks overlap with it in topic and differ in shape. The dewlab pages are short runs of experiments for students who can already work with little scaffolding. These notebooks add a fuller path with explanations in plain language, a warm-up that returns to the previous notebook, a practice bank and a set of challenges, because half of your group needs more support than a bare experiment gives. Each notebook links to the matching dewlab pages as further reading.

I took the experiential approach from the dewlab style guide: predict in writing before running, discover before naming, mistakes as information, and no verdicts on a learner's answer. I did not read theartofmathematics.org, so the notebooks follow your description and your own guide, and not that site.

## What the learners know, and what they have not met

The group has seven learners at Level 5, and the experience runs from none to a good deal. Learners at the lower end have not met the idea that a program runs line by line from the top. They treat the `=` sign as an equation, and they expect a name to follow another name. They do not separate the text `"5"` from the number 5. They have not read an error message as information. Learners at the upper end can write short programs, and they lack a few precise ideas: that `input` always returns a string, that `/` always returns a float, that conditions are checked from the top and stop at the first match, and that `x == 3 or 4` is always true.

The notebooks use these misconceptions as experiments. Each one appears as a prediction cell, so the learner meets the surprise first and the name for it second.

## The three notebooks

**Notebook 1, names and values.** Nine sections: assignment, changing a value, choosing names, the four types (int, float, str, bool), arithmetic with `//` and `%`, text, comparisons that give bools, converting between types, and a small café till. A name is introduced first as a label attached to a value, and the sections about `b = a` and `points = points + 5` take apart the two most common misreadings of `=`.

**Notebook 2, input and print.** A warm-up on Notebook 1, then six sections: what `print` shows (with `sep` and `end`), putting values into a sentence with f-strings and `:.2f`, `input` and the fact that it returns a string, the four-step shape of a small program (ask, convert, calculate, show), a section that names the four common errors, and a bill splitter. The error section asks learners to guess the error name before they run each cell.

**Notebook 3, decisions.** A warm-up, then seven sections: comparisons, `if`, `else`, `elif` and the order of conditions, `and`, `or` and `not`, a guessing game that combines all three notebooks, and a three-question quiz with a changing score.

I read your request as three separate topics in this order: variables with types, then input and print, then if/else. Input comes before decisions because the decisions become interesting when a person supplies the values. If you meant two topics in the first notebook and a combined third notebook, the sections move without much change.

## Format: notebook or Word document

I chose Jupyter notebooks. A Word document asks the learner to copy code into a second tool, and copying brings typing errors that have nothing to do with the lesson. In a notebook, a text cell and the code cell under it sit together, so the explanation, the question and the answer stay in one place, and the learner can change one number and run the cell again within seconds. The notebooks use only core Python, so they should run in the college's Jupyter installation and in Colab. I tested them in a Jupyter kernel here, and not in either of those two.

The repository can also save a tutorial page as a notebook, so the same notebooks could later become dewlab pages. I did not build the dewlab page version, because you asked for a notebook-only version first.

## Length

Each notebook is built for about three hours of class, with the learners working at their own pace and you supporting them. I have not timed it with learners, so the figures below come from counting the tasks and from the dewlab guide's estimate of an hour for a tutorial.

| Part | What it holds | Time |
| --- | --- | --- |
| Opening cell and warm-up | One program to run and a short recall of the earlier notebook | 15 minutes |
| Part A, the main path | Six to nine sections, each with a prediction, a short explanation and one or more tasks | about 90 minutes |
| Part B, practice | Ten problems of mixed kinds (predict, make, fix, explain), with hints and folded answers | 45 minutes in class, then home |
| Part C, challenges | Six or seven open challenges, each with a first step anyone can take | the rest of the class, then home |

The learners who are struggling stay in Part A and the first problems of Part B for the whole class, and that amount is enough for them. The learners who are ahead move faster through Part A and spend their time in Part C. You do not need a minute by minute plan, because the notebook holds the structure.

## The two halves of the group

Every notebook has a fast lane. A note near the top names three problems in Part B (B3, B7 and B10 in Notebook 1, and B3, B6 and B10 in Notebooks 2 and 3). A learner who recognises the material tries those three first, and moves to Part C when all three run as planned. A learner who struggles with the three goes back to the section that matches the problem.

Part C holds the challenges for experienced learners: swapping two variables, why `0.1 + 0.2` looks odd, taking apart the digits of a number, a banner that fits any name, FizzBuzz, leap years, rock paper scissors, a text adventure, and checking text with `.isdigit()` before calling `int()`. The tree of stars in Notebook 2 points forward to loops, which the learners have not met. The repetition in its code gives them a reason to learn loops.

The notebook for the struggling half carries the support that the other half can skip. Every task has a hint, and every answer folds away behind the line *Here is one answer. Yours may be different and work too.* The hints start with a question about what the learner can see, and the answers come after an attempt.

## Learners whose first language is not English

The text follows the dewlab plain-language rules: short sentences, one idea in each, a subject and a verb in every sentence, and few phrasal verbs. Each technical term is explained where it first appears, and the same words return in the same form. A word list at the end of each notebook gives the meanings. Below it sits an empty table headed *My word list*, where a learner can write each word's meaning in their own words or in another language. No notebook asks a learner about their background or first language.

Other support comes from the form of the notebook. Code carries part of the meaning, so a learner can follow the logic without reading every sentence. Error messages get their own section in Notebook 2, which turns an unfamiliar English sentence into a pattern. A learner can also try the browser's own translation on the text cells.

## Decisions to review

Several choices are mine, and you may want to reverse them.

The contexts are everyday and invented: a café, a bus card, a taxi, a bill. I did not build the dewlab idea of a world that the learner chooses.

The mark bands in Notebook 3 (80, 65 and 50) match the Distinction, Merit and Pass bands that I remember for QQI results. The notebook does not call them official. Please check them against what your learners see.

I used the euro sign in one cell of Notebook 2. If the college notebooks display it badly, those cells can use the word `euro`.

The notebooks ask learners to write a guess in a comment before each prediction cell. I think this is the part of the experiential approach that costs least and teaches most, and it also means a learner has written something down before the output arrives.

I have not tried the notebooks with learners. The code was run in a notebook kernel and in a test harness with scripted input, and all the answers ran without error, but the text needs your reading and a trial with the group before it settles.

## Further reading

The Python tutorial at docs.python.org (the sections on numbers and text, on `if` statements and on output formatting) is linked from the notebooks. The dewlab Experiments and Exercises module at deweydex.github.io/dewlab holds further experiments on the same topics.
