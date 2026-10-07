# SOC 2 Readiness Summary: Cris Santos Company | Emergency Services | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (licensed private ambulance service; PE-backed) |
| Tier / Vertical | Mid-Market / Emergency Services |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1), Confidentiality (C1) |
| System | EMS billing services provided to 4 municipal fire-rescue departments |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-04 by the vCISO, the Security Manager, and the Director of Revenue Cycle, using P02, P05, P06, and P07 evidence; presented to the audit committee 2026-09-16 |

## 1. Why SOC 2 for this organization
An ambulance service is usually **not** a SOC 2 service organization, because it delivers care to patients rather than services to other businesses. The billing services line changes that:
- The company bills ambulance claims for 4 municipal fire-rescue departments, about 70,000 client transports and about $52 million of client collections a year.
- Each department is a HIPAA covered entity, and the company is its business associate.
- The clients rely on the company's controls for the security, timeliness, and accuracy of their claims and the confidentiality of their patients' data.
- Two clients' renewals (2027 and 2028) now require an annual SOC 2 Type 2 report. The other two accept a report if one is available.

For the billing services, the company is a service organization, and a SOC 2 Type 2 report is the right assurance tool. The dispatch and patient care platform (P02) is **not** in this report's scope: it serves the company's own patients and the counties, which rely on contract terms and the P07 assessment instead.

**Why these categories.**
- **Security** is required in every SOC 2 report.
- **Processing Integrity** matters most to the clients: claims must be complete, accurate, timely, and authorized. It is also where the AI coding module (AI-003) creates risk.
- **Confidentiality** covers client data separation and return or destruction at contract end.
- **Availability** covers the clients' cash flow during platform or company outages.
- **Privacy** criteria are out of scope. Patient privacy duties run through HIPAA and the client BAAs, and the clients did not request the Privacy category.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 and this assessment found gaps in access reviews, change management, vendor management, and AI coding review. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1, then run a 6-month observation period from 2027-04-01.

**Alternatives considered:**
- **Type 1 first (point in time):** offered to the 2 requiring clients as an interim report for 2027-03-31. Both agreed to accept this plan with quarterly status updates.
- **HITRUST certification:** heavier than the clients asked for.
- **Security questionnaire only:** acceptable to 2 clients, but not to the 2 whose renewals require SOC 2.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so that the internal audit work in P07 does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Claims coding, submission, follow-up, payment posting, and client reporting for 4 municipal fire-rescue departments |
| Infrastructure | Revenue cycle office at headquarters; identity provider (SYS-04); productivity suite and cloud fax (SYS-05); company endpoints used by the billing services team |
| Software | Billing and revenue cycle platform with clearinghouse (SYS-03), including the AI coding module (AI-003) |
| People | 18 billing services staff (part of the 48 revenue cycle staff), the Director of Revenue Cycle, the IT and security team, the MSSP |
| Data | Client patients' PHI from client ePCR imports, claims, remittances, and client reports |
| Procedures | POL-01 to POL-05, the standards index (P06), the P08 billing vendor breach runbook, and the billing services procedures still to be written |
| Subservice organizations (carve-out) | Billing platform vendor (with its clearinghouse affiliate), identity provider, cloud fax vendor, MSSP. Their controls are covered by their own SOC 2 reports and by the complementary subservice organization controls listed in the company's system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 13 | 15 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Processing Integrity (PI1, 5) | 1 | 3 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **15** | **21** | **7** | **18** |

**Ready (15):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2;
- monitoring and control design: CC4.1, CC4.2, CC5.1;
- access and assets: CC6.2, CC6.4, CC6.5, CC6.8;
- capacity and storage: A1.1, PI1.5.

**Not ready (7):**
- CC2.3: no system description, statement of service commitments, or client incident notice procedure;
- CC6.3: annual reviews, and all 18 billing staff can open all 4 client workspaces;
- CC7.4: the client notice procedure is not written and the runbook is not exercised;
- CC8.1: changes to coding rules, fee schedules, and the AI module have no second approver or test;
- CC9.2: vendor standard not issued; 2 subcontractor BAAs do not cover client PHI;
- A1.3: the company has never tested its own outage workarounds;
- PI1.3: about 35% of claims were coded straight through by AI-003 without human review.

Each maps to a P07 POA&M item (POAM-001, POAM-014, POAM-017, POAM-020, POAM-021, POAM-022). The Partially ready criteria mostly depend on standards being issued (P06), billing services procedures being written, and monitoring of billing platform logs.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments for BP-08 and BP-09), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to SP 800-53 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.4, CC2.1, CC2.3, CC3.3, CC3.4, CC5.3, CC6.1, CC6.7, CC7.1, CC7.3, CC8.1, CC9.2, A1.2, PI1.1, PI1.2, PI1.3, PI1.4, C1.1, C1.2 | System description draft; client teams and workspace restrictions; portal-only client reports; daily import reconciliations; 100% coder review records and monthly AI accuracy audits; change tickets with second approval; signed BAA extensions; fraud risk assessment |
| 2027 Q1 | CC1.2, CC5.2, CC6.3, CC6.6, CC7.2, CC7.4, CC7.5, A1.3 | Quarterly access review sign-offs; SIEM use cases for billing platform logs; tabletop report (2027-02-17); outage workaround test; STD-01 |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the 2 requiring clients | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly AI accuracy audits, daily reconciliations, vendor reviews) |
| 2027 Q2 | CC9.1 | Secondary platform evaluation |

**Status reporting.** The vCISO reports readiness monthly to the COO and the CFO, and quarterly to the audit committee and the 2 requiring clients.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 14 Common/Inherited and 33 Hybrid), and the billing services report will carve out its subservice organizations. The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor risk standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | PHI at scale (more than 10,000 patients), privileged access to company systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited PHI, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No PHI and no system access | Contract terms only | At contract renewal |

Of 58 vendors with PHI access, 9 are Tier 1 and 21 are Tier 2 under this approach. The CSV holds 7 Tier 1 reviews and 1 Tier 2 example. The remaining 2 Tier 1 reviews (the cardiac monitor relay vendor and the SD-WAN provider) are due by 2027-03-31 (POAM-017).

**Key findings:**
1. **Billing platform vendor (VEN-01):** unqualified Type 2 covering all four requested categories, and its recovery objectives meet the BIA. Two problems remain: its breach notice term (30 days) is too long for the company to meet its own 10-business-day term to clients, and the AI coding model was excluded from Processing Integrity testing. Both are follow-ups for the 2027 renewal.
2. **CAD vendor (VEN-03):** its report covers support operations only. The AI triage service (AI-001) is outside its scope, and the vendor's 8-business-hour reinstall support cannot meet the 1-hour CAD RTO, so the company must be able to rebuild CAD itself (POAM-012).
3. **ePCR vendor (VEN-02):** unqualified, and its RTO of 4 hours and RPO of 15 minutes meet the BIA. Its complementary user entity controls (user provisioning and audit review) are open company gaps (POAM-001, POAM-007). **The vendor's controls protect the company only once those gaps close.**
4. **MSSP (VEN-06):** one escalation exception, and the SIEM platform is carved out. Log source coverage is the company's CUEC and is incomplete (POAM-006).
5. **Cloud fax (VEN-08, Tier 2):** its BAA covers company patients only and must be extended to client PHI before the billing services observation period.
