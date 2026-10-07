# SOC 2 Readiness Summary: Cris Santos Company | Emergency Services | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (licensed private ambulance service) |
| Tier / Vertical | Small / Emergency Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. Security-only self-benchmark; no CPA examination planned |
| Part A | Company self-benchmark against the Security criteria (`soc2-readiness.csv`) |
| Part B | ePCR vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-21 by the IT Manager |

## 1. Why SOC 2 for this organization
**The company is not a SOC 2 service organization.** SOC 2 reports on controls at an organization that provides services to other businesses, where those controls affect the user entities' own security or reporting. The company delivers ambulance care and transport to patients. It receives patient information from hospitals and the county for treatment and dispatch, as a covered entity in its own right, not as a business associate processing data on their behalf. No customer relies on the company's systems to run its own controls. A SOC 2 report would therefore have no natural audience, and no customer has asked for one. The vertical overlay names no sector-specific assurance alternative for Emergency Services.

SOC 2 still helps in two ways:

**A. A structured answer to the county.** The county ambulance service agreement is up for renewal in 2027. The county's renewal packet includes a security questionnaire about the CAD-to-CAD interface and dispatch continuity. The company uses the Security criteria (CC1-CC9) as a **self-benchmark** to answer it consistently and to track progress. This is not a CPA-issued report, and it will not be described as one.

Why Security only:
- The county asks about security and continuity of the interface. It does not ask for availability, confidentiality, processing integrity, or privacy commitments of the kind a service organization makes to its customers.
- Dispatch availability is covered by the contingency work under CC7.5 and CC9.1, the BIA (P05), and the POA&M.
- Patient privacy is governed by the HIPAA Privacy Rule, not by the TSC Privacy criteria.

**B. Third-party risk management.** The company relies on its ePCR vendor for the patient care record, hospital delivery, and state data export, and inherits controls from it (P02, P04). The vendor's SOC 2 Type 2 report is the evidence for those controls. The company reviews it every year (HIPAA 164.308(b), SA-9). The billing vendor's report will be requested next (P04).

## 2. System description (scope)
- **Services:** ambulance dispatch and patient care documentation, including the county CAD-to-CAD interface.
- **Infrastructure and software:** the Dispatch and Patient Care Platform (SSP, P02).
- **People:** 60 workforce members and the MSP.
- **Data:** CAD incident data, call recordings, ePHI in patient care records, and workforce data.
- **Procedures:** POL-01 to POL-05, the manual dispatch binder, and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 20 | 9 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: roles are designated
- CC3.1 and CC3.2: objectives and risk analysis are done
- CC4.2: deficiencies are tracked

**Not ready:**
- CC3.4 and CC8.1: no change management (the AI triage module was switched on without review)
- CC6.1 and CC6.3: shared CAD accounts, late removal, excess rights
- CC6.8, CC7.1, and CC7.2: no EDR, scanning, or monitoring
- CC7.5: recovery untested (the same gap as risks R-001 and R-002)
- CC9.2: vendor management

## 4. Findings from the ePCR vendor report (Part B)
- **Opinion:** Type 2, unqualified. One change-management exception at the vendor, remediated.
- **Availability:** the vendor's stated RTO of 4 hours and RPO of 15 minutes **meet the company's BIA** for patient care documentation (BP-03: RTO 8 h, RPO 1 h).
- **Controls the company must run.** The report lists controls the customer must operate for the vendor's controls to work (complementary user entity controls): user provisioning and timely removal, MFA through the customer's identity provider, role assignment, review of access audit reports, and security of devices that store offline records. Two are open gaps at the company: removal timing (POAM-001) and audit review (POAM-009). **The vendor's controls only protect the company once those gaps are closed.**
- **Follow-ups:**
  - Obtain a bridge letter through 2026-07-31.
  - Confirm that the vendor reviews its carved-out hosting provider's SOC 2 report.
  - Ask for a monthly EMSTARS export confirmation report.
  - Negotiate 24-hour notice of security incidents at BAA renewal.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.3, CC9.2, CC2.2, CC7.3-7.4, CC6.8, CC7.1 | Departure tickets, signed BAAs, policy acknowledgments, tabletop report, EDR deployment, first scan |
| 2027 Q1 | CC6.1, CC7.2, CC7.5, CC8.1, CC3.4 | Named CAD accounts, alert tickets, restore test and drill records, change log |
| 2027 Q2 | CC9.1, CC2.3, CC1.2, CC3.3 | Alternate dispatch drill, county interface terms, owner review minutes, updated risk analysis |

**Response to the county:** answer the questionnaire from this self-benchmark, attach the POA&M (P07) and the manual dispatch procedure summary, and commit to an update before the 2027 renewal.
