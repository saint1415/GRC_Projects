# Business Impact Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Micro

**Organization:** Cris Santos Company, LLC (CPA and tax preparation firm) | **Tier:** Micro (7 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Office Manager (Qualified Individual) with the Owner CPA, the Bookkeeper, the Client Services Coordinator, and the MSP lead technician, 2026-07-06 to 2026-07-17 | **Approved:** Owner CPA, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the firm, how long each can be down, and how much data each can lose. It supports:
- the identification and management of systems and data "in accordance with their relative importance to business objectives" required by the FTC Safeguards Rule (16 CFR 314.4(c)(2), N54-R01);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01);
- the recovery order in the incident response runbook (P08).

No rule requires this firm to have a contingency plan by name. The Safeguards Rule requires safeguards appropriate to the firm's size (314.3(a)), and IRS Pub. 4557 recommends backup and recovery planning for tax professionals (N54-R03). Filing deadlines make availability a real business risk: a firm that cannot file on April 15 or October 15 pushes penalties onto its clients.

## 2. System and business description
One Florida office suite and 7 employees. The firm prepares about 880 individual and 170 business returns a year, does monthly bookkeeping and payroll for 38 small-business clients, and answers IRS notices. Nearly everything runs in vendor SaaS: the tax software (SYS-01), the client portal (SYS-02), the productivity suite with the client folders (SYS-03), the client accounting and payroll platforms (SYS-04), and practice management (SYS-05). On site are 8 computers and a leased MFP (SYS-06) and the office network (SYS-07). The MSP runs IT and the suite backup (SYS-08). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million in annual revenue: about $4,400 per business day on average and about $10,500 per business day from February to April.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $20,000 (about 2 filing-season days) | $5,000 to $20,000 | Less than $5,000 |
| Operations | The firm cannot prepare, file, or pay clients' employees | One function stops; others slowed | Staff slowed but working |
| Regulatory | Missed filing or payroll deadline for many clients; reportable data theft (IRS, FTC, Florida) | Missed notice response or late extension for a few clients | Internal policy deviation |
| Safety | Not applicable. No function of the firm affects physical safety | | |
| Reputation | Client losses across the client base; local media coverage | Complaints from several clients; online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Tax return preparation and review | High | 24 h | 8 h | 1 h |
| BP-02 E-file transmission and signatures | High | 24 h | 8 h | 1 h |
| BP-03 Client document intake and return delivery | High | 24 h | 8 h | 4 h |
| BP-04 Payroll processing for bookkeeping clients | High | 24 h | 8 h | 24 h |
| BP-05 Monthly bookkeeping and client accounting | Moderate | 120 h | 72 h | 24 h |
| BP-06 IRS notice responses and representation | Moderate | 72 h | 48 h | 24 h |
| BP-07 Client communications | Moderate | 24 h | 8 h | 24 h |
| BP-08 Billing and firm administration | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- The values are for the filing season and the extension deadlines, the worst case. Outside those periods BP-01 to BP-03 could tolerate several days.
- Deadlines drive BP-01 and BP-02. In the last week before April 15 or October 15, one lost day means returns or extensions are filed late for clients. Extensions are the fallback, but they also need the tax software.
- Pay dates drive BP-04. Clients' employees must be paid on time, and a missed payroll tax deposit brings penalties for the client. Its RPO is 24 hours because the payroll data itself is held by the payroll platform vendor; only the input worksheets live in SYS-03.
- Recent scans drive the 4-hour RPO for BP-03. Scans saved on the reception desktop sync to SYS-03 within minutes, but scans held on the MFP or not yet filed would have to be redone.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Tax software (SaaS) | Returns, e-file, acknowledgments | Tax software vendor's backups and replication (SOC 2 report states RTO 4 h and RPO 1 h; see P09) | BP-01, BP-02, BP-06 |
| SYS-02 Client portal (SaaS) | Document upload, e-signature, return delivery | Portal vendor's service; no recovery figures available | BP-02, BP-03, BP-07 |
| SYS-03 Productivity suite (SaaS) | Email, client folders, payroll input worksheets | Vendor service resilience; daily copy to SYS-08 | BP-01, BP-03, BP-04, BP-06, BP-07 |
| SYS-08 Suite backup (SaaS, MSP-operated) | Daily copy of mailboxes and cloud storage, 1 year of retention | **Full restore never tested** | BP-03, BP-04, BP-06 |
| SYS-04 Client accounting and payroll platforms (SaaS) | Clients' ledgers; client payroll | Platform vendors' own backups | BP-04, BP-05 |
| SYS-05 Practice management (SaaS) | Client list, invoices, payments | Vendor service | BP-08 |
| SYS-06 Endpoints | 4 desktops, 4 laptops, MFP | No local data by design except recent scans on the reception desktop and the MFP drive | All |
| SYS-07 Office network and internet | Firewall, Wi-Fi, one internet line | Firewall configuration backed up by the MSP | All |
| People | 7 employees; seasonal assistant in season | Cross-training: the Owner CPA can approve payroll; the Office Manager covers reception | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Contract security terms | Evidence of recovery capability |
|---|---|---|---|
| Tax software vendor | BP-01, BP-02, BP-06 | Vendor standard terms | SOC 2 Type 2 report reviewed (P09); RTO 4 h and RPO 1 h meet this BIA |
| Client portal vendor | BP-02, BP-03 | Vendor standard terms | None reviewed; vendor status page only |
| Productivity suite vendor | BP-01, BP-03, BP-04, BP-06, BP-07 | Vendor standard terms | Vendor service commitments (standard terms) |
| Payroll platform vendor | BP-04 | Vendor standard terms | None reviewed |
| MSP | Recovery of every on-site system; operates the backup | **None** | No written recovery commitment; the contract has only a 4-business-hour response time |
| Backup service (MSP subcontractor) | Restore of email and client folders | Through the MSP (not reviewed) | None until the first full restore test |
| Internet provider | Every SaaS function | Not applicable | None; single line |

**Key findings:**
1. **The tax software vendor meets the BIA.** Its stated RTO (4 h) and RPO (1 h) meet the targets for BP-01 and BP-02.
2. **The client folder backup is unproven.** SYS-08 has never had a full restore test, so the RPO for BP-03, BP-04, and BP-06 is an assumption (risk R-022).
3. **The internet line is a single point of failure for every High function** in the deadline weeks (risk R-017).
4. **The MSP contract has no recovery commitment.** A 4-business-hour response time is not a recovery time. The contract amendment in P01 (R-006) adds one.
5. **Two key vendors are unknown quantities.** The portal and payroll vendors have never been asked for recovery figures or security evidence (P03 G-028 to G-030).

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Internet and office network (SYS-07) | 2 h | Owner CPA's phone hotspot; cellular failover router planned (R-017) |
| 2 | Clean endpoints (SYS-06) | 4 h | Laptops first; MSP reimages desktops |
| 3 | Productivity suite sign-in and email (SYS-03) | 4 h | Phones forwarded to the Office Manager's cell; portal notice to clients |
| 4 | Tax software (SYS-01) | 8 h | Vendor-hosted; any clean laptop; extensions as the fallback |
| 5 | Payroll platform (SYS-04) | 8 h | Any clean laptop; repeat prior payroll with client approval |
| 6 | Client portal (SYS-02) | 8 h | Paper Forms 8879 and in-office delivery |
| 7 | Client folders restore (SYS-08 to SYS-03) | 24 h | Ask clients to re-send documents through the portal |
| 8 | Client accounting platforms (SYS-04) | 72 h | Catch up after restore |
| 9 | Practice management (SYS-05) | 72 h | Invoice after restore |
