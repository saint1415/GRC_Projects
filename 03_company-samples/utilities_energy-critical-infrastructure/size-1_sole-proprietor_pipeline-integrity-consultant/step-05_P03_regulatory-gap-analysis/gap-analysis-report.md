# Regulatory Gap Analysis: Cris Santos Company | Energy | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (pipeline integrity engineering consultant) |
| Tier / Vertical | Sole Proprietorship / Energy |
| Primary regulation named for this vertical | TSA Security Directive Pipeline-2021-02G (C-ENERGY-R03): **not applicable to the consultant**; it reaches the business only through Client A's contract |
| Binding rule analyzed | 49 CFR Part 1520, Protection of Sensitive Security Information. Text read from eCFR, current through 2026-09-23 |
| Also analyzed | Client A Supplier Cybersecurity and Information Protection Addendum (contract flow-down); Fla. Stat. 501.171 (2026) for subcontractor personal information |
| Assessment dates | 2026-08-10 to 2026-08-14 (self-assessment) |
| Assessor | Engineer-owner, with the on-call IT support contractor (under NDA since 2026-08-07). Evidence is self-attested, checked on screen where possible |
| Adopted | 2026-09-11 |

## 1. Applicability

### 1.1 TSA SD Pipeline-2021-02G does not apply to the consultant
SD 02G Section II.A.1 applies the directive to "Owner/Operators of TSA-designated critical pipeline systems or facilities" that TSA has notified, and Section II.A.2 says TSA will notify any additional Owner/Operators it identifies. Section VII.P defines Owner/Operator as a person who owns or maintains operational control over pipeline facilities and whom TSA has identified as one of the most critical. The consultant owns no pipeline facility, controls none, and has never received a TSA notification. **SD 02G does not apply, and neither does SD 01G (C-ENERGY-R02)**, which has the same applicability. This matches the size substitution in the registry: a sole proprietor cannot run a transmission pipeline.

**Authorized Representative check.** SD 02G Section II.A.4 makes Authorized Representatives (Section VII.A: agents, contractors, and subcontractors authorized to perform measures in the Owner/Operator's TSA-approved Cybersecurity Implementation Plan) liable alongside the Owner/Operator for their own non-compliance. Client A's MSA states that the consultant performs no plan measures. The leak-detection data path review is advice to Client A, not a plan measure. **The consultant is not an Authorized Representative today.** If Client A ever assigns plan measures to the consultant, this analysis must be redone against those measures (G-033).

### 1.2 How the directive still reaches the consultant
Two routes:
1. **SSI.** SD 02G Section IV.B requires Client A to store and transmit its plans, reports, and assessment results consistent with 49 CFR Part 1520. The plan excerpt and zone drawing Client A gave the consultant are therefore SSI.
2. **Contract.** Client A flows its expectations down through the supplier addendum (MFA, encryption, approved services, 24-hour incident notice, return or destruction of data). These are contract terms, not TSA requirements, and are labeled that way in `gap-analysis.csv`.

### 1.3 49 CFR Part 1520 applies to the consultant directly
Part 1520 governs "the maintenance, safeguarding, and disclosure of records and information that TSA has determined to be" SSI (1520.1(a)). Its duties fall on covered persons (1520.7). The consultant is one on two grounds:
- 1520.7(j): "Each person who has access to SSI, as specified in § 1520.11." Client A's work order documents the owner's need to know under 1520.11(a)(1) (G-002).
- 1520.7(k): "Each person employed by, contracted to, or acting for a covered person ... including a person formerly in such position." Client A holds SSI with a need to know under the directive, so it is a covered person, and the consultant is contracted to it. The words "formerly in such position" mean the duties continue after the engagement ends.

There is **no size threshold** in Part 1520. Violations are grounds for a civil penalty (1520.17).

### 1.4 Florida
Fla. Stat. 501.171(1)(b) defines "covered entity" to include "a sole proprietorship ... that acquires, maintains, stores, or uses personal information." The business holds names and Social Security numbers of 5 subcontractors (W-9s), which is personal information under 501.171(1)(g)1.a.(I). So 501.171(2) (reasonable security measures) and the breach notice duties in (3) to (6) apply. The disposal duty in 501.171(8) covers "customer records," which the statute limits to records an individual provides to buy or lease a product or obtain a service. W-9s from subcontractors are not customer records, so (8) is recorded as not applicable (G-031); POL-01 applies the same disposal method anyway.

**Open question for counsel (not assumed either way).** The current (2026) statute lists "any information regarding an individual's geolocation" as a data element. Client GIS data sometimes includes landowner names next to parcel locations along the right-of-way. Whether that combination is personal information under 501.171 has not been decided here.

### 1.5 Not applicable, with reasons (rows G-032 to G-037)
- **NERC CIP (C-ENERGY-R01):** not a NERC-registered entity; no BES assets.
- **49 CFR 192.631 (C-ENERGY-R04):** applies to operators with controllers working in a control room; the consultant is neither.
- **CIRCIA (C-ENERGY-R05):** proposed only, not in effect. Under the proposal, the consultant is also below the SBA size standard for NAICS 541330 ($25.5 million) and is not a pipeline Owner/Operator required to report to TSA.
- **CEII rules:** the owner never requests CEII from FERC; client documents come under the client contracts.

## 2. Method
1. **Requirements.** Part 1520 rows follow the regulation's own section and paragraph structure, at the most granular citation that imposes a separate duty (public-domain federal text; brief quotes). The Client A addendum rows follow the contract's section numbers. Florida rows follow 501.171's subsections.
2. **Crosswalk.** All CSF 2.0 and SP 800-53 columns are an **author mapping**. NIST publishes no official mapping for Part 1520, the directives, or the contract.
3. **Evidence.** Self-attested by the owner and checked on screen with the IT support contractor: sharing reports, the 180-day activity log, account security pages, the SSI files and printout, the USB drive, and the home office on 2026-08-13.
4. **Status.** Met, Partially met, Not met, or Not applicable, as of the end of fieldwork (2026-08-14). Gaps were rated with the P01 risk scale.

## 3. Results summary
| Section | Met | Partially met | Not met | N/A |
|---|---|---|---|---|
| A. 49 CFR Part 1520 (binding) | 2 | 4 | 6 | 3 |
| B. Client A addendum (contract) | 2 | 5 | 6 | 0 |
| C. Fla. Stat. 501.171 (binding) | 0 | 1 | 1 | 1 |
| D. Vertical requirements not applicable | 0 | 0 | 0 | 6 |
| **Total (37)** | **4** | **10** | **13** | **10** |

Of the 23 unmet or partially met rows, gap risk is 6 High, 13 Moderate, and 4 Low. The Part 1520 gaps are about **where SSI is kept and who can reach it**, not about marking the original document, which arrived correctly marked. The addendum gaps show the same pattern as the risk register: the consultant has a decent device baseline (updates, antivirus, laptop encryption) and weak data handling.

## 4. Action list (half page)
In order. The first five cost little and take under a day.

| # | Action | Citation | Gap risk | Target |
|---|---|---|---|---|
| 1 | Move SSI to a separate folder shared with no one; delete the USB copy; lock up or shred the printout | 1520.9(a)(1)-(2) (G-003 to G-005) | High | 2026-09-30 |
| 2 | Hardware-encrypted backup drive; destroy the old one with a record | Addendum s.3 (G-017) | High | 2026-09-15 |
| 3 | Accounting SaaS MFA; password manager; W-9 PDFs out of the file account | 501.171(2) (G-029) | High | 2026-09-15 |
| 4 | Mark the zone drawing and the draft review; confirm with Client A | 1520.9(b), 1520.13 (G-007, G-009) | Moderate | 2026-09-30 |
| 5 | Adopt and print the P08 runbook with the 24-hour Client A clock, the TSA SSI report, and the Florida clocks | Addendum s.6; 1520.9(c); 501.171(4) (G-011, G-020, G-030) | Moderate | 2026-09-30 |
| 6 | AI tool: deletion request; follow Client A's instructions; approved-services list in POL-01 | Addendum s.4 (G-018) | Moderate | 2026-09-30 |
| 7 | Client A written approval of the GIS subcontractor; subcontractor security terms | Addendum s.5 (G-019) | Moderate | 2026-10-30 |
| 8 | Destroy 2024 Client A project data and send a certificate; close-out checklist | Addendum s.7; 1520.19(b) (G-012, G-021) | Moderate | 2026-10-30 |
| 9 | Answer the 2026 questionnaire from these deliverables; correct the 2025 answer | Addendum s.11 (G-025) | Moderate | 2026-10-30 |
| 10 | Security course and SSI awareness module | Addendum s.12; 1520.7 (G-001, G-026) | Moderate | 2026-10-30 |

High and Moderate gaps are in the risk register (P01) and the POA&M (P07).

## 5. Pending regulatory changes
- **SD Pipeline-2021-02G expires 2027-05-02 and SD 01G expires 2027-01-15** unless renewed. Renewal letters change Client A's duties, not the consultant's, but the supplier addendum may be updated to match.
- **TSA "Enhancing Surface Cyber Risk Management" NPRM** (November 7, 2024) would turn pipeline cyber requirements into permanent regulations for covered Owner/Operators. It was not final as of 2026-09-25. Its effect on contractors was not analyzed here.
- **CIRCIA final rule** (C-ENERGY-R05): not published as of 2026-09-25. Recheck when final.
- None of these is treated as a current obligation.
