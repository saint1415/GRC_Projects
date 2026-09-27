# SOC 2 Readiness Summary: Cris Santos Company | Finance and Insurance | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union (member-owned federal credit union) |
| Tier / Vertical | Micro / Finance and Insurance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Credit union readiness self-assessment (`soc2-readiness.csv`), used to answer the cyber insurer's renewal questionnaire and to structure the annual board report |
| Part B | Core processor SOC 2 Type 2 and SOC 1 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-18 to 2026-08-20 by the ISO with the independent IT audit consultant; approved by the President and CEO 2026-08-31 |

## 1. Why SOC 2 for this organization
A community credit union is **not** a SOC 2 service organization. It serves its members; it does not provide services to other businesses. The Trust Services Criteria are used here for three practical reasons.

**A. Answering the cyber insurer.** The cyber policy renews on 2026-11-01 and the renewal questionnaire is due 2026-10-31. Its questions on governance, access, MFA, backups, incident response, and vendor oversight follow the Trust Services Criteria. The credit union will answer with this self-assessment and the POA&M (P07), and name the ISO as the security contact.

**B. Structuring the board report.** Appendix A III.F asks for an annual report on the program's status. The criteria give the volunteer board a familiar, complete checklist.

**C. Relying on the core processor.** The core processor carries most of the credit union's inherited controls (P02 section 10.2). Its SOC reports are the evidence for those controls, and reviewing them is part of the service provider monitoring in Appendix A III.D.3, which says the credit union should review audits, summaries of test results, or equivalent evaluations of its service providers.

**Assurance alternatives in this vertical.** Regulators do not ask a credit union for a SOC 2 report. NCUA examinations and the annual supervisory committee audit (Part 715) are the credit union's own assurance; SOC 1 and SOC 2 reports from the core processor and other providers are the assurance over vendors. **The credit union will not get a SOC 2 audit.** Nobody has asked for one, and most controls were defined in August 2026, far short of the operating period a Type 2 report needs.

**Why Confidentiality and not another category.** The core objective of Appendix A (II.B) is the security and confidentiality of member information, and the insurer's questionnaire asks how member data is classified, stored, and disposed of. Availability depends mostly on vendors and is handled through the BIA (P05) and vendor SOC reviews. Processing Integrity is covered by the core processor's SOC 1 report. Privacy notices follow Regulation P and were not requested.

## 2. System description (scope)
- **Services:** deposit, loan, wire, card, and online banking services for about 6,400 members.
- **Infrastructure and software:** the Core and Digital Banking Platform (SSP, P02): core, online banking, wire portal, productivity suite, imaging server, 11 computers and 2 check scanners, office network.
- **People:** 7 employees, the board, the Supervisory Committee, and the MSP.
- **Data:** member information (NPI), wire instructions, credentials, SAR information.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 7 | 17 | 9 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: ISO designated in writing; roles defined
- CC3.1, CC3.2, CC3.3: risk tolerance set; 2026 risk assessment done, with fraud scenarios (BEC, account takeover, embezzlement)
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked and reported
- CC6.4: physical security (keyed entry, alarm, vault, cameras)

**Not ready:**
- CC2.1: no inventory of where member information is stored
- CC3.4 and CC8.1: changes, including the AI scoring add-on, made without the credit union's recorded approval
- CC6.2 and CC6.3: access granted and removed without a process (the former MSR's account)
- CC7.1, CC7.2, CC7.3: no vulnerability scanning, monitoring, or incident records
- CC7.5: recovery unproven (the same gap as risk R-010)

## 4. Evidence inventory
The insurer's questionnaire asks for evidence. What the credit union can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| ISO designation; POL-02, POL-03, POL-04; board minutes | CC1.2, CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC3.3, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Core processor SOC review | CC9.2 | Yes | Digital banking provider review (2026-11); bridge letter (2026-10) |
| MFA settings for the suite, admin console, and wire portal | CC6.1 | Yes | Cloud console MFA screenshots (2026-09) |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Wire file callback sampling | CC1.5, CC6.6 | No | Monthly from 2026-10 |
| Restore test records | CC7.5 | No | Quarterly from 2026-09 |
| Training and phishing exercise records | CC1.4, CC2.2 | BSA training only | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |
| Device disposal certificates; mailbox clean-up checks | CC6.5, C1.1, C1.2 | Paper shredding only | From 2026-10 |

## 5. Findings from the core processor reports (Part B)
- **Opinions:** SOC 2 Type 2 and SOC 1 Type 2, unqualified, 12 months ending 2026-03-31. One SOC 2 exception (3 of 40 sampled changes lacked approval), remediated.
- **Availability:** the stated RTO of 8 hours and RPO of 15 minutes **do not fully meet the BIA** (RTO 4 h for teller services). Offline teller mode covers one business day. The RPO meets the BIA.
- **Controls the credit union must run.** The reports list complementary user entity controls: user setup and removal, role and override assignment, review of user activity and exception reports, restricting access to authorized locations, and protecting downloaded balance files. Three are open gaps at the credit union: removal (POAM-001, POAM-005), report review (POAM-007), and the unencrypted desk that holds the balance file (R-012). **The processor's controls protect the credit union only once those gaps are closed.**
- **Follow-ups:** a bridge letter to 2026-09-30; written confirmation of the Part 749.2(b) language; an incident notice side letter fast enough for the 72-hour NCUA clock.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC6.1, CC6.2, CC7.3 | Acknowledgments; reporting cards (POAM-010); cloud console MFA (POAM-003); onboarding checklist (POAM-001); incident log |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC2.3, CC3.4, CC5.2, CC5.3, CC6.3, CC6.5, CC6.6, CC6.7, CC6.8, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Quarterly board status; training (POAM-006); inventory; change approval; termination process (POAM-005); member MFA; secure upload; EDR; scanning; log review (POAM-007); tabletop and restore tests (POAM-008, POAM-009); continuity plan; vendor reviews (POAM-013); mailbox clean-up |
| 2027 Q1 (by 2027-03-31) | CC5.1 | Remaining partially implemented SSP controls closed through the POA&M |

**Response to the insurer:** send this summary, the readiness checklist, and the POA&M by 2026-10-31, and commit to an updated self-assessment with the August 2027 board report.
