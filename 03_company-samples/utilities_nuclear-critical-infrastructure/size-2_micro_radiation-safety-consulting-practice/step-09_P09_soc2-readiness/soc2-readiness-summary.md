# SOC 2 Readiness Summary: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radiation safety consulting practice) |
| Tier / Vertical | Micro / Nuclear Reactors, Materials, and Waste |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Practice readiness self-assessment (`soc2-readiness.csv`), used to answer a Part 37 client's vendor security questionnaire |
| Part B | Calibration system vendor (SYS-02) SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | Part B 2026-08-20; Part A 2026-09-10, by the Office Manager with the independent consultant; approved by the owner 2026-09-15 |

## 1. Why SOC 2 for this organization
A 7-person consulting practice is **not** a SOC 2 service organization in the usual sense. It does not run a system that clients use. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a client questionnaire.** In August 2026 one of the practice's Part 37 clients, a hospital with a blood irradiator, sent a vendor security questionnaire as part of its own annual security program review. The hospital wants to know how the practice protects the security plan and approved-individual list it holds, and its questions follow the Security and Confidentiality criteria. The practice will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-10-30. A reactor client has said it will send a similar supplier questionnaire before the spring 2027 outage.

**The practice will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the practice's controls were defined in September 2026. An audit would also cost several times the practice's whole annual security budget (P01 section 4). The hospital's questionnaire accepts a self-assessment with supporting evidence.

**B. Relying on the calibration system vendor.** SYS-02 holds the practice's calibration and leak test records, the only copy of its source inventory records, and client instrument lists. Its SOC 2 Type 2 report is the evidence for the controls the practice inherits (P02 section 10.2), and reviewing it each year is part of supplier oversight (POL-02 A.5; SA-9).

**Why Confidentiality and not another category.** The client's real question is "can you keep our security information confidential?" Confidentiality (C1) covers how the practice identifies confidential information and how it disposes of it at the end of an engagement, which are the two Part 37 duties clients care about most (P03 G-010, G-017). Availability matters to the practice internally (P05) but the client did not ask about it. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** consulting RSO work, Part 37 security program services, shielding and surveys, calibration and leak tests, reactor outage support.
- **Infrastructure and software:** the Practice Business Platform (SSP, P02): productivity suite, SYS-02, accounting and payroll, 7 laptops, 2 lab workstations, USB drives used at client sites, office network, suite backup.
- **People:** 7 staff and the MSP.
- **Data:** client security information (6 Part 37 clients), client reports and instrument records, personnel records.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 15 | 12 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security Officer designated; custodian of client security information named
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked monthly
- CC6.4: physical access (locked suite, calibration room, and network closet; vendor data centers under SOC 2)

**Not ready:**
- CC6.1, CC6.2, CC6.3: client security information open to all staff; departures missed (the client's main concern)
- CC6.5 and C1.2: no return or destruction of client copies at close-out
- CC6.7: reports emailed as attachments; personal USB drives taken to plants
- CC1.4, CC2.1: no training; no inventory
- CC7.1, CC7.2, CC7.3, CC7.5: no scanning, log review, incident log, or tested recovery
- CC8.1: firewall changes made without approval (the 2024 port forward)

**What to tell the client.** The honest answer today is: "Your information is behind MFA in a business cloud service, but until 2026-10-15 every one of our 7 staff could open it. We found this ourselves, told you, and are fixing it on this schedule." That answer, with the dates, is more useful to the client's own security review than a claim the practice cannot support. Claims in the questionnaire must match this assessment, because overstated security claims to clients can be a deceptive practice under FTC Act Section 5.

## 4. Evidence inventory
The questionnaire asks for evidence. What the practice can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-10) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Client approval list (that client's rows only) and restricted folder membership report | CC6.1, CC6.2, C1.1 | No | From 2026-10-15, monthly |
| SYS-02 vendor SOC 2 review | CC9.2 | Yes | Bridge letter (2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account and folder reconciliation and log review checklists | CC6.3, CC7.2 | No | Monthly from 2026-10 |
| USB drive inventory and pre-trip scan log | CC6.7 | No | From 2026-10-15 |
| Restore test records | CC7.5 | No | Quarterly from 2026-10 |
| Close-out confirmations of returned or destroyed client copies | CC6.5, C1.2 | No | From 2026-11 (first: the 2 former clients) |
| Training and phishing exercise records | CC1.4, CC2.2 | No | From 2026-11 |
| Tabletop exercise report | CC7.4 | No | 2026-12 |

## 5. Findings from the SYS-02 vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31, covering Security, Availability, and Confidentiality. One exception (missing change approval for 2 of 40 sampled changes), remediated with an automated approval gate.
- **Availability:** the vendor's stated RTO of 8 hours and RPO of 1 hour **meet the practice's BIA** for calibration (BP-03: RTO 24 h, RPO 8 h).
- **Controls the practice must run.** The report lists complementary user entity controls: timely user removal, MFA for all users, periodic access review, and protection of exported reports. Two are open gaps at the practice: removal (POAM-001, POAM-004) and MFA for all users (POAM-005). **The vendor's controls protect the practice only once those gaps are closed.**
- **Data use.** The system description says aggregated customer data is used to develop analytics features, and the analytics features themselves are outside the tested scope. This matters for the AI pilot (P10).
- **Follow-ups:** request a bridge letter to 2026-09-30; ask for the analytics features to be brought into scope; ask for 24-hour incident notice at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q4, first half (by 2026-10-31) | CC1.1, CC2.1, CC2.2, CC2.3, CC3.3, CC5.3, CC6.1, CC6.2, CC6.3, CC6.6, CC6.7, CC7.2, CC7.3, CC7.5, C1.1 | Restricted folders (POAM-002); departure checklist (POAM-001, POAM-004); MFA on MSP-held logins (POAM-005); company drives (POAM-010); delivery rule (POAM-003); inventory; acknowledgments; first restore test (POAM-008); questionnaire response by 2026-10-30 |
| 2026 Q4, second half (by 2026-12-31) | CC1.2, CC1.4, CC1.5, CC3.4, CC5.1, CC5.2, CC6.5, CC6.8, CC7.1, CC7.4, CC8.1, CC9.1, CC9.2, C1.2 | Training (POAM-006); close-out and destruction of old copies; EDR; scans and lab network segment (POAM-012); tabletop; MSP amendment and review (POAM-013); contingency plan |

**Response to the client:** send this summary, the readiness checklist rows for Security and Confidentiality, and the POA&M items that touch client information by 2026-10-30; name the Office Manager as security contact; and commit to an updated self-assessment in April 2027, before the next annual review of the client's security program.
