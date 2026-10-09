# Business Impact Analysis: Cris Santos Company | Administrative and Support and Waste Management and Remediation Services | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded staffing and workforce solutions company) | **Tier:** Enterprise (12,000 internal employees; about 78,000 associates on assignment a week) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk and technology committee of the board, 2026-09-10
**Sources:** process owner interviews 2026-06-01 to 2026-07-10 (EV-070, EV-071), dependency and contract review (EV-072), site and entity register (EV-056), FY2025 revenue and payroll report (EV-054), operational volume report (EV-055), Treasury pay delivery records (EV-065), DR test and backup records (EV-023, EV-017, EV-024), ACQ-1 records (EV-057, EV-058), and the data platform rebuild observation (EV-073). The `source_evidence` column in `bia.csv` names the source of each process's values. Downtime limits are the owners' statements, reviewed and approved by the Chief Operating Officer and the Chief Risk Officer.

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the firm depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties, client systems, and the acquired firm ACQ-1. It feeds:
- the enterprise contingency program and the tier-1 disaster recovery plans;
- the availability rating and recovery objectives in the Associate Lifecycle and Payroll Platform (ALPP) System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the payroll and HR breach runbook (P08);
- the Availability and Processing Integrity criteria for the two SOC 2 service lines (P09);
- the E-Verify outage procedure (Florida worked example: Fla. Stat. 448.095(2)(c)) and the Form I-9 timing duty (8 CFR 274a.2(b)(1)(ii)) assessed in P03.

**Results in one line:** 17 processes were analyzed; 9 are High criticality, 7 Moderate, and 1 Low. 6 processes need recovery within 8 hours, and one (the SL-1 Workforce Management Platform) within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies: 15 are single points of failure, 2 more are partial single points of failure, and 4 have never been tested.

## 2. System and business description
Cris Santos Company is a staffing firm headquartered in Florida with about 380 branches and 140 on-site offices at client facilities in 38 states and the District of Columbia. It has 12,000 internal employees and is the W-2 employer of about 78,000 temporary associates on assignment in an average week (about 310,000 different associates in 2025). Revenue is about $4.8 billion a year. Four segments (Commercial, Professional including Government Solutions, Healthcare, and Workforce Solutions) share one technology platform, listed in the intake [asset inventory](../step-00_P00_intake/asset-inventory.csv) and [vendor register](../step-00_P00_intake/vendor-register.csv): the front-office ATS (SYS-01), the onboarding and Form I-9 platform (SYS-02), the customer-managed payroll and billing engine (SYS-03), time capture (SYS-04), the identity platform (SYS-05), a multi-cloud estate across two public cloud providers plus two colocation data centers (SYS-06), the Workforce Management Platform (SYS-07), the network and endpoints (SYS-08), screening and verification services (SYS-09), ERP and internal HCM (SYS-10), and about 1,400 vendors (SYS-11). ACQ-1, a travel nurse firm acquired in 2025, still runs its own systems until 2027-03-31.

**The weekly rhythm drives everything.** Associates are paid every Friday. Time must be approved by Monday noon, payroll runs Monday to Thursday, and ACH files must reach the banks by Thursday 14:00. An outage on a Tuesday is far worse than the same outage on a Saturday, so the payroll-related MTDs below are stated for the payroll window.

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day ($4.8 billion in FY2025 revenue, EV-054) and to the firm's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | A weekly payroll is missed or late for more than 5,000 associates; a tier-1 service stops enterprise-wide; or more than 50 sites cannot dispatch associates | One segment, one state, or up to 50 sites stop | Staff slowed but working |
| Regulatory | Reportable breach of 500 or more individuals; systemic late Forms I-9 or E-Verify cases; state wage payment violations at scale; missed SEC filing | Missed contractual or documentation deadline; breach under 500 | Internal policy deviation |
| Safety | Plausible harm to patients at client hospitals (unqualified clinician on shift) or to associates (unsafe site, loss of pay causing hardship at scale) | Delayed but safe placements; individual pay hardship | None |
| Reputation | National media, analyst or ratings action, or loss of managed-program clients | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
Listed in recovery priority order.

| Priority | Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|---|
| 1 | BP-01 Associate payroll and pay delivery | High | 24 h (payroll window) | 8 h | 15 min | $2.40M |
| 2 | BP-02 Time capture and approval | High | 48 h | 12 h | 1 h | $1.10M |
| 3 | BP-08 SL-1 Workforce Management Platform | High | 12 h | 4 h | 15 min | $0.60M |
| 4 | BP-04 Candidate sourcing, recruiting, and job order fulfillment | High | 24 h | 8 h | 1 h | $1.60M |
| 5 | BP-05 Associate onboarding, Form I-9, and E-Verify | High | 48 h | 24 h | 1 h | $0.90M |
| 6 | BP-07 Healthcare clinician credentialing and compliance files | High | 24 h | 12 h | 4 h | $0.45M |
| 7 | BP-09 SL-2 payrolling and employer-of-record services | High | 24 h (payroll window) | 8 h | 15 min | $0.40M |
| 8 | BP-16 ACQ-1 clinician payroll, ATS, and credentialing (legacy) | High | 24 h | 12 h | 4 h | $0.50M |
| 9 | BP-15 Branch and on-site office operations | Moderate | 24 h | 8 h | 24 h | $0.35M |
| 10 | BP-06 Background screening and drug testing | Moderate | 72 h | 24 h | 4 h | $0.30M |
| 11 | BP-10 Associate Service Center | Moderate | 24 h | 8 h | 24 h | $0.15M |
| 12 | BP-14 Government Solutions contract delivery | Moderate | 72 h | 24 h | 4 h | $0.20M |
| 13 | BP-12 Internal staff payroll and HR | Moderate | 72 h | 48 h | 24 h | $0.12M |
| 14 | BP-03 Client billing, invoicing, and collections | High | 120 h | 72 h | 24 h | $18.50M (cash deferred) |
| 15 | BP-11 Payroll tax filing, garnishments, and year-end forms | Moderate | 120 h | 72 h | 24 h | $0.10M |
| 16 | BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| 17 | BP-17 Analytics, reporting, and AI services | Low | 72 h | 48 h | 24 h | $0.06M |

**What drives the values:**
- **Pay on time** sets the shortest MTDs for payroll (BP-01, BP-09). A missed Friday payroll for 78,000 associates is the firm's worst plausible operational outcome: it creates hardship for associates, wage payment exposure in 38 states, and a reputational event within hours.
- **Patient safety at client hospitals** sets the clinician credentialing MTD (BP-07, BP-16): a clinician whose license has lapsed must not work a shift.
- **Legal clocks** set onboarding (BP-05): Section 2 of Form I-9 is due within 3 business days of hire, and E-Verify cases within 3 business days, so the MTD is 48 hours with a paper fallback.
- **Contracts** set the SL-1 platform (BP-08: 99.9% monthly availability) and SL-2 payrolling (BP-09) objectives, because clients run their programs on them (P09).
- **Cash, not time,** drives billing (BP-03). Clients pay on terms, so the MTD is 5 days, but each business day of outage defers about $18.5 million of invoices. This is why BP-03 is High criticality with a late recovery priority.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Payroll engine recovery (DEP-03).** The payroll engine met its 15-minute RPO in the 2026-05-16 DR test but took 9.5 hours to recover against its 8-hour RTO, because database replicas in the standby region were not pre-staged and bank and paycard file endpoints were re-pointed by hand (EV-023). This is P01 risk R-005 and POA&M item POAM-010.
2. **Pay delivery concentration (DEP-10, DEP-11).** Bank B has proven it can take all ACH volume (tested 2025-11-14, EV-065), so the banks are not a single point of failure. The paycard program manager is: about 9,400 associates a week are paid on cards, there is no tested fallback beyond courier checks, and its SOC report has not been reviewed since 2024 (R-015; POAM-009).
3. **ACQ-1 (DEP-21 to DEP-23).** ACQ-1's legacy ATS backs up nightly (actual RPO 24 hours against a 4-hour target), its outsourced payroll provider's contract states a 48-hour RTO against a 12-hour BIA RTO, and none of its restores has been tested (EV-058). Its directory is not federated (R-004; POAM-002, POAM-003).
4. **Client systems (DEP-16).** About 400 client VMS instances send time and receive invoices through shared service accounts and long-lived API keys (EV-026). A compromised key exposes worker data in both directions (R-007; POAM-008).
5. **Legacy on-premises components (DEP-07, DEP-08).** The time clock server in DC-1 runs an unsupported operating system, and the scanned I-9 archive in DC-2 has no access audit trail (EV-013, EV-036; R-011; POAM-011; POAM-007).
6. **Government-run and industry dependencies (DEP-14).** E-Verify is a single point of failure the firm cannot remove; the workaround is procedural (document the outage and create cases after recovery).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Front-office ATS and CRM | Vendor SaaS; career sites, recruiter workflow, AI ranking add-on, credentialing module | BP-04, BP-07, BP-14 |
| SYS-02 Onboarding and Form I-9 platform | Vendor SaaS; tax and bank forms, electronic I-9, screening orders | BP-05, BP-06, BP-09 |
| SYS-03 Payroll and billing engine | Customer-managed on Cloud provider A; pay, pay files, invoices, tax files | BP-01, BP-03, BP-09, BP-11, BP-13 |
| SYS-04 Time capture | Mobile app, client portal, VMS feeds, 140 on-site time clocks | BP-02 |
| SYS-05 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-06 Cloud provider A | Landing zone, integration platform, payroll engine, WMP | BP-01 to BP-05, BP-08, BP-09 |
| SYS-06 Cloud provider B | Enterprise data platform and AI services | BP-13, BP-17 |
| SYS-06 Colocation DC-1 and DC-2 | Network core, time clock server, I-9 archive, offline backup copies | BP-02, BP-05; recovery of all |
| SYS-07 Workforce Management Platform | The firm's own VMS for managed-program clients | BP-08 |
| SYS-08 Network, endpoints, kiosks | SD-WAN to about 520 sites with cellular failover | BP-15 and all site-based work |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to DC-2 | RPO for all Cloud A and B workloads |
| People | Payroll operations (3 centers), recruiters, onboarding specialists, credentialing specialists, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | Network core, SD-WAN, DNS, and colocation connectivity | 2 h | Cellular failover at sites |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 4 | Integration platform and SYS-07 Workforce Management Platform | 4 h | Status page; program offices work by email |
| 5 | SYS-03 payroll engine and bank and paycard file transfer | 8 h target (9.5 h demonstrated) | Prior-week advance procedure |
| 6 | SYS-01 ATS and SYS-04 time capture | 8 h (vendor) and 12 h | Hot lists; paper timesheets; time clock buffer |
| 7 | SYS-02 onboarding and Form I-9 platform; E-Verify access | 24 h | Paper Form I-9; documented E-Verify outage |
| 8 | ACQ-1 legacy ATS, credentialing system, and payroll provider | 12 h target (48 h per provider contract) | Paper credential checks; repeat prior pay |
| 9 | CCaaS for the Associate Service Center | 8 h | Branch phones; recorded message |
| 10 | Screening provider integrations | 24 h | Provider portals |
| 11 | ERP and internal HCM | 48 h | Repeat prior payroll; manual journal entries |
| 12 | Enterprise data platform and AI services | 48 h | Last published reports |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Payroll engine recovery 9.5 h against an 8 h RTO | P01 R-005; P02 CP-10; POAM-010 |
| ACQ-1 RPO 24 h and RTO 48 h against BIA targets; legacy directory | P01 R-004; POAM-002; POAM-003 |
| Paycard program manager without tested fallback or current SOC review | P01 R-015; POAM-009 |
| Client VMS integrations with shared accounts and long-lived keys | P01 R-007; POAM-008 |
| Time clock server on an unsupported operating system | P01 R-011; POAM-011 |
| Scanned I-9 archive without an access audit trail | P01 R-017; POAM-007 |
| Weekly payroll timing not reflected in the incident severity scale | P08 section 3 (payroll window escalation) |
