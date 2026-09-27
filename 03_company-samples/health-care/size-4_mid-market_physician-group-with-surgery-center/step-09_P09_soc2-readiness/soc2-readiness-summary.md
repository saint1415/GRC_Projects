# SOC 2 Readiness Summary: Cris Santos Company | Health Care | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed multi-specialty physician group with an ASC and an imaging center) |
| Tier / Vertical | Mid-Market / Health Care and Social Assistance |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| Target report | SOC 2 **Type 2**, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30 |
| Part A | Company readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-09-15 by the vCISO and the Security Manager, using P02, P05, and P07 evidence |

## 1. Why SOC 2 for this organization
A physician group is usually **not** a SOC 2 service organization, because it delivers care to patients rather than services to other businesses. That changes with the joint venture:
- A regional hospital system and the company are forming a joint venture for a second ASC.
- The company's **central business office** will provide revenue cycle services to the joint venture (eligibility, claims, prior authorization, posting).
- The **Enterprise Clinical Platform (ECP)** will host joint venture patient records and images.
- The hospital partner's audit committee requires a SOC 2 Type 2 report from any affiliate that provides services affecting joint venture patient data or revenue. It asked for Security, Availability, and Confidentiality.

For those services, the company is a service organization, and a SOC 2 Type 2 report is the right assurance tool.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. P07 found gaps in access reviews, recovery testing, vulnerability management, and vendor oversight. Starting the observation period before those are fixed would produce exceptions or a qualified opinion. The plan is to remediate through 2027 Q1, then run a 6-month observation period from 2027-04-01.

**Alternatives considered:**
- **Type 1 first (point in time):** offered to the partner as an interim report for 2027-03-31. The partner agreed to accept this plan with quarterly status updates.
- **HITRUST certification:** common in health care, but the partner specifically asked for SOC 2.
- **Security questionnaire only:** not acceptable to the partner's audit committee.

**Service auditor independence.** The SOC 2 examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so that the internal audit work in P07 does not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | Revenue cycle services (CBO) and clinical platform services (ECP) provided to the joint venture |
| Infrastructure | ECP components SYS-01 to SYS-08 (P02), with emphasis on the landing zone (P04), the CBO network at Clinic 1, and the SD-WAN |
| Software | EHR/PM (vendor SaaS), identity provider, PACS/RIS, interface engine, data warehouse, clearinghouse connection |
| People | CBO staff (about 120), IT and security team, MSSP, vCISO |
| Data | Joint venture patients' PHI, claims, remittances |
| Procedures | POL-01 to POL-05, the standards index, and the P08 runbooks |
| Subservice organizations (carve-out) | EHR vendor, identity provider, cloud provider, MSSP, clearinghouse. Their controls are covered by their own SOC 2 reports and the complementary subservice organization controls listed in the company's system description |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 10 | 19 | 4 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **11** | **22** | **5** | **23** |

**Ready (11):**
- governance and risk: CC1.1, CC1.3, CC1.5, CC3.1, CC3.2;
- monitoring: CC4.1, CC4.2;
- control design: CC5.1;
- access and transmission: CC6.2, CC6.7;
- capacity: A1.1.

**Not ready (5):**
- CC6.3: access reviews and the transfer process;
- CC7.1: vulnerability management;
- CC7.5 and A1.3: recovery is not documented or tested;
- CC9.2: vendor management, with 30 PHI vendors without BAAs.

Each maps to a P07 POA&M item. The Partially ready criteria mostly depend on standards being issued (P06) and on monitoring coverage (SIEM onboarding).

**Mapping to other work.** Evidence is reused from P02 (control statements), P05 (availability commitments), P06 (policies), P07 (test results), and P08 (incident procedures). The `related_sp800_53` column links each criterion to the P02 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.1, CC2.3, CC3.4, CC6.3 (transfer workflow), CC6.8, CC7.1, CC7.3, CC9.2 (BAAs), C1.1 | Reconciled device inventory; joint venture security schedule; AI review records; transfer tickets; console allowlisting records; monthly scan reports; decision log; signed BAAs |
| 2027 Q1 | CC1.2, CC1.4, CC2.2, CC3.3, CC5.2, CC5.3, CC6.1, CC6.3 (quarterly reviews), CC6.6, CC7.2, CC7.4, CC6.5, CC7.5, CC8.1, CC9.1, A1.2, A1.3, C1.2 | CFO fraud review; lease sanitization certificates; quarterly review sign-offs; privileged access management logs; SIEM source list; tabletop reports; restore test records; change tickets with second reviewer; standards |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the partner | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, restore tests, vendor reviews) |
| 2027 Q2 | CC6.4 (badge readers at Clinics 4-8) | Badge system reports |

**Status reporting.** The vCISO reports readiness monthly to the COO and quarterly to the audit committee and the joint venture partner.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 16 Common/Inherited and 31 Hybrid). The program in `vendor-soc2-review.csv` makes that reliance evidence-based, and it is the core of the vendor risk standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | PHI at scale (more than 10,000 patients), privileged access to company systems, or support for a High-criticality BIA process | SOC 2 Type 2 (or equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, CUECs mapped to company controls, availability versus the BIA, and incident terms | Annually |
| **Tier 2** | Limited PHI, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No PHI and no system access | Contract terms only | At contract renewal |

Of about 140 PHI vendors, 12 are Tier 1 and about 60 are Tier 2 under this approach. The CSV holds the first 7 Tier 1 reviews (including the EHR vendor and the MSSP) and 1 Tier 2 example. The remaining 5 Tier 1 reviews are due by 2027-03-31 (POAM-018).

**Key findings:**
1. **EHR vendor:** unqualified Type 2. Its stated RTO of 12 hours and RPO of 1 hour **do not meet the BIA** (RTO 2-4 hours; ASC RPO 15 minutes). Two of the complementary user entity controls (CUECs) the company must operate are open gaps: access reviews (POAM-001) and audit log review (POAM-006). **The vendor's controls only protect the company once those gaps close.**
2. **MSSP:** unqualified Type 2 (Security only), with an exception for missed 30-minute escalations in 2 of 40 samples. The SIEM platform is carved out, and the platform's own SOC 2 must be obtained. Log source coverage is the company's CUEC and is incomplete.
3. **Clearinghouse:** its disaster recovery test was not completed in the report period, which confirms P01 R-012 as High and supports the secondary clearinghouse decision.
4. **PACS vendor:** has no SOC 2 report. One is required at renewal, and the vendor service account finding (R-050) shows why.
5. **AI scribe vendor:** its BAA permits de-identified data use and must be amended before expansion (P10).
