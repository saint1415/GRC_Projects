# Regulatory Gap Analysis: Cris Santos Company | Commercial Facilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed commercial office and retail property owner-operator) |
| Tier / Vertical | Mid-Market / Commercial Facilities (NAICS 531120) |
| Primary benchmark | CISA Cross-Sector Cybersecurity Performance Goals, Version 2.0 (CPG 2.0), December 2025 (C-COMMERCIAL-FACILITIES-R05). **Voluntary** |
| OT tailoring | NIST SP 800-82 Rev. 3, *Guide to Operational Technology (OT) Security* (final, September 2023) |
| Secondary standard (binding by contract) | PCI DSS v4.0.1, requirements in the v4.0.1 SAQ P2PE (October 2024) (C-COMMERCIAL-FACILITIES-R01) |
| Legal baseline | FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02); Fla. Stat. 501.171(2), (3), (4), (6), and (8) |
| Pending rule tracked | CIRCIA, proposed 6 CFR Part 226 (C-COMMERCIAL-FACILITIES-R06) |
| Assessment dates | 2026-07-06 to 2026-07-31 (walkthroughs 2026-07-14 to 2026-07-23 at 6 of 14 properties); evidence refreshed with P07 results through 2026-08-21 |
| Assessors | GRC Analyst and Security Manager with the vCISO, the VP of Engineering, the Director of Security Operations, the Controller, and the General Counsel; reviewed by the co-sourced internal audit firm |
| Approved | Chief Operating Officer, 2026-09-15 |

## 1. Applicability

### 1.1 What the vertical names, and what binds this company
**Primary business line:** owning, leasing, and operating office and retail property in Florida, including building operations (BAS, access control, video) and limited card acceptance.

The vertical overlay names the CISA CPGs, with PCI DSS for payment environments, because **no mandatory sector-specific cybersecurity regulation exists for commercial facilities**. Each candidate was checked for this company at its size:

| Candidate | Applies? | Reason |
|---|---|---|
| CISA CPG 2.0 (R05) | **Voluntary** | CPG 2.0 states that the goals are not "Mandated by CISA" and that CISA intends organizations "to voluntarily adopt" them. There are no size tiers. The COO adopted CPG 2.0 as the company's baseline on 2026-07-01 |
| PCI DSS v4.0.1 (R01) | **Yes, by contract** | The company is a merchant (about 16,000 card transactions a year) and its merchant agreement requires PCI DSS compliance. PCI DSS is an industry standard, not law. The acquirer sets the validation type (SAQ P2PE) |
| FTC Act Section 5 (R02) | **Yes** | No size threshold. Reaches unreasonable data security and misleading statements about data practices, including analytics and biometric technology |
| Fla. Stat. 501.171 | **Yes** | The company is a "covered entity" (a commercial entity that acquires, maintains, stores, or uses personal information; 501.171(1)(b)). Subsection (2) requires "reasonable measures to protect and secure data in electronic form containing personal information"; subsections (3)-(6) set notice duties; subsection (8) requires disposal of customer records. Text read from the 2026 Florida Statutes |
| CCPA/CPRA (R03) | No | Revenue (about $100 million) exceeds the CPI-adjusted $26,625,000 threshold, but the company does not do business in California. **Recheck before any acquisition or marketing in California**, because the revenue test alone would then be met |
| SEC cybersecurity disclosure (R04) | No | Privately held; not an Exchange Act reporting company |
| CIRCIA (R06) | **Not yet (proposed rule only), but the company would be covered as proposed** | No final rule had been published as of 2026-10-06 (Federal Register search). The NPRM (89 FR 23644, 2024-04-04) proposes that an entity in a critical infrastructure sector is covered if it exceeds the SBA small business size standard for its industry (proposed 6 CFR 226.2). The company exceeds the $34.0 million standard for NAICS 531120, so it would be covered if the final rule keeps that criterion. Treated as pending (section 5) |

**Decision.** The binding rules (Florida's "reasonable measures", FTC Section 5) do not define reasonable security. The company uses CPG 2.0, the Sector Risk Management Agency's own baseline, to define it, tailored for OT with SP 800-82 Rev. 3. PCI DSS is analyzed as the secondary standard because it is the only binding control set. Florida's notice and disposal duties are analyzed at subsection level because they carry deadlines and civil penalties (501.171(9)). The CPG rows are rated like requirements so the roadmap can show gaps, but **a CPG gap is not a compliance violation.**

### 1.2 CPG 2.0 version and structure (verified)
The version was re-checked on 2026-10-06 against the saved CISA report, *Cross-Sector Cybersecurity Performance Goals, Version 2.0* (December 2025), used by the Small sample. cisa.gov could not be fetched again that day (HTTP 403), so no newer version could be ruled out from the live page; the report states a targeted revision cycle of 24 to 36 months.
- CPG 2.0 replaces CPG 1.0.1 and adds a GOVERN function to align with NIST CSF 2.0.
- **34 goals** in six functions: 1 Govern (1.A-1.E), 2 Identify (2.A-2.E), 3 Protect (3.A-3.S), 4 Detect (4.A-4.B), 5 Respond (5.A-5.B), 6 Recover (6.A). The report's mapping table renumbers the v1.0.1 goals (for example v1.0.1 2.F segmentation is now 3.I).
- OT guidance appears as "OT:" lines within goals. Those lines were used in this analysis.
- Each goal lists NIST CSF 2.0 references, which were used for the crosswalk.

### 1.3 PCI DSS scope and SAQ
- **Card channels.** Card-present and phone bookings at 6 management offices, only through 14 terminals from a validated PCI-listed P2PE solution. Rent is paid by ACH. Parking is the parking operator's own merchant account and is **outside the company's PCI scope** (a vendor-risk item, P01 R-014). Tenant app amenity bookings are billed to tenant accounts.
- **SAQ.** The acquirer requires an annual **SAQ P2PE**. Its eligibility criteria include: all processing through a validated PCI-listed P2PE solution; the only systems that handle account data are the solution's terminals; the merchant does not otherwise receive, transmit, or store account data electronically; any retained data is on paper; and all P2PE Instruction Manual (PIM) controls are implemented. The SAQ covers requirements 3 (paper only), 9.4 (paper only), 9.5, 12.1, 12.6, 12.8, and 12.10.1.
- **Eligibility finding.** Five emails with card numbers were found in the event mailboxes, and phone bookings at Towers 2 and 4 are written on paper with security codes. The Controller will not sign the 2026 SAQ P2PE until G-035, G-037, G-038, and G-042 are closed and the acquirer confirms the path.
- PCI DSS v4.0.1 is still the current version (vertical requirements file, verified 2026-09-25). PCI SSC ran a request for comments on v4.0.1 in June and July 2026 toward a next version; no publication date was found.

## 2. Method
1. **Requirements.** CPG rows are the 34 goals at goal level, citing the goal ID; summaries paraphrase the goal and its OT line. PCI DSS rows are the eligibility statement plus the 21 requirements listed in the v4.0.1 SAQ P2PE. PCI DSS is copyrighted, so rows list requirement numbers with short topic labels written for this analysis; read the official standard for the text. Legal rows cite the statute subsection.
2. **Crosswalk.** CPG rows use the CSF 2.0 references published in CPG 2.0, with an SP 800-53 subset selected by the author from the CPG's own references. For goal 3.O, CPG 2.0 lists PR.IR-01 and DE.CM-01, which repeat goal 3.I, so an author mapping (PR.DS-11; CP-9, CP-4, CP-10) is used instead and labeled. PCI and legal rows are author mappings; no official NIST mapping of PCI DSS v4.0.1 or Fla. Stat. 501.171 exists.
3. **Evidence.** Interviews (COO, General Counsel, Controller, VP of Engineering, Building Technology Manager, Director of Security Operations, 4 of 14 chief engineers, 6 SCC operators, 8 engineering staff, conference center staff, both BAS integrators); document review (contracts, the 2025 SAQ P2PE, the processor agreement, the 2024 IR plan, network diagrams); configuration exports (14 property firewalls, identity provider, access control platform roles, backup jobs, visitor system settings); the MSSP external scan of 2026-07-21; a mailbox search on 2026-07-22; and walkthroughs of Tower 1, Tower 2, Mixed-Use 1, Park 2, Retail 2, and Retail 5. Tower 4 was covered by interview.
4. **Evidence sampling.** Where a control operates many times, a random sample was tested from a system-generated population, using the co-sourced internal audit firm's attribute sampling table (25 items for a control that operates many times a year; 5 to 12 for weekly or monthly controls; whole population where it is small):
   - terminations: 25 of 96;
   - tenant credential revocation requests: 25 of about 2,600;
   - privileged accounts (MFA): 25 of 31;
   - OT devices (default credentials, with P07): 30 at Park 2, Retail 2, and Tower 1;
   - Platform B controllers (inventory): 40;
   - backup job days: 31 of 31 (July 2026);
   - critical vulnerability findings: 40 of 40 (Q1-Q2 2026);
   - vendor contracts with access or data: 41 of 41;
   - Platform B program changes found in integrator invoices: 10;
   - incidents: 10 of 34;
   - paper booking forms at Tower 2: 20;
   - monthly POI inspection records: 12;
   - media destruction certificates: 10.
   Each `evidence` cell names the sample and its result.
5. **Status.** Each row was rated Met, Partially met, Not met, or Not applicable. Gaps were rated on the P01 risk scale.

## 3. Results summary
| Source | Rows | Met | Partially met | Not met | N/A |
|---|---|---|---|---|---|
| CPG 2.0 Govern (1.A-1.E) | 5 | 1 | 4 | 0 | 0 |
| CPG 2.0 Identify (2.A-2.E) | 5 | 0 | 4 | 1 | 0 |
| CPG 2.0 Protect (3.A-3.S) | 19 | 1 | 18 | 0 | 0 |
| CPG 2.0 Detect (4.A-4.B) | 2 | 0 | 2 | 0 | 0 |
| CPG 2.0 Respond (5.A-5.B) | 2 | 0 | 2 | 0 | 0 |
| CPG 2.0 Recover (6.A) | 1 | 0 | 1 | 0 | 0 |
| **CPG 2.0 subtotal** | **34** | **2** | **31** | **1** | **0** |
| PCI DSS v4.0.1 SAQ P2PE (eligibility plus 21 requirements) | 22 | 6 | 12 | 3 | 1 |
| Legal baseline (15 U.S.C. 45(a); Fla. Stat. 501.171(2), (3), (4), (6), (8)) | 6 | 0 | 6 | 0 | 0 |
| **Total** | **62** | **8** | **49** | **4** | **1** |

The 53 rows that are Partially met or Not met break down by gap risk as 6 High, 26 Moderate, and 21 Low. All six High gaps are CPG goals: 1.E (managed service provider risk), 3.F (MFA), 3.I (segmentation), 3.O (backups), 3.Q (logging), and 3.S (internet-facing devices).

**The pattern: a program built for the towers, not yet for the portfolio.** Almost every CPG row is Partially met for the same reason. The 2025 tower project delivered OT zones, the remote access gateway, backups, and manual procedures at Towers 1-4 and the Platform A properties. The 8 Platform B properties (Parks 1-2, Retail 1-6) still have flat networks, an always-on integrator tool without MFA, no backups, and unsupported servers. A mid-market program with a security team, an MSSP, and a landing zone is in place; its gaps are about **scale and coverage**, not about missing functions.

**Two areas stand out beyond OT:**
- **Data held without a decision.** Visitor ID scans (about 610,000 records) are kept indefinitely, which weakens the "reasonable measures" position under 501.171(2) and makes any breach far larger (G-058, G-062).
- **PCI findings are about paper and email, not systems.** The P2PE terminals keep card data out of company systems, but two conference centers work around them.

## 4. Priority gaps
| Gap | Citation | Risk level | Action | Owner | Target |
|---|---|---|---|---|---|
| Integrator B remote access without MFA, approval, or logging | CPG 1.E, 3.F | High | Remove the tool; gateway with named accounts, MFA, approval, recording | Building Technology Manager | 2026-11-30 |
| Internet-exposed Park 2 BAS interface | CPG 3.S | High | Remove forwarding; monthly external scans | IT Director | 2026-10-15 |
| No OT zones at 10 properties; Tower 1 any-any rule | CPG 3.I | High | Remove the rule; SP 800-82 Rev. 3 zones at all properties | IT Director | 2027-06-30 |
| Platform B backups missing; restores never tested | CPG 3.O | High | Platform B images; controller program exports; quarterly restore tests | IT Director | 2027-03-31 |
| No OT or access platform logging | CPG 3.Q | High | Forward Platform A, gateway, and platform logs; OT monitoring | Security Manager | 2027-03-31 |
| Card data in email; paper forms with security codes | SAQ P2PE eligibility; Req. 3.2.1, 3.3.1.2, 9.4.6 | Moderate | Stop paper capture; purge and block; cross-cut shredding | Controller | 2026-10-31 |
| Notice readiness: no decision log; audit events kept 90 days | Fla. Stat. 501.171(4) | Moderate | Decision log; export audit events with 3-year retention | General Counsel | 2026-11-30 |
| Visitor ID scans kept indefinitely | Fla. Stat. 501.171(8), (2) | Moderate | Retention schedule; 30-day purge | Director of Security Operations | 2026-12-31 |
| 25 vendor contracts without notice terms | CPG 1.D; Fla. Stat. 501.171(6) | Moderate | Security addendum | General Counsel | 2027-03-31 |
| OT asset inventory 55% | CPG 2.A | Moderate | Passive OT discovery | Building Technology Manager | 2026-12-31 |
| Degraded-mode procedures only at the towers | CPG 6.A | Moderate | BAACS contingency plan and procedures | Vice President of Engineering | 2026-12-31 |
| Analytics and biometric practices not disclosed | 15 U.S.C. 45(a) | Moderate | Notices; P10 conditions | General Counsel | 2026-12-31 |

High and Moderate gaps are carried into the risk register (P01) and the POA&M (P07). The full list, with evidence, is in `gap-analysis.csv`.

**Before signing the 2026 SAQ P2PE:** close every open row among G-035 to G-046 (eligibility, paper data, and PIM controls) and G-050, and record the acquirer's confirmation. If card data is found in email again, the company is not eligible for SAQ P2PE for that channel and must ask the acquirer how to validate.

## 5. Program roadmap
| Phase | Window | Outcomes | Gaps closed (examples) |
|---|---|---|---|
| **1. Stabilize** | 2026 Q4 | Tower 1 rule removed; Park 2 exposure closed; Integrator B on the gateway; default passwords changed; paper card capture stopped; visitor purge; decision log; face verification pilot suspended (P10); OT tabletop 2026-11-19; first Platform A restore test | 1.E, 3.A, 3.F, 3.S; SAQ P2PE eligibility, 3.2.1, 3.3.1.2, 9.4.6; 501.171(4), (8) |
| **2. Build** | 2027 Q1 | Passive OT discovery and inventory; Platform B backups and controller program copies; OT and platform logs to the SIEM; vendor security addenda; standards issued; OT training; BAACS contingency plan | 2.A, 2.E, 3.O, 3.Q, 1.D, 3.J, 6.A; 501.171(6) |
| **3. Segment and upgrade** | 2027 Q2 | OT zones at Mixed-Use 1-2, Parks 1-2, and Retail 1-6; Platform B upgrade; SOC 2 observation period starts 2027-04-01 (P09) | 3.I, 3.G, 3.M, 4.A |
| **4. Sustain** | 2027 Q3-Q4 | Annual risk assessment (July 2027); passive OT assessment by an outside firm; Tier 1 vendor reviews; due diligence for the 2027 acquisitions | 2.C, 1.B, 1.E (annual cycle) |

Progress is reported quarterly to the audit committee as the count of rows moving from Partially met or Not met to Met.

## 6. Pending regulatory changes
- **CIRCIA:** no final rule as of 2026-10-06. The Unified Agenda listed a final rule for September 2026, and CISA held town halls in June 2026 to refine scope and burden, so coverage may narrow. **If the final rule keeps the NPRM's size criterion, this company is covered**: it would have to report covered cyber incidents to CISA within 72 hours of reasonably believing one occurred, and ransom payments within 24 hours of payment (6 U.S.C. 681b(a)). Ransomware on the BAS (P08) is the most likely covered incident. The `pending_rule_change` column flags CPG 1.C, 3.Q, and 5.B, and P01 R-044 tracks readiness. The 2026-11-19 tabletop includes a dry run of a CIRCIA-style report.
- **PCI DSS:** the June-July 2026 request for comments starts work on the next version. v4.0.1 remains in force. Every PCI row carries this note.
- **CPG 2.0** states a targeted revision cycle of 24 to 36 months.

None of these is treated as a current obligation.
