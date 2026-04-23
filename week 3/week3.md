## Competency Claim — Week 3

**C2 - Code literacy and documentation**
I can read a buggy Python script, identify what each section does, and fix
errors based on error messages. When a script fails silently or crashes, being
able to trace the error to its source is essential for producing reliable
analysis — a script that runs but produces wrong results is worse than one
that crashes, because the error is invisible.

I diagnosed and fixed three bugs in week3_analysis_buggy.py: a ValueError
caused by a text value ("fifteen") in the experience_years field, which I
fixed by wrapping the conversion in a try/except block and tracking only valid
rows in the average calculation; a reversed sort that returned the lowest
satisfaction scores instead of the highest, fixed by adding reverse=True; and
empty role values being counted as a valid category, fixed by skipping blank
entries with an early continue.

**C3 - Data cleaning and file handling**
I can load a messy CSV, normalize inconsistent text formatting, and write
cleaned output to a new file. Raw survey data is rarely analysis-ready —
the same category entered as "ux designer", "UX DESIGNER", and "Ux Designer"
will be counted as three separate groups, which distorts any frequency
analysis. Cleaning is not optional; it determines whether the results are
meaningful.

My script standardizes capitalization in the role, department, and
primary_tool columns using .strip().title(), removing extra whitespace and
making comparisons consistent. The cleaned data is saved to
week3_survey_cleaned.csv so it can be reused in future analysis without
repeating the cleaning step.