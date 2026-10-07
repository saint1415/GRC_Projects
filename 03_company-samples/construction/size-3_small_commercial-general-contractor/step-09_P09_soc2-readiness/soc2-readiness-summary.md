# SOC 2 Readiness Summary: Cris Santos Company | Construction | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (commercial and institutional building general contractor) |
| Tier / Vertical | Small / Construction |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only, as a self-benchmark |
| Part A | Security-only self-benchmark (`soc2-readiness.csv`) |
| Part B | Review of the project management platform vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the IT Manager |

## 1. Why SOC 2 for this organization
**The company is not a SOC 2 service organization, and it is not preparing for a SOC 2 audit.** SOC 2 reports on controls at a company that provides services to other businesses, where those services affect the security of the customer's own systems or data. A general contractor builds buildings. Owners do not rely on the company's IT systems to run their operations. The technology and security systems group installs and commissions client systems but does not operate them afterward, and it sells no managed service.

**What owners and agencies actually ask for instead:**
- **Federal agencies:** compliance with FAR 52.204-21 and FAR 52.204-25, which are already in the contracts. For DoD work, a current CMMC Level 1 (Self) status with an affirmation in SPRS (32 CFR 170.15). **CMMC is the assurance mechanism that matters for this company** (P03).
- **Private and institutional owners:** occasional security questionnaires, mostly about how the company protects owners' drawings and facility security details, and increasingly about how it prevents payment fraud.

SOC 2 appears here for two reasons:

**A. Security-only self-benchmark.** The Trust Services Criteria give a well-known, complete checklist for the company's own control environment. Scoring against the Security category (CC1-CC9) shows how far the company is from a mature program. The results also answer owner questionnaires consistently. No other category is in scope, because the company makes no availability, confidentiality, processing integrity, or privacy commitments to customers under a SOC 2 system description.

**B. Third-party risk management.** The company depends on its project management platform vendor for most of the controls around FCI and drawings (P02, P04). That vendor *is* a service organization, and its SOC 2 Type 2 report is the evidence for the inherited controls. The company reviews it every year (POL-01 4.8; SA-9).

## 2. System description (scope of the self-benchmark)
- **Services:** construction project delivery, billing, and subcontractor payment.
- **Infrastructure and software:** the Project Delivery and Payment Platform (SSP, P02).
- **People:** 60 employees and the MSP.
- **Data:** FCI, drawings and bid data, payment instructions, payroll, and client facility security details.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 20 | 9 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles and the CMMC Affirming Official are designated
- CC3.1 and CC3.2: objectives are set and the risk assessment is done
- CC4.2: deficiencies are tracked in the POA&M

**Not ready:**
- CC2.3: owners and subcontractors have no reliable way to confirm a payment change
- CC3.4: changes such as adopting the AI tool are not risk-assessed
- CC6.3: late terminations, stale external users, and no separation of duties for payments
- CC6.5: no media sanitization
- CC7.1, CC7.2, and CC7.3: no vulnerability scanning, and no monitoring or evaluation of mailbox and sign-in events. These are the detection gaps behind the business email compromise risk
- CC7.5: recovery is unproven (backups not isolated or tested)
- CC8.1: no change management

Most gaps overlap with the FAR 52.204-21 gaps in P03, so one remediation plan (the P07 POA&M) serves both.

## 4. Findings from the vendor report (Part B)
- **Opinion:** Type 2, unqualified, for the 12 months ending 2026-04-30. One change-approval exception at the vendor, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 1 hour **meet the BIA** for project document control (RTO 8 h, RPO 4 h; P05 BP-03).
- **Controls the company must run.** The report lists controls the customer must operate for the vendor's controls to work (complementary user entity controls): single sign-on and MFA, user provisioning and removal (including external collaborators), permission assignment, activity log review, and keeping the customer's own exports. Three of them are open gaps at the company:
  - external user removal (POAM-001)
  - log review (POAM-005)
  - independent exports (P01 R-025)

  **The vendor's controls only protect the company's data once those gaps are closed.**
- **Government cloud status:** the vendor does not claim FedRAMP Moderate equivalence. That is fine for FCI. It would matter only if the company accepted covered defense information (DFARS 252.204-7012(b)(2)(ii)(D)), which it has decided not to do before 2028.
- **Follow-ups:** put the 72-hour incident notice in the contract, and request the bridge letter each year.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.2, CC2.3, CC6.3, CC6.5, CC7.2, CC7.3, CC7.4 | Policy acknowledgments, owner remittance notices, termination tickets, sanitization certificates, alert and review records, tabletop report |
| 2027 Q1 | CC6.6, CC6.8, CC7.1, CC7.5, CC9.1 | Network change records, scan reports, restore test records, contingency plan |
| 2027 Q2 | CC3.4, CC8.1, CC1.2, CC9.2 | Change log, new-vendor risk reviews, owner review minutes, vendor SOC 2 reviews |

**Use of this assessment.** Answer owner security questionnaires from this checklist and the P03 gap analysis. Do not describe it as a SOC 2 report or an attestation. Re-run the self-benchmark in August 2027, after the CMMC Level 1 self-assessment cycle.
