# SOC 2 Readiness Summary: Cris Santos Company | Healthcare and Public Health | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed 112-bed community acute-care hospital) |
| Tier / Vertical | Mid-Market / Healthcare and Public Health |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Service in scope | Affiliated practice EHR services (BP-17): EHR access, user administration, help desk, training, and lab and imaging interfaces for 18 independent physician practices |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Hospital readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-17 by the vCISO and the Information Security Manager, using P02, P05, P06, and P07 evidence; vendor reviews 2026-08-17 to 2026-08-28 |

## 1. Why SOC 2 for a hospital
A hospital is usually **not** a SOC 2 service organization: it delivers care to patients, not services to other businesses. The affiliated practice program changes that for one service line:
- 18 independent physician practices (about 240 users) use the hospital's EHR through its ambulatory module, under the hospital's license.
- The hospital provides their accounts and roles, help desk, training, and lab and imaging interfaces under a services agreement, and is their **business associate** under a BAA with each practice.
- The two largest practices and the regional accountable care organization (ACO) they belong to asked for a SOC 2 Type 2 report covering Security, Availability, and Confidentiality before the 2027 contract renewals.

For that service, the hospital is a service organization and its controls affect the practices' own HIPAA compliance, so a SOC 2 Type 2 report is the right assurance tool. The hospital's inpatient and emergency operations are not in scope.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in access reviews, vendor access, recovery testing, and vendor oversight that would produce exceptions. The plan is to remediate through 2027 Q1 and start a 6-month observation period on 2027-04-01.

**Alternatives considered:**
- **Type 1 first (point in time):** offered to the practices and the ACO as an interim report as of 2027-03-31. Both largest practices accepted this plan with quarterly status updates.
- **HITRUST certification:** common in health care, but the ACO asked specifically for SOC 2, and HITRUST would cost more for one service line.
- **Security questionnaire only:** acceptable to 16 smaller practices, not to the ACO.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the internal audit work in P07 does not raise an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Affiliated practice EHR services (BP-17) |
| Infrastructure | Identity provider (SYS-02), the cloud landing zone that hosts the interface engine (SYS-04, P04), the campus network segments that carry help desk and interface traffic (SYS-06), help desk endpoints (SYS-07), security operations (SYS-10) |
| Software | EHR ambulatory module (vendor-hosted), interface engine, help desk ticketing, identity provider |
| People | Director of Physician Services and the physician services team, help desk, IT and security team, MSSP, vCISO |
| Data | Practice patients' PHI in the shared EHR; practice user identities |
| Procedures | POL-01 to POL-05, the standards index, the P08 runbooks (including practice notification), and the services agreement |
| Subservice organizations (carve-out) | EHR vendor, identity provider, cloud provider, MSSP. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the hospital's system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 18 | 5 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **11** | **21** | **6** | **23** |

**Ready (11):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring: CC4.1, CC4.2;
- control design: CC5.1;
- transmission and malware protection: CC6.7, CC6.8;
- capacity: A1.1.

**Not ready (6):**
- CC3.4: significant changes (an EHR upgrade switched on the sepsis model, and new practices were onboarded, without review);
- CC6.3: access reviews, departures, and practice role scope;
- CC6.6: vendor VPN accounts without MFA and a flat clinical network;
- CC7.5 and A1.3: recovery is not documented or tested, including the 8-hour practice restoration commitment;
- CC9.2: vendor management (42 PHI vendors without BAAs; the EHR vendor BAA does not expressly cover practice PHI).

Each maps to a P07 POA&M item. Most Partially ready criteria depend on standards being issued (P06), the practice user lifecycle, and monitoring coverage.

**Out of scope (23):** Processing Integrity was not requested. Privacy was not requested; the hospital's HIPAA privacy program and the BAAs cover practice data.

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments for BP-17), P06 (policies), P07 (test results), and P08 (incident and notification procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.3, CC3.4, CC6.2, CC6.3 (end dates, monthly reconciliation, role restriction), CC6.5, CC6.6 (vendor access platform), CC7.3, CC9.2 (BAAs and EHR vendor BAA amendment), C1.1 | Practice notification procedure; change impact reviews; sponsor attestations; reconciliation reports; device return certificates; vendor platform session logs; decision log; signed BAAs; synthetic test data |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.2, CC3.3, CC5.2, CC5.3, CC6.1, CC6.4, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1, CC9.1, A1.2, C1.2 | Audit committee minutes; help desk training; practice user training; fraud review; drift reports; standards; MFA for administrators; badge readers; monthly scans; access analytics; tabletop reports; DR plan; change tickets with second reviewer; practice exit procedure |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the practices and the ACO | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly reconciliations and scans, restore tests including practice access, vendor reviews) |
| 2027 Q2 | A1.3 (practice access in the April 2027 restore test) | Restore test record |

**Status reporting.** The vCISO reports readiness monthly to the COO and the Director of Physician Services, and quarterly to the audit committee, the two largest practices, and the ACO.

## 5. Vendor SOC 2 review program (Part B)
The hospital relies on vendor controls for many inherited controls (P02: 7 Common/Inherited and 38 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor risk standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | PHI at scale (more than 10,000 individuals), privileged or network access to hospital systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to hospital controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited PHI, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No PHI and no system access | Contract terms only | At contract renewal |

Of about 210 PHI vendors, 15 are Tier 1 and about 80 are Tier 2 under this approach. The CSV holds the first 8 Tier 1 reviews (the EHR vendor, MSSP, cloud provider, identity provider, clearinghouse, PACS vendor, vendor access platform, and coding assistance vendor) and 1 Tier 2 example (the AI scribe vendor during its pilot). The remaining 7 Tier 1 reviews (including the LIS, dispensing cabinet, infusion pump, and patient monitoring manufacturers) are due by 2027-03-31 (POAM-017).

**Key findings:**
1. **EHR vendor:** unqualified Type 2. Its stated RTO of 12 hours **does not meet the BIA** (2 hours for clinical processes); its 15-minute RPO does. Three of the complementary user entity controls the hospital must operate are open gaps: access reviews (POAM-001), audit review (POAM-007), and review of vendor feature activations (POAM-024, the sepsis model). **The vendor's controls protect the hospital and the practices only once those gaps close.** The BAA must also be amended to cover practice PHI.
2. **MSSP:** unqualified Type 2 (Security only), with an exception for missed 30-minute escalations in 2 of 40 samples; P07 measured 22 minutes in its own test. The SIEM platform is carved out, and its own SOC 2 must be obtained. Log source coverage is the hospital's CUEC and is incomplete.
3. **Clearinghouse:** qualified opinion on Availability because its disaster recovery test was not completed. Its 72-hour RTO meets the claims MTD only at the limit, which confirms P01 R-020 and supports the secondary connection.
4. **PACS vendor:** has no SOC 2 report, holds privileged access, and held domain administrator service accounts. A SOC 2 Type 2 or HITRUST certification is required at the 2027 renewal.
5. **AI scribe vendor:** its BAA permits de-identified data use and must be amended before the pilot expands (P10).
