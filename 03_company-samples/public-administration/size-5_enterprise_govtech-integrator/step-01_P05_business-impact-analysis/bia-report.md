# Business Impact Analysis: Cris Santos Company | Public Administration | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded GovTech systems integrator serving state and local agencies) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** the four segment presidents and the Chief Risk Officer, 2026-08-14 | **Reported to:** risk committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company and its agency customers depend on, how long each can be down, how much data each can lose, and what each depends on, including cloud providers, colocation sites, agency-owned systems, subcontractors, and the acquired AQ-1 platform. It feeds:
- the contingency plans required by every agency contract (SP 800-53 CP-2 at the Moderate baseline, with the CJIS and Pub. 1075 overlays);
- the availability rating and recovery objectives in the ACMC System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the ransomware runbook (P08);
- the Availability and Processing Integrity criteria for the two SOC 2 service lines (P09).

**A GovTech twist.** Most of the harm from an outage falls on the agencies and the people they serve: officers who cannot see release conditions, families waiting for food assistance, courts without dockets. The company's own costs (service credits, liquidated damages, idle staff) are real but smaller. This BIA rates both, and the impact ratings in `bia.csv` reflect harm to agencies and the public as well as to the company.

**Results in one line:** 18 processes were analyzed; 8 are High criticality, 8 Moderate, and 2 Low. 4 processes need recovery within 4 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 12 of them single points of failure and 2 never tested.

## 2. System and business description
Cris Santos Company serves about 145 state and local agencies in 16 states from its Florida headquarters and five delivery centers, with 12,000 employees and about $4.8 billion in annual revenue. The technology estate is described in `../00_company-facts.md` section 3: the multi-tenant Agency Case Management Cloud (SYS-01) and its integration hub (SYS-02) on Cloud provider A; four integrated eligibility system (IES) environments (SYS-03) on Cloud provider B; the enterprise identity platform (SYS-04); two colocation data centers with legacy managed hosting for 9 court and sheriff customers (SYS-09); a CUI enclave for the DoD subcontract (SYS-10); and the AQ-1 court e-filing platform acquired in December 2025 (SYS-15).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $1 million per day, or more than $10 million cumulative | $100,000 to $1 million per day | Less than $100,000 per day |
| Operations | A tier-1 service stops for many agencies or a whole state program; more than 20 agencies affected | One service line, one state, or up to 20 agencies | Staff slowed but working |
| Regulatory and contract | Missed CJIS, IRS, HIPAA, or state reporting clock; contract termination right triggered; missed SEC filing | Missed service-level or documentation deadline | Internal policy deviation |
| Public safety and welfare | Plausible harm to people: wrongful arrest or missed violation, families without food or medical assistance past federal deadlines | Delayed but safe service | None |
| Reputation | National media, analyst or ratings action, loss of an agency contract or a procurement debarment review | Regional media; agency complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-11 Agency support and incident communications | High | 4 h | 2 h | 1 h | $0.20M |
| BP-12 Security monitoring and incident response | High | 4 h | 1 h | 15 min | $0.10M |
| BP-01 ACMC justice and public safety casework | High | 8 h | 4 h | 15 min | $0.90M |
| BP-05 Integration hub interfaces | High | 8 h | 4 h | 15 min | $0.60M |
| BP-09 Legacy hosted court and sheriff records systems | High | 12 h | 8 h | 1 h (actual 24 h) | $0.80M |
| BP-02 ACMC revenue and tax compliance casework | High | 24 h | 8 h | 15 min | $1.10M |
| BP-06 IES eligibility processing | High | 24 h | 8 h | 15 min | $2.60M |
| BP-08 Eligibility contact centers and document processing | High | 24 h | 8 h | 4 h | $0.70M |
| BP-03 ACMC driver license hearings and suspensions | Moderate | 24 h | 8 h | 15 min | $0.20M |
| BP-10 AQ-1 court e-filing | Moderate | 24 h | 12 h | 1 h | $0.15M |
| BP-07 AG-04 Medicaid enrollment and premium processing | Moderate | 48 h | 24 h | 1 h | $0.30M |
| BP-13 Software delivery and emergency patching | Moderate | 72 h | 24 h | 1 h | $0.25M |
| BP-14 Federal programs delivery and CUI enclave | Moderate | 72 h | 24 h | 4 h | $0.80M |
| BP-15 Systems integration and implementation delivery | Moderate | 72 h | 24 h | 4 h | $1.20M |
| BP-16 Payroll and timekeeping | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-17 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-04 ACMC local government services | Low | 72 h | 24 h | 1 h | $0.40M |
| BP-18 Agency billing and collections | Low | 168 h | 72 h | 24 h | $0.50M |

**What drives the values:**
- **Public safety** sets the shortest operational MTDs: officers supervising pretrial defendants (BP-01), warrant and docket systems (BP-09), and the interfaces that carry criminal history checks (BP-05).
- **Federal program deadlines** drive eligibility. SNAP expedited households must get benefits by the 7th calendar day and normal applications must be processed within 30 days (7 CFR 273.2(g)(1), (i)(3)(i)), so a day-long IES outage (BP-06) creates a backlog that can push families past those dates. The contract RTO is 8 hours.
- **Reporting clocks** make agency communications (BP-11) a tier-1 process even though it earns little: a suspected CJI incident must be reported within 1 hour (CJISSECPOL v6.1 IR-6), and a revenue agency must report a possible FTI disclosure within 24 hours (Pub. 1075 sec. 1.8).
- **Contracts** set most RTOs (8 hours for ACMC and IES) and the penalties behind the dollar values.
- **Regulation** tightens financial close (BP-17) at quarter-end, when the MTD drops to 48 hours for SEC filings.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Integration hub edge in DC-1 (DEP-04).** All 31 site-to-site VPN tunnels to agency sites terminate on appliances in one colocation site with no alternate. The last test re-established only 12 of 31 tunnels. 7 appliances still use FIPS 140-2 modules on CJI paths (POAM-006), and 2 had default vendor passwords when Internal Audit tested them (POAM-007). This is P01 risks R-006 and R-016.
2. **Legacy hosting (DEP-07, DEP-09).** 6 of the 9 legacy customers are hosted only in DC-1. Backups are nightly and not immutable, so the real RPO is 24 hours against a 1-hour target, and only 2 systems were restore-tested in 2025. A ransomware attack that reaches the legacy backup system could leave court and sheriff records unrecoverable (P01 R-015, POAM-008).
3. **Eligibility recovery (DEP-02).** The AG-04 IES recovered in 14 hours against its 8-hour contract RTO in the 2026-04-25 test, because the database restore and the rules engine cache rebuild ran in sequence (P01 R-009, POAM-015).
4. **Single print and mail vendor (DEP-14).** One vendor prints and mails eligibility notices for 3 of the 4 IES states; only AG-03 has a contracted alternate, and the fallback was never tested. Notices are part of the federal timeliness chain (P01 R-035).
5. **AQ-1 (DEP-10).** The acquired e-filing platform has never had a DR test and runs on its own identity directory. It also has network peering into the integration hub, which is the most likely path for an attacker to move from AQ-1 into agency systems (P01 R-003, POAM-001, POAM-004).
6. **Help desk subcontractor (DEP-12).** The tier-1 help desk vendor's overnight tier, outside the United States, could view tickets from FTI tenants. Routing was changed on 2026-08-20 (P01 R-007, POAM-009).
7. **Agency-owned dependencies (DEP-05, DEP-06, DEP-22).** State message switches, revenue file endpoints, and agency identity providers sit outside company control. Contracts require agencies to tell the company of their own outages; the workaround is procedural.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-01 ACMC (Cloud provider A, two U.S. regions) | Multi-tenant case management; dedicated FTI database instances with customer-managed keys | BP-01 to BP-04 |
| SYS-02 Integration hub (cloud services plus DC-1 edge) | 640 interfaces and 31 VPN tunnels | BP-01, BP-02, BP-05, BP-09 |
| SYS-03 IES environments (Cloud provider B) | Four single-tenant eligibility systems | BP-06 to BP-08 |
| SYS-04 Identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-07 Security operations platform | SIEM, EDR, SOAR | BP-12 and recovery validation for all |
| SYS-09 DC-1 and DC-2 | Legacy hosting; offline backup vault | BP-09 |
| SYS-10 CUI enclave | DoD subcontract work | BP-14 |
| SYS-12 Ticketing and telephony | Agency support and notices | BP-08, BP-11 |
| SYS-15 AQ-1 platform | Court e-filing | BP-10 |
| Immutable backups | Separate backup accounts with write-once retention for ACMC and IES; copy in a second region | RPO for all cloud workloads |
| People | Platform operations, eligibility operations staff, SOC, data center operations, Director of Regulated Data Compliance | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Out-of-band communications, agency contact list, status pages (BP-11) | 1 h | Printed incident binder; company mobile phones |
| 2 | Identity platform and break-glass accounts | 1 h | Sealed break-glass accounts; secondary region |
| 3 | Security tooling (SIEM, EDR) for clean-room validation | 1 h | Second SOC site |
| 4 | Integration hub cloud services and the DC-1 VPN edge | 4 h | Agencies use message switch terminals |
| 5 | ACMC criminal justice tenants | 4 h | Printed supervision rosters |
| 6 | ACMC FTI tenants (with each agency's key coordination) | 8 h | Agencies' own tax systems |
| 7 | IES environments (all 4 states) | 8 h | Paper applications; agency benefit issuance |
| 8 | Eligibility contact centers and document processing | 8 h | Recorded messages; hold paper |
| 9 | Legacy court and sheriff systems (DC-1, then DC-2) | 8 h target (24 h RPO today) | Printed dockets; message switch warrant checks |
| 10 | ACMC motor vehicle tenant | 8 h | Agency driver record system |
| 11 | AQ-1 e-filing | 12 h | Paper filing |
| 12 | Software delivery platform; CUI enclave; corporate systems | 24 h | Break-glass deployment; agency-furnished systems |
| 13 | ACMC local government tenants | 24 h | Phone and paper intake |
| 14 | Payroll, ERP, billing | 48 to 72 h | Repeat prior payroll; manual invoices |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| AG-04 IES recovered in 14 h against an 8 h RTO | P01 R-009; P03 G-055 (CP-4); POAM-015 |
| Legacy backups not immutable; real RPO 24 h | P01 R-015; P03 G-059 (CP-9); POAM-008 |
| Integration hub edge is one site; 7 appliances on FIPS 140-2 modules | P01 R-006, R-016; P03 G-148 (SC-13), CJ-10; POAM-006 |
| 6 legacy customers hosted only in DC-1 | P01 R-034; P03 G-057 (CP-7) |
| Single print and mail vendor for 3 IES states, untested fallback | P01 R-035; P03 G-173 (SR-6) |
| AQ-1 never DR-tested and on its own identity directory | P01 R-003, R-036; POAM-001 |
| Help desk vendor overnight tier outside the United States | P01 R-007; P03 PB-06; POAM-009 |
