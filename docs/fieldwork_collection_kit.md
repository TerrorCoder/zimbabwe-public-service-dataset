# Zimbabwe Public Service Data Collection: Fieldwork Collection Kit & SOP

**Author:** Dataprenuers Project Team  
**Role:** Field Research Lead (Vimbainashe Mandaza) & Field Operations  
**Version:** 1.0.0  
**Target Agencies:** Civil Registry Department, Deeds & Companies Office, ZIMRA, PRAZ, POTRAZ, Ministry of ICT  

---

## 1. Executive Summary & Purpose

While online portals provide baseline procedural guidelines, empirical research shows that **fees, processing times, required supporting documents, and counter workflows** frequently differ at physical agency offices in Harare (Makombe Complex, Kurima House, Deeds Office, etc.) and provincial registry centers.

This Fieldwork Collection Kit provides a standardized, repeatable protocol for field researchers to visit public service agency offices, record verified administrative details, and bridge the gap between online documentation and ground truth.

---

## 2. Fieldwork Preparation & Safety Protocol

### 2.1 Pre-Visit Checklist
Before conducting an agency office visit, field researchers must prepare the following equipment and documents:
- [ ] **Official Identification**: National ID card and University/Organization credentials.
- [ ] **Courtesy Notice Letter**: Copy of the project notification letter submitted to the agency on 9 July 2026.
- [ ] **Physical Data Collection Log Sheets**: Printed copies of `agency_verification_form.csv`.
- [ ] **Digital Field Device**: Fully charged smartphone or tablet with offline recording capabilities.
- [ ] **Data Bundle & Airtime**: Active connectivity for emergency cross-verification.
- [ ] **Pre-filled Baseline Card**: Summary of current online data for the targeted service (`SVC-###`).

### 2.2 Ethical & Legal Guidelines
- **Public Information Only**: Only collect non-personal administrative guidelines, published fee structures, steps, and counter instructions. **Never collect personal data, citizen identity details, or individual tax records.**
- **Transparent Attribution**: Inform agency noticeboard/helpdesk officers that you are auditing public service procedures for educational and AI accessibility benchmarking.

---

## 3. Standard Field Data Collection Procedure

When visiting an agency office, follow this 5-step workflow:

```
[1. Noticeboard Audit] ──> [2. Helpdesk Query] ──> [3. Physical Form Audit] ──> [4. Queue/Fee Verification] ──> [5. Record Sign-off]
```

### Step 1: Noticeboard & Wall Poster Audit
- Inspect official posters, banner stands, and noticeboards displayed in waiting areas.
- Photograph or record official fee schedules, acceptable payment methods (USD cash, EcoCash, ZiG, POS Swipe), and working hours.

### Step 2: Helpdesk / Information Counter Query
- Approach the official information desk or desk supervisor.
- Verify required original documents and copies needed (e.g., whether certified copies must be under 3 months old).

### Step 3: Physical Application Form Audit
- Obtain a sample blank application form (e.g., CR1, CR5, CR6, Passport Form, Tax Registration Form).
- Check for form tokens or fee requirements for the form paper itself.

### Step 4: Queue & Processing Time Verification
- Record average queue times, daily token cut-off times (e.g., whether passport queues close at 11:00 AM), and turnaround times for standard vs urgent service options.

### Step 5: Field Log Completion & Timestamping
- Fill in the field verification log sheet (`agency_verification_form.csv`) immediately after leaving the office.

---

## 4. Key Data Fields to Record

| Field Name | Description & Verification Standard |
| :--- | :--- |
| **`record_id`** | Assigned SVC ID (e.g. SVC-001) |
| **`agency_office_location`** | Exact location/branch visited (e.g. Makombe Complex Harare, Kurima House, Bulawayo Registry) |
| **`verified_fee_usd`** | Actual fee charged at counter in USD |
| **`accepted_payment_modes`** | Cash USD, EcoCash, ZiG, Bank Swipe POS, Bank Transfer |
| **`mandatory_documents`** | List of exact document requirements verified on ground |
| **`counter_processing_steps`** | Sequential step-by-step path inside the building |
| **`queue_cutoff_time`** | Time when new applicants are no longer admitted (e.g., 10:30 AM) |
| **`field_notes_and_bottlenecks`** | Key practical tips for citizens (e.g., "Bring 2 passport-sized photos with white background") |
| **`verified_by`** | Name of field researcher |
| **`verification_timestamp`** | ISO 8601 Date and Time |

---

## 5. Agency-Specific Verification Focus Areas

### A. Civil Registry Department (Makombe Complex & Provincial Offices)
- **Focus**: Verify e-passport appointment rules vs walk-in queues; emergency passport supervisor clearance process; birth certificate late registration search fees.

### B. Deeds and Companies Office (Harare & Bulawayo)
- **Focus**: Verify online CORES portal submission vs manual counter submissions; form CR1 availability; accounting officer certification requirements for PBCs.

### C. ZIMRA (Kurima House & Regional Stations)
- **Focus**: Verify self-service kiosk availability; TaRMS onboarding support desks; physical inspection scheduling turnaround for VAT.

### D. PRAZ (Harare Headquarters)
- **Focus**: Verify bank transfer clearance turnaround times; physical collection of PRAZ certificate vs portal download.

### E. POTRAZ (Ruwa Headquarters & Ministry of ICT)
- **Focus**: Verify application submission window; board committee review schedule; security clearance form distribution.
