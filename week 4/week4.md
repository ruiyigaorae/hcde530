## Competency Claim — Week 4

**C4 - APIs and data acquisition**
I can call a real public API, parse the JSON response, and save structured
data to a CSV file for further analysis. Knowing how to pull data directly
from a source — rather than relying on pre-packaged datasets — is essential
for HCD research, where the questions often emerge before the data exists in
a convenient form.

I chose the Federal Register API because it provides direct access to U.S.
federal government documents, including rules, notices, and presidential
documents related to AI policy. I wrote a script that searches for documents
containing "artificial intelligence", fetches at least 50 records using
pagination (since the API returns 20 records per page), and extracts five
fields per document: title, publication_date, agency_names, document_number,
and type. The script saves the results to week4_federal_register.csv.

The API returned 1,406 matching documents in total. Of the 60 records I
downloaded, 47 were Notices, 5 were Presidential Documents, 5 were Proposed
Rules, and 3 were Rules, a distribution that itself tells a story about how
AI governance is currently being enacted in the U.S.: mostly through
administrative notices rather than binding regulation.

HCD reflection
For HCD practitioners, understanding the policy environment around AI is not
optional — it shapes what products can be built, what data can be collected,
and what disclosures are required. Being able to pull and analyze this data
programmatically means I can track regulatory changes over time, identify
which agencies are most active on AI issues, and connect policy signals to
design decisions. This skill bridges my research background in AI governance
with the technical capacity to work with real institutional data at scale.