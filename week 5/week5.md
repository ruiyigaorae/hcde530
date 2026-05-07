## Competency Claim — Week 5

**C5 - Data analysis with pandas**
I can load a real-world dataset into pandas, inspect its structure, and apply
multiple operations to answer specific analytical questions. Raw data from
government APIs requires cleaning and careful interpretation — the same record
can mean very different things depending on document type, and missing agency
fields can silently distort conclusions if not caught early.

I used five pandas operations on 200 Federal Register documents related to
artificial intelligence: df.head() and df.info() to confirm the schema and
catch a missing agency_names column (which I traced back to a field name
mismatch in the fetch script and fixed); value_counts() to find that 81% of
AI-related federal documents are Notices rather than binding Rules; a date
filter to confirm that all 200 records postdate 2022, showing that federal AI
governance is almost entirely a post-ChatGPT phenomenon; groupby to identify
NIST as the most active agency with 35 documents, followed by the Executive
Office of the President with 20; and isnull().sum() to verify data completeness
after the fix.

**Why this matters for HCD**
Understanding which agencies are most active on AI and what kinds of documents
they produce is directly relevant to HCD practitioners working in regulated
industries. A product team building AI tools for healthcare or education needs
to know whether the relevant agency is issuing binding rules or advisory
notices — the compliance burden is very different. Being able to answer that
question programmatically, from primary sources, is a practical governance skill.