# Business Impact Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Enterprise

**Organization:** Cris Santos Company, LLP (national CPA and tax firm; privately owned by its partners) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Operating Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** Audit and Risk Committee of the Partnership Board, 2026-09-15

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the firm depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired firms. It feeds:
- the enterprise contingency and disaster recovery program, including the deadline contingency procedure for filing season;
- the recovery sections of the written incident response plan required by 16 CFR 314.4(h) (P08);
- the asset prioritization in 16 CFR 314.4(c)(2) ("in accordance with their relative importance to business objectives");
- the contingency planning the firm performs as a HIPAA business associate (45 CFR 164.308(a)(7));
- the availability rating and recovery objectives in the Tax Engagement Platform System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the Availability criteria for the two SOC 2 service lines (P09).

**Results in one line:** 17 processes were analyzed; 10 are High criticality, 6 Moderate, and 1 Low. 5 processes need recovery within 8 hours. The dependency map (`dependency-map.csv`) lists 24 dependencies, 14 of them single points of failure and 4 never tested.

## 2. System and business description
Cris Santos Company is a national CPA and tax firm headquartered in Florida, with 64 offices in 14 states, 12,000 employees, about 1,500 seasonal tax staff from January to April, and about $4.8 billion in annual receipts (tax 46%, assurance 30%, advisory 24%). It prepares about 420,000 individual and 96,000 business returns a year, audits about 140 SEC issuers, and runs two service lines that clients rely on as outsourcers: client accounting and payroll services (SL-1) and tax compliance outsourcing (SL-2). The technology estate is described in `../00_company-facts.md` section 3: the tax software and e-file transmitter (SYS-01), client document portal (SYS-02), DMS and tax workflow (SYS-03), identity platform (SYS-04), productivity suite (SYS-05), a multi-cloud estate with two colocation data centers (SYS-06), the audit platform (SYS-07), the client accounting and payroll platform (SYS-08), the network (SYS-09), and about 14,800 laptops (SYS-10). Two acquired firms, AF-05 and AF-06, still run their own systems.

**The calendar drives everything.** The values below are **peak-season** values: January 15 to April 15, and September 1 to October 15 (the September 15 business extension deadline and the October 15 individual extension deadline). Outside those windows, the MTD for BP-01, BP-02, and BP-05 relaxes to 72 hours. Assurance (BP-07) peaks separately from late February to March, when issuer clients file their annual reports.

## 3. Impact categories and values
Dollar thresholds are scaled to about $19.0 million of average receipts per business day (about $27 million per business day for the tax practice at the April peak). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2 million per day, or more than $20 million cumulative | $500,000 to $2 million per day | Less than $500,000 per day |
| Operations | A tier-1 service stops firm-wide, or more than 10 offices cannot serve clients | One service line, one region, or up to 10 offices stop | Staff slowed but working |
| Regulatory | Missed filing deadlines for many clients; a reportable breach (FTC, IRS, states, HIPAA clients); an attest engagement accepted without an independence check | Missed deadlines for a few clients; a contractual notice deadline missed | Internal procedure deviation |
| Safety | Not applicable. The firm has no processes that affect physical safety; harm to clients is financial and is scored under Regulatory and Reputation | | |
| Reputation | National media; loss of large corporate or SL-1 clients; regulator inquiry | Regional media; client complaints | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-16 Identity and access (enabling service) | High | 4 h | 2 h | 15 min | $19.00M (all work stops) |
| BP-01 Individual and private client tax preparation and review | High | 24 h | 8 h | 1 h | $7.50M |
| BP-02 Electronic filing, acknowledgments, and extensions | High | 24 h | 8 h | 1 h | $2.00M |
| BP-09 Client accounting and payroll services (SL-1) | High | 24 h | 8 h | 1 h | $2.60M |
| BP-11 Client communications | High | 24 h | 8 h | 4 h | $1.20M |
| BP-03 Client document intake and data extraction | High | 24 h | 12 h | 4 h | $1.80M |
| BP-06 Tax compliance outsourcing and global mobility (SL-2) | High | 24 h | 12 h | 4 h | $1.40M |
| BP-17 Tax operations at acquired firms AF-05 and AF-06 | High | 24 h | 12 h | 24 h | $0.90M |
| BP-05 Business, trust, and international tax compliance | High | 48 h | 24 h | 4 h | $5.20M |
| BP-07 Assurance engagements (including issuer audits) | High | 48 h | 24 h | 4 h | $3.90M |
| BP-04 Client e-signature and return delivery | Moderate | 48 h | 24 h | 4 h | $0.60M |
| BP-15 Firm payroll, HR, and seasonal onboarding | Moderate | 72 h | 48 h | 24 h | $0.30M |
| BP-10 Advisory and consulting engagements | Moderate | 72 h | 48 h | 24 h | $1.90M |
| BP-13 Engagement acceptance, independence, and conflicts | Moderate | 72 h | 48 h | 24 h | $0.40M |
| BP-08 SOC examination engagements | Moderate | 120 h | 72 h | 24 h | $0.50M |
| BP-14 Time, billing, collections, and firm finance | Moderate | 120 h | 72 h | 24 h | $0.30M |
| BP-12 IRS and state notice response and representation | Low | 72 h | 48 h | 24 h | $0.20M |

The identity row is counted once; its $19.0 million is the whole firm's daily receipts, not an amount to add to the other rows.

**What drives the values:**
- **Deadlines, not revenue, drive tax.** A day lost in the last week before April 15 or October 15 cannot be made up. The fallback is to file extensions early for every unfinished client, which moves the risk but does not remove it. Business returns (BP-05) have longer MTDs because extensions are routine, but partnership penalties accrue per partner per month once a deadline passes.
- **IRS e-file rules drive BP-02 and BP-04.** The ERO may not transmit until the taxpayer signs Form 8879 (IRS Pub. 1345), so an outage of the e-signature identity verification service blocks transmission unless clients sign on paper.
- **Pay dates drive SL-1 (BP-09).** Client employees must be paid on the pay date and payroll tax deposits have fixed deadlines, so SL-1 has the same 8-hour RTO as the tax platform. Its SOC 1 and SOC 2 commitments make the objectives contractual (P09).
- **Issuer clients drive assurance (BP-07).** Issuer audits must finish before clients' annual report deadlines, so assurance is High in its own peak even though its MTD is 48 hours.
- **Email carries the attack.** BP-11 is a critical channel and the business email compromise path in P08. If a tenant or mailbox is shut down during an incident, clients must be told through the website and portal where to reach the firm.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **One e-file transmitter (DEP-01).** The tax software vendor transmits 100% of the firm's e-files (outside AF-05 and AF-06). Its contract RTO is 12 hours against an 8-hour peak-season BIA RTO, and there is no tested alternative. A 2-day transmitter outage in the week before April 15 would put about 18,000 returns a day at risk of late filing. This is P01 risk R-005 and POA&M item POAM-019.
2. **Tax workflow recovery (DEP-03).** In the 2026-05-09 disaster recovery test, the tax workflow and e-file queue recovered in 9.5 hours against an 8-hour RTO; the tax software database met its 1-hour RPO (P01 R-031; POAM-011).
3. **Acquired firms (DEP-21, DEP-22).** AF-05 and AF-06 run their own email tenants, tax software, and file servers with nightly backups, so their real RPO is 24 hours, and their restores have never been tested. AF-05's tenant is not monitored by the SOC (P01 R-003; POAM-005).
4. **E-signature identity verification (DEP-10).** Every electronic Form 8879 depends on one identity verification service with no SOC report reviewed and no tested fallback other than wet signatures (P01 R-037; POAM-015).
5. **Offshore provider (DEP-12).** The offshore tax outsourcing provider drafts about 22% of business returns in season. Work can return on-shore, so it is not a single point of failure, but the IRC 7216 consent and SSN masking exceptions make it a confidentiality dependency (P01 R-008; POAM-008).
6. **SL-1 banking (DEP-14).** One ACH originating bank carries 100% of SL-1 direct deposits. The manual upload fallback was drilled in 2025-11.
7. **Industry-wide dependency (DEP-11).** IRS and state e-file systems are outside the firm's control; the workaround is procedural (paper filing and IRS outage relief).

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-04 Identity platform | SSO, MFA, privileged access, identity governance | All |
| SYS-01 Tax preparation and e-file software | Licensed software on Cloud provider A; vendor transmitter | BP-01, BP-02, BP-05, BP-06, BP-12 |
| SYS-02 Client document portal | Uploads, e-signature, delivery; corporate tax portal view for SL-2 | BP-03, BP-04, BP-06, BP-11 |
| SYS-03 DMS and tax workflow | DMS SaaS (files since 2015) and legacy archive (2004 to 2014); firm-built workflow and e-file queue | BP-01, BP-03, BP-05, BP-10, BP-12 |
| SYS-05 Productivity suite | Email, files, chat | BP-11 and every process for email |
| SYS-06 Cloud provider A and B; DC-1 and DC-2 | Platform and landing zone; immutable backups; offline copies | All recovery |
| SYS-07 Audit platform | Assurance and SOC engagement workpapers | BP-07, BP-08 |
| SYS-08 Client accounting and payroll platform | SL-1 service delivery | BP-09 |
| SYS-09 Network and zero-trust access | 64 offices and remote work | All |
| SYS-10 Endpoints | About 14,800 laptops (staff can work remotely), about 900 printer-scanners | All |
| SYS-11 Practice management and ERP | Engagement acceptance, independence, billing, HR | BP-13, BP-14, BP-15 |
| People | Preparers and reviewers, e-file operations, intake hubs, SL-1 and SL-2 delivery teams, SOC, IT operations | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-04 identity platform and break-glass accounts | 2 h | Sealed break-glass accounts; standby region |
| 2 | Network core, SD-WAN, zero-trust access, DNS | 2 h | Cellular failover; remote work |
| 3 | Security tooling (EDR console, SIEM) for clean-room validation | 2 h | Managed security service provider tooling |
| 4 | SYS-01 tax software and the e-file queue | 8 h | Early extensions; paper filing as a last resort |
| 5 | SYS-05 email (or a clean replacement mailbox set after a compromise) | 8 h | Website notice; portal messages; phones |
| 6 | SYS-08 payroll engine and ACH file creation (SL-1) | 8 h | Repeat prior payroll; manual bank upload |
| 7 | SYS-02 client portal and SYS-03 DMS and intake | 12 h | Work from source images; manual keying |
| 8 | SL-2 corporate tax portal | 12 h | Secure file exchange through the DMS |
| 9 | AF-05 and AF-06 legacy environments | 12 h target (24 h per their provider contracts) | Move urgent work to the enterprise platform |
| 10 | SYS-07 audit platform | 24 h | Offline synchronized engagement files |
| 11 | E-signature identity verification | 24 h | Wet signatures |
| 12 | SYS-11 HR, engagement acceptance, ERP | 48 h | Manual independence checks; repeat prior payroll |
| 13 | Advisory data rooms and analytics | 48 h | Reschedule |
| 14 | SOC examination tools, notice response tools, billing | 72 h | Reschedule; call agencies for more time; manual invoices |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| E-file transmitter concentration; contract RTO 12 h against 8 h | P01 R-005; POAM-019 |
| Tax workflow recovered in 9.5 h against an 8 h RTO | P01 R-031; P02 CP-10; POAM-011 |
| AF-05 and AF-06 RPO 24 h and untested restores; AF-05 not monitored | P01 R-003; POAM-005 |
| E-signature identity verification service without SOC report or tested fallback | P01 R-037; POAM-015 |
| Offshore provider consent and masking exceptions | P01 R-008; P03 G-048 and G-051; POAM-008 |
