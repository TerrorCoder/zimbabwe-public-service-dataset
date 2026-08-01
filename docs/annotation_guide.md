# Zimbabwe Public Service Multilingual Annotation & Translation Guide

**Supervised by:** Dr. Kudzai Gotosa (Linguist, University of Zimbabwe)  
**Maintained by:** Dataprenuers AI Engineering Team  
**Languages:** English (`en`), Shona (`sn`), Ndebele (`nd`)  

---

## 1. Overview & Objective

To ensure high evaluation quality for Retrieval-Augmented Generation (RAG) and Question-Answering (QA) models, each public service record in the dataset is annotated with natural user questions/intents across **English, Shona, and Ndebele**.

This guide defines the linguistic rules, domain terminology translations, and intent phrasing standards for annotators and reviewers.

---

## 2. Intent Phrasing Principles

1. **Natural Citizen Phrasing**: Draft questions as ordinary citizens or informal traders ask them, using everyday conversational language rather than rigid bureaucratic jargon.
2. **Intent Diversity**: For each record (`SVC-###`), provide 5 intent variants covering distinct information needs:
   - **Procedure/Method Intent**: "How do I apply for X?" / "Ndinonyoresa sei X?"
   - **Cost/Fee Intent**: "How much does X cost?" / "X inodhura marii?"
   - **Prerequisite/Requirements Intent**: "What documents are needed for X?" / "Ndezvipi zvinodiwa paX?"
   - **Turnaround Time Intent**: "How long does X take?" / "X inotora mazuva mangani?"
   - **Location/Access Intent**: "Where do I get X?" / "Ndingawana kupi X?"

---

## 3. Standard Domain Glossary (English - Shona - Ndebele)

| English Term | Shona Equivalent | Ndebele Equivalent | Notes / Guidance |
| :--- | :--- | :--- | :--- |
| **Passport** | Pasipoti | Ipasipoti | Retain loan word as commonly understood |
| **Birth Certificate** | Chitupa chemwana / Pepa rekuberekwa | Isithupha somntwana / Incwadi yokuzalwa | Distinguish between long and short form |
| **National ID** | Chitupa chemusoro / ID | Isithupha sobuntu / I-ID | Commonly referred to as ID |
| **Tax Clearance** | Mutero wakachena / Tax Clearance (ITF263) | I-Tax Clearance egcweleyo | Reference official ITF263 code |
| **Company Registration** | Kunyoresa kambani | Ukubhalisa ikhamphani | Covers PBC and Pvt Ltd |
| **Fee / Cost** | Mari inodhura / Muripo | Yimbuyelo / Imali ebizwayo | Explicitly specify USD or ZiG currency |
| **Requirements** | Zvinodiwa / Zvinyorwa | Izincwadi ezidingakalayo | Refers to supporting documents |
| **Turnaround Time** | Mazuva anotorwa / Nguva inonoka | Isikhathi esithathwayo / Insuku | Standard vs emergency processing |

---

## 4. Annotation & Verification Workflow

```
[1. Intent Draft by AI Engineer] ──> [2. Peer Linguistic Review] ──> [3. Native Speaker Sign-off] ──> [4. Release Tag]
```

1. **Drafting Phase**: Initial intent variations drafted and tagged as `draft-quality`.
2. **Peer Review**: Second team member reviews phrasing for grammatical consistency.
3. **Native Speaker Verification**: Qualified Shona/Ndebele language reviewer validates natural phrasing and terminology accuracy.
4. **Adjudication**: Any disagreement is logged and resolved by the Team Lead (Lincoln Tinaye Rwodzi).
