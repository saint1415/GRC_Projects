# Business Impact Analysis: Cris Santos Company | Public Administration | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed GovTech systems integrator serving state and local agencies) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** GRC Manager with the Director of Cloud Operations, the Director of Managed Services, the Director of Customer Support, and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-17 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: ACMC hosted services, managed services, delivery, engineering, security, and corporate functions. It rates 18 business processes and quantifies what an outage costs in money, operations, and regulatory exposure, for the company and for the agencies that depend on it.

The results feed:
- the contingency plan the Moderate baseline requires (CP-2, with the RA-9 criticality analysis), due 2026-12-31;
- the availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability criteria in the SOC 2 readiness assessment (P09).

Most of the downtime harm falls on **other organizations**: sheriff's officers, benefits caseworkers, tax collectors, and motor vehicle clerks who cannot reach their cases. The contracts turn that harm into service credits, termination rights, and, for regulated data, reporting duties that start before any system is back.

## 2. System and business description
The company runs three business lines (`../00_company-facts.md` sections 1 and 3):
- **ACMC hosted services:** the Agency Case Management Cloud, a multi-tenant service in an 8-account cloud landing zone, for 43 live agencies with about 3.1 million individuals' records. Regulated tenants: AG-01 (FTI, in a separate enclave account), AG-02 and AG-39 (CJI), AG-03 (SNAP, TANF, and Medicaid applicant data), and AG-04 (motor vehicle records).
- **Managed services:** 55 engineers administer about 410 servers that 9 agencies host on their own premises, through the remote management platform (SYS-10). This includes AG-02's records management and jail management systems, which hold CJI.
- **Delivery:** about 25 implementation and data migration projects at any time.

Contracts set a recovery time objective (RTO) of **8 hours** and a recovery point objective (RPO) of **1 hour** for the regulated tenants, 24 hours and 4 hours for municipal tenants, and a 4-hour response for severity 1 managed services issues.

## 3. Impact categories and values
Dollar values are scaled to about $100 million in annual receipts over about 250 business days: about $220,000 per business day for ACMC services, $120,000 for delivery, and $60,000 for managed services. Service credits are capped at 10% of the monthly fee.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per event) | More than $100,000 (service credits, lost billable work, response costs) or a credible threat to a contract worth more than $5 million a year | $25,000 to $100,000 | Less than $25,000 |
| Operations | An agency cannot run a core program (supervision, benefits intake, tax collection, motor vehicle casework), or 9 managed agencies lose support | One agency function slowed or on paper | Internal work slowed |
| Regulatory | A CJIS, IRS, or program timeliness requirement is missed by an agency, or the company breaches a Security Addendum, Exhibit 7, or DPPA term | A contract notice or recovery term is missed | Internal policy deviation |
| Safety | Plausible harm to a person (an officer without a supervisee's warrant status, an inmate record unavailable, or a household without food benefits past the expedited deadline) | Delayed but safe service | None |
| Reputation | Agency or media statements; loss of a customer; GovRAMP or SOC 2 status at risk | Complaints from agency program managers | Internal only |

**How loss at MTD was estimated.** Estimated loss is service credits, plus revenue that is not recovered, plus extra labor, over the maximum tolerable downtime (MTD). Process owners supplied the assumptions: credits at the 10% cap for the affected tenants, about 60% of billable delivery work stopping when company environments are down (half of it never recovered), and overtime for support and agency data replay. Contract termination risk is described separately because it is a multi-year loss, not a per-event one.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-18 Security monitoring and incident response | Security | High | 4 | 2 | 1 | $10,000 |
| 2 | BP-08 Customer support and agency incident communications | ACMC hosted services | High | 4 | 2 | 24 | $10,000 |
| 3 | BP-09 Remote administration of agency-hosted systems | Managed services | High | 8 | 4 | 24 | $35,000 |
| 4 | BP-01 Supervision and jail program case management (CJI) | ACMC hosted services | High | 12 | 8 | 1 | $55,000 |
| 5 | BP-02 Benefits application intake and verification (AG-03) | ACMC hosted services | High | 24 | 8 | 1 | $112,000 |
| 6 | BP-04 Motor vehicle title and registration casework (AG-04) | ACMC hosted services | High | 24 | 8 | 1 | $24,000 |
| 7 | BP-03 Tax compliance casework (AG-01, FTI enclave) | ACMC hosted services | High | 48 | 8 | 1 | $74,000 |
| 8 | BP-06 Agency data interfaces | ACMC hosted services | High | 24 | 8 | 1 | $30,000 |
| 9 | BP-05 Municipal constituent services and permitting | ACMC hosted services | Moderate | 72 | 24 | 4 | $80,000 |
| 10 | BP-13 Software release and emergency patching | Engineering | Moderate | 72 | 24 | 24 | $25,000 |
| 11 | BP-10 Monitoring and patching of agency-hosted systems | Managed services | Moderate | 72 | 24 | 24 | $40,000 |
| 12 | BP-11 Implementation and data migration projects | Delivery | Moderate | 72 | 48 | 24 | $110,000 |
| 13 | BP-17 Contract management, proposals, and compliance reporting | Corporate | Moderate | 72 | 48 | 24 | $15,000 |
| 14 | BP-15 Payroll, HR, and personnel security screening | Corporate | Low | 120 | 72 | 24 | $15,000 |
| 15 | BP-14 Analytics and agency reporting dashboards | Engineering | Low | 120 | 72 | 24 | $10,000 |
| 16 | BP-16 Billing, collections, and finance | Corporate | Low | 120 | 72 | 24 | $20,000 |
| 17 | BP-07 AI eligibility assistant (AI-001) | ACMC hosted services | Low | 168 | 72 | 24 | $15,000 |
| 18 | BP-12 Agency user training | Delivery | Low | 168 | 120 | 24 | $5,000 |

**Summary:** 8 High, 5 Moderate, and 5 Low processes (18 in total). The sum of estimated losses at each process's MTD is $685,000.

**Enterprise-wide scenario.** If the whole ACMC were down for 72 hours (for example, ransomware), service credits would reach the 10% cap for every tenant, about $458,000. Lost delivery work would add about $180,000, and managed services credits about $125,000, for about $763,000 in all. The larger exposure is contractual: AG-01 and AG-03 together are worth about $23.5 million a year, and both contracts allow termination for a security breach. Incident response and notification costs come on top (see P01 R-001 to R-003).

**What drives the values:**
- **Agency clocks drive BP-18 and BP-08 to the top.** A suspected CJI incident must be reported within 1 hour (CJISSECPOL v6.1 IR-6), AG-01 must reach TIGTA and the IRS Office of Safeguards within 24 hours (Pub. 1075 section 1.8), and Florida agencies must report ransomware within 12 hours (Fla. Stat. 282.318 and 282.3185). The company has to detect the incident and reach the agencies inside those windows, even with no system back.
- **The 4-hour managed services response term drives BP-09.** The agency systems keep running without the company, but AG-02's jail management system supports about 2,400 inmates, and a failure the company cannot reach is a safety issue.
- **Contract recovery terms drive BP-01 to BP-04 and BP-06** (RTO 8 hours). BP-01 has the shortest MTD among platform processes because each sheriff can run only one shift on printed rosters.
- **SNAP timeliness drives BP-02.** Expedited households must have benefits by the seventh calendar day after filing (7 CFR 273.2(i)(3)); others within 30 days (273.2(g)(1)). One day down is survivable; several days push expedited cases past the deadline.
- **Cash and contract value**, not time, drive BP-11 and BP-17.

## 5. Key findings
1. **The 8-hour contract RTO is not proven for the largest tenants.** The 2025-11 restore test of the AG-03 tenant took **14 hours**. Region B failover has never been tested, and document object storage is versioned but not in the write-once vault (gap 5). Action: contingency plan update, quarterly timed restores, and a region B failover exercise (P01 R-006, R-014; P07 CP-4, CP-10).
2. **One platform carries every regulated tenant.** BP-01 to BP-04 share the regulated-tier cluster, the integration hub, and the production account. The FTI enclave is separate, which limits the blast radius for AG-01, but its recovery runs on the same team and runbooks.
3. **The managed services platform is a single point of failure and of compromise.** SYS-10 is the only way engineers reach 410 agency servers, and it holds standing domain administrator credentials for all of them (gap 1). If it is down, BP-09 and BP-10 stop. If it is compromised, an attacker reaches every managed agency at once (P01 R-001, R-013).
4. **Detection and notice capability is the first recovery priority.** If the identity provider or SIEM is lost in an incident, the company cannot meet the 1-hour CJI clock. The printed incident binder and out-of-band contact tree are the workaround (P08).
5. **The AI assistant is not a recovery priority.** BP-07 is Low: caseworkers in the other 3 regions already work without it. Its risks are decision risks, covered in P10.

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-04 Workforce identity provider and privileged access management | Single sign-on, MFA, just-in-time cloud elevation, break-glass accounts | All |
| SYS-06 Cloud landing zone | Management, security and log archive, shared services, production, FTI enclave, staging, development, and backup accounts | BP-01 to BP-07, BP-14, BP-18 |
| SYS-01 ACMC application tier | Containers, message queue, document storage | BP-01 to BP-05, BP-07 |
| SYS-02 ACMC data tier | Regulated-tier cluster, shared municipal cluster, FTI enclave instance, region B replicas | BP-01 to BP-05 |
| SYS-03 Integration hub | AG-01 file transfer, AG-02 and AG-39 message-switch connectors, AG-03 API, AG-04 motor vehicle feed | BP-01 to BP-04, BP-06 |
| SYS-14 Backups | Write-once vault in region B, 35 days; point-in-time recovery in production | Recovery of BP-01 to BP-05 |
| SYS-10 Remote management platform | Sessions into 9 agency networks through jump servers | BP-09, BP-10 |
| SYS-12 Security monitoring | SIEM with the MDR provider; log archive account | BP-18; recovery validation |
| SYS-13 Ticketing and status page | Support and agency notices | BP-08 |
| SYS-07 Repositories and pipeline | Builds and deploys fixes | BP-13 |
| SYS-08 Analytics service | Agency reports | BP-14 |
| SYS-09 AI eligibility assistant | Managed model service | BP-07 |
| Third parties | Cloud provider, identity provider vendor, remote management platform vendor, MDR provider, ticketing vendor, repository vendor, payroll provider | As listed in `bia.csv` |
| People and facilities | 40 cloud administrators (6 in the FTI enclave group), 55 managed services engineers, 45 support staff, the security team, the Director of Contracts and Compliance; headquarters and the delivery center | All |

## 7. Agency clocks and contract terms linked to recovery
The company is a contractor, so its recovery objectives come from contracts and from the agencies' own legal duties, not from a regulation that names the company. The table links each driver to the processes it sets.

| Driver | What it requires | Processes it sets | Status today |
|---|---|---|---|
| Contract recovery terms (all ACMC contracts) | RTO 8 hours and RPO 1 hour (regulated tenants); 24 and 4 hours (municipal); 99.9% monthly availability | BP-01 to BP-06 | Not proven: 14-hour restore in 2025-11 (finding 1) |
| Managed services contracts | Response within 4 hours for severity 1 | BP-09 | Met in operation; no plan for loss of SYS-10 |
| CJISSECPOL v6.1 IR-6 (through the CJIS Security Addendum) | Suspected incidents reported within 1 hour of discovery | BP-18, BP-08 | Rule in POL-03 (2026); clocks for AG-39 under State B procedures not yet mapped |
| Pub. 1075 section 1.8 (through Exhibit 7) | AG-01 reports to TIGTA and the IRS Office of Safeguards within 24 hours | BP-18, BP-08 | Contact path tested in the 2025 tabletop |
| Fla. Stat. 282.318 and 282.3185 (agency duties) | Florida state agencies and local governments report ransomware within 12 hours | BP-08 | Company target: tell each agency within 1 hour |
| CJISSECPOL v6.1 SI-2 and RA-5 | Critical updates within 15 days on CJI systems | BP-10, BP-13 | Met for the ACMC; not tracked for AG-02's on-premises systems |
| SNAP timeliness (7 CFR 273.2) | Benefits by day 7 (expedited) and day 30 | BP-02 | Agency workaround exists for 1 day |

## 8. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Out-of-band communications: printed contact list, phones, status page | 1 h | Incident binder at both offices and with every on-call lead |
| 2 | SYS-04 identity provider and break-glass accounts; SYS-12 monitoring | 1 h | Two sealed break-glass accounts per account tier; MDR runs from its own platform |
| 3 | SYS-10 remote management platform (clean instance) or on-site support for AG-02 | 4 h | Engineers on site at AG-02; agency IT staff guided by phone |
| 4 | Clean landing zone accounts and network rules from infrastructure code | 3 h | Rebuild in region B |
| 5 | Regulated-tier cluster and FTI enclave database from the last clean point | 6 h | Write-once vault copies in region B |
| 6 | Application tier and agency sign-in: AG-02 and AG-39, then AG-03, then AG-04, then AG-01 | 8 h (contract RTO) | Agency paper and native-system workarounds (section 4) |
| 7 | SYS-03 integration hub, replaying agency files and messages | 8 h | Agencies resend files; manual lookups |
| 8 | Shared municipal cluster and tenants | 24 h | Paper intake |
| 9 | SYS-07 pipeline, then monitoring and patching for managed agencies | 24 h | Hold releases; agency IT staff patch critical items |
| 10 | Staging and development accounts for delivery projects | 48 h | Consultants work on agency premises |
| 11 | SYS-08 analytics, payroll, billing | 72 h | Repeat prior payroll; manual invoices |
| 12 | SYS-09 AI eligibility assistant | After all others | Manual review (normal process) |
