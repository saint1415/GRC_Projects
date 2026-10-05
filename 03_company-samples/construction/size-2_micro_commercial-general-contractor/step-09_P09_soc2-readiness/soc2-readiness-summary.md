# SOC 2 Readiness Summary: Cris Santos Company | Construction | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Tier / Vertical | Micro / Construction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) plus Confidentiality (C1), as a readiness self-assessment |
| Part A | Security and Confidentiality self-assessment (`soc2-readiness.csv`) |
| Part B | Review of the SYS-01 vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 by the Office Manager with the Project Manager and Estimator |
| Approved | 2026-08-31 by the Owner and President |

## 1. Why SOC 2 for this organization
**The company is not a SOC 2 service organization, and it is not preparing for a SOC 2 audit.** SOC 2 reports on controls at a company whose services affect the security of its customers' own systems or data. A general contractor builds and renovates buildings. Owners do not rely on the company's IT systems to run their operations.

**What owners and agencies actually ask for instead:**
- **Federal agencies:** compliance with FAR 52.204-21 and 52.204-25, which are already in FC-1. For the expected DoD job, a current CMMC Level 1 (Self) status with an affirmation in SPRS (32 CFR 170.15). **CMMC is the assurance mechanism that matters for federal work** (P03).
- **Private and institutional owners:** security questionnaires. In July 2026 a private hospital system that the company wants to work for sent its contractor security questionnaire. It must be answered by 2026-10-15 before the hospital will release facility drawings, infection-control plans, and security system layouts. The questionnaire asks about protecting confidential owner information and about payment fraud.

SOC 2 appears here for two reasons:

**A. Security plus Confidentiality self-assessment.** The Trust Services Criteria give a well-known, complete checklist. Scoring against Security (CC1-CC9) and Confidentiality (C1) lets the company answer the hospital questionnaire, and later ones, consistently and honestly. Confidentiality was chosen as the second category because owners' drawings and security details are what owners entrust to the company. Availability, Processing Integrity, and Privacy are out of scope: the company makes no such commitments to customers under a SOC 2 system description.

**B. Third-party risk management.** The company depends on its project management and pay application platform (SYS-01) for most controls around drawings and FCI (P02, P04). That vendor *is* a service organization, and its SOC 2 Type 2 report is the evidence for the inherited controls. The company reviews it every August (POL-02 A.5; SA-9).

## 2. System description (scope of the self-assessment)
- **Services:** renovation and tenant improvement construction, progress billing, and subcontractor payment.
- **Infrastructure and software:** the Project and Payment System (SSP, P02).
- **People:** 7 employees (5 with system accounts) and the MSP.
- **Data:** owners' drawings and security details, FCI, bids and pricing, payment instructions, and payroll.
- **Procedures:** POL-02 to POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 19 | 10 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total in scope (35)** | **4** | **20** | **11** | |

**Ready:**
- CC1.3: the security lead and the CMMC Affirming Official are designated
- CC3.1 and CC3.2: objectives are set and the risk assessment is done
- CC4.2: deficiencies are tracked in the POA&M

**Not ready:**
- CC1.4: nobody, including the security lead, has security training
- CC2.3: owners have no reliable way to confirm a payment change, and outsiders have no security contact
- CC3.4: new tools, such as the AI estimating trial, are adopted without review
- CC6.3: late removal of a departed employee and one person controlling vendor bank details
- CC6.5 and C1.2: no record that devices or leased printer storage were wiped
- CC7.1, CC7.2, and CC7.3: no vulnerability scanning, and no monitoring or evaluation of mailbox and sign-in events. These are the detection gaps behind the business email compromise risk
- CC7.5: recovery is unproven
- CC8.1: no change records

Most gaps overlap with the FAR 52.204-21 gaps in P03, so one remediation plan (the P07 POA&M) serves both.

**Evidence inventory.** For each in-scope criterion, the `evidence` column names the record that exists today. The records that exist are: P01 to P10 deliverables, the MSP's monthly reports and exports, the SYS-01 vendor's SOC 2 report and bridge letter, user exports, and the FC-1 submittal log. The records still missing are the ones the questionnaire will ask for first: signed policy acknowledgments, training completions, a call-back log, user review records, restore test results, and wipe certificates.

## 4. Findings from the vendor report (Part B)
- **Opinion:** Type 2, unqualified, for the 12 months ending 2026-03-31, with no exceptions.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** for project documents (RTO 8 h, RPO 4 h; P05 BP-03).
- **Controls the company must run.** The report lists controls the customer must operate for the vendor's controls to work (complementary user entity controls): MFA for its users, adding and removing users (including external collaborators), assigning permissions, reviewing activity, and keeping its own exports. Four of them are open gaps at the company:
  - MFA not enforced for company users (POAM-007)
  - users from closed projects not removed (POAM-001)
  - no activity review (POAM-005)
  - no company export of drawings and pay app packages (POAM-013)

  **The vendor's controls protect the company's data only once those gaps are closed.**
- **Government cloud status:** the vendor does not claim FedRAMP Moderate equivalence. That is fine for FCI. It would matter only if the company accepted covered defense information (DFARS 252.204-7012(b)(2)(ii)(D)), which it has decided not to do.
- **Follow-ups:** get the 72-hour incident notice into an order form or addendum (today the company is on click-through terms), and request the bridge letter each year.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC5.3, CC6.4 | Policy acknowledgments, owner remittance notices, the call-back log, the visitor sheet, the key list |
| 2026 Q4 | CC1.4, CC3.4, CC6.3, CC6.5, CC6.7, CC7.2, CC7.3, CC7.4, CC7.5, C1.1, C1.2 | Training completions, new-tool approvals, user reviews, wipe certificates, alert and review records, tabletop report, restore test record |
| 2027 Q1 | CC6.6, CC6.8, CC7.1, CC8.1, CC9.2 | Guest Wi-Fi configuration, scan reports, change log, MSP and payroll vendor reviews |

**Use of this assessment.** Answer the hospital questionnaire from this checklist, the P03 gap analysis, and the P07 results, and say plainly which items are still in progress. Do not describe it as a SOC 2 report or an attestation. Re-run the self-assessment in August 2027, after the first CMMC Level 1 self-assessment cycle.
