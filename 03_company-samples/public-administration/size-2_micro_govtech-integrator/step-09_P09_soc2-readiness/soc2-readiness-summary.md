# SOC 2 Readiness Summary: Cris Santos Company | Public Administration | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Micro / Public Administration |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) and Confidentiality (C1) |
| Target report | None in 2026. Readiness self-assessment now; a SOC 2 Type 1 decision in 2027 Q3 (section 6) |
| Part A | Company readiness self-assessment (`soc2-readiness.csv`), used to answer the AC-02 renewal questionnaire |
| Part B | Platform vendor SOC 2 Type 2 report review (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-21 by the Operations Manager with the independent consultant; approved by the owner 2026-08-31 |

## 1. Why SOC 2 (or an alternative) for this organization
The company **is** a service organization: four agencies rely on its controls over their data in the hosted applications. Two things make the Trust Services Criteria useful now.

**A. The AC-02 renewal questionnaire.** The county's procurement office sent a security questionnaire with the 2027 renewal. It asks for one of: a SOC 2 report, GovRAMP verification, or a self-assessment against the Trust Services Criteria with a remediation plan. The response is due 2026-10-30.

**The company will not get a SOC 2 audit in 2026.** A Type 2 report needs controls that have operated over a period, usually 6 to 12 months, and most of the company's controls were defined in August 2026. A Type 1 report would show controls designed on paper that the P07 assessment found mostly not operating yet. The county accepts a self-assessment with a plan, so that is the response.

**Why not GovRAMP now.** GovRAMP (formerly StateRAMP) is the verification program state and local governments name in procurements (N92-R08; not law). The platform vendor is listed as verified, which covers the platform layer. The company's own layer (tenant configuration, SYS-02, staff, and laptops) would need its own verification, which is out of reach for a 7-person company until the P03 remediation plan is done. Revisit in 2027 if a customer requires it.

**B. Relying on the platform vendor.** The platform vendor carries most of the company's inherited controls (P02 section 10.2). Its SOC 2 Type 2 report, with its FedRAMP Moderate authorization, is the evidence for those controls, and reviewing it each year is part of vendor oversight (SA-9; POL-02 A.5).

**Why Confidentiality and not Availability.** The county's questions are about who can see applicant data, where it goes, and how it is destroyed, and the company's main gaps are there (the helpdesk, the AI add-on, the FTI spill, deletion at contract end). Availability is carried mostly by the platform vendor, whose report includes it (Part B). Processing Integrity and Privacy were not requested; agencies set the privacy notices for their own programs.

## 2. System description (scope)
- **Services:** hosted case management applications for AC-01 to AC-04, the sheriff data interface, and support.
- **Infrastructure and software:** the Hosted Case Management Service (SSP, P02): the platform tenant (SYS-01), the integration server and export storage (SYS-02), the AI pre-screening pilot (SYS-09), and the supporting suite, helpdesk, repository, and laptops.
- **People:** 7 staff and the MSP.
- **Data:** CJI (AC-01), assistance applicant data with Social Security numbers (AC-02), constituent data (AC-03, AC-04). FTI is outside the system by design.
- **Procedures:** POL-02, POL-03, POL-04 and the P08 runbook.
- **Subservice organizations:** the platform vendor (carve-out; its own report reviewed in Part B), the IaaS provider (carve-out).

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 6 | 20 | 7 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Availability (A1, 3) | | | | 3 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:**
- CC1.3: Security and Compliance Officer designated; roles defined
- CC3.1 and CC3.2: risk tolerance set and a 2026 risk assessment done
- CC4.1 and CC4.2: independent assessment done; deficiencies tracked in the POA&M
- CC6.4: physical access (data centers inherited; no agency data in the office)

**Not ready:**
- CC1.4: competence and screening (unscreened support role; overdue FTI recertification)
- CC2.1: no complete inventory of devices and agency data
- CC3.3: fraud risk not assessed
- CC6.3: administrator accounts used daily; no access reviews
- CC7.1, CC7.2: no scanning of SYS-02 and no monitoring
- CC7.5: recovery unproven (the same gap as risk R-004)
- C1.2: no deletion certificate process at contract end

## 4. Evidence inventory
The questionnaire asks for evidence. What the company can send now, and what it will start collecting:

| Evidence | Criteria | Available now | Start collecting |
|---|---|---|---|
| Designation letter; POL-02, POL-03, POL-04 | CC1.3, CC2.2, CC5.3 | Yes | Signed acknowledgments (2026-09) |
| Risk register summary (P01) and assessment summary (P07) | CC3.2, CC4.1, CC4.2 | Yes | Monthly POA&M notes (2026-09) |
| Platform vendor SOC 2 review and FedRAMP listing | CC9.2, CC6.4 | Yes | Bridge letter (2026-10) |
| CJIS Security Addendum certifications (held by AC-01) | CC1.1, CC1.4 | Yes (4) | Fifth certification (2026-10) |
| MSP monthly report (patching, antivirus, encryption) | CC6.8, CC7.1 | Yes (July 2026) | Monthly |
| Account review and log review records | CC6.2, CC6.3, CC7.2 | No | Monthly and quarterly from 2026-10 |
| Restore test records | CC7.5 | No | Quarterly from 2026-10 |
| Training and phishing exercise records | CC1.4, CC2.2 | Agency courses only | From 2026-10 |
| Change tickets | CC8.1 | No | From 2026-10 |
| Deletion certificates | C1.2, CC6.5 | No | At each contract end or implementation go-live |
| Tabletop exercise report | CC7.4 | No | 2026-11 |

## 5. Findings from the platform vendor report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31, covering Security, Availability, and Confidentiality. One exception (1 of 40 sampled changes lacked documented approval), remediated.
- **The AI add-on is not in the report.** The system description excludes the add-on and its model subprocessor, which matches the vendor's August 2026 letter that the add-on is outside its FedRAMP authorization. P10 treats it as unassessed.
- **Availability:** 99.9% availability and a platform RPO of 1 hour meet the BIA for platform failures. The full-tenant restore (up to 48 hours) **does not meet the 24-hour RTO** when records are deleted with a company credential, so the company's own exports must cover that case (POAM-008).
- **Controls the company must run.** The report lists complementary user entity controls: provisioning and removal, role design and access review, MFA, export and review of tenant audit logs, protection of API credentials, and telling the vendor about suspected compromise. Four are open gaps at the company (POAM-001, POAM-002, POAM-004, POAM-007). **The vendor's controls protect agency data only once those gaps are closed.**
- **Incident notice:** the vendor commits to 72 hours after confirming an incident, which is too slow for the company's 1-hour CJI notice. Ask for notice of suspected incidents within 24 hours at renewal.
- **Follow-ups:** request a bridge letter to 2026-09-30; ask when the AI add-on will enter the report and the authorization.

## 6. Remediation plan
| Quarter | Criteria addressed | Linked items |
|---|---|---|
| 2026 Q3 (by 2026-09-30) | CC1.1, CC2.1, CC2.2, CC6.7 | Acknowledgments and confidentiality agreements; inventory; staff briefing (POAM-009); FIPS 140-3 on SYS-02 (POAM-011) |
| 2026 Q4 | CC1.2, CC1.4, CC1.5, CC2.3, CC3.4, CC5.1, CC5.2, CC5.3, CC6.1, CC6.2, CC6.3, CC6.5, CC6.6, CC6.8, CC7.1-CC7.5, CC8.1, CC9.1, CC9.2, C1.1, C1.2 | Questionnaire response (2026-10-30); screening and training (POAM-005, POAM-006); access (POAM-001 to POAM-004); logs and monitoring (POAM-007); recovery (POAM-008); network (POAM-010); laptops (POAM-012); patching (POAM-013); vendors (POAM-014); contingency plan; contract-end checklist |
| 2027 Q3 | CC3.3 | Fraud scenarios in the July 2027 risk update; decision on a SOC 2 Type 1 or GovRAMP path once controls have operated for 6 months |

**Response to AC-02:** send this summary, the readiness checklist, the P07 summary, and the POA&M by 2026-10-30, name the Operations Manager as security contact, and commit to an updated self-assessment in April 2027.
