# Public Agency Correction and Notice Protocol

**Dataset Maintainer:** Dataprenuers Team  
**Data Steward Contact:** Lincoln Tinaye Rwodzi (`lincoln@dataprenuers.co.zw` / GitHub Repository Issues)  

---

## 1. Principle of Attributable & Correctable Data

All records in the **Zimbabwe Public Service Knowledge & AI Benchmark Dataset** represent public administrative procedures sourced from official government publications, statutory instruments, and physical agency office notices.

We maintain a transparent, responsive correction framework allowing government agencies, public officials, and citizens to submit corrections or updates at any time.

---

## 2. Correction Request Procedure

### Step 1: Submission
Agencies or users may submit corrections by opening a GitHub Issue on the official repository (`https://github.com/TerrorCoder/zimbabwe-public-service-dataset`) or contacting the Data Steward via official email.

### Step 2: Verification
Upon receipt of a notice:
- The Data Steward cross-references the requested change against published Statutory Instruments or official agency gazettes.
- If verified, the record's `last_verified` date and fee/procedure fields are updated immediately in `processed/records.jsonl`.

### Step 3: Release & Changelog Audit
- The modification is logged in `CHANGELOG.md`.
- A patch release (e.g. `v1.0.1`) is tagged and published.
