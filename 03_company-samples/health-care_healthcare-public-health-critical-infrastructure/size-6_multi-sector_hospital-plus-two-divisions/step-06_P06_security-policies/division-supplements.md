# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead (for the College, the College IT director); alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA, one severity scale, no contract no data, minimum-necessary protocols between covered entities | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, Group AI Standard (P10), device security review standard | Group CISO |
| **Division supplement** | Regulator-specific and system-specific standards (for example, hospital downtime and diversion, MA utilization management, Title IV notices) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Hospital System | v2026 | 2026-08-20 (to the final 2026 group policies) | Aligned | Attest by 2026-12-31 |
| Health Plan | v2026 | 2026-08-25 | Aligned | Attest by 2026-12-31 |
| College | None. Pre-acquisition IT standards (2022) still in use | n/a | **Not issued** (P01 GR-18, ED-012); conflicts listed in section 4 | Issue the first College supplement by 2026-12-31 |

## 3. What each supplement adds
### 3.1 Hospital System supplement (covered entity; business associate of 64 community-connect practices)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Clinical downtime | Downtime workstations on every unit tested each quarter; reports refreshed every 2 hours; paper workflows drilled each year in every ED, pharmacy, and laboratory | POL-03 4.6 | 164.308(a)(7)(ii)(C); 482.15(b)(5) |
| Diversion during IT outages | Hospital incident command decides diversion with the ED medical lead when ED care, laboratory, imaging, or communications will exceed their BIA MTD; status reviewed every 2 hours; walk-in and on-property arrivals always screened | POL-03 4.6 | 42 CFR 489.24; 482.15(a)(2), (c)(7) |
| Cyber annex | The P08 runbook is the cyber annex of the unified emergency plan and is reviewed with it at least every 2 years | POL-01 4.14 | 482.15(a), (f)(4) |
| Students and trainees | Accounts only from the secure roster feed; end date at rotation end; MFA; training before activation; monthly reconciliation with each school | POL-02 4.4 | 164.308(a)(3)(ii)(A)-(C); 164.312(d) |
| Medical devices | Device security review before purchase; unsupported devices in restricted zones; vendor access only through PAM | POL-01 4.13; POL-02 4.10 | 164.308(a)(1)(ii)(B); C-HPH-R04 (procurement lever) |
| EHR break-glass | Break-glass access reviewed by the Privacy Officer within 2 business days | POL-02 4.9 | 164.312(a)(2)(ii) |
| Privacy monitoring | Weekly EHR access monitoring review, including VIP, coworker, and employee-as-patient rules; student accounts included | POL-05 4.1 | 164.308(a)(1)(ii)(D) |
| Decision support | Every patient care decision support tool inventoried; input variables reviewed; mitigation documented; thresholds changed only through change control | POL-01 4.12; POL-05 4.9 | 45 CFR 92.210 |
| Community-connect practices | Incident notices to practices per their BAAs; practice users federated with MFA | POL-03 4.4; POL-02 4.12 | 164.410; 164.314(a)(2)(iii) |
| Paper records | Health information management custody log; back-entry schedule for outages longer than 24 hours | POL-04 4.8 | 482.15(b)(5) |

### 3.2 Health Plan supplement (covered entity; MA organization; state-licensed insurer and HMO; business associate of 40 ASO plans)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| UM and AI | No UM policy, procedure, or model-assisted workflow used without UM committee approval; reviewers document consideration of the enrollee's medical history, physician recommendations, and clinical notes | POL-01 4.12 | 42 CFR 422.137(b); 422.101(c)(1)(i) |
| Adverse decisions | Physician or appropriate professional review before any expected adverse medical necessity decision | POL-01 4.12 | 42 CFR 422.566(d) |
| Enrollee records | Purposes documented for every system and every feed received from the Hospital System | POL-04 4.3 | 42 CFR 422.118(a) |
| State insurance notices | List of states that enacted a version of NAIC Model #668, with commissioner contacts and deadlines, kept current in the notification matrix | POL-03 4.5 | N52-R07 |
| ASO plan notices | Notice register by each employer plan's BAA terms | POL-03 4.4 | 164.410 |
| Broker and member authentication | MFA required for brokers; no SMS-only after 2027-03-31; member step-up MFA | POL-02 4.12 | 164.312(d) |
| Call-center verification | One-time code to the member's registered phone before disclosing PHI | POL-05 4.1 | 164.514(h) |

### 3.3 College supplement (Title IV participant; FERPA institution) - first issue due 2026-12-31
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Qualified Individual | College IT director designated; written annual report to the board risk committee each November | POL-01 4.2 | 16 CFR 314.4(a), (i) |
| Risk assessment | Written assessment each year and after material changes, with the 314.4(b)(1) criteria | POL-01 4.3 | 16 CFR 314.4(b) |
| MFA | MFA for every user of the SIS and financial aid system, faculty included, by 2026-11-30 | POL-02 4.3 | 16 CFR 314.4(c)(5) |
| Education records | Consent before disclosure to clinical sites; rosters only through the secure feed; reasonable methods for file shares | POL-04 4.4; POL-02 4.2 | 34 CFR 99.30; 99.31(a)(1)(ii) |
| Notices | FSA breach report immediately; FTC notice within 30 days of discovery for 500 or more consumers | POL-03 4.5 | SAIG Enrollment Agreement; 16 CFR 314.4(j) |
| Retention | Disposal schedule for financial aid documents | POL-04 4.7 | 16 CFR 314.4(c)(6) |
| Teaching | De-identified case material only; no patient information in the LMS | POL-05 4.8 | 164.514(b) (hospital duty, enforced by the College) |
| Proctoring and AI | Proctoring flags reviewed by faculty before any academic action; face data retention limited by contract | POL-01 4.12 | P10; Fla. Stat. 501.702 (biometric definition, applicability unsettled) |

## 4. College drift: pre-acquisition standards that conflict with 2026 group policy
The College's 2022 IT standards were written before the acquisition. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 ED-012; P07 College sample).

| Topic | College standard (2022) | Group policy (2026) | Effect |
|---|---|---|---|
| MFA | Email only | All remote, email, privileged, and customer-information systems (POL-02 4.3) | SIS and financial aid accounts exposed (ED-001; POAM-020) |
| Risk assessment | Every 3 years | Annually and after major changes (POL-01 4.3) | No reassessment after the 2025 file share move (POAM-019) |
| Incident response | College plan with its own severity scale | One group scale and plan (POL-03 4.2) | FSA and FTC notices outside the group matrix (POAM-021) |
| Reporting | Updates to the College president | Written annual report to the board risk committee (POL-01 4.2) | 16 CFR 314.4(i) not met (POAM-025) |
| Training | Annual module, no phishing exercises | Monthly phishing exercises (POL-05 4.3) | Phishing exposure (ED-011, ED-015; POAM-022) |
| Data sent to hospitals | Rosters by email | Secure roster feed (POL-04 4.4) | Misdirected or intercepted rosters (ED-003) |

**Why the drift happened.** The 2023 acquisition kept the College's IT team and standards in place while integration focused on finance and HR. **Fix:** the first College supplement, the migration to SYS-G1 by 2027-06-30, and the annual attestation required by POL-01 4.5.

## 5. Attestation
Each division security and compliance lead (for the College, the Qualified Individual) signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 for all three divisions.
