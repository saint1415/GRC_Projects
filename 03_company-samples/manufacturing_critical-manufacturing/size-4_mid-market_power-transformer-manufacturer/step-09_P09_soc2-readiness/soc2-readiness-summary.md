# SOC 2 Readiness Summary: Cris Santos Company | Critical Manufacturing | Mid-Market

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Mid-Market / Critical Manufacturing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Categories in scope | Security (CC1-CC9), Availability (A1), Confidentiality (C1) |
| System in scope | The Fleet Monitoring Service (FMS) |
| Target report | SOC 2 **Type 2** on the FMS, observation period 2027-04-01 to 2027-09-30 (6 months), report expected by 2027-11-30, ahead of the two subscriber renewals on 2027-12-31 |
| Part A | FMS readiness assessment (`soc2-readiness.csv`) |
| Part B | Vendor SOC 2 review program (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-24 to 2026-09-04 by the vCISO, the Security Manager, and the Director of Digital Services, using P02, P04, P05, and P07 evidence; approved by the COO 2026-09-15 |

## 1. Why SOC 2 for this organization
A transformer manufacturer is usually **not** a SOC 2 service organization: it sells equipment, and no customer's controls depend on its systems. The Small sample of this company reached exactly that conclusion. At mid-market size one business line changes the answer:
- The **Fleet Monitoring Service** is a subscription service. Fourteen utilities push TMU data for about 1,150 power transformers into it, and company reliability engineers send condition advisories back through a customer portal.
- The subscribers rely on the FMS's security, availability, and confidentiality. Its agreements commit to 99.5% monthly availability and to keeping each utility's asset data confidential.
- The two largest subscribers have written a SOC 2 Type 2 requirement (Security, Availability, Confidentiality) into their renewals on 2027-12-31.

For the FMS, the company is a service organization, and a SOC 2 Type 2 report is the right assurance tool. The ERP and plants are not in scope: no customer relies on them as a service.

**Why Type 2, and why not now.** A Type 2 report tests whether controls operated effectively over a period. The FMS has no application log monitoring, no change control for releases and model updates, and no tested recovery (CC7.2, CC8.1, CC7.5, A1.3). Starting the observation period before those are fixed would produce exceptions. The plan is to remediate through 2027-Q1, then run a 6-month observation period from 2027-04-01.

**Alternatives considered:**
- **Type 1 first (point in time):** offered to the two subscribers for 2027-03-31; both accepted the plan with quarterly status letters.
- **A company-wide SOC 2:** rejected. The plants and ERP are not services to customers, and utility supplier questionnaires are answered from the P03 CSF profile instead.
- **ISA/IEC 62443 product or process certification:** relevant to the TMU configuration software, not to the FMS service. Revisit after STD-10 is in place.
- **Security questionnaire only:** not acceptable to the two subscribers.

**Service auditor independence.** The examination will be performed by an independent CPA firm that is **not** the co-sourced internal audit firm, so the internal audit work in P07 and the planned FMS pre-assessment do not create an independence question.

## 2. System description (scope)
| Element | In scope |
|---|---|
| Services | FMS data ingestion, condition analytics, urgent alert review, and advisories in the customer portal |
| Infrastructure | The FMS production account and the shared landing zone services it uses: management and security account (guardrails, federation), shared services account (log archive), backup account (P04) |
| Software | Ingestion interface, time-series database, analytics service including the AI-003 model, customer portal |
| People | 12 Digital Services staff (4 reliability engineers, 5 software and cloud engineers, 2 customer success, the Director), the Security Manager's team, the MSSP |
| Data | Subscribers' TMU data and transformer health records (Restricted); portal user contact details |
| Procedures | POL-01 to POL-05; STD-02, STD-07, STD-10 (in draft); P08 runbook 2 |
| Subservice organizations (carve-out) | Public cloud provider and identity provider (their controls are covered by their own SOC 2 reports and the complementary subservice organization controls to be listed in the system description) |

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 11 | 18 | 4 | 0 |
| Availability (A1, 3) | 1 | 1 | 1 | 0 |
| Confidentiality (C1, 2) | 0 | 2 | 0 | 0 |
| Processing Integrity (PI1, 5) | 0 | 0 | 0 | 5 |
| Privacy (P1-P8, 18) | 0 | 0 | 0 | 18 |
| **Total (61)** | **12** | **21** | **5** | **23** |

**Ready (12):**
- governance and risk: CC1.1, CC1.3, CC3.1, CC3.2, CC3.3, CC4.2, CC5.1;
- access and boundaries: CC6.2, CC6.4, CC6.6, CC6.7;
- capacity: A1.1.

**Not ready (5):**
- CC2.3: subscribers have no security contact and the notice procedure is untested;
- CC7.2: FMS application logs are not monitored;
- CC7.5 and A1.3: FMS recovery is not designed or tested;
- CC8.1: no change control for releases and AI-003 model updates.

Each maps to a POA&M item (POAM-018, POAM-019). Most Partially ready criteria depend on standards being issued (P06) and on the FMS operating procedures.

**Processing Integrity** was not requested for the first report. It is a candidate for 2028, because the AI-003 advisories are outputs that utilities act on (P10).

**Mapping to other work.** Evidence is reused from P02 (control statements), P04 (FMS account controls), P05 (BP-14 availability needs), P06 (policies), P07 (test results), and P08 (runbook 2). The `related_sp800_53` column links each criterion to SP 800-53 controls. AICPA publishes a TSC-to-SP 800-53 mapping (see SRC-TSC).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC1.5, CC2.3, CC5.2, CC6.5, CC7.2, CC9.1, C1.2 | Approved FMS control matrix; security contact and notice drill records; FMS administrators in the quarterly access review; deletion certificates; SIEM use cases for the FMS; FMS section of the contingency plan |
| 2027 Q1 | CC1.2, CC1.4, CC2.1, CC2.2, CC3.4, CC4.1, CC5.3, CC6.1, CC6.3, CC6.8, CC7.1, CC7.3, CC7.4, CC7.5, CC8.1, CC9.2, A1.2, A1.3, C1.1 | Quarterly audit committee reports with the FMS as a standing item; training records; SBOMs; operating procedures; change tickets with approvals for releases and model updates; internal audit pre-assessment; certificate revocation settings; portal user confirmations; blocking dependency scans; penetration test report; tabletop report; restore test record; continuous backup settings |
| 2027-03-31 | Type 1 (design) report as an interim deliverable to the two subscribers | Management's system description and assertion |
| 2027-04-01 to 2027-09-30 | Type 2 observation period | All recurring control evidence (quarterly reviews, monthly scans, change tickets, restore tests, notice drills) |

**Status reporting.** The Director of Digital Services reports readiness monthly to the COO; the vCISO reports it quarterly to the audit committee and in letters to the two subscribers.

## 5. Vendor SOC 2 review program (Part B)
The company relies on vendor controls for many inherited controls (P02: 10 Common/Inherited and 32 Hybrid; P04: 4 Provider and 19 Shared rows). The program in `vendor-soc2-review.csv` makes that reliance evidence-based and is the core of the vendor and supplier risk standard (STD-03).

**Tiering approach:**
| Tier | Criteria | Assurance required | Frequency |
|---|---|---|---|
| **Tier 1** | Privileged access to company systems, firmware or software that reaches utility substations, or support for a High-criticality BIA process | SOC 2 Type 2 (or equivalent independent assessment) plus bridge letter; review of opinion, scope, subservice organizations, exceptions, complementary user entity controls mapped to company controls, availability versus the BIA, and incident terms. Product suppliers: secure development and firmware integrity evidence | Annually |
| **Tier 2** | Company or personal data, no privileged access, supports Moderate or Low processes | Security questionnaire; SOC 2 if available | Every 2 years |
| **Tier 3** | No data and no system access | Contract terms only | At contract renewal |

Of about 190 suppliers with system access or data, 22 are Tier 1 under this approach. The CSV holds the first 7 Tier 1 reviews and 1 Tier 2 example. The remaining 15 Tier 1 reviews (mostly OEMs with plant remote access) are due by 2027-03-31 (POAM-012).

**Key findings:**
1. **Cloud provider:** unqualified Type 2 with one remediated exception. The provider's controls only protect the company once its own complementary controls work, and two do not yet: FMS log monitoring (POAM-019) and a full restore test (POAM-005).
2. **MSSP:** unqualified Type 2 (Security only), with an exception for missed 30-minute escalations in 2 of 40 samples. The SIEM platform is carved out, so the platform's own report must be obtained (P01 R-015, High). Log source coverage is the company's complementary control and is incomplete.
3. **SD-WAN provider:** qualified for Availability because failover testing lapsed for 3 months. This supports the second wired carrier at Plant 2 (P01 R-021). The report was obtained after the P07 fieldwork.
4. **EDI provider and ERP software vendor:** no SOC 2 reports. The ERP vendor's ISO/IEC 27001 certificate is accepted for now, with recorded support sessions reviewed monthly.
5. **TMU electronics supplier:** SOC 2 does not fit a product supplier. The review uses a product security questionnaire and the company's own hash checks; the next agreement must add a 10-business-day advisory term and an SBOM requirement.
