---
title: "Your questions"
slug: 00-your-questions
course: database-methods
course_title: "Database Methods"
series: entry
series_title: "Start here"
version: 2026.09.06.1
---

# Your questions

Before the first notebook of this course, a page for you rather than for the subject. The course teaches databases, and it will use examples chosen by the people who wrote it. Those examples are not your life. This page asks what is.

Nothing here is marked and nothing here is a test. What you write is the beginning of a conversation with your teacher and the others in the room, and the questions people bring on this page are the questions the course will come back to.

## Three situations

Write down three situations from your own life, work or community where you have thought "there must be a better way to keep track of this", or "I wish I could tell what will happen next", or "somebody must know the answer to this and I do not". They do not have to be about computers. Some that people have brought before:

- a set of records someone keeps in a notebook or a spreadsheet
- a question you have asked an office that took a week to answer
- a club, a team, a shop or a family that keeps track of things
- a public dataset about where you live that you have never looked at

Double-click this cell and write yours underneath. A sentence each is enough.

1.

2.

3.

## One of them, closer

Choose the one of the three that matters most to you and answer, in a few sentences each: what information would you need to have in front of you to think about it properly, where that information is now, and who else has the same problem.

Keep this page. At the end of the course you will come back to it and ask which of the three a database you could now build, and which you could not, and why.

```python exec
id: 00-your-questions-1
# A first, tiny step: write the three situations as a Python list of strings, one per line.
# It is the first data this course will hold, and it is yours.

my_situations = [
    "",
    "",
    "",
]

for number, situation in enumerate(my_situations, start=1):
    print(number, situation)
```

## For the teacher

The situations written on this page are the generative themes of this group, in Freire's sense: the material the course's examples should be drawn from where they can be, and the questions to return to when a notebook's own example feels far away. Reading these pages before the second session, and naming two or three of the situations aloud in it, is the single act that most changes how the rest of the course is received. The final notebook of the course asks learners to come back to this page.
