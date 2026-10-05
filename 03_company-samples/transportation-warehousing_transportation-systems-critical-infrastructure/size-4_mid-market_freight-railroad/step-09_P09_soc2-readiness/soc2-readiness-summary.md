# SOC 2 Readiness Summary: Cris Santos Company | Transportation Systems | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed Class II regional freight railroad, north and central Florida) |
| Tier / Vertical | Mid-Market / Transportation Systems |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Processing Integrity (PI1) |
| Target report | SOC 2 **Type 2** on the shared dispatch and car management service, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30. Interim Type 1 as of 2027-03-31 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-15 by the vCISO and the Cybersecurity Manager, with the Director of Customer Service and Car Management, using P02, P05, P06, and P07 evidence |

## 1. Why SOC 2 for this organization
A freight railroad is not usually a SOC 2 service organization: it moves freight, and its assurance obligations run to TSA and the FRA, not to customers' auditors. That changed in 2025:
- Since 2025-07 the company **dispatches 2 affiliated Class III short lines** (140 route miles under track warrant control) from desks in its NOC and runs their car management in its TMS. That is $4 million a year of service revenue (P05).
- On 2026-06-12 a **third, unaffiliated short line** signed a services agreement for the same service, starting 2027-01-01 (about 90 route miles). Its agreement requires a SOC 2 Type 2 report on the service, covering at least 6 months, by 2027-12-31. It asked for Security, Availability, and Processing Integrity: dispatching must be secure, available (2-hour restoration), and accurate (correct authority and car records).

For that service, the company is a service organization, and a SOC 2 Type 2 report is the assurance the customer asked for.

**What SOC 2 does not replace.** The TSA directives and FRA rules remain the binding requirements for the TDPO. SOC 2 is a contractual assurance report for the service customers. Much of the evidence overlaps (P07 results also count toward the TSA CAP), but the SOC 2 report must not describe vulnerabilities in a way that discloses SSI. The system description is reviewed by the Director of Safety, Security, and Hazmat for SSI before issue, and the service auditor signs a need-to-know record (POL-04 4.2).

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated over a period. P07 found gaps in access reviews, patching, CAD/CTC monitoring, and recovery testing. Starting the period before those are fixed would produce exceptions on the criteria the customer cares about most (CC6.3, CC7.2, CC7.5, A1.3). The plan is to remediate through 2027 Q1, then run a 6-month observation period from 2027-04-01. That meets the 2027-12-31 contract date with about a month of margin.

**Alternatives considered:**
- **Type 1 first (point in time, as of 2027-03-31):** offered to the contracted short line as an interim deliverable. It agreed, with quarterly status updates.
- **Security questionnaire or an agreed-upon procedures report:** the contracted short line's lenders asked specifically for SOC 2.
- **Including the 2 affiliates only by contract:** they are owned by the same sponsor and accept the report as their evidence too, so one report covers all 3 customers.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the P07 work does not raise an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Train dispatching (track warrants, work authority, bulletins) for the client railroads' lines; car management (car orders, switch lists, waybills, car location reports) in the TMS |
| Infrastructure | TDPO components used by the service (P02): CAD/CTC office system and the affiliate desks at the primary NOC and backup NOC; dispatch radio consoles; dispatch zones and boundary firewalls; identity; the backup vault in the cloud landing zone (P04) |
| Software | CAD/CTC office system, TMS (vendor SaaS), identity provider, PAM, EDR, SIEM |
| People | 36 dispatchers including 4 chief dispatchers; 12 car management and customer service staff; the IT and cybersecurity team; the MSSP |
| Data | Movement authorities, train sheets, and dispatcher logs for the client lines; client car and waybill data, including RSSM flags |
| Procedures | POL-01 to POL-05, the standards index, the manual dispatch procedure, and the P08 runbooks |
| Subservice organizations (carve-out) | TMS vendor, cloud provider, identity provider, MSSP. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the system description (Part B) |
| Out of scope | The company's own CTC field network and PTC systems (not used for the client lines); the client railroads' own field equipment and crews |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A | Total |
|---|---|---|---|---|---|
| Security (CC1-CC9) | 13 | 16 | 4 | 0 | 33 |
| Availability (A1) | 1 | 1 | 1 | 0 | 3 |
| Processing Integrity (PI1) | 2 | 3 | 0 | 0 | 5 |
| Confidentiality (C1) | 0 | 0 | 0 | 2 | 2 |
| Privacy (P1-P8) | 0 | 0 | 0 | 18 | 18 |
| **Total** | **16** | **20** | **5** | **20** | **61** |

Of the 41 in-scope criteria, 16 are Ready, 20 Partially ready, and 5 Not ready.

**Ready (16):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC2.2, CC3.1, CC3.2, CC4.2, CC5.1;
- access and protection: CC6.2, CC6.4, CC6.5, CC6.7, CC6.8;
- capacity: A1.1;
- processing: PI1.3 (CAD/CTC authority checks), PI1.4 (daily car location reports, 20 of 20 reconciled).

**Not ready (5):**
- CC6.3: application role reviews annual; dual administrator rights;
- CC7.1: CAD/CTC servers 14 months behind certified patches;
- CC7.2: CAD/CTC events, the core of the service, are not monitored;
- CC7.5 and A1.3: restoration of CAD/CTC from backup has never been tested, so the 2-hour restoration commitment is not demonstrated.

Each maps to a P07 POA&M item (POAM-001, POAM-002, POAM-006, POAM-007, POAM-011). The Partially ready criteria mostly depend on standards being issued (P06), the contract and system description work (POAM-014, POAM-022), and the contingency plan (POAM-010).

**Why Processing Integrity matters here.** For a dispatch service, a processing error is a safety event: a wrong authority or a wrong car record. PI1.3 is Ready because CAD/CTC enforces authority limits and conflict checks and dispatchers use read-back. The gaps are upstream, in car data inputs (PI1.2) and written processing specifications (PI1.1).

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls.

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.3 (system description and security schedule), CC3.4 (CIP amendment; onboarding assessment), CC6.1 (named accounts), CC6.3 (termination workflow, dual rights removed, first quarterly role review), CC6.6 (vendor access through the jump host), CC7.1 (certified patch level), CC7.3 (classification checklist), CC7.4 (runbooks adopted; 2026-12-10 exercise with affiliate notice), CC9.1 (contingency plan), PI1.1 (processing specifications) | Account lists; role review sign-offs; PAM session records; patch reports; incident log with identification times; exercise report; signed plan |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC3.3, CC4.1, CC5.2, CC5.3, CC7.2 (CAD/CTC logs in the SIEM), CC7.5 and A1.3 (quarterly restore tests), CC8.1, CC9.2, PI1.2, PI1.5 | Audit committee minutes; role training records; SIEM source list and alert reviews; restore test reports with data reconciliation; change tickets; vendor reviews; consist exception reports |
| 2027-03-31 | Type 1 report date (design) | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring evidence: quarterly role reviews, monthly patch and scan reports, restore tests, MSSP monthly reports, daily reconciliations, vendor reviews |
| 2027 Q3 | A1.2 (alternate dispatch arrangement for a storm affecting both NOCs) | Emergency read access test; affiliate dispatch support agreement |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee and the client railroads.

## 5. Vendor SOC 2 review program (Part B)
The TDPO relies on vendors for many inherited and hybrid controls (P02: 28 Hybrid and 5 Common/Inherited). The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of the vendor risk standard (STD-03).

**Tiering approach (STD-03):**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Reaches a Critical Cyber System, holds SSI, or supports a High-criticality BIA process | SOC 2 Type 2 plus bridge letter, or, where no SOC 2 exists (OT vendors), a security questionnaire with evidence and a contract security schedule; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability against the BIA, and incident notice terms | Annually |
| **Tier 2** | Holds Restricted data or supports a Moderate process | SOC 2 or a security questionnaire | Every 2 years |
| **Tier 3** | Neither | Contract terms only | At renewal |

The company has 8 Tier 1 vendors. At P07 fieldwork, SOC 2 reports had been reviewed for 3 of them (TMS, cloud provider, identity provider). Since then the MSSP and PTC vendor reports were reviewed, and questionnaire-based reviews were done or started for the 3 OT vendors without SOC 2 reports. The CSV holds all 8 Tier 1 vendors and 2 Tier 2 examples (10 rows). The radio and detector vendor reviews finish by 2027-01-31, within the POAM-014 date of 2027-03-31.

**Key findings:**
1. **TMS vendor (VEN-01):** unqualified Type 2 covering Security, Availability, and Processing Integrity, with 2 exceptions. Its stated RTO of 24 hours **does not meet the BIA** (8 hours for car management; 30 minutes for the RSSM duty). It is the main subservice organization for the shared service, so its CUECs (access reviews, data input accuracy) become the company's controls in the SOC 2 report, and both have open gaps.
2. **PTC vendor (VEN-05):** unqualified Type 2, Security only. Its 8-hour support SLA does not meet the 6-hour RTO for PTC operations.
3. **MSSP (VEN-02):** unqualified Type 2 with an escalation exception. Its contract excludes OT, which is the larger risk (POAM-006).
4. **OT vendors without SOC 2 (VEN-06 to VEN-08):** the CAD/CTC, radio, and detector vendors have no SOC 2 and no security terms. For them, the company's own controls on the access path (PAM jump host) are the assurance, which is why POAM-004 and POAM-014 matter.
5. **Incident notice:** only the PTC vendor has a 24-hour security incident notice term. STD-03 sets 24 hours for Tier 1 OT vendors at renewal.
