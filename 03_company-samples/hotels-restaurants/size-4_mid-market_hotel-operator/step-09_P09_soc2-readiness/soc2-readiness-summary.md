# SOC 2 Readiness Summary: Cris Santos Company | Accommodation and Food Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Florida hotel owner and operator: 2 independent resorts and 4 franchised select-service hotels) |
| Tier / Vertical | Mid-Market / Accommodation and Food Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2** on the hotel management platform, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30. The REIT management agreement requires it within 18 months of the 2027-01-01 start date, that is by 2028-07-01 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 and AOC review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 to 2026-09-04 by the vCISO, the Security Manager, and the GRC Analyst, using P02, P05, P06, and P07 evidence; approved by the Chief Operating Officer 2026-09-15 |

## 1. Why SOC 2 for this organization
A hotel owner that runs its own hotels is not a SOC 2 service organization: it sells rooms, food, and events to guests. Its assurance tool is **PCI DSS validation** (the vertical's named alternative), and that remains the case for the 6 owned hotels (P03).

That changes on **2027-01-01**. Under the hotel management agreement signed 2026-06-30 (fictional), the company will manage 2 hotels owned by a publicly traded lodging REIT and will provide them with central reservations, revenue management, accounting, and its IT platform. For those services the company is a service organization, and the REIT relies on its controls.
- **Accounting services** affect the REIT's financial reporting, so the REIT asked for a **SOC 1 Type 2** report. That is a separate engagement on internal control over financial reporting and is not assessed here.
- **The hotel management platform** holds the REIT hotels' guest data, rates, and operating data. The REIT asked for a **SOC 2 Type 2** report covering **Security, Availability, and Confidentiality**.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in access reviews, vendor oversight, logging, and recovery testing. Starting the observation period before they are fixed would produce exceptions. The plan is to remediate through 2027 Q1 and run a 6-month observation period from 2027-04-01 (P01 R-047).

**Alternatives considered:**
- **Type 1 first:** not needed. The REIT's 18-month window allows a Type 2 report first, and a Type 1 would cost about the same preparation effort for less assurance.
- **PCI DSS AOC only:** the REIT asked for SOC 2; an AOC covers card data only, not availability or the owners' confidential data.
- **Questionnaire only:** not acceptable under the agreement.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is neither the co-sourced internal audit firm (which performed P07) nor the QSA firm, so that no assessor reviews its own work.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Central reservations (CRO), revenue management, and hosting of hotel operating data for the 2 REIT-owned managed hotels. Accounting services are covered by the SOC 1 report |
| Infrastructure | Corporate office and CRO network and PCs; SD-WAN; the 4-account cloud landing zone (P04); the privileged access broker; the backup account |
| Software | Resort PMS tenant (SYS-01, onto which the managed hotels move from 2027-01-01), identity provider (SYS-09), data warehouse and CRM (SYS-10), revenue-management system (SYS-13), contact center (SYS-15), productivity suite (SYS-11), SIEM (SYS-12) |
| People | CRO (22 agents), revenue management, the IT team (8), Security Manager and analyst, GRC Analyst, vCISO, MSSP |
| Data | Managed hotels' guest profiles and reservations, rates and forecasts, operating and financial data (classified Confidential under POL-04) |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks, and the BIA recovery objectives |
| Out of scope | Resort-specific systems (lock servers, Resort 2 POS, CCTV), Hotels 3 to 6 and the franchisor's platform, and the managed hotels' own on-site systems, which stay with the owner |
| Subservice organizations (carve-out) | SYS-01 vendor, public cloud provider, identity provider, MSSP and its SIEM platform, contact center vendor, revenue-management vendor. Their controls are covered by their own reports and the complementary subservice organization controls in the company's system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 17 | 6 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **11** | **19** | **8** | **23** |

**Ready (11):**
- governance and risk: CC1.1, CC1.2, CC1.3, CC3.1, CC3.2;
- monitoring: CC4.1, CC4.2;
- control design: CC5.1;
- access provisioning: CC6.2;
- event evaluation: CC7.3 (MSSP escalated a simulated attack in 22 minutes);
- capacity: A1.1.

**Not ready (8):**
- CC2.1: inventory and data flows incomplete (POAM-007, POAM-016);
- CC6.3: access reviews, transfers, card display rights (POAM-001, POAM-002);
- CC6.6: vendor remote access without MFA; slow edge patching (POAM-004, POAM-010);
- CC6.7: card data in email and recordings (POAM-013);
- CC7.5 and A1.3: recovery never tested (POAM-011);
- CC9.2: vendor management (POAM-012);
- C1.2: no retention schedule in force (POAM-017).

Each Not ready criterion maps to a P07 POA&M item. Most Partially ready criteria depend on standards being issued (P06 schedule) and on monitoring coverage. Readiness itself is tracked as POAM-021.

**Processing Integrity and Privacy are N/A** because the REIT did not request them. Accounting accuracy is covered by the SOC 1 report, and guest privacy duties come from the FTC Act and state law (P03).

**What helps.** Several Not ready findings concern resort systems that are outside the SOC 2 boundary (the Resort 2 POS, lock servers, Hotels 3 to 6). They still count here because the directory, the identity provider, vendor access, and the SIEM are shared across the whole company. Fixing the shared controls closes both the PCI DSS and SOC 2 gaps.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.1 (device inventory), CC3.4, CC6.3, CC6.5, CC6.6 (vendor access), CC6.7, CC7.4, C1.2 | Reconciled inventory; AI intake records; 6-month review sign-offs; transfer tickets; wipe certificates; broker session logs; data discovery scans; tabletop reports; deletion records |
| 2027 Q1 | CC1.4, CC1.5, CC2.2, CC2.3, CC3.3, CC5.2, CC5.3, CC6.1, CC6.4, CC6.8, CC7.1, CC7.2, CC7.5, CC8.1, CC9.2, A1.2, A1.3, C1.1 | Standards; system description draft; fraud review; broker logs for administrators; closet key logs; EDR coverage reports; monthly scan reports; SIEM source list; restore test records; change tickets; Tier 1 vendor reviews; SYS-01 recovery terms; data warehouse tagging |
| 2027-03-15 | Readiness review by the selected service auditor | Management's draft system description and control matrix |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (6-month access reviews, monthly scans, quarterly restore tests, vendor reviews, daily log review records) |
| 2027 Q2 | CC9.1 (hurricane plan IT sections by 2027-05-31) | Updated hurricane plans |
| By 2027-11-30 | SOC 2 Type 2 report to the REIT | Report and bridge letter process |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee. From 2027-01-01 the COO also gives the REIT a quarterly status update.

## 5. Vendor SOC 2 and AOC review program (Part B)
The company relies on vendors for many controls (P02 inherited and hybrid controls; P04 shared responsibility). For a hotel company, a SOC 2 report is not enough on its own: any vendor that stores, processes, or transmits card data, or can affect its security, must also provide a **PCI DSS service provider AOC** each year (PCI DSS 12.8.4), and the split of requirements must be written down (12.8.5). The program in `vendor-soc2-review.csv` reviews both and is the core of STD-03.

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Card data; guest data at scale (more than 10,000 guests); privileged or remote access to company systems; or support for a High-criticality BIA process | SOC 2 Type 2 plus bridge letter, **and** a service provider AOC where card data or the CDE is involved; review of opinion, scope, subservice organizations, exceptions, complementary user entity controls mapped to company controls, availability against the BIA, and notice terms | Annually |
| **Tier 2** | Limited guest data, no card data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No guest or card data and no system access | Contract terms only | At renewal |

Of the 31 vendors that handle card or guest data, 12 are Tier 1. The CSV holds 10 of the 12 Tier 1 reviews and 1 Tier 2 example (the revenue-management vendor). The remaining 2 Tier 1 reviews (the HR and payroll vendor with time clock finger templates, and the SD-WAN managed service provider) are due by 2027-03-31 (POAM-012).

**Key findings:**
1. **Resort PMS vendor (VEN-01):** unqualified Type 2 and a current AOC. Its stated RTO of 4 hours **does not meet the 2-hour check-in RTO** (BP-01), and recovery terms are not in the contract. Every complementary user entity control it lists (user removal, least privilege, activity review, workstation protection) is an open company gap. **The vendor's controls protect guest data only once those gaps close.** The report does not cover Confidentiality, which the REIT wants; the company will ask the vendor to add it.
2. **Channel manager (VEN-06):** its AOC expired in 2026-04 and it has no SOC 2 report, although online travel agency virtual cards pass through it. Current AOC by 2027-01-31 or replacement.
3. **Contact center vendor (VEN-07):** says card data is outside its PCI DSS scope, but spoken card numbers pass through its platform. Pause-and-resume recording and keypad entry remove the question (POAM-013, POAM-016).
4. **Resort 2 POS vendor (VEN-11):** no SOC 2, no AOC, and always-on remote access into the CDE, the entry point in the R-001 scenario. Its access moves to the broker by 2026-11-30, and the relationship ends with the P2PE cloud POS in 2027.
5. **Booking engine (VEN-05) and revenue-management vendor (VEN-08)** have Type 1 reports only. Both will be asked for Type 2 reports because they will support the REIT services.
6. **Incident notice terms are too slow.** Most vendors promise notice within 72 hours of *confirming* an incident. The company's acquirer clock is 24 hours from *suspicion*, and Florida gives a third-party agent at most 10 days (Fla. Stat. 501.171(6)(a)). STD-03 sets the contract language for renewals.

**The franchisor** is not in the vendor list, but it runs the brand PMS, gateway, and firewalls at Hotels 3 to 6. It has provided a summary letter on its PCI DSS compliance, not an AOC copy, and there is no written responsibility matrix. Both are required by 2027-03-31 (POAM-012; P01 R-006).
