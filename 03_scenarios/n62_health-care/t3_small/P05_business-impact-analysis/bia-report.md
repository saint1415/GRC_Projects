# Business Impact Analysis: Cris Santos Company | Health Care and Social Assistance | Small

**Organization:** Cris Santos Company, LLC (multi-specialty physician practice) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Security Officer) with the Clinic Managers and Billing Manager | **Approved:** Practice Administrator, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the practice depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan required by the HIPAA Security Rule (45 CFR 164.308(a)(7)), including the Applications and Data Criticality Analysis (164.308(a)(7)(ii)(E));
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

## 2. System and business description
The practice runs two Florida clinics with 60 employees and about 240 visits per clinic day. Clinical and billing work runs on the Clinical and Revenue Cycle Platform (CRCP): a SaaS EHR/PM, an identity provider, a cloud tenant (imaging archive, interface engine, backups), clinic networks, endpoints, and medical devices. See `../scenario-facts.md` sections 3-4.

## 3. Impact categories and values
Dollar values are scaled to $9.6 million in annual revenue, about $38,400 per clinic day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $100,000 (about 3 days of revenue) | $25,000 to $100,000 | Less than $25,000 |
| Operations | Both clinics cannot see patients | One clinic or one service line stops | Staff slowed but working |
| Regulatory | Reportable breach or federal program issue | Missed documentation or timeliness requirement | Internal policy deviation |
| Safety | Plausible patient harm (missed allergy, medication, or critical result) | Delayed but safe care | None |
| Reputation | Regional media coverage or loss of referral partners | Patient complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Clinical documentation and care | High | 8 h | 4 h | 1 h |
| BP-02 Scheduling and registration | High | 8 h | 4 h | 1 h |
| BP-03 E-prescribing | High | 8 h | 4 h | 1 h |
| BP-04 Diagnostic imaging | Moderate | 24 h | 12 h | 4 h |
| BP-05 Lab orders and results | Moderate | 24 h | 12 h | 4 h |
| BP-06 Claims and revenue cycle | Moderate | 72 h | 48 h | 24 h |
| BP-07 Patient communications | Moderate | 24 h | 8 h | 24 h |
| BP-08 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- Patient safety drives BP-01 and BP-03: providers cannot safely prescribe without allergy and medication lists.
- Revenue drives BP-06 more than time does, because payers accept late claims within their filing limits.
- An MTD of 8 hours equals one clinic day. Beyond that, the practice would have to cancel and reschedule about 480 visits across both clinics.

**Key finding:** the EHR vendor's contracted recovery commitments must meet the 4-hour RTO and 1-hour RPO for BP-01 to BP-03. The vendor's SOC 2 report (reviewed in P09) should confirm its availability commitments. The practice-managed backups for the imaging archive and interface engine have **never been restore-tested**, so the 12-hour RTO for BP-04 and BP-05 is unproven (risk R-005 in P01).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-01 EHR/PM (SaaS) | System of record, portal, e-prescribing | BP-01, BP-02, BP-03, BP-05, BP-06, BP-07 |
| SYS-02 Identity provider | Single sign-on and MFA for all cloud systems | All |
| SYS-05 Clinic networks and internet | Firewalls, Wi-Fi, primary and backup ISP at Clinic A, single ISP at Clinic B | All |
| SYS-06 Endpoints | 70 workstations and laptops, 12 tablets | All |
| SYS-04 Imaging archive | X-ray image storage and viewing | BP-04 |
| SYS-04 Interface engine | HL7 interfaces to the lab and clearinghouse | BP-05, BP-06 |
| SYS-08 Clearinghouse | Eligibility and claims | BP-02, BP-06 |
| People | Providers, clinical staff, front desk, billing, IT Manager, MSP | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-02 Identity provider and break-glass accounts | 1 h | Two break-glass admin accounts stored offline (to be created; see P01 R-005) |
| 2 | SYS-05 Internet and clinic network | 2 h | Cellular hotspot kit at each clinic (to be purchased) |
| 3 | SYS-06 Clean endpoints for front desk and providers | 4 h | Pre-imaged spare laptops (4 per clinic) |
| 4 | SYS-01 EHR/PM access | 4 h | Vendor-hosted; paper downtime forms until restored |
| 5 | SYS-04 Interface engine | 12 h | Lab portal and fax |
| 6 | SYS-04 Imaging archive | 12 h | Modality local storage; outside imaging center |
| 7 | SYS-08 Clearinghouse connectivity | 48 h | Queue claims |
| 8 | Payroll SaaS | 72 h | Repeat prior payroll |
