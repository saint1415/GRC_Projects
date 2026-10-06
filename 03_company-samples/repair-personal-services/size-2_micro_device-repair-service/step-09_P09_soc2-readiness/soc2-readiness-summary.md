# SOC 2 Readiness Summary: Cris Santos Company | Other Services | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (independent electronics and device repair shop) |
| Tier / Vertical | Micro / Other Services (except Public Administration) |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Part A | Shop readiness self-assessment (`soc2-readiness.csv`), used to answer the property management account's security questionnaire |
| Part B | Ticketing and POS vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-17 to 2026-08-21 by the Shop Manager with the independent consultant; approved by the Owner 2026-08-31 |

## 1. Why SOC 2 for this organization
A 7-person repair shop is **not** a SOC 2 service organization. It repairs devices; it does not operate systems that its customers rely on for their own controls. The Trust Services Criteria are used here for two practical reasons.

**A. Answering a questionnaire.** In July 2026 the shop's largest business account, a property management company that sends its staff laptops and phones for repair, sent a vendor security questionnaire. Its questions follow the Trust Services Criteria for Security and Confidentiality: how the shop controls who can reach devices and data in its custody, and how it deletes data afterwards. The shop will answer with this self-assessment, the POA&M (P07), and a named security contact. The response is due 2026-10-30.

**The shop will not get a SOC 2 audit.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the shop's controls were defined in August 2026. An audit would also cost far more than the account asked for. The questionnaire instructions accept a self-assessment.

**B. Relying on the ticketing and POS vendor.** SYS-01 holds every customer record and carries most of the shop's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report is the evidence for those controls. Reviewing it each year is part of vendor oversight (POL-02 A.6; CSF 2.0 GV.SC-07).

**Why Confidentiality and not another category.** The account's real question is what happens to its staff's data while their devices are in the shop and after they come back. That is Confidentiality: identifying confidential information (C1.1) and disposing of it (C1.2). It also matches the shop's own biggest risks (P01 R-001, R-004, R-005). Availability matters less to the account, which has spare laptops, and the shop's availability depends mostly on SYS-01 (covered in Part B). Processing Integrity and Privacy were not requested.

## 2. System description (scope)
- **Services:** device repair, data transfer, and basic data recovery for consumers and 18 business accounts.
- **Infrastructure and software:** the Service Ticketing and Point-of-Sale System (SSP, P02): SYS-01, the P2PE terminals, the productivity suite, office and bench endpoints, bench storage, shop network, and cloud backup.
- **People:** 7 workforce members and the MSP.
- **Data:** customer records, device content in custody, passcodes (until purged), card data (inside the P2PE terminals only).
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 16 | 12 | 0 |
| Confidentiality (C1, 2) | 0 | 0 | 2 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security and Privacy Lead designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked in the POA&M

**Not ready:**
- CC1.4: no training
- CC2.1: no inventory of devices, terminals, or customer data locations
- CC2.3: the intake form's privacy promise is not true in practice
- CC3.4 and CC8.1: changes (such as the AI assistant) made without review
- CC6.2, CC6.3: access granted and removed without a process (the former technician's account)
- CC6.5: no verified wiping of recycled devices
- CC7.1, CC7.2, CC7.3, CC7.5: no scanning, monitoring, incident records, or tested recovery
- C1.1 and C1.2: at fieldwork, passcodes sat in open notes, technicians had no access rule, and customer data was kept indefinitely

**Confidentiality is the weak spot, and it is the account's main question.** Both C1 criteria are Not ready. The honest answer to the account is that the rules were written in August 2026 (POL-04 4.3 to 4.7) and the technical fixes are dated in the POA&M, with the passcode purge and the restricted field due 2026-10-31, the same week the response is due.

## 4. Evidence inventory
The questionnaire asks for evidence. What the shop can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3, C1.1 | Yes | Signed acknowledgments and confidentiality agreements (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Ticketing vendor SOC 2 review | CC9.2 | Yes | Bridge letter (2026-10) |
| Processor P2PE listing and SAQ P2PE (prior year) | CC6.7 | Yes | 2026 SAQ (2026-12) |
| MSP monthly report (patching, antivirus, encryption) | CC5.2, CC6.8 | Yes (July 2026) | Monthly |
| Account reconciliation and log review checklists | CC6.2, CC6.3, CC7.2 | No | Monthly from 2026-10 |
| Sanitization records per device | CC6.5, C1.2 | No | From 2026-10 |
| Retention purge records (bench storage, ticket notes) | C1.2 | No | From 2026-10 |
| Restore test records | CC7.5 | No | Quarterly from 2026-09 |
| Training and phishing simulation records | CC1.4, CC2.2 | No | From 2026-10 |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the ticketing vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-05-31, **Security only**. One exception (a missed quarterly access review for vendor support staff), remediated.
- **Recovery:** the system description states hourly backups (RPO 1 hour, which meets the BIA) and an 8-hour recovery time target, which **does not meet** the 4-hour RTO for intake and payment (P05). The shop covers the gap with paper intake and the terminals' standalone mode.
- **The AI assistant is outside the report.** The vendor launched it in April 2026, after most of the report period, and the system description does not mention its model provider. The report gives no assurance over it; P10 sets the conditions instead.
- **Controls the shop must run.** The report lists complementary user entity controls: named users, role assignment, MFA, removal of departed users, review of activity and exports, and protecting data typed into free-text fields. Four are open gaps at the shop (POAM-001, POAM-005, POAM-011). **The vendor's controls protect the shop's data only once those gaps are closed.**
- **Follow-ups:** request a bridge letter to 2026-09-30; ask for the AI model provider's name and data terms; ask for 24-hour incident notice and a 4-hour recovery target at renewal.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.2, CC2.3, CC6.2, CC7.3, CC7.5 | Acknowledgments and confidentiality agreements (POAM-013); intake notice rewrite; joiner checklist and named counter accounts (POAM-001); incident log (POAM-009); first restore test (POAM-007) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.1, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.3 to CC6.8, CC7.1, CC7.2, CC7.4, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Monthly oversight notes; training (POAM-004); inventory; change approval; passcode purge and restricted field (POAM-011); role clean-up (POAM-002); sanitization records (POAM-010); network separation and EDR (POAM-006); USB control (POAM-012); log review (POAM-005); tabletop; contingency plan; vendor terms (POAM-014) |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk assessment |

**Response to the property management account:** send this summary, the readiness checklist, and the POA&M by 2026-10-30, name the Shop Manager as security contact, offer to wipe and certify the account's devices to SP 800-88 Rev. 2 on request, and commit to an updated self-assessment in April 2027.
