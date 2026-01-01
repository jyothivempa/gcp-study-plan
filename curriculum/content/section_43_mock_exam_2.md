# SECTION 43: Mock Exam 2 (Module 10)

> **Format**: 15 Advanced Questions. Case Studies included.

## Scenario 1: Mountkirk Games (Abbrev)
Mountkirk is building a mobile game. They expect global traffic. They need to scale the backend automatically. They have a legacy SQL database they want to migrate.

**Q1**: Which database service should they use for their legacy SQL migration if they want minimal changes?
*   A. BigQuery
*   B. **Cloud SQL**
*   C. Cloud Spanner
*   D. Datastore

> **Answer: B.** Legacy SQL + Lift & Shift = Cloud SQL. Spanner requires rewriting schemas.

**Q2**: They need to store 5TB of player avatars (images). The images are accessed frequently for the first 30 days, then rarely. What should they use?
*   A. Persistent Disk on the Web Servers.
*   B. **Cloud Storage (Standard Class) with a Lifecycle Rule** to move to Nearline after 30 days.
*   C. Cloud Storage (Coldline).
*   D. Bigtable.

> **Answer: B.** Object storage for images. Lifecycle rule for cost optimization (Module 9!).

---

## Scenario 2: TerramEarth (Abbrev)
TerramEarth collects IoT data from 2 million tractors.
**Q3**: They need to ingest this data in real-time. Which service is the "front door"?
*   A. Cloud Functions.
*   B. **Cloud Pub/Sub**.
*   C. Dataflow.
*   D. BigQuery.

> **Answer: B.** IoT / Streaming Ingestion = Pub/Sub.

---

*(More questions...)*

## Final Readiness Check
If you are passing these 2 mocks and the daily quizzes with >80%, **schedule your exam**.
Go to Webassessor. Book it. Do it.
