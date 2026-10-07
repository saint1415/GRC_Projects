# SOC 2 Readiness Summary: Cris Santos Company | Information Technology | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (cloud hosting and managed infrastructure provider) |
| Tier / Vertical | Mid-Market / Information Technology |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1), Processing Integrity (PI1, backup service) |
| Current report | SOC 2 Type 2 (Security, Availability) for the commercial private cloud and the backup service; period 2025-07-01 to 2026-06-30; unqualified opinion with 3 exceptions |
| Target report | SOC 2 **Type 2** with expanded scope, observation period **2027-01-01 to 2027-09-30** (9 months), report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | Fieldwork 2026-08-24 to 2026-09-11 by the GRC Manager and the GRC analysts, using P02, P05, P06, and P07 evidence; approved by the Chief Technology Officer 2026-09-22 |

## 1. Why the scope is growing
The company is a service organization: customers outsource hosting, managed services, and backups to it, and their auditors rely on its controls. The current SOC 2 report covers only the commercial private cloud and the backup service for Security and Availability. Customers have asked for more:
- **Banks (38)** need assurance over managed services and backups for their own vendor management programs, and over confidentiality of their data.
- **Backup and DR customers (620)** want assurance that backups are complete and restorable, which is **Processing Integrity**.
- **Enterprise prospects** require **Confidentiality** in vendor questionnaires.
- **DC-3** now runs commercial clusters and must join the description so the report covers where customer VMs actually run.

**New scope for the 2027 report:** add Confidentiality and Processing Integrity (backup service), the managed services line (RMM tool), and DC-3. Privacy is out of scope: the company processes customer data as a service provider and does not collect personal information from data subjects for its own purposes.

**Why the observation period starts 2027-01-01.** The Type 2 report tests operating effectiveness over a period. P07 found gaps in shared and privileged accounts, logging, vendor reviews, and recovery testing, and the managed services line has never been examined. The High items close by 2026-12-31 (P07 POA&M), so the observation period starts the next day and runs 9 months.

**Relationship to FedRAMP.** The Government Cloud is covered by its FedRAMP certification, not by this report. Many controls are shared (identity provider, SIEM, pipeline), so evidence from P07 and the FedRAMP assessment is reused. The SOC 2 examination is performed by an independent CPA firm that is neither the co-sourced internal audit firm nor the FedRAMP assessment service.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Managed private cloud (commercial), managed services, managed backup and DR, DNS and edge services |
| Infrastructure | Commercial clusters at DC-1, DC-2, and DC-3; commercial partition of the HCP (P02); the backup platform at DC-2 and DC-3; the RMM tool |
| Software | Portal and control plane (commercial deployment), backup software, RMM tool, identity provider, SIEM, ITSM |
| People | NOC and customer support, platform engineering, software engineering, site reliability, managed services, backup and DR, security and GRC |
| Data | Commercial customer VM data, DNS zones, backups, tenant metadata, customer contact data |
| Procedures | POL-01 to POL-05, the standards index (P06), and the P08 runbooks |
| Subservice organizations (carve-out) | Colocation providers (DC-1, DC-2, DC-3), public cloud provider, identity provider, SIEM vendor, RMM vendor, MDR partner, code hosting vendor, DDoS scrubbing service. Their controls are covered by their own SOC 2 reports or FedRAMP packages and the complementary subservice organization controls listed in the description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 13 | 17 | 3 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 2 | 3 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **16** | **23** | **4** | **18** |

**Ready (16):**
- governance, risk, and monitoring: CC1.1, CC1.2, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2, CC3.4, CC4.1, CC4.2;
- control design and policies: CC5.1, CC5.3;
- transmission: CC6.7;
- environmental protection and backups: A1.2;
- backup processing and stored data: PI1.3, PI1.5.

**Not ready (4):**
- CC6.1: managed services, newly in scope, still uses 2 shared RMM super-administrator accounts, and DC-1 clusters A and B use a shared local account without MFA (POAM-020, POAM-002);
- CC7.2: RMM and DC-1 clusters A and B not monitored, and AI triage auto-closes alerts (POAM-005, POAM-006);
- CC9.2: 5 of 14 Tier 1 vendor reviews overdue and 4 contracts without incident notice terms (POAM-013);
- A1.3: a skipped quarterly restore test, the failed commercial control plane test, and no DC-1 failover test (POAM-009).

**The 3 exceptions in the current report are all visible here:** late terminations (CC6.2), one change without documented approval (CC8.1, closed 2026-08), and a skipped restore test (A1.3). Two are still open, so the auditor will test them closely.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Period | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1, CC6.2, CC6.4, CC6.6, CC6.8, CC7.1, CC7.2, CC7.3, CC7.4, CC7.5, CC8.1, CC9.1, CC9.2, A1.3, PI1.1, PI1.2, PI1.4 | RMM account list and two-person approval records; PAM logs for DC-1; SIEM source list; auto-close sampling records; monthly scan reports; restore test reports; tabletop report; Tier 1 review files; DC-3 provider report review |
| 2027 Q1 | CC1.4, CC2.1, CC2.3, CC3.3, CC5.2, CC6.3, CC6.5, C1.2, A1.1 | Role-based training records; CMDB tags; quarterly access reviews for both partitions; serial-level destruction certificates; capacity plan |
| 2027-01-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, restore tests, vendor reviews, change samples) |
| By 2027-06-30 | C1.1 (encryption of the remaining older commercial volumes) | Storage encryption reports. The auditor will see this as a partial-period deviation; management will describe it in the system description |

**Status reporting.** The GRC Manager reports readiness monthly to the CTO and quarterly to the audit committee. Bank customers get a readiness letter in 2026-12 and the report when it is issued.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 16 Common/Inherited and 35 Hybrid), and the SOC 2 report will carve out 8 subservice organizations. The program in `vendor-soc2-review.csv` makes that reliance evidence-based. It is the core of STD-09 (vendor and supply chain risk).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Access to customer data at scale, privileged reach into customer systems, or support for a High-criticality BIA process | SOC 2 Type 2 or a FedRAMP package, plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability against the BIA, and incident terms | Annually |
| **Tier 2** | Limited customer data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No customer data and no system access | Contract terms only | At contract renewal |

Of about 260 vendors, 34 have access to customer data or production systems and 14 are Tier 1. The CSV holds all 14 Tier 1 vendors: **9 reviews complete** (one with follow-up open) and **5 overdue**, scheduled by 2026-11-30 (POAM-013).

**Key findings:**
1. **RMM vendor (VEN-07):** unqualified opinion with 2 exceptions on its own administrator access reviews, never followed up before this review. The contract has no incident notice terms. Combined with the company's own RMM gaps, this is why R-001 is Very High.
2. **Four Tier 1 contracts lack incident notice terms** (RMM, ITSM, backup software, and hardware maintenance vendors). STD-09 now requires 72 hours or less; amendments are due by 2027-03-31.
3. **DC-1 colocation provider (VEN-01):** unqualified, but it commits to nothing for multi-day regional events. The DC-1 hurricane scenario depends on the company's own failover (P05; P08 `ir-runbook-dc1-site-loss.md`).
4. **CUECs are where the company's gaps show.** The SIEM vendor's controls only help if the company sends the right sources and limits AI auto-close; the code hosting vendor's controls only help if machine tokens are managed (POAM-004, POAM-005, POAM-006).
5. **DC-3 provider (VEN-03):** its report must be reviewed before DC-3 enters the SOC 2 description.
