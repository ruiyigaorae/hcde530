## Mini Project 1: Competency Claim

**C3 - Data cleaning and file handling**
I can pull data from a real public API, clean it, and save it to a CSV that 
is ready for analysis. The agency field required debugging — the API returns 
agencies as a nested array under agencies[].name, not a flat agency_names 
field. Finding and fixing that mismatch was the difference between 200 empty 
cells and usable data. I also handled SSL certificate failures on macOS with 
a fallback context, and regenerated the CSV after each fix to confirm the 
output was correct.

**C4 - APIs and data acquisition**
I can read API documentation, construct paginated requests, and extract 
structured data from JSON responses. The Federal Register API returns 20 
records per page across 1,400+ matching documents; my script loops until it 
collects at least 200 records and handles both list and dict response formats. 
I chose this API because it gives direct access to primary-source U.S. AI 
policy data, which is more reliable than news summaries for governance research.

**C5 - Data analysis with pandas**
I can use pandas to profile a dataset, filter by date, group by category, and 
count value distributions. The analysis confirmed that federal AI governance is 
notice-heavy and post-2022, findings that would not be visible from casual 
reading of the data.

**C6 - Data visualization**
I can build charts that make a specific argument, choose chart types that fit 
the data structure, and save publication-ready images. The three charts together 
tell a coherent story: who is driving federal AI activity, what form it takes, 
and when it accelerated. Building the timeline required fixing a float x-axis 
bug and accounting for an incomplete 2026: both judgment calls about honest 
representation of the data.