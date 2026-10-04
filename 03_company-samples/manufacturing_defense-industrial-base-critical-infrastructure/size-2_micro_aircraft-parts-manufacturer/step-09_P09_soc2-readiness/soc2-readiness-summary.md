# SOC 2 Readiness Summary: Cris Santos Company | Defense Industrial Base | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts machine shop, DoD subcontractor) |
| Tier / Vertical | Micro / Defense Industrial Base |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer Customer C's supplier security questionnaire |
| Part B | Review of the MSP's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-20 by the Office Manager with the independent consultant; approved by the President 2026-08-31 |

## 1. Why SOC 2 for this organization
A 7-person machine shop is **not** a SOC 2 service organization. It makes parts; it does not provide services that affect its customers' financial reporting or systems. CMMC Level 2 is the assurance that matters for its DoD work (32 CFR Part 170), and this summary does not replace it. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a commercial questionnaire.** On 2026-07-08 Customer C, a commercial aerospace tier-1 supplier, sent a supplier security questionnaire organized by the Trust Services Criteria. Customer C shares drawings (some EAR-controlled) and wants to know they are kept confidential. It accepts a self-assessment; the response is due 2026-09-30. The company will answer with this self-assessment, the POA&M (P07), and the Office Manager as security contact. Most of the evidence is the same evidence CMMC needs, so the work is reused, not repeated.

**The company will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. The money is better spent on the CMMC roadmap.

**B. Relying on the MSP.** The MSP runs most technical controls (P02 section 10.2) and holds the keys to every system. Its SOC 2 Type 2 report is the main outside evidence of how it protects those keys. Reviewing it each year is part of supplier oversight (SA-9; POL-02 A.5).

**Why Confidentiality and not another category.** Customer C's concern is its drawings. Confidentiality (C1.1, C1.2) covers identifying and disposing of confidential information, which maps directly onto the shop's CUI problems: drawings in the wrong systems and in the trash. Availability is covered by the BIA (P05) and was not requested; Processing Integrity and Privacy do not fit the business.

## 2. System description (scope)
- **Services:** build-to-print machining for aerospace and defense customers.
- **Infrastructure and software:** the CUI Machining Enclave (SSP, P02) plus the commercial suite and ERP that hold Customer C's commercial drawings and order data.
- **People:** 7 employees and the MSP.
- **Data:** customer drawings and models (CUI and commercial confidential), NC and CMM programs, order data, employee records.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 16 | 12 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security and Compliance Coordinator designated; roles written in the SSP
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies on a POA&M

**Not ready:**
- CC1.4: no training; 4 of 5 employees could not say what CUI is
- CC2.1: incomplete inventory; no log review
- CC3.3: fraud risk not assessed
- CC6.2 and CC6.3: no access approvals or reviews; late removal
- CC6.5 and C1.2: paper drawings in the general trash; no wipe records
- CC6.7: drawings move through the commercial suite, ERP, backup cloud, and USB drives
- CC7.1, CC7.2, CC7.3: no scanning, monitoring, or incident records
- CC7.5: recovery never tested
- CC8.1: no change control

## 4. Evidence inventory
| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3, C1.1 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| MSP SOC 2 review; FedRAMP listing for the CUI suite | CC9.2 | Yes | Bridge letter and responsibility matrix (2026-10) |
| MSP monthly report (patching, antivirus) | CC6.8, CC7.1 | Yes (July 2026) | Monthly, with review notes |
| Account checks and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Shred bin service records and wipe certificates | CC6.5, C1.2 | No | From 2026-09 |
| Restore test record | CC7.5 | No | First test 2026-11 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-11 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the MSP report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-04-30, Security only.
- **The exception matches what P07 found.** The auditor found MFA not enforced for 2 of 40 sampled technician accounts on the RMM platform. P07 found the same weakness on a technician account with access to this company (R-023). The company has asked for evidence of the MSP-wide fix.
- **Carved-out subservice organizations:** the RMM platform vendor and the backup cloud. The backup cloud is the one holding CUI images and is not FedRAMP authorized, so the SOC 2 report gives no comfort on the company's biggest MSP-related gap (POAM-010).
- **Controls the company must run.** The report lists complementary user entity controls: approve technician access requests, tell the MSP when employees leave, review monthly reports, and define backup scope and retention. **All four are open gaps at the company** (POAM-001, POAM-009, POAM-010, POAM-012). The MSP's controls protect the company only once those gaps are closed.
- **What a SOC 2 report cannot do here.** It does not mention CUI, FedRAMP, U.S.-person technicians, or CMMC. Under 32 CFR 170.19(c)(2)(ii) the company still needs the MSP's services documented in its SSP and a responsibility matrix (POAM-009).
- **Follow-ups:** bridge letter to 2026-09-30; FIPS validation status of RMM and backup encryption; 24-hour incident notice in the contract amendment.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC6.4, CC6.5, CC7.3, C1.2 | Acknowledgments; questionnaire response; visitor control (POAM-006); shred bin; incident log |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC3.4, CC5.2, CC5.3, CC6.1, CC6.2, CC6.3, CC6.6, CC6.7, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, C1.1 | Monthly oversight notes; training (POAM-011); inventory (POAM-013); account process (POAM-001, POAM-012); MFA (POAM-002); VLAN (POAM-004); boundary clean-up and backup (POAM-010); MSP amendment (POAM-009); scanning; log review (POAM-007); tabletop (POAM-008); restore test; change log; contingency plan |
| 2027 Q1 | CC5.1, CC6.8 | Allowlisting; remaining SSP controls before the Level 2 self-assessment |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to Customer C:** send this summary, the readiness checklist, and the POA&M by 2026-09-30, name the Office Manager as security contact, and commit to an updated self-assessment in April 2027, after the CMMC Level 2 self-assessment.
