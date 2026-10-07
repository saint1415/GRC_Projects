# SOC 2 Readiness Summary: Cris Santos Company | Utilities | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded investor-owned electric utility) |
| Tier / Vertical | Enterprise / Utilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service lines | SL-1 Utility Services (CIS hosting, billing, meter data management, and outage call overflow for 7 client utilities, about 410,000 meters); SL-2 fleet charging services (managed charging for 62 fleet and municipal clients, 1,450 chargers) |
| Categories in scope | SL-1: Security, Availability, Confidentiality (existing report), plus Processing Integrity and Privacy (new). SL-2: Security, Availability, Confidentiality, and Processing Integrity. Together the two service lines cover all five categories |
| Target reports | SL-1: Type 2, period 2027-01-01 to 2027-12-31 (fourth annual report; Processing Integrity and Privacy added). SL-2: first Type 2, period 2027-04-01 to 2027-09-30 |
| Files | `soc2-readiness.csv` (every criterion for each service line: 122 rows); `soc2-evidence-map.csv` (25 evidence items) |
| Prepared | 2026-08-21 by the GRC team with the service line owners; reviewed by the CISO and the Chief Audit Executive |

## 1. Why SOC 2 for this organization
Most of the company's work is regulated utility service, which SOC 2 does not cover; the grid systems are assured through NERC CIP audits by SERC (the vertical's assurance alternative) and the P07 internal assessment. Two service lines are different: the company **provides services to other businesses**, so it is a service organization for them, and their clients ask for a CPA's SOC 2 report.
- **SL-1 Utility Services.** Four municipal utilities and three electric cooperatives in Florida and Georgia rely on the company for customer billing and meter data. The company is their third-party agent for customer personal information (Fla. Stat. 501.171(6) worked example). SL-1 has issued a SOC 2 Type 2 report (Security, Availability, Confidentiality) every year since 2024; the 2025 report had no exceptions. The clients now ask for **Processing Integrity** because bill accuracy is the core commitment, and for **Privacy** because the company handles their customers' SSNs and bank account numbers.
- **SL-2 fleet charging services.** Commercial fleets and municipalities buy managed charging. Contracts renewing in 2027 require a SOC 2 Type 2 report including **Processing Integrity**, because energy and session data drive client billing and fleet cost allocation.

**Alternatives considered:** a NERC CIP audit report (it covers BES Cyber Systems, not these services, and is not shared with clients); ISO/IEC 27001 certification (two SL-2 clients would accept it, but most clients and both cooperatives' auditors asked for SOC 2, and one framework per service line is cheaper to run).

**Relationship to other assurance:** the enterprise common controls (P02 section 10.3; P04 section 5) support both service lines, so one set of evidence serves both reports and the SOX program. Cloud provider A (SL-1), cloud provider B (SL-2 fleet portal), the AMI vendor (SL-1), and the charging management SaaS vendor (SL-2) are subservice organizations presented with the carve-out method; their own SOC 2 reports are reviewed under CC9.2.

## 2. System description (scope)
| Element | SL-1 Utility Services | SL-2 fleet charging services |
|---|---|---|
| Services | Customer billing, payment posting, meter data management, outage call overflow for client utilities | Charger operations, session authorization, energy reporting, client billing |
| Infrastructure | Utility Services platform on Cloud provider A (CIS and MDM partitions per client); landing zone controls (P04) | Charging management SaaS (vendor); fleet portal on Cloud provider B; 1,450 company-operated chargers at client sites |
| Software | Commercial CIS and MDM (customer-managed); AMI head-end (vendor SaaS) | Vendor charging platform; company-built fleet portal and billing interface |
| People | Utility Services team (180); CIS team; SOC; identity and cloud platform teams | eMobility operations (90); fleet portal developers; SOC |
| Data | Client utilities' customer records (SSNs, bank accounts, usage), bills, payments | Fleet driver identifiers, vehicle and session data, energy reports, invoices |
| Procedures | P06 policy hierarchy; P08 runbook; Utility Services operating procedures | P06; P08; eMobility operating procedures |
| Subservice organizations (carved out) | Cloud provider A; AMI vendor; payment processor; bill print vendor | Charging management SaaS vendor; Cloud provider B; payment service for public-access chargers |

## 3. Readiness results
**SL-1 Utility Services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 31 | 2 | 0 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | 4 | 1 | 0 | 0 |
| Privacy (P1-P8, 18) | 14 | 3 | 0 | 1 |

**SL-2 fleet charging services**
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33) | 22 | 11 | 0 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 1 | 1 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 2 | 1 | 0 |
| Privacy (P1-P8, 18) | | | | 18 |

Across both service lines: Ready 79, Partially ready 22, Not ready 2, N/A 19 (122 rows).

**SL-1** is ready for its next Type 2 on the existing categories except two Security items shared with the enterprise customer data findings: cross-partition tests are not automated (CC6.1), and CIS export rights and the AMI bulk disconnect role are too broad (CC6.3; POAM-026 and POAM-018). Availability needs client-specific recovery tests (A1.3). The new categories have 4 partially ready items: rate table change evidence (PI1.3), SSN retention and purge for client partitions (P4.2, P4.3), and a disclosure log for client-instructed disclosures (P6.2). P3.2 is N/A because the company does not collect consent; the clients do.

**SL-2** is not yet ready for a Type 2 period to start. Not ready: A1.3 (no recovery test) and PI1.5 (no agreed retention for session data). Partially ready: CC1.3, CC2.3, CC3.1, CC4.1, CC6.1, CC6.2, CC6.3, CC7.1, CC7.5, CC8.1, CC9.2, A1.2, C1.2, PI1.3, PI1.4. The gaps are what a new service line usually lacks: a system description, client user management, recovery testing, reconciliations, and assurance over the charging SaaS vendor, whose SOC 2 report covers Security only. Privacy is out of scope for SL-2 because the fleet clients are responsible for notice and consent to their drivers. Closing these items by 2027-03-31 makes SL-2 ready to start its period on 2027-04-01.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Actions | Evidence to start collecting |
|---|---|---|---|
| 2026 Q4 | SL-1 CC6.3; SL-2 CC1.3 drafting | Export rights reduced and bulk disconnect approval (POAM-026, POAM-018); SL-2 system description drafted | Role exports; approval logs |
| 2027 Q1 | SL-1 CC6.1, PI1.3, P4.2, P4.3, P6.2; SL-2 CC1.3, CC2.3, CC3.1, CC4.1, CC6.1 to CC6.3, CC7.1, CC7.5, CC8.1, CC9.2, A1.2, A1.3, C1.2, PI1.3 to PI1.5 | Cross-partition test automation; rate change dual review; SSN purge; disclosure log; SL-2 client MFA and attestations; charging SaaS contract amendment; offline-mode test; reconciliations; retention terms | Test reports; purge logs; reconciliations; contract amendment |
| 2027 Q1 (March) | Readiness check by Internal Audit for both lines; SL-2 Type 2 period starts 2027-04-01 | Mock walkthrough with the service auditor | Walkthrough results |
| 2027 Q2 | SL-1 A1.3 (due 2027-06-30) | Client-specific recovery tests | Test report per client |

**Evidence map.** `soc2-evidence-map.csv` lists each evidence item, its source system, owner, frequency, and the Type 2 sample the service auditor is expected to draw. Items marked "Both" are enterprise common controls collected once and used for both reports. Status: 14 collecting, 2 ready, 9 not started (each tied to a 2027 Q1 or Q2 action above).

**Client communication:** SL-1 clients receive the 2025 report, a bridge letter, and a roadmap letter for Processing Integrity and Privacy; SL-2 clients receive this summary, a bridge letter describing the remediation, and the expected first report date (2027-11).
