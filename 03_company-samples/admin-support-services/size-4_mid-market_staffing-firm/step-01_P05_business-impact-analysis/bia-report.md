# Business Impact Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed staffing and temporary help firm) | **Tier:** Mid-Market (600 internal staff; about 3,600 associates on assignment weekly) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Security Manager with the vCISO, the process owners named in `bia.csv`, and the IT Director | **Fieldwork:** 2026-07-13 to 2026-08-07 | **Approved:** Chief Operating Officer, 2026-09-22 (presented to the audit committee the same day)
**Sources:** process owner interviews 2026-07-13 to 2026-07-17 (EV-061), FY2025 revenue report by business unit (EV-054), operating volume report (EV-055), payroll calendar (EV-041), credit agreement and funding procedure (EV-057), MSP client agreements and program report (EV-046, EV-056), vendor SOC 2 reports and recovery commitments (EV-044), and backup and restore records (EV-022, EV-023). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits and loss assumptions are the owners' statements, reviewed and approved by the Chief Operating Officer.

## 1. Overview and purpose
This BIA covers every business unit: Light Industrial (including the 6 on-site programs), Office and Professional, Healthcare Staffing, Managed Workforce Solutions, and the HQ shared services (payroll and billing, the onboarding and compliance center, credentialing, the recruiting contact center, finance, and HR). It rates 15 business processes and quantifies what an outage costs in money, operations, regulatory exposure, safety, and reputation.

The results feed:
- the contingency plan due 2026-12-31 (CP-2; CSF 2.0 RC.RP), including the manual payroll procedure (POAM-011);
- the backup and recovery part of the electronic Form I-9 records security program (8 CFR 274a.2(g)(1)(ii));
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment for the Managed Workforce Solutions system (P09).

## 2. System and business description
The firm places about 3,600 associates a week with about 950 Florida clients from headquarters, 14 branches, and 6 on-site programs, and runs the contingent workforce programs of 2 MSP clients. Every business day it onboards about 55 new associates, and every Friday it pays about $1.45 million in wages. Work runs on the Associate Payroll and Applicant Tracking Platform (APATP) described in the SSP (P02): the SaaS ATS with the I-9 module, the SaaS payroll and billing platform, the identity provider, the timekeeping app and fingerprint clocks, the credentialing platform, the 4-account cloud landing zone (integration platform, data warehouse, document archive, backups), the SD-WAN networks, and about 970 endpoints. The components and suppliers are listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv).

## 3. Impact categories and values
Dollar values are scaled to $100.0 million in receipts (EV-054): about $385,000 billed per business day (branch units about $215,000, on-site programs about $70,000, Managed Workforce Solutions about $19,000) and about $57,500 per calendar day in Healthcare, where shifts run 7 days a week.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $100,000, or any loss of payroll funds above $25,000 | $25,000 to $100,000 | Less than $25,000 |
| Operations | Associates not paid on payday, or a business unit cannot fill or run its shifts | One branch, one on-site program, or one MSP client stops | Staff slowed but working |
| Regulatory | Missed I-9 or E-Verify deadlines across many hires; a clinician placed without verified credentials; a missed breach notice; inability to produce I-9s on inspection | A single late form or notice | Internal policy deviation |
| Safety | A clinician without verified credentials or health clearance at a patient's bedside, or associates sent to a closed or unsafe site | Delayed site safety information | None |
| Reputation | Loss of an MSP client or a top-20 client, or public wage complaints | Associate complaints or online reviews | Internal only |

**How loss at MTD was estimated.** Estimated loss is gross margin that is not recovered, plus extra labor, client credits, and refill costs, over the MTD. Process owners supplied the assumptions (EV-061): about 30% of next-day branch orders go unfilled in a 24-hour dispatch outage, about 5% of associates leave after a missed payday, and a delayed new start loses about $350 of gross margin per day. Cash that is delayed but not lost (BP-11) is shown separately.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-05 Healthcare shift scheduling and credential verification | Healthcare Staffing | High | 12 | 4 | 1 | $25,000 |
| 2 | BP-04 Branch order intake and dispatch | Light Industrial; Office and Professional | High | 24 | 8 | 4 | $45,000 |
| 3 | BP-06 On-site program operations | Light Industrial | High | 24 | 8 | 4 | $30,000 |
| 4 | BP-08 Associate communications and recruiting contact center | Shared services | Moderate | 24 | 8 | 24 | $10,000 |
| 5 | BP-01 Weekly associate payroll | Payroll and Billing | High | 48 | 24 | 4 | $125,000 |
| 6 | BP-07 Managed workforce (MSP and VMS) services | Managed Workforce Solutions | High | 48 | 24 | 4 | $20,000 |
| 7 | BP-12 Treasury and payroll funding | Finance | Moderate | 48 | 24 | 24 | $15,000 |
| 8 | BP-02 Time capture and client approval | All units | High | 72 | 24 | 4 | $40,000 |
| 9 | BP-03 Associate onboarding (I-9, E-Verify, screening) | Onboarding and compliance center | High | 72 | 24 | 4 | $60,000 |
| 10 | BP-09 Recruiting and candidate screening | All units | Moderate | 72 | 48 | 24 | $30,000 |
| 11 | BP-10 Compliance records and inspection response | Onboarding and compliance center | Moderate | 72 | 48 | 24 | $15,000 |
| 12 | BP-14 Workers' compensation and safety reporting | Safety and Risk | Low | 72 | 48 | 24 | $5,000 |
| 13 | BP-11 Client billing and collections | Payroll and Billing | Moderate | 120 | 72 | 24 | $20,000 (plus about $1.9 million cash delayed per week) |
| 14 | BP-13 Internal staff payroll and HR | HR and Finance | Low | 120 | 72 | 24 | $10,000 |
| 15 | BP-15 Direct hire placements | Managed Workforce Solutions | Low | 168 | 120 | 24 | $10,000 |

**Summary:** 7 High, 5 Moderate, and 3 Low processes (15 in total). The sum of estimated losses at each process's MTD is $460,000.

**Payday override.** Priorities are ordered by MTD. From the Wednesday payroll cutoff until Friday's pay is released, BP-01 (and BP-12, which funds it) moves to priority 1, because the 48-hour MTD is already running.

**Enterprise-wide scenario.** If the whole APATP were unavailable for 72 hours (for example, ransomware that also locks the identity provider), the firm would lose about $350,000 of branch, on-site, and Healthcare billings that are not recovered, pay about $180,000 in client credits, refill costs, and overtime, and miss a payday if the outage started on a Wednesday (BP-01 at its full $125,000 estimate). Incident response and breach notice costs come on top (P01 R-002 to R-004).

**What drives the values:**
- **Safety and law drive BP-05.** It has the shortest MTD (12 hours) because a clinician cannot start a shift until the credential file is verified (Fla. Stat. 400.980(5)), and hospitals fill missed shifts themselves within hours.
- **Payday drives BP-01.** A missed payday is the single most damaging event for a staffing firm: temporary workers move to competitors within days, and overtime must be paid on the regular payday (29 CFR 778.106).
- **Legal clocks drive BP-03 and BP-10.** Section 2 of Form I-9 and the E-Verify case are due within 3 business days, and an inspection notice gives at least 3 business days to produce forms.
- **Client contracts drive BP-04, BP-06, and BP-07.** Fill-rate credits, on-site program credits, and MSP availability commitments turn hours of downtime into money and, at worst, a lost client.

## 5. Key findings
1. **The ATS vendor's recovery objectives do not meet two processes.** The ATS vendor states RTO 12 hours and RPO 1 hour (EV-044). Dispatch (BP-04) and on-site programs (BP-06) need RTO 8 hours. The daily assignment export makes the 24-hour MTD achievable by phone, but dispatch slows sharply. Action: recovery terms at the 2027 ATS renewal and a twice-daily export (P01 R-023).
2. **The credentialing platform states no recovery objective.** BP-05 needs RTO 4 hours and RPO 1 hour, and the vendor has no SOC 2 report. The daily credential status export is the only fallback and was not in place for 2 of 5 sampled days (EV-071; P01 R-024; P09 vendor review).
3. **Payroll is the dominant clock, and the fallback does not exist yet.** The payroll vendor's RTO of 8 hours meets BP-01, but a ransomware event at the vendor could last days. There is no written or tested off-cycle manual payroll procedure (EV-036; P01 R-005; P08 `ir-runbook-payroll-outage.md`).
4. **Firm-managed recovery is unproven.** The data warehouse restore was tested in 2026-03 (EV-023), but the integration platform has never been restored, and the document archive (scanned Forms I-9 from 2012-2021) is replicated, not backed up (EV-022). The RTOs for BP-02, BP-03, and BP-10 depend on them (P01 R-012, R-026; P07 CP-4).
5. **Payroll funding has a single path.** The Thursday credit line draw depends on the bank portal and the borrowing base report from the payroll platform. A phone fallback exists but has never been exercised (EV-057; BP-12).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-02 Payroll, billing, and back-office platform (SaaS) | Pay calculation, funding, tax, pay cards, invoices | BP-01, BP-11, BP-12, BP-13 |
| SYS-01 ATS and front-office platform (SaaS) | Candidates, onboarding, I-9 module, associate portal, client portal, texting | BP-02 to BP-06, BP-08 to BP-10, BP-15 |
| SYS-03 Identity provider | SSO and MFA for every staff application except E-Verify and the VMS | All |
| SYS-10 Credentialing platform (SaaS) | Clinician credential files and the client compliance portal | BP-05, BP-10 |
| SYS-06 Timekeeping app and 12 fingerprint clocks | Punches, geofence, on-site attendance | BP-02, BP-06 |
| SYS-11 VMS (SaaS) | MSP requisitions, supplier timesheets, consolidated invoices | BP-02, BP-07 |
| SYS-04 Integration platform | New hires, rates, time, credentials, and VMS data into payroll | BP-01, BP-02, BP-07, BP-11 |
| SYS-04 Document archive, data warehouse, and backup account | Scanned I-9s 2012-2021; reporting; 30-day write-once backups | BP-10; reporting |
| SYS-07 Screening provider; SYS-08 E-Verify | Consumer reports, drug screens; eligibility cases | BP-03 |
| SYS-12 Contact center platform | Recruiting calls, IVR, recordings | BP-08 |
| SYS-13 Networks | SD-WAN at HQ, 14 branches, and 6 on-site offices; dual ISP at HQ only | All |
| SYS-14 Endpoints | 640 laptops, 230 smartphones, 42 kiosks | All |
| SYS-15 SIEM and EDR (MSSP) | Detection and recovery validation | Recovery validation |
| People and facilities | Payroll team (17), onboarding center (27), credentialing (12), contact center (42), recruiters and account managers, on-site staff, IT (12), security and GRC (3), MSSP | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-03 identity provider and break-glass accounts | 1 h | Two break-glass accounts per critical system, sealed and offline (tested quarterly) |
| 2 | SYS-13 HQ network and internet (payroll, credentialing, contact center) | 2 h | Dual ISP at HQ; cellular hotspots; payroll and credentialing teams can work remotely |
| 3 | SYS-14 clean laptops for payroll, credentialing, and dispatch staff | 4 h | 20 pre-imaged spare laptops at HQ and 2 per branch |
| 4 | SYS-10 credentialing platform access (vendor) | 4 h target (vendor states none) | Daily credential status export; state license lookups |
| 5 | SYS-01 ATS, associate portal, client portal, and texting (vendor) | 12 h (vendor) | Twice-daily assignment export; paper I-9 packets; paper timesheets |
| 6 | SYS-02 payroll platform (vendor) | 8 h (vendor) | Off-cycle manual payroll from the prior register (procedure due 2026-12-31) |
| 7 | SYS-12 contact center platform | 8 h | Smartphone calls and texts; carrier closure message |
| 8 | SYS-06 timekeeping app and fingerprint clocks | 24 h | Paper timesheets and sign-in sheets; clocks hold punches locally |
| 9 | SYS-04 integration platform | 24 h | Manual entry of new hires and time batches into payroll |
| 10 | SYS-11 VMS (vendor) | 24 h (vendor) | Email requisitions; spreadsheet timesheets |
| 11 | SYS-08 E-Verify and SYS-07 screening provider access | 24 h | Direct website use from any managed laptop; outage screenshots |
| 12 | SYS-15 SIEM feeds and EDR console | 8 h | MSSP works from its own platform; needed before reconnecting restored systems |
| 13 | SYS-04 document archive | 48 h | Restore from the backup account once archive backups exist (POAM-010) |
| 14 | SYS-04 data warehouse and BI | 72 h | Reports run directly in the ATS and payroll platform |
