## Week 6 — Chart Justifications and Competency Claim

### Chart 1: Top 10 Federal Agencies by AI-Related Documents
**Chart type:** Horizontal bar chart  
**Question answered:** Which federal agencies are most active in publishing 
AI-related documents?

I used a horizontal bar chart because I am comparing ranked categories by a 
single count, and horizontal bars make long agency names readable. The Commerce 
Department leads with around 60 documents, mostly because NIST sits inside 
Commerce and is the primary federal body responsible for AI standards. Health 
and Human Services coming in third reflects how much regulatory attention AI 
in clinical and public health contexts has attracted in recent years.

### Chart 2: AI-Related Federal Documents by Type
**Chart type:** Vertical bar chart  
**Question answered:** What kinds of federal actions are being taken on AI?

A bar chart works here because I am comparing a small number of discrete 
categories. The result is pretty striking: 162 of 200 documents are Notices, 
while only 6 are binding Rules. That means U.S. federal AI governance is 
currently operating almost entirely through information-gathering and signaling 
rather than enforceable regulation. For anyone trying to understand what 
compliance actually requires right now, that distinction matters a lot.

### Chart 3: AI-Related Federal Documents Published Per Year
**Chart type:** Line chart with markers  
**Question answered:** When did federal AI governance activity accelerate?

A line chart makes sense for showing change over time. Activity jumped sharply 
from 2023 to 2025, peaking at 77 documents in 2025. The 2026 number is lower 
because the dataset was pulled mid-year and the year is not complete yet. The 
overall pattern confirms that federal AI governance is almost entirely a 
post-2022 development, which lines up with the public release of large language 
models and Biden's 2023 Executive Order on AI.

---

## Competency Claim

**C6 - Data visualization**
I can build charts that answer a specific question, choose chart types that 
fit the data structure, and save images from a Python script. Each of the three 
charts here addresses a different question about U.S. AI governance: who is 
producing documents, what kinds, and when. Building the timeline chart required 
handling an incomplete year for 2026 and fixing a float x-axis bug, both of 
which involved making judgment calls about how to represent the data honestly 
rather than just running the code and accepting whatever came out.