# SOC 2 Readiness Summary: Cris Santos Company | Transportation and Warehousing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed marine cargo terminal operator: Terminal 1, Terminal 2 and an off-dock depot) |
| Tier / Vertical | Mid-Market / Transportation and Warehousing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30, ahead of the carrier alliance renewal on 2027-12-31. Interim Type 1 report as of 2027-03-31 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 to 2026-09-04 by the vCISO, the Security Manager (alternate CySO) and the GRC analyst, using P02, P05, P06 and P07 evidence; accepted by the Chief Operating Officer 2026-09-15 |

## 1. Why SOC 2 for this organization
A marine terminal operator is not usually a SOC 2 service organization: its regulator-facing assurance is the Coast Guard-approved FSP and, from 2027, the Cybersecurity Plan. Two services change that:
- The **customer portal and truck appointment system** (SYS-14) gives about 1,200 trucking companies and cargo owners container availability, appointments and invoices.
- The **EDI services** (SYS-04) exchange bay plans, load and discharge lists and container status with 16 carrier services and customers, and pass customs release and hold status to the gates.

Carriers rely on those services for their own operations and reporting. The **carrier alliance** at T1 (3 services, about 45% of T1 revenue) asked, through its vendor risk program, for a SOC 2 Type 2 report on the portal and EDI services before its agreement renews on 2027-12-31. It asked for Security, Availability, Processing Integrity and Confidentiality. Losing the alliance is P01 R-043 (High).

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in access reviews, recovery testing, change management and vendor oversight. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1, issue a Type 1 report as of 2027-03-31, then run a 6-month observation period from 2027-04-01. The alliance accepted this plan on 2026-09-10, with quarterly status updates.

**Alternatives considered:**
- **Security questionnaire and the Coast Guard Plan only:** not acceptable to the alliance's vendor risk program, and the Plan is SSI, so it cannot be shared with customers.
- **ISO/IEC 27001 certification:** the alliance asked for SOC 2 specifically; certification would also take longer than the renewal window.
- **CTPAT partnership:** voluntary supply chain security program; it does not give the alliance assurance over portal and EDI controls. Decision on CTPAT deferred to 2027 by the PE sponsor.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so that the internal audit work in P07 does not create an independence question.

**SSI boundary.** The system description and the auditor's workpapers must not disclose SSI (49 CFR 1520.9). The description will cover the portal and EDI services at the level a customer needs, and FSP or Plan details will stay out of it (POL-04 4.2).

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Customer portal and truck appointment services; EDI services with carriers, T2 customers and trucking companies; the customs release and hold feed as an input to those services |
| Infrastructure | Cloud landing zone accounts that host the portal, EDI gateway, integration services and TOS database (P04); identity provider; SIEM; the T1 gate server room for the gate transaction interface |
| Software | Customer portal (company-built), EDI gateway and integration services, TOS modules that feed the portal and EDI (container availability, holds, appointments, billing events) |
| People | TOS application team (5) and the development contractor, IT and security team, customer service (portal support), MSSP, vCISO |
| Data | Container status and availability, bills of lading and booking data, appointments, trucking company and driver contacts, invoices; driver license numbers (tokenized in the portal) |
| Procedures | POL-01 to POL-05, the standards index, both P08 runbooks, the contingency plan (due 2026-12-31) |
| Subservice organizations (carve-out) | Public cloud provider, identity provider, MSSP and its SIEM platform, payment service provider (hosted payment page; card data never reaches the company). Their controls are covered by their own reports and the complementary subservice organization controls in the system description |
| Out of scope | Crane and yard equipment OT, the T2 network, security systems, the FSPs and the Cybersecurity Plan (covered by the Coast Guard rule, not by SOC 2) |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 13 | 16 | 4 | 0 |
| Availability (A1, 3) | 2 | 0 | 1 | 0 |
| Processing Integrity (PI1, 5) | 1 | 4 | 0 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **16** | **22** | **5** | **18** |

**Ready (16):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC4.2, CC5.1;
- access, physical and media: CC6.2, CC6.4, CC6.5;
- malware and event evaluation: CC6.8, CC7.3;
- capacity and backup infrastructure: A1.1, A1.2;
- stored data integrity: PI1.5.

**Not ready (5):**
- CC6.3: transfers keep prior roles, semiannual reviews, gate module accounts outside the identity provider;
- CC6.7: 2 carrier services still send EDI by plain FTP;
- CC7.5 and A1.3: recovery is not tested and the RTO was missed;
- CC8.1: the development contractor can merge to production without company approval.

Each maps to a P07 POA&M item. Most Partially ready criteria depend on standards being issued (P06), the TOS application audit log reaching the SIEM, and EDI processing checks (POAM-028).

**Processing Integrity is the category most specific to a terminal.** Carriers rely on accurate and complete status messages, and a wrong release status can let a held container leave the gate. The controls exist in part (syntax and check-digit validation, daily reconciliation for the 9 T1 carrier services), but they need business-rule checks on release changes and completeness reports for outbound messages before the observation period.

**Privacy is out of scope.** The alliance did not request it. The limited personal information in the portal (trucking company contacts, driver details) is protected under Security and Confidentiality and Fla. Stat. 501.171.

**Mapping to other work.** Evidence is reused from P02 (control statements), P04 (shared responsibility), P05 (availability commitments), P06 (policies), P07 (test results) and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.4, CC2.3, CC6.6, CC6.7, CC7.1, CC7.4, CC8.1, CC9.1, PI1.1, C1.1 | Training records; portal security commitments; vulnerability disclosure channel; FTP retirement; static analysis results; branch protection settings; drill report (2026-11-18); contingency plan; processing commitments |
| 2027 Q1 | CC1.2, CC2.1, CC2.2, CC3.3, CC3.4, CC5.2, CC5.3, CC6.1, CC6.3, CC7.2, CC7.5, CC9.2, A1.3, PI1.2, PI1.3, PI1.4, C1.2 | Audit committee minutes; SIEM source list with the TOS audit log; two-person override records; quarterly access review sign-offs; privileged access management logs; customer administrator MFA; failover and restore test records; vendor contract amendments; reconciliation reports; retention schedule |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the alliance | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, restore tests, reconciliations, vendor reviews, change tickets) |
| 2027-11-30 | Type 2 report delivered to the alliance | |

**Status reporting.** The vCISO reports readiness monthly to the Chief Operating Officer and quarterly to the audit committee and the alliance.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 8 Common/Inherited and 34 Hybrid), and Subpart F requires a process for vendors to notify the company of vulnerabilities and incidents and monitoring of third-party remote connections (101.650(f)(2)-(3)). The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of the vendor and remote access standard (STD-04).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Remote or network access to critical IT or OT systems, hosting of critical systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or an equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and notification terms | Annually |
| **Tier 2** | Other system access or company Confidential or Restricted data | Security questionnaire; SOC 2 if available; contract terms | Every 2 years |
| **Tier 3** | No access and no sensitive data | Contract terms only | At contract renewal |

Applying it to the 27 vendors with remote or network access, plus the 3 providers that host or broker critical systems (the cloud provider, the identity provider and the remote access service vendor), gives 12 Tier 1 and 18 Tier 2 vendors. The CSV holds the first 8 Tier 1 reviews and 1 Tier 2 example. The remaining 4 Tier 1 reviews (the T1 crane OEM, the OCR vendor, the reefer monitoring vendor and the CCTV integrator) are due by 2027-03-31 (POAM-019).

**Key findings:**
1. **Four reports on file, all unqualified** (cloud provider, identity provider, MSSP, TOS vendor). The vendors' controls protect the company only when the company's complementary controls work, and several are open gaps: failover testing (POAM-010), access reviews (POAM-001), MSSP log sources (POAM-005, POAM-006) and vendor support sessions (POAM-003).
2. **MSSP:** escalation missed the 30-minute target in 2 of 40 samples, and the SIEM platform is carved out. The platform's own report must be obtained.
3. **Three Tier 1 vendors have no assurance report:** the privileged remote access service vendor, the T2 mobile harbor crane OEM and the scheduling optimization vendor. The first two sit directly on the path to crane controllers (P01 R-003). Each needs an alternative (questionnaire, penetration test summary, contract terms) before the company relies on it.
4. **The T2 OEM holds the only copies of T2 PLC programs,** so T2 recovery depends on a vendor with no notification terms and no assurance report (POAM-011, POAM-019).
5. **The TOS vendor's 72-hour notice term** does not meet the Subpart F standard of notice without delay. An amendment is requested.
