# Business Impact Analysis: Cris Santos Company | Manufacturing | Micro

**Organization:** Cris Santos Company, LLC (medical device startup) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Operations Manager (Information Security Coordinator) with the Head of Engineering, the QA/RA Manager, the Cloud Software Engineer, and the MSP lead technician, 2026-07-20 to 2026-07-31 | **Approved:** CEO, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the startup, how long each can be down, and how much data each can lose. The company has no product on the market yet, so the business impact of an outage today is mostly **schedule and runway**: every week the 510(k) slips costs about $43,000 of seed funding. The BIA supports:
- the availability rating in the SSP (P02) for the Product Development and Release Platform;
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08);
- the future cybersecurity management plan, which must show how updates reach fielded devices (FD&C Act 524B(b)(2); P03).

No regulation sets recovery times for a device developer. The drivers are the QMSR record requirements (design history must be kept and retrievable, 21 CFR 820.10 and ISO 13485 clause 4.2.5, incorporated by reference) and the submission schedule.

## 2. System and business description
One Florida office suite with a small engineering lab and 7 employees. The company designs the WM-1 wireless monitoring system (sensor, bedside hub, cloud service) and outsources production to a contract manufacturer. Most systems are SaaS: the source code repository and CI/CD service (SYS-01), the eQMS and PLM (SYS-02), and the productivity suite (SYS-03). The one cloud workload is the pre-production WM-1 cloud service (SYS-04). On site are 7 laptops and 2 lab workstations (SYS-05), the office and lab network (SYS-06), the signing key on one laptop (SYS-07), and 22 of the 30 pre-production units (SYS-08). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to a monthly operating cost of about $190,000, about $8,600 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $40,000 (about one week of runway) or a submission slip of more than 2 weeks | $8,000 to $40,000 | Less than $8,000 |
| Operations | Engineering or release work stops for the whole team | One function stops; others slowed | Staff slowed but working |
| Regulatory | Loss of design history records; a deficient or late FDA submission | Missed internal QMS timeline; incomplete record | Internal procedure deviation |
| Safety | Firmware that could reach patients is compromised or cannot be updated after clearance | Test units or evaluation units behave unsafely in testing | None |
| Reputation | Loss of the partner hospital system or an investor; public vulnerability disclosure before a fix | Partner hospital complaint; delayed milestone report to investors | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Firmware build, signing, and release | High | 72 h | 24 h | 0 |
| BP-02 Design history and quality records | High | 72 h | 24 h | 24 h |
| BP-03 Premarket submission preparation and FDA correspondence | High | 72 h | 24 h | 24 h |
| BP-04 Firmware and software development | Moderate | 72 h | 24 h | 8 h |
| BP-05 WM-1 cloud service (pre-production) | Moderate | 72 h | 24 h | 24 h |
| BP-06 Design verification and security testing | Moderate | 120 h | 48 h | 24 h |
| BP-07 Contract manufacturing support | Moderate | 120 h | 48 h | 24 h |
| BP-08 Vulnerability intake and product security monitoring | Moderate | 72 h | 24 h | 24 h |
| BP-09 Business administration | Low | 120 h | 48 h | 24 h |

**What drives the values:**
- **BP-01 has an RPO of zero** because the signing key is irreplaceable. Every unit trusts only that key. If it is lost, every unit must be re-keyed and a pilot build repeated (about $60,000 and 6 weeks). After clearance, a lost key would leave fielded devices unpatchable, which section 524B(b)(2) does not allow.
- **BP-02 and BP-03 are High** because the design history file is the evidence for the 510(k). Losing approved records would force them to be recreated and re-signed.
- **BP-05 is Moderate today and will become the most critical function after clearance.** Hubs show vital signs and sound alarms locally without the cloud, and no patient uses the service yet. Recovery targets for the clinical service (minutes, not hours) must be set before launch and are tracked in P01 (R-015).
- Most functions tolerate 3 to 5 days because engineers can work on local copies. The limit is the schedule, not safety.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-07 Signing key and release tooling | Private key file on the Head of Engineering's laptop; release scripts | Copy on an encrypted USB drive in the office safe. **Never tested; one custodian** | BP-01, BP-07 |
| SYS-01 Source code repository and CI/CD (SaaS) | Firmware and cloud code; build runners; build logs | Vendor replication; every engineer has a full local clone | BP-01, BP-04 |
| SYS-02 eQMS and PLM (SaaS) | Design history file, risk management file, supplier records | Vendor backups (vendor SOC 2 report not yet requested); no company export | BP-02, BP-03, BP-06, BP-07 |
| SYS-03 Productivity suite (SaaS) | Email, files, chat, shared folders | Vendor service resilience; **no third-party backup** | BP-03, BP-07, BP-08, BP-09 |
| SYS-04 WM-1 cloud service (PaaS tenant) | Ingestion, dashboard, update service, database | Daily database snapshots kept 7 days (provider default). **Never restore-tested**; infrastructure is not defined as code | BP-01, BP-05, BP-06 |
| SYS-05 Endpoints | 7 MSP-managed laptops; 2 unmanaged lab workstations | Laptops: no local-only data by design; lab workstations: raw test data uploaded daily | All |
| SYS-06 Office and lab network | Firewall, Wi-Fi, lab bench network, one internet line | MSP backs up the firewall configuration | BP-04, BP-06 |
| SYS-08 Pre-production units | 22 lab units; 8 at the partner hospital simulation center | Units can be reflashed from released images | BP-06 |
| People | 7 employees | **Only the Head of Engineering can sign firmware**; the Cloud Software Engineer is the only cloud administrator | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Source code and CI service vendor | BP-01, BP-04 | Vendor status history and documentation; SOC 2 report not yet requested |
| eQMS vendor | BP-02, BP-03 | Contract states daily backups; no SOC 2 report or export tested |
| Cloud provider (PaaS) | BP-01 (update service), BP-05, BP-06 | SOC 2 Type 2 report reviewed 2026-08-24 (P09). The company, not the provider, owns backups and restore of its own data |
| Productivity suite vendor | BP-03, BP-07, BP-08, BP-09 | Standard service terms |
| MSP | Laptops, network, suite administration | 4-business-hour response; no recovery time commitment; does not cover the lab workstations, repository, or cloud tenant |
| Contract manufacturer | BP-07 | ISO 13485 certificate; quality agreement (no cybersecurity or continuity terms) |
| Regulatory consultant | BP-03 | Holds copies of submission drafts |

**Key findings:**
1. **The signing key is a single point of failure.** One file, one custodian, one untested backup. It is also the company's highest-value secret (P01 R-001).
2. **The eQMS has never been exported.** The company depends entirely on the vendor for its design history file (P01 R-013).
3. **Cloud backups are unproven.** Snapshots exist but nobody has restored one, and the environment is built by hand, so a rebuild would take days (P01 R-015).
4. **Key people are single points of failure.** Only one person can sign firmware and only one can administer the cloud tenant (P01 R-014).
5. **The MSP covers corporate IT only.** The engineering systems that matter most (repository, cloud tenant, lab workstations, signing key) are outside its contract.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Signing key and release tooling (SYS-07) | 24 h | Restore from the office safe USB copy onto a clean MSP-managed laptop; move to an HSM-backed key service by 2026-12-31 (P01 R-001) |
| 2 | Identity and email (SYS-03) | 8 h | MSP restores access; phones for coordination |
| 3 | eQMS and PLM (SYS-02) | 24 h | Vendor-hosted; drafts in the productivity suite until restored |
| 4 | Source code repository and CI (SYS-01) | 24 h | Local clones; local builds for development only |
| 5 | Engineering laptops (SYS-05) | 24 h | MSP reimages; spare laptop held by the Operations Manager |
| 6 | WM-1 cloud service (SYS-04) | 24 h | Redeploy from the repository; restore the newest clean snapshot; regenerate test data from simulators |
| 7 | Lab network and lab workstations (SYS-06, SYS-05) | 48 h | Rebuild workstations from vendor installers; bench tests on laptops |
| 8 | Contract manufacturer handoff (SYS-09 interface) | 48 h | Encrypted drive by courier |
| 9 | Business administration tools | 48 h | Payroll service and bank portals |
