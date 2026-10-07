# SOC 2 Readiness Summary: Cris Santos Company | Government Services and Facilities | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed facilities support contractor operating government buildings) |
| Tier / Vertical | Mid-Market / Government Services and Facilities |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | SOC 2 **Type 1** as of 2027-06-30, then **Type 2** with an observation period of 2027-07-01 to 2027-12-31 (report expected by 2028-02-28, ahead of the state contract deadline of 2028-06-30) |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-15 by the vCISO and the GRC analyst, using P02, P05, P06, and P07 evidence |

## 1. Why SOC 2 for this organization
**The company is a service organization for its state, county, and city customers.** It operates their building automation and access control systems on its own platform (the IFOP), holds about 41,000 cardholder records and their security system layouts, and monitors 46 sites around the clock. The customers' own security depends on the company's controls. That is the situation SOC 2 is designed to report on.

Three customer demands make it concrete:
- **State agency.** The renewal term that began 2026-07-01 requires a SOC 2 Type 2 report by 2028-06-30, in addition to the annual independent assessment against SP 800-53 Moderate.
- **County A and County B.** Their addenda ask each year for a SOC 2 report or an equivalent independent assessment. The 2026 P07 assessment and this readiness report are the equivalent for now.
- **The City** has said it will add the same request at its 2027 renewal.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in remote access, OT monitoring, recovery, and subcontractor oversight. Starting the observation period before those close would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q2, issue a Type 1 report as of 2027-06-30, then run a 6-month observation period.

**Alternatives considered:**
- **GovRAMP:** verifies cloud providers selling to state and local governments. The company hosts BAS supervisory services for the state, so the state may ask for it at the 2028 rebid. It is not law and not in any current contract. Building SOC 2 evidence on SP 800-53 now keeps that option open (C-GOVERNMENT-R08).
- **FedRAMP:** not applicable. The company operates no system for GSA; GSA's building systems run under GSA's own ATO.
- **CMMC:** a DoD program; the company has no DoD contracts.
- **An SP 800-53 assessment only:** the state already gets one each year (P07). The counties accept it today but asked for SOC 2 because their auditors understand it. AICPA's mapping of the Trust Services Criteria to SP 800-53 lets one control set serve both.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so that the P07 work does not create an independence question.

**Why Availability and Confidentiality.** Customers rely on the ROC and access control administration staying available (BIA BP-01 to BP-03) and on security plans, cardholder data, face templates, and GSA CUI staying confidential. Processing Integrity and Privacy were not requested.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | 24x7 remote monitoring and operation of building automation and access control for the state, County A, County B, and the City; badge administration; video support; critical environment support for the County A EOC and the state data center building |
| Infrastructure | IFOP components (P02): BAS clusters, broker, 5-account landing zone (P04), 46 site edge firewalls, OT sensors, primary and backup ROC |
| Software | BAS supervisory software, access control and video SaaS tenants, identity provider, CMMS |
| People | ROC (24 staff), Building Technology (60), IT and security (18), program managers, and the subcontractors with remote access |
| Data | Cardholder records, face templates, video exports, building drawings and security system layouts |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, and manual-mode procedures |
| Subservice organizations (carve-out) | Cloud provider, access control SaaS vendor, identity provider vendor, MSSP, CMMS vendor. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the company's system description |
| Excluded | GSA's building systems (GSA-owned and authorized), the school district's BAS server, and corporate ERP and HR systems |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 8 | 19 | 6 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **9** | **22** | **7** | **23** |

**Ready (9):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring: CC4.1, CC4.2;
- control design: CC5.1;
- capacity: A1.1.

**Not ready (7):**
- CC6.1: subcontractor remote access outside the broker; shared accounts (POAM-001, POAM-003);
- CC6.3: late removal in customer tenants and excess privilege (POAM-004, POAM-005);
- CC6.6: flat networks, the cellular modem, and stale edge firmware (POAM-006, POAM-008);
- CC7.1: no OT vulnerability identification or OT baselines (POAM-007, POAM-008, POAM-015);
- CC7.2: OT events not monitored (POAM-011);
- CC7.5 and A1.3: recovery tests missed their RTOs, and 4 customers lack manual-mode procedures (POAM-009, POAM-010).

Each maps to a P07 POA&M item. Most Partially ready criteria depend on standards being issued (P06) and on subcontractor terms (POAM-013).

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies and standards), P07 (test results and samples), and P08 (incident procedures). The `related_sp800_53` column links each criterion to P02 controls.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC6.1 (subcontractors onto the broker; shared accounts retired), CC6.4, CC6.5, CC6.7, CC2.2, CC3.3, CC9.2, C1.1 | Broker session approvals; weekly bypass checks; key log; wipe receipts; data loss rule reports; acknowledgments; signed subcontractor addenda |
| 2027 Q1 | CC1.2, CC1.4, CC2.3, CC3.4, CC5.2, CC5.3, CC6.2, CC6.3, CC7.3, CC7.4, CC7.5, CC8.1, CC9.1, A1.2, A1.3, C1.2 | Quarterly access reviews; tenant federation records; OT training records; standards; tabletop reports; restore test records; CMMS approvals with hashes; contingency plan; interconnection agreements |
| 2027 Q2 | CC2.1, CC6.6, CC6.8, CC7.1, CC7.2 | Segmentation change records; sensor coverage at 46 sites; OT events in the SIEM; firmware reports; workstation replacements |
| 2027-06-30 | Type 1 report (design) | Management's system description and assertion |
| 2027-07-01 to 2027-12-31 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans and firmware reviews, quarterly restore tests, weekly change reports, annual subcontractor reviews) |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee, and sends a short status to the state agency and County A each quarter.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 22 Common/Inherited and 62 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of STD-03.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Holds customer personal information or CUI, has privileged or remote access to company or customer systems, or supports a High-criticality BIA process | SOC 2 Type 2 (or, where none exists, a security questionnaire plus an evidence-based review) and a bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited personal information, no privileged access, supports Moderate or Low processes | SOC 2 if available, otherwise a security questionnaire | Every 2 years |
| **Tier 3** | No customer data and no system access | Contract terms only | At contract renewal |

The CSV holds 8 reviews: 7 Tier 1 (the access control SaaS vendor, cloud provider, identity provider, MSSP, CMMS vendor, BAS software vendor, and integrator SUB-1) and 1 Tier 2 (the HR suite). Reviews of SUB-2 to SUB-7 follow the SUB-1 model by 2027-03-31 (POAM-013).

**Key findings:**
1. **Access control SaaS vendor:** unqualified Type 2 for Security, Availability, and Confidentiality, and its RTO and RPO meet the BIA. But **the face verification and video analytics modules are not in the system description**, so the company has no assurance for the systems that hold face templates and run the analytics (P10). Two of the CUECs the company must operate are open gaps: quarterly access reviews (POAM-004) and audit log review (POAM-011). **The vendor's controls only protect the customers once those gaps close.**
2. **BAS software vendor:** no SOC 2 and no incident notice commitment. Contract terms at the 2027 renewal.
3. **MSSP:** one missed escalation in 40 samples; the SIEM platform is carved out, so its own report must be obtained.
4. **CMMS vendor:** no fixed breach notice time, which is why P01 R-028 is shared through a 72-hour clause at renewal.
5. **SUB-1:** the model subcontractor review. The other six OT subcontractors have not been reviewed.
