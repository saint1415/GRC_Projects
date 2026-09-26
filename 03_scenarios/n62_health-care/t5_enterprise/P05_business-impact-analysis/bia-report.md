# Business Impact Analysis: Cris Santos Company | Health Care | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded multi-specialty medical group with ASCs, imaging centers, and a CLIA-certified central lab) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the group depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and acquired practices. It feeds:
- the HIPAA contingency plan, including the applications and data criticality analysis (45 CFR 164.308(a)(7)(ii)(E));
- the ASC emergency preparedness programs (42 CFR 416.54(a)(3) continuity of operations);
- the availability rating and recovery objectives in the LIS System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the ransomware runbook (P08);
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 9 are High criticality, 7 Moderate, and 1 Low. 7 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies, 11 of them single points of failure and 6 never tested.

## 2. System and business description
Cris Santos Company runs 159 sites in Florida, Georgia, Alabama, and South Carolina: 140 clinics, 6 ambulatory surgery centers, 12 imaging centers, and 1 central CLIA-certified laboratory. It has 12,000 employees (about 1,800 providers), about 2.1 million active patients, and about $4.8 billion in annual revenue. The technology estate is described in `../scenario-facts.md` section 3: a vendor-hosted enterprise EHR (SYS-01), an identity platform (SYS-02), a multi-cloud estate across two public cloud providers plus two colocation data centers (SYS-03), an SD-WAN (SYS-04), about 20,000 endpoints and 9,000 networked medical devices (SYS-05), ERP and payroll (SYS-06), and about 900 vendors (SYS-07). Eight practices were acquired in 2025-2026; three are not yet integrated (AQ-06 to AQ-08).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the group's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | A tier-1 service stops enterprise-wide, or more than 20 sites cannot see patients | One service line, one state, or up to 20 sites stop | Staff slowed but working |
| Regulatory | Reportable breach of 500 or more; CLIA or CMS condition-level finding; missed SEC filing | Missed contractual or documentation deadline; breach under 500 | Internal policy deviation |
| Safety | Plausible patient harm (missed critical value, medication, or surgical history) | Delayed but safe care | None |
| Reputation | National media, analyst or ratings action, or loss of client contracts | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-01 Ambulatory clinical care and documentation | High | 12 h | 4 h | 15 min | $8.50M |
| BP-02 Scheduling, registration, and eligibility | High | 12 h | 4 h | 15 min | $2.10M |
| BP-03 E-prescribing (including controlled substances) | High | 8 h | 4 h | 15 min | $0.40M |
| BP-04 Clinical laboratory testing and result reporting | High | 8 h | 4 h | 15 min | $1.50M |
| BP-05 Lab reference testing for external clients (SL-2) | High | 12 h | 4 h | 15 min | $0.35M |
| BP-06 Ambulatory surgery (6 ASCs) | High | 8 h | 4 h | 15 min | $1.90M |
| BP-07 Diagnostic imaging (12 imaging centers) | High | 12 h | 6 h | 1 h | $1.60M |
| BP-11 Telehealth and contact center telephony | Moderate | 12 h | 4 h | 24 h | $0.90M |
| BP-17 Clinical care at AQ-07 and AQ-08 (legacy EHRs) | High | 12 h | 8 h | 15 min | $0.45M |
| BP-10 Patient-app platform (SL-1 and own patients) | Moderate | 24 h | 8 h | 1 h | $0.50M |
| BP-12 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-14 Supply chain and medication inventory | Moderate | 48 h | 24 h | 24 h | $0.30M |
| BP-13 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-08 Claims submission and remittance | High | 120 h | 72 h | 24 h | $9.20M |
| BP-09 Patient billing, payment posting, and collections | Moderate | 168 h | 72 h | 24 h | $0.60M |
| BP-16 Health information exchange, referrals, and records release | Moderate | 24 h | 12 h | 4 h | $0.10M |
| BP-15 Care management and population health | Low | 72 h | 48 h | 24 h | $0.08M |

**What drives the values:**
- **Patient safety** sets the shortest MTDs: clinical care, e-prescribing, laboratory result reporting (critical values under 42 CFR 493.1291(g)), and ASC surgery.
- **Cash, not time,** drives claims (BP-08). Payers accept late claims within filing limits, so the MTD is 5 days, but each day of outage defers about $9.2 million of collections through the primary clearinghouse.
- **Regulation** tightens financial close (BP-13) during the quarter-end window, when the MTD drops to 48 hours because of SEC filing deadlines.
- **Contracts** set the lab reference testing (BP-05) and patient-app (BP-10) objectives, because external clients rely on them (P09).

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Clearinghouse concentration (DEP-08).** One clearinghouse carries 70% of claims and most eligibility checks. The secondary clearinghouse has no contracted surge capacity, and the manual fallback (payer portals for the top 10 payers) has never been tested. The industry saw this failure mode in 2024, when an attack on a major clearinghouse disrupted claims processing nationwide. A 30-day outage would defer about $277 million of collections. This is P01 risk R-005 and POA&M item POAM-019.
2. **Acquired practices (DEP-21 to DEP-23).** AQ-07 and AQ-08 run their own EHRs with nightly backups, so their real RPO is 24 hours against a 15-minute target, and their vendor contracts state a 24-hour RTO against an 8-hour BIA RTO. Neither restore has been tested. Both also send lab orders into the LIS and claims to the secondary clearinghouse, so an outage or compromise there spreads to BP-04 and BP-08.
3. **Laboratory (DEP-03, DEP-12 to DEP-14).** The LIS met its RPO but recovered in 5.5 hours against its 4-hour RTO in the 2026-05-16 disaster recovery test. The courier and specimen tracking service has no SOC report and no tested fallback.
4. **Single EHR instance (DEP-01).** The vendor's contract RTO (4 hours) and RPO (15 minutes) meet the BIA, and the vendor's failover test was observed in April 2026. The read-only downtime service is the main workaround for BP-01 to BP-03.
5. **Industry-wide dependencies (DEP-11).** The national e-prescribing network is a single point of failure the group cannot remove; the workaround is procedural.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 Enterprise EHR/PM | Vendor-hosted system of record, portal back end, e-prescribing | BP-01 to BP-03, BP-06, BP-07, BP-08, BP-16 |
| SYS-02 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-03 Cloud provider A workloads | LIS, interface engines, outreach portal | BP-04, BP-05, BP-08, BP-16 |
| SYS-03 Cloud provider B workloads | Patient-app platform, data warehouse, AI services | BP-10, BP-13, BP-15 |
| SYS-03 Colocation DC-1 and DC-2 | PACS, network core, immutable backup copies | BP-07; recovery of all |
| SYS-04 SD-WAN | Site connectivity with cellular failover | All site-based processes |
| SYS-05 Endpoints and medical devices | Workstations, analyzers, modalities, ASC devices | BP-01, BP-04, BP-06, BP-07 |
| SYS-06 ERP and payroll | Finance, payroll, supply chain | BP-09, BP-12 to BP-14 |
| Immutable backups | Separate backup accounts with write-once retention; weekly copy to DC-2 | RPO for all Cloud A and B workloads |
| People | Providers, lab staff, revenue cycle, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-02 identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 2 | Network core, SD-WAN, DNS, and colocation connectivity | 2 h | Cellular failover at sites |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | MSSP tooling |
| 4 | SYS-01 EHR access and interface engines | 4 h | Vendor read-only downtime service; paper |
| 5 | LIS and instrument middleware | 4 h | Manual result entry with second-person verification |
| 6 | ASC clinical systems and device networks | 4 h | ASC downtime kits |
| 7 | E-prescribing connectivity and telephony | 4 h | Paper or phone prescriptions; backup carrier |
| 8 | PACS and RIS | 6 h | Read at modality consoles |
| 9 | Patient-app platform and outreach portal | 8 h | Contact center; fax to clients |
| 10 | AQ-07 and AQ-08 legacy EHRs | 8 h target (24 h per vendor contract) | Paper downtime |
| 11 | HIE and referral interfaces | 12 h | Fax |
| 12 | ERP and payroll | 48 h | Repeat prior payroll |
| 13 | Data warehouse and care management tools | 48 h | Last exported lists |
| 14 | Clearinghouse connectivity and claims pipeline | 72 h | Payer portals; secondary clearinghouse |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Clearinghouse concentration and untested manual fallback | P01 R-005; P03 G-024 and G-026; POAM-019 |
| LIS recovery 5.5 h against 4 h RTO | P01 R-031; P02 CP-10; POAM-011 |
| AQ-07 and AQ-08 RPO 24 h and RTO 24 h against BIA targets | P01 R-015; POAM-005 |
| Courier and specimen tracking vendor without SOC report | P01 R-037; POAM-015 |
| ASC emergency exercises without a cyber outage scenario | P03 (42 CFR 416.54(d)(2)); POAM-021 |
