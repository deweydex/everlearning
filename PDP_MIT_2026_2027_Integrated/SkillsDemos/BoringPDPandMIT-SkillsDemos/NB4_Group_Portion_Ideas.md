# Group Portion Ideas (10% of PDP SD2)

## Purpose

This 10% component satisfies PDP Learning Outcome 12: "Work as part of a team to design, develop, release and review multiple versions of a multi-modular program over an extended period of time." It sits alongside SD2a (15%) and SD2b (15%) to complete the 40% total for PDP Skills Demo 2.

The group work is not graded for Maths for IT, but it involves mathematical content (Section 3: calculus/derivatives) that helps students prepare for the Maths for IT exam.


## Option A: Peer Review and Documentation Sprint

Teams of 3-5 students exchange their SD2a and SD2b notebooks. Each team:

1. **Reviews** another team member's code: reads through, runs it, identifies where documentation or comments could be improved, flags any bugs or edge cases that were missed.

2. **Improves documentation**: adds or refines docstrings, comments, and markdown explanations in their own notebooks based on feedback received.

3. **Creates a shared "study functions" module**: the team collaborates on a single Python file (or notebook) containing well-documented versions of key functions from both SD2a and SD2b, plus new functions that explore derivatives -- content that prepares everyone for the exam but is not itself graded under Maths for IT.

The derivative exploration could include:
- A function that computes the numerical derivative of any function at a point using the limit definition
- A function that computes the symbolic derivative of a polynomial (given as a coefficient list, this is elegant: the derivative of `[c0, c1, c2, c3]` is `[c1, 2*c2, 3*c3]`)
- Graphing a function alongside its derivative to build visual intuition
- Exploring the product rule, quotient rule, and chain rule through specific examples

**Deliverables**: each student submits their improved notebooks plus the team's shared study module. Evidence of the review process (comments, tracked changes, or a brief write-up of feedback given and received).


## Option B: The Function Explorer

Teams build a collaborative "function explorer" tool as a Jupyter notebook. Each team member is responsible for one module:

- **Person A**: Polynomial evaluation and graphing (building on SD2b work)
- **Person B**: Derivative computation (numerical and/or symbolic)
- **Person C**: Root finding and analysis (where does f(x) = 0? where are the turning points?)
- **Person D** (if applicable): Integration by numerical approximation (rectangles, trapezoids)

The team then integrates these modules into a single notebook where a user can:
1. Enter a polynomial
2. See its graph
3. See its derivative graph overlaid
4. Find roots and turning points
5. Optionally see an integral approximation

This naturally involves multiple versions (each person builds independently, then integration requires revision), team coordination, and release of a working tool.

**Deliverables**: the integrated notebook, individual contribution logs, and a brief team reflection on what worked, what was difficult about integration, and how they resolved differences.


## Option C: Exam Prep Workshop

Teams collaboratively create exam preparation materials for the Maths for IT exam, focusing on Section 3 (Functions and Calculus) and Section 4 (Geometry and Trigonometry) content that is not covered by the assignments.

Each team:

1. **Identifies** the exam-only learning outcomes: graphing functions (3.2), trig functions (3.3), completing the square (3.4), limits (3.5), derivatives from first principles (3.6), differentiation rules (3.7), coordinate geometry (4.1-4.3), and trigonometry (4.4-4.10).

2. **Creates worked examples** as a Jupyter notebook with both mathematical explanation and Python verification. For instance: "Here is how to differentiate $3x^2 + 2x$ by hand using the power rule. Let's verify with our numerical derivative function."

3. **Writes practice problems** with solutions for other teams to use.

4. **Reviews** another team's materials and provides feedback.

This option has the advantage of being directly useful to students while naturally involving team collaboration, version control, and documentation.

**Deliverables**: the exam prep notebook, evidence of peer review, and a brief reflection.


## Marking Considerations

Whichever option is chosen, the 10% could be assessed across:
- Quality of team collaboration and evidence of multiple versions (3 marks)
- Documentation and code quality in the team deliverable (3 marks)
- Individual contribution and reflection (4 marks)

The derivative/calculus content is present in all three options but is assessed only under PDP criteria (code quality, documentation, teamwork) rather than Maths for IT criteria. This means students get exposure to the material for exam preparation without the pressure of it counting toward the maths grade.


## Recommended Sequencing

This group portion would come after both SD2a and SD2b are complete, ideally 2-3 weeks before the Maths for IT exam. This timing means:
- Students have all their individual work done and can focus on collaboration
- The derivative content serves as timely exam revision
- The peer review improves the quality of already-submitted individual work
