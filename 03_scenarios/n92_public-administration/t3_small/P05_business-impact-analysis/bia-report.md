# Business Impact Analysis: Cris Santos Company | Public Administration | Small

**Organization:** Cris Santos Company, LLC (GovTech systems integrator) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Cloud Operations Lead with the Director of Customer Delivery, Customer Support Manager, and Director of Engineering | **Approved:** Chief Operating Officer, 2026-08-31

## 1. Overview and purpose
This BIA identifies which processes the company and its agency customers depend on, how long each can be down, and how much data each can lose. It supports:
- the contingency plan the Moderate baseline requires (CP-2, with RA-9 criticality analysis), due 2026-12-31;
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

Unlike a typical small business, most of the downtime cost here falls on **other organizations**: sheriff's officers, benefits caseworkers, and tax collectors who cannot reach their cases. The contracts turn that into service credits and termination rights for the company.

## 2. System and business description
The Agency Case Management Platform (ACMP) is a multi-tenant case management service hosted in the company's cloud tenant for 11 Florida agencies (`../scenario-facts.md` sections 1 and 3). Three customers hold regulated data: AC-01 (FTI), AC-02 (CJI), and AC-03 (SNAP, TANF, and Medicaid applicant data). Every agency contract sets a recovery time objective of **8 hours** and a recovery point objective of **1 hour** for the three large customers, and 24 hours and 4 hours for municipal customers, with monthly service credits below 99.5% availability.

## 3. Impact categories and values
Dollar values are scaled to $20.4 million in annual receipts, about $78,000 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $250,000 (service credits, response costs, and contract risk) | $50,000 to $250,000 | Less than $50,000 |
| Operations | An agency cannot run a core program (supervision, benefits intake, tax collection) | One agency function slowed or on paper | Internal work slowed |
| Regulatory | A CJIS, IRS, or program timeliness requirement is missed by an agency, or the company breaches a Security Addendum or Exhibit 7 term | Contract notice or recovery term missed | Internal policy deviation |
| Safety | Plausible harm to a person (for example, an officer without a supervisee's warrant status, or a household without food benefits past the expedited deadline) | Delayed but safe service | None |
| Reputation | Agency or media statements; loss of a customer | Complaints from agency program managers | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-05 Customer support and agency incident communications | High | 4 h | 2 h | 24 h |
| BP-01 Supervision case management for AC-02 (CJI) | High | 12 h | 8 h | 1 h |
| BP-02 Benefits application workflow for AC-03 | High | 24 h | 8 h | 1 h |
| BP-04 Agency data interfaces | High | 24 h | 8 h | 1 h |
| BP-03 Tax compliance casework for AC-01 (FTI) | High | 48 h | 8 h | 1 h |
| BP-06 Municipal constituent services | Moderate | 72 h | 24 h | 4 h |
| BP-07 Software release and emergency patching | Moderate | 72 h | 24 h | 24 h |
| BP-08 Implementation and data migration | Low | 120 h | 72 h | 24 h |
| BP-10 Payroll, billing, and finance | Low | 120 h | 72 h | 24 h |
| BP-09 AI eligibility assistant (pilot) | Low | 168 h | 72 h | 24 h |

**What drives the values:**
- **BP-05 comes first** because the company's legal and contract clocks start before any system is back. A suspected CJI incident must be reported inside 1 hour (CJISSECPOL IR-6), AC-01 must reach TIGTA and the IRS Office of Safeguards within 24 hours (Pub. 1075 section 1.8), and Florida agencies must report ransomware within 12 hours (Fla. Stat. 282.318 and 282.3185). If the ticketing system is down, the printed contact list in the incident binder is the workaround.
- **BP-01** has the shortest MTD among platform processes. The sheriff can run one shift from nightly printed rosters, but not a second day of court hearings without current conditions and violation records.
- **BP-02** is driven by SNAP timeliness. Expedited households must have benefits available by the seventh calendar day after filing (7 CFR 273.2(i)(3)); others within 30 days (273.2(g)(1)). A day of downtime is survivable; several days would push expedited cases past their deadline.
- **BP-03** tolerates 2 days because the revenue agency's own tax system keeps collections running, but it is the largest contract and renews in 2027.
- **BP-09** is Low: the AI assistant is a pilot and caseworkers do the full review without it.

**Key finding:** every platform process depends on the same database cluster, backups, and cloud account. The backups share the production account and region, are not immutable, and have **never been restored end to end** (P03 G-059, G-055). The 8-hour RTO in the contracts is therefore unproven, and in a ransomware case where an attacker holds administrator rights (P01 R-001) it is not achievable today.

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-03 Workforce identity provider | Single sign-on and MFA for administrators and support | All |
| Cloud account access | Administrator roles, break-glass accounts (to be created) | All platform processes |
| SYS-01 ACMP production | Container service, database cluster, AC-01 dedicated database, document storage | BP-01, BP-02, BP-03, BP-06, BP-09 |
| SYS-12 Backups | Point-in-time recovery and daily snapshots | BP-01 to BP-04, BP-06 |
| SYS-02 Integration gateway | AC-01 file transfer, AC-02 message switch, AC-03 API | BP-01 to BP-04 |
| SYS-04 Agency sign-in | Federation with agency identity providers; municipal local accounts | BP-01 to BP-03, BP-06 |
| SYS-07 Ticketing and status page | Support and agency notices | BP-05 |
| SYS-06 Repository and pipeline | Builds and deploys fixes | BP-07 |
| People | Cloud Operations Lead and 4 cloud engineers, 20 engineers, 7 support staff, Contracts and Compliance Manager | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Agency communications (BP-05): printed contact list, phones, status page | 1 h | Incident binder at headquarters and with each on-call engineer |
| 2 | Workforce identity and cloud account access | 1 h | Two sealed break-glass accounts with hardware keys (to be created; P01 R-029) |
| 3 | Clean cloud account and network rules from infrastructure code | 3 h | Rebuild in a second U.S. region (target design, P01 R-008) |
| 4 | Database cluster and AC-01 dedicated database from last clean point | 6 h | Immutable separate-account copies (to be built; P01 R-001) |
| 5 | Application tier and agency sign-in for AC-02, then AC-03, then AC-01 | 8 h | Agencies' paper and native-system workarounds (section 4) |
| 6 | Integration gateway, replaying agency files and messages | 8 h | Agencies resend files; manual lookups |
| 7 | Municipal tenants | 24 h | Paper intake |
| 8 | Pipeline, then payroll and finance, then implementation work | 72 h | Hold releases; repeat prior payroll |
| 9 | AI eligibility assistant | After all others | Manual review (normal process) |
