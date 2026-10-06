# Business Impact Analysis: Cris Santos Company | Public Administration | Micro

**Organization:** Cris Santos Company, LLC (GovTech systems integrator) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Operations Manager (Security and Compliance Officer) with the owner, the Lead Platform Engineer, the Implementation and Support Analyst, and the MSP lead technician, 2026-07-27 to 2026-08-07 | **Approved:** owner, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the company, how long each can be down, and how much data each can lose. It supports:
- the contingency plan that the SP 800-53 Moderate baseline in the AC-02, AC-03, and AC-04 contracts requires (CP-2, with the RA-9 criticality analysis), due 2026-11-30;
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

Most of the harm from an outage here falls on **other organizations**: pretrial officers who cannot see their caseload, county caseworkers who cannot decide rent and utility applications, and city code inspectors. The contracts turn that into service credits and termination rights for the company. With 4 customers, losing one contract would cost between 5% and 30% of receipts.

## 2. System and business description
The company hosts case management applications for 4 Florida local agencies on a licensed low-code platform (SYS-01), runs one cloud workload for the sheriff's data interface and nightly exports (SYS-02), and supplies one consultant to a prime integrator on a state revenue agency project (SC-01, work done inside the agency's virtual desktop, SYS-10). Staff work on 8 MSP-managed laptops (SYS-06) and use SaaS for email, helpdesk, and code (SYS-03 to SYS-05). See `../00_company-facts.md` sections 1 to 3.

**Contract recovery terms.** AC-01 and AC-02: recovery time 24 hours, recovery point 4 hours, 99.5% monthly availability with service credits. AC-03 and AC-04: recovery time 72 hours, recovery point 24 hours.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual receipts, about $4,400 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20,000 (about 5 business days), or a customer gives notice to end its contract | $5,000 to $20,000 (service credits, overtime, response costs) | Less than $5,000 |
| Operations | An agency cannot run a core program (pretrial supervision, assistance decisions) or the company cannot reach its customers | One agency function on paper or slowed | Internal work slowed |
| Regulatory | A CJIS, IRS, or Florida reporting clock is missed by the company or an agency, or a Security Addendum or Exhibit 7 term is breached | A contract recovery or notice term is missed | Internal policy deviation |
| Safety | Plausible harm to a person (an officer unaware of a supervisee's violation; a household evicted or disconnected while waiting) | Delayed but safe service | None |
| Reputation | Agency or media statements; loss of a customer or the subcontract | Complaints from agency program managers | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Agency support and incident communications | High | 4 h | 2 h | 24 h |
| BP-02 Pretrial supervision case management (AC-01, CJI) | High | 48 h | 24 h | 4 h |
| BP-04 Emergency assistance application processing (AC-02) | High | 48 h | 24 h | 4 h |
| BP-03 Sheriff nightly booking interface (AC-01) | Moderate | 72 h | 24 h | 24 h |
| BP-05 Municipal code enforcement and constituent requests | Moderate | 120 h | 72 h | 24 h |
| BP-06 Revenue agency conversion validation (SC-01, FTI) | Moderate | 72 h | 24 h | 24 h |
| BP-07 Configuration changes, fixes, and releases | Moderate | 72 h | 48 h | 24 h |
| BP-08 Implementation and data migration projects | Low | 120 h | 72 h | 24 h |
| BP-09 Billing, payroll, and office administration | Low | 120 h | 72 h | 24 h |
| BP-10 AI eligibility pre-screening (pilot) | Low | 168 h | 120 h | 24 h |

**What drives the values:**
- **BP-01 comes first** because the company's reporting clocks start before any system is back: 1 hour for a suspected CJI incident (CJISSECPOL v6.1 IR-6), immediate notice to the prime and the revenue agency so the agency can report to TIGTA and the IRS Office of Safeguards within 24 hours (Pub. 1075 sec. 1.8.4), and enough facts for each county and city to file its 12-hour ransomware report (Fla. Stat. 282.3185(5)(b)). If email and the helpdesk are down, the printed contact card and company phones are the workaround.
- **BP-02 and BP-04** take their RTO and RPO from the contracts (24 hours and 4 hours). Their MTD of 48 hours comes from the agencies' paper workarounds: about 2 days of printed rosters for pretrial officers, and the county's 5-business-day decision rule for assistance applications.
- **BP-06** is Moderate because the FTI work never leaves the agency's virtual desktop; the company loses billings, not data. But only 2 laptops are approved to connect, so the laptops are the bottleneck.
- **BP-10** is Low: caseworkers review every application without the AI pilot.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Platform tenant (SaaS/PaaS) | 4 agency workspaces and a developer sandbox | Platform vendor: continuous backup (platform RPO 1 hour) for platform failures; full-tenant restore on request within 48 hours, 14 days kept. Company: nightly export to SYS-02 storage (RPO 24 hours) | BP-02, BP-04, BP-05, BP-07, BP-08, BP-10 |
| SYS-02 Integration server and export storage (IaaS) | Linux virtual machine and object storage bucket | Nightly exports kept 30 days in the same cloud account; **never restore-tested**. Server rebuilt by hand from SYS-05 scripts (no image backup) | BP-02, BP-03 |
| SYS-03 Productivity suite (SaaS) | Email, files, chat, staff sign-in | Vendor resilience; SaaS-to-SaaS backup run by the MSP (30 days) | BP-01, BP-06, BP-08, BP-09 |
| SYS-04 Helpdesk (SaaS) | Agency tickets and status notices | Vendor resilience | BP-01 |
| SYS-05 Source code repository (SaaS) | Interface scripts and exported configurations | Vendor resilience; working copies on 2 laptops | BP-03, BP-07 |
| SYS-06 Laptops | 8 MSP-managed laptops; 2 approved for SC-01 | MSP reimage from its standard build | All |
| SYS-09 AI add-on | Platform vendor feature | Vendor | BP-10 |
| SYS-10 Agency virtual desktop (external) | Revenue agency environment | Agency | BP-06 |
| People | 7 staff. The Lead Platform Engineer is the only person who has rebuilt SYS-02 | Owner holds the second SSH key; no written rebuild procedure | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Agreement | Evidence of recovery capability |
|---|---|---|---|
| Platform vendor (with its AI add-on) | BP-02, BP-04, BP-05, BP-07, BP-08, BP-10 | Platform subscription; data processing terms | SOC 2 Type 2 report and FedRAMP Moderate authorization (reviewed in P09). Stated 99.9% availability and platform RPO 1 hour meet the contracts. **Full-tenant restore within 48 hours does not meet the 24-hour RTO** if records are deleted by an attacker using company credentials |
| IaaS provider | BP-03; company export copies | Provider standard terms | FedRAMP Moderate authorized service in a U.S. region |
| MSP | Laptops, suite administration, firewall | Monthly service contract | **4-business-hour response time; no recovery time commitment** |
| Productivity suite vendor | BP-01, BP-06, BP-09 | Standard business terms | Vendor service commitments |
| Helpdesk vendor | BP-01 | Standard terms (never reviewed) | None reviewed |
| Revenue agency and prime | BP-06 | Subcontract with Exhibit 7 terms | Agency-operated |
| Sheriff IT (file drop and identity provider) | BP-02, BP-03 | AC-01 contract | Sheriff-operated; 7 days of files kept |

**Key findings:**
1. **The platform vendor meets the contracts for its own failures, not for ours.** If an attacker or a company administrator deletes or corrupts agency records, the vendor's full-tenant restore takes up to 48 hours and rolls back every workspace. The company's own nightly export gives a 24-hour recovery point, which misses the 4-hour RPO in the AC-01 and AC-02 contracts, and it has never been restored (risk R-004).
2. **The exports sit next to the server that makes them.** The bucket shares the cloud account and administrator keys with SYS-02. An attacker who reaches SYS-02 can delete both (R-001).
3. **One person can rebuild SYS-02.** There is no written rebuild procedure and no server image (R-017).
4. **The MSP contract has no recovery commitment.** A 4-business-hour response time is not a recovery time, and every laptop recovery depends on the MSP (R-012).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Agency communications: printed contact card, company phones, helpdesk status message | 1 h | Phone calls to each agency security contact |
| 2 | Workforce identity: productivity suite and platform administrator access from a clean laptop | 2 h | Spare laptop (SYS-06); owner's platform administrator account |
| 3 | Platform tenant check: confirm AC-01 and AC-02 workspaces intact, or request vendor restore | 4 h (check); up to 48 h (vendor restore) | Re-import AC-01 cases from the sheriff's files; agencies' paper workarounds |
| 4 | AC-01 and AC-02 workspaces back in service | 24 h | Paper rosters (AC-01); paper applications (AC-02) |
| 5 | SYS-02 rebuilt in a clean account; sheriff interface replayed from the 7-day file drop | 24 h | Manual entry of new defendants |
| 6 | AC-03 and AC-04 workspaces | 72 h | Paper complaint forms |
| 7 | Approved laptops for SC-01 | 24 h | Agency-site workstation through the prime |
| 8 | Repository, release tooling, and implementation work | 48 to 72 h | Hold changes |
| 9 | Billing and payroll | 72 h | Payroll service repeats the prior payroll |
| 10 | AI pre-screening pilot | After all others, and only after the P10 conditions are met | Manual review |
