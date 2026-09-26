# SOC 2 Self-Benchmark and Vendor Report Review: Cris Santos Company | Healthcare and Public Health | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural critical access hospital) |
| Tier / Vertical | Small / Healthcare and Public Health |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; read the criteria text in the AICPA publication |
| Categories in scope | Security (CC1-CC9) only |
| Part A | Security-only self-benchmark of the hospital (`soc2-readiness.csv`) |
| Part B | Review of the EHR vendor's SOC 2 Type 2 report (`vendor-soc2-review.csv`, added to the template set) |
| Prepared | 2026-08-20 by the IT Manager with the CFO |

## 1. Why this is not a SOC 2 readiness assessment
SOC 2 reports on the controls of a **service organization**, a company that provides services to other businesses (its user entities). A critical access hospital provides care to patients. It does not host systems or process data for other businesses, no customer has asked it for a SOC 2 report, and no transfer partner or payer relationship depends on one. So the hospital will not pursue a SOC 2 examination, and "readiness" in the audit sense does not apply.

The Trust Services Criteria are still useful in two ways:

**A. A structured self-benchmark (Security only).** The common criteria (CC1-CC9) give the governing body a second, outside yardstick for the program, next to the HIPAA gap analysis and the HHS CPG benchmark in P03. Only Security is scored. Availability, Confidentiality, Processing Integrity, and Privacy are marked N/A because the hospital makes no commitments to user entities in those categories; the same topics are covered by binding rules (HIPAA, 42 CFR 485.625) elsewhere in this set.

**B. Third-party risk management.** The EHR vendor is a service organization, and the hospital relies on it for most inherited controls (P02, P04) and for its most critical processes (P05). The vendor's SOC 2 Type 2 report is the main evidence for those controls, and the hospital reviews it every year (HIPAA 164.308(b), SA-9, CPG Vendor/Supplier Cybersecurity Requirements).

Other assurance options considered: HITRUST certification is out of proportion for a 60-person hospital. The HHS CPGs and 405(d) HICP (P03) are the better-fitting sector yardsticks; the TSC benchmark is kept because governing body members recognize the SOC 2 structure.

## 2. System description (scope of the self-benchmark)
- **Services:** emergency, inpatient, swing-bed, laboratory, imaging, and pharmacy services for the hospital's patients.
- **Infrastructure and software:** the Hospital Clinical Information System (SSP, P02).
- **People:** 60 employees, about 40 contracted clinicians and agency nurses, and the MSP.
- **Data:** ePHI, claims, public health reports, and workforce data.
- **Procedures:** POL-01 to POL-05, the P08 runbook, downtime procedures, and the emergency preparedness plan.

## 3. Results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 4 | 21 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready:** CC1.3 (roles designated), CC3.1 (objectives), CC3.2 (risk analysis), CC4.2 (deficiencies tracked in the POA&M).

**Not ready:**
- CC3.3: fraud and insider misuse not in the risk analysis
- CC3.4: major changes (the 2024 cloud move and the 2026 sepsis model go-live) were not risk-assessed
- CC6.3: stale contracted and agency accounts; no access reviews
- CC6.6: vendor VPN without MFA; flat internal network
- CC7.1 and CC7.2: no vulnerability scanning; no 24x7 monitoring
- CC7.5: no hospital recovery procedures; backups not isolated
- CC9.2: vendor management

The Not ready list matches the Very High and High risks in P01 and the High POA&M items in P07. The self-benchmark adds one point the other deliverables do not stress: **change management (CC3.4, CC8.1)** for clinical systems. The sepsis model went live, and pump drug libraries change, without a security or risk review.

## 4. Findings from the EHR vendor report (Part B)
- **Opinion:** Type 2, unqualified, for the 12 months ending 2026-03-31. Two exceptions (change approvals and a late access review), both remediated.
- **Availability does not meet the BIA.** The vendor's stated RTO of 8 hours is longer than the 2-hour RTO the ED and inpatient processes need (P05). The RPO of 15 minutes meets the need. Until the contract changes, the hospital's downtime procedures must carry up to 8 hours.
- **Controls the hospital must run.** The report lists complementary user entity controls: timely user removal, MFA for remote access, role assignment, audit report review, securing the connection to the vendor, and telling the vendor about suspected compromise. Four are open gaps at the hospital (POAM-001, POAM-011, POAM-018, POAM-006). **The vendor's controls only protect the hospital once those gaps are closed.**
- **No assurance on the sepsis model.** Clinical content and predictive models are outside the report's scope. The model's performance and bias questions are handled in P10, not by the SOC 2 report.
- **Disconnection practice.** The vendor may cut the hospital's connection when it sees malicious traffic and will reconnect only after evidence of containment. That is built into the P08 runbook.
- **Follow-ups:**
  - Negotiate a contractual RTO of 4 hours or better and 24-hour incident notice at the next BAA amendment.
  - Confirm the vendor reviews its carved-out data center and e-prescribing providers.
  - Request an updated bridge letter at 2026-12-31.

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.2, CC6.3, CC6.6 (vendor MFA), CC2.2, CC7.3-7.4, CC9.2 (BAAs) | End-dated accounts, access reviews, vendor MFA configuration, incident log, tabletop report, signed BAAs |
| 2027 Q1 | CC6.6 (segmentation), CC6.8, CC7.1, CC7.2, CC7.5 | Segmentation design and rules, 24x7 alert tickets, scan reports, restore test records |
| 2027 Q2-Q3 | CC3.3, CC3.4, CC8.1, CC1.5 | 2027 risk analysis with fraud scenarios, change reviews for clinical systems, manager reviews |

The governing body receives this benchmark with the P03 CPG benchmark each year. The next update is due with the July 2027 risk analysis.
