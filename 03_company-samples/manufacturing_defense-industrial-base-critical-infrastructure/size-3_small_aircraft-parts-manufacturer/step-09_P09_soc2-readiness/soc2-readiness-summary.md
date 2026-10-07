# SOC 2 Readiness Summary: Cris Santos Company | Defense Industrial Base | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (aircraft parts manufacturer, DoD subcontractor) |
| Tier / Vertical | Small / Defense Industrial Base |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None now. Readiness self-assessment for Customer C; no CPA engagement planned |
| Primary assurance | CMMC Level 2 certification assessment by a C3PAO (32 CFR Part 170), target window 2027-02-15 to 2027-02-26 |
| Prepared | 2026-08-24 by the IT Manager; approved by the Vice President of Operations 2026-08-31 |

## 1. Why SOC 2 (or an alternative) for this organization
**CMMC is the assurance that matters for most of the revenue.** About 58% of revenue is defense work for Prime A and Prime B. For them, the recognized evidence is a CMMC status in SPRS: Level 2 (C3PAO) for Prime A's awards from Phase 2 (32 CFR 170.23(a)(3)), plus the SP 800-171 DoD Assessment score required by DFARS 252.204-7019 and 252.204-7020. A SOC 2 report does not replace either one.

**Customer C asked for something different.** Customer C, a commercial aerospace tier-1 supplier (about 25% of revenue), added a supplier cybersecurity section to its annual supplier review. It accepts either a SOC 2 report or a self-assessment against the Trust Services Criteria, and asked for the **Security category only**. The company is a parts manufacturer, not a service organization that hosts systems for Customer C, so a CPA-issued SOC 2 report would be unusual and costly. The company will send this readiness self-assessment instead.

**Why not a SOC 2 audit now:**
- Most controls were defined in August 2026; a Type 2 report needs 6 to 12 months of operating evidence.
- CMMC certification is the funded priority. Its evidence covers most of the Security category, so a later SOC 2 effort would reuse it.
- Customer C does not require a CPA report.

**Alternatives considered:** Customer C's own questionnaire (it accepted this format instead) and ISO/IEC 27001 certification (not requested by any customer; out of proportion today).

## 2. System description (scope)
- **Services:** machining, inspection, and delivery of aircraft parts, and the engineering data exchange that supports them.
- **Infrastructure and software:** the CUI Engineering Enclave (SSP, P02), which holds Customer C's controlled drawings as well as DoD CUI, plus the corporate network and ERP used for orders and shipping.
- **People:** 250 employees, with 64 enclave accounts; the corporate MSP (no enclave access).
- **Data:** customer technical data (CUI, ITAR, and EAR controlled), order data, and employee records.
- **Procedures:** POL-01 to POL-05, the P08 runbook, and the POA&M (P07).

## 3. Readiness results
From `soc2-readiness.csv` (61 criteria; 33 in scope).

| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 8 | 16 | 9 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total (61)** | **8** | **16** | **9** | **28** |

**Ready (8):**
- CC1.3 and CC1.5: roles, authority, and accountability are defined
- CC3.1 and CC3.2: objectives and a 2026 risk assessment exist (P01)
- CC4.2: deficiencies are tracked in the POA&M
- CC5.1: controls are selected from SP 800-171 and SP 800-53 against risk
- CC6.2: access is approved and export-checked before it is granted
- CC6.6: the enclave boundary and remote access passed testing (P07 SC-7 and AC-17)

**Not ready (9):**
- CC3.4 and CC8.1: no change management or security impact analysis
- CC6.3: late account removal and no access reviews
- CC6.5: printed drawings in general recycling
- CC6.7: data can leave through public AI, file-sharing sites, and USB drives
- CC7.1 and CC7.2: no vulnerability scanning, log review, or 24x7 monitoring
- CC7.5: no recovery plan; MES backups weekly and local
- CC9.2: outside processors receive CUI without flowdown or review

## 4. How CMMC evidence maps to the Security category
Every in-scope criterion lists the SP 800-53 controls behind it, and those controls trace to SP 800-171 requirements in the SSP (P02) and the gap analysis (P03). The mapping is the author's, not an AICPA or NIST crosswalk. The same evidence serves both efforts:

| CMMC evidence | Security criteria it supports |
|---|---|
| SSP v2.0 and asset inventory with CMMC categories | CC2.1, CC5.1, CC5.2 |
| Risk register (P01) and annual risk assessment (3.11.1) | CC3.1, CC3.2, CC3.3 |
| P07 assessment results and POA&M (3.12.1, 3.12.2) | CC4.1, CC4.2 |
| Identity provider exports, access reviews, termination records (3.1.1, 3.5.3, 3.9.2) | CC6.1, CC6.2, CC6.3 |
| Visitor logs and badge reports (3.10.1 to 3.10.5) | CC6.4 |
| Destruction certificates and media inventory (3.8.3, 3.8.7) | CC6.5, CC6.7 |
| Scan reports, log review records, EDR tickets (3.11.2, 3.3.5, 3.14.6) | CC7.1, CC7.2 |
| Incident log, tabletop report, DIBNet drill (3.6.1 to 3.6.3) | CC7.3, CC7.4 |
| Change tickets and baselines (3.4.1 to 3.4.3) | CC3.4, CC8.1 |
| Supplier flowdown and SPRS or CMMC checks (DFARS 252.204-7012(m), 252.204-7020(g)) | CC9.2 |

Two Security criteria rely on work that CMMC does not require: CC7.5 and CC9.1 (recovery and business disruption). They are covered by the contingency plan due 2026-12-31, built from the BIA (P05).

## 5. Remediation plan and evidence calendar
All remediation items are already on the CMMC roadmap (P03 section 4) and the POA&M (P07). No separate SOC 2 project is funded.

| Quarter | Criteria addressed (by target date in `soc2-readiness.csv`) | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.1, CC1.2, CC1.4, CC2.1, CC2.2, CC2.3, CC3.4, CC4.1, CC5.2, CC5.3, CC6.1, CC6.3, CC6.4, CC6.5, CC6.7, CC7.1, CC7.3, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2 (22) | Policy acknowledgments, owner review minutes, training records, termination and access review records, visitor logs, destruction certificates, baselines, change tickets, scan reports, tabletop report, restore test, flowdown clauses |
| 2027 Q1 | CC3.3, CC6.8, CC7.2 (3) | Updated risk assessment with fraud scenarios, allowlisting enforcement records, weekly log reviews and managed detection tickets |

The C3PAO assessment (2027-02-15 to 2027-02-26) will test most of this evidence and gives Customer C independent confirmation for the criteria it overlaps.

**Response to Customer C:** send this summary, the readiness checklist, and a one-page letter stating the CMMC Level 2 target date. Commit to an updated self-assessment after the C3PAO assessment, by 2027-04-30.
