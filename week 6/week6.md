## Week 6 — Chart Justifications and Competency Claim

### Chart 1: Top 10 Federal Agencies by AI-Related Documents
**Chart type:** Horizontal bar chart  
**Question answered:** Which federal agencies are most active in publishing 
AI-related documents?

A horizontal bar chart is appropriate here because I am comparing a ranked 
list of categories (agencies) by a single numeric value (document count). 
The finding is that the Commerce Department dominates with ~60 documents, 
largely because NIST — which sits inside Commerce — is the primary federal 
body responsible for AI standards through the AI Risk Management Framework. 
Health and Human Services is third, reflecting significant regulatory attention 
to AI in clinical and public health contexts.

### Chart 2: AI-Related Federal Documents by Type
**Chart type:** Vertical bar chart  
**Question answered:** What kinds of federal actions are being taken on AI — 
binding rules or informational notices?

A bar chart is appropriate for comparing a small number of discrete categories. 
The finding is stark: 162 of 200 documents (81%) are Notices, while only 6 are 
binding Rules. This means U.S. federal AI governance is currently operating 
almost entirely through information-gathering and signaling rather than 
enforceable regulation — a meaningful finding for any HCD practitioner trying 
to understand actual compliance requirements.

### Chart 3: AI-Related Federal Documents Published Per Year
**Chart type:** Line chart with markers  
**Question answered:** When did federal AI governance activity accelerate?

A line chart is appropriate for showing change over time. The data shows a 
sharp increase from 2023 to 2025, peaking at 77 documents in 2025. The 2026 
drop to 39 is expected — the dataset was pulled mid-year and 2026 is incomplete. 
The overall pattern confirms that federal AI governance is almost entirely a 
post-2022 phenomenon, likely triggered by the public release of large language 
models and Biden's 2023 Executive Order on AI.

---

## Competency Claim

**C6 - Data visualization**
I can build charts that make a specific argument clearly, choose chart types 
that match the data structure, and save publication-ready images from a Python 
script. Each chart here answers a different analytical question about U.S. AI 
governance: who is producing documents, what kinds, and when. The timeline 
chart required handling an incomplete year (2026) and fixing a float x-axis 
bug — both judgment calls about how to represent the data honestly rather than 
just mechanically.