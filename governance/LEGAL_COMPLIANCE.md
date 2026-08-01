# Statutory Legal Compliance & Regulatory Risk Analysis

**Dataset Maintainer:** Dataprenuers Team  
**Jurisdiction:** Republic of Zimbabwe & International Open Data Frameworks  
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Executive Legal Summary

The **Zimbabwe Public Service Knowledge & AI Benchmark Dataset** is a structured, machine-readable dataset compiled to advance public information accessibility, civic literacy, and AI model evaluation in English, Shona, and Ndebele.

This document presents a comprehensive statutory legal analysis demonstrating that the creation, distribution, and utilization of this dataset **fully complies with Zimbabwean national laws and international intellectual property standards**, carrying zero risk of legal infringement.

---

## 1. Freedom of Information Act [Chapter 10:33] (Zimbabwe)

### Statutory Foundation
The **Freedom of Information Act [Chapter 10:33]** (enacted pursuant to Section 62 of the Constitution of Zimbabwe) guarantees the fundamental constitutional right of every citizen to access information held by public entities, government bodies, statutory boards, and local authorities.

### Legal Assessment
- Public service workflows, statutory fees, required document checklists, and office locations are administrative guidance created by state entities for public guidance and compliance.
- Under Section 5 and Section 9 of the Freedom of Information Act, public entities have a statutory obligation to make public service procedures accessible to citizens.
- **Conclusion:** Consolidating public service guidance into an open-access AI dataset directly implements the statutory purpose of the Freedom of Information Act.

---

## 2. Copyright and Neighboring Rights Act [Chapter 26:01] (Zimbabwe)

### Doctrine of Factual Non-Copyrightability
Under Zimbabwean copyright jurisprudence and international copyright conventions (Berne Convention, TRIPS Agreement):
1. **Facts vs. Expression**: Copyright protects original creative or artistic expression. Factual data—such as official fee amounts, application deadlines, statutory requirements, and physical office addresses—are non-copyrightable facts.
2. **Official Government Publications**: Official texts of an administrative, statutory, or legal nature (including Statutory Instruments, Acts of Parliament, and official gazettes) are intended for open public dissemination and fall into the public domain.

### Compilation & Database Rights
- The original custom JSONL schema, relational taxonomy, data standardization pipeline, and original Shona/Ndebele intent translations constitute original compilation work owned by the dataset maintainers.
- This compilation work is legitimately licensed to the public under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

---

## 3. Cyber and Data Protection Act [Chapter 12:07] (Zimbabwe)

### Data Privacy & PII Compliance
The **Cyber and Data Protection Act [Chapter 12:07]** regulates the processing of Personally Identifiable Information (PII) to protect individual privacy.

### Audit & Certification Results
- **Zero PII Guarantee:** Automated static analysis (`scripts/audit_pii.py`) audited all 20,000 dataset records and verified **0 PII violations**.
- The dataset contains **no individual citizen names**, **no private mobile phone numbers**, **no personal email addresses**, **no National ID numbers**, and **no private case files**.
- Only public administrative metadata (e.g., official agency helpdesk URLs, general institutional phone lines, and physical headquarter office locations) is recorded.

---

## 4. Official Secrets Act [Chapter 11:09] (Zimbabwe)

### National Security Assessment
The **Official Secrets Act [Chapter 11:09]** protects classified state security, military, defense, and confidential intelligence information.

### Legal Assessment
- Every record in this dataset represents standard, unclassified public citizen services (e.g. e-passport applications, business incorporation, vehicle licensing, tax TIN onboarding, small claims litigation).
- **Zero classified, secret, military, or security intelligence information** is indexed in the dataset.

---

## 5. Risk Mitigation & Statutory Disclaimers

To protect the dataset maintainers, contributors, and downstream AI developers, the following safeguards are active:

1. **Non-Official Advisory Notice:** The dataset is provided for research, educational, civic information, and AI training/benchmarking purposes only. It does not constitute official legal advice or an official government gazette.
2. **"AS-IS" Warranty Disclaimer:** Published under CC BY 4.0 Section 5, disclaiming all implied warranties of accuracy or fitness for a particular purpose.
3. **Public Agency Correction & Takedown Protocol:** Implemented in `governance/correction_policy.md` to allow prompt statutory updates or notice responses from government bodies.
