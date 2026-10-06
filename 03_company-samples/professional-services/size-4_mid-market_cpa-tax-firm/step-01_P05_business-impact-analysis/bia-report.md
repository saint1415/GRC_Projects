# Business Impact Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Mid-Market

**Organization:** Cris Santos Company, Inc. (PE-backed CPA, tax, and advisory firm, with its attest affiliate Cris Santos Assurance, LLP) | **Tier:** Mid-Market (600 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** GRC Manager with the Director of Information Security and the process owners named in `bia.csv` | **Fieldwork:** 2026-07-06 to 2026-07-31 | **Approved:** Chief Operating Officer, 2026-09-22 (presented to the audit committee the same day)

## 1. Overview and purpose
This BIA covers every business unit: the tax practice, tax operations (document processing, e-file, and the offshore preparation program), the Attest Firm, client accounting services (CAS), advisory, and enterprise support functions. It rates 18 business processes and puts a dollar, operational, and regulatory value on an outage of each.

The results feed:
- the contingency plan and the recovery sections of the written incident response plan required by 16 CFR 314.4(h) (P08);
- the asset prioritization in 16 CFR 314.4(c)(2), which asks the Company to manage systems "in accordance with their relative importance to business objectives";
- the contingency plan and criticality analysis for the ePHI the Company holds as a business associate (45 CFR 164.308(a)(7));
- the FIPS 199 availability rating and contingency controls in the SSP (P02);
- impact ratings and exposure estimates in the risk register (P01);
- the recovery order in both incident runbooks (P08);
- the Availability and Processing Integrity criteria in the SOC 2 readiness assessment for the CAS service (P09).

## 2. System and business description
The Company runs 6 Florida offices and a central document processing center, with 600 employees plus about 130 seasonal staff and interns from January to April. It files about 47,400 returns a year, the Attest Firm performs about 1,050 engagements, and CAS runs payroll for about 210 business clients. Tax work runs on the Tax and Client Data Platform (TCDP) described in the SSP (P02): the vendor-hosted tax software, the client portal, the DMS, the 5-account cloud landing zone, the identity provider, the productivity suite, 6 office networks, 776 endpoints, and the MSSP-operated security tooling. CAS runs on vendor SaaS (SYS-08), and the Attest Firm on the audit and SOC engagement platform (SYS-09). See `../00_company-facts.md` sections 3 and 4.

**The calendar drives everything.** About half of tax receipts are billed from February 1 to April 15. The March 15, April 15, September 15, and October 15 deadlines are the peak risk windows. The tax values below are **peak-season** values. Outside those windows the MTD for BP-01 to BP-03 relaxes to 72 hours. CAS payroll (BP-10) has a different rhythm: pay dates come every week of the year, so its values do not change with the season.

## 3. Impact categories and values
Dollar values are scaled to $100 million in annual revenue over about 250 business days: about $400,000 per business day on average, and about $530,000 of tax work alone per business day in peak season (individual about $340,000, business about $190,000).

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (per day of outage) | More than $100,000 in unrecovered revenue, penalty reimbursements, and overtime | $20,000 to $100,000 | Less than $20,000 |
| Operations | A whole practice (tax, CAS, or the Attest Firm) cannot deliver its core service | One office, one service line, or one team stops, or throughput drops by more than 30% | Staff slowed but working |
| Regulatory | Missed filing deadlines for many clients, a reportable data breach (FTC, IRS, states, HIPAA covered entity clients), or a payroll tax deposit missed for many clients | Missed deadline for a few clients, or a missed contractual report date | Internal procedure deviation |
| Safety | Not applicable. The Company has no processes that affect physical safety. Harm to clients and their employees is financial and is scored under Regulatory, Reputation, and the `client_harm_impact` column | | |
| Reputation | Regional media coverage, loss of referral sources, or loss of CAS or attest clients | Client complaints or online reviews | Internal only |

**How loss at MTD was estimated.** Estimated loss is revenue that is not recovered, plus penalty reimbursements and extra labor, over the MTD. The process owners supplied the recovery assumptions: about 30% of tax work lost in peak season is not recovered before the deadline (clients go on extension and some leave), about 15% of attest work and 10% of advisory and bookkeeping work is not recovered, and CAS payroll losses are mostly reimbursed client penalties and emergency processing fees. Billing delays are shown as delayed cash, not loss.

## 4. Process criticality and downtime (from `bia.csv`)
| Priority | Process | Unit | Criticality | MTD (h) | RTO (h) | RPO (h) | Estimated loss at MTD |
|---|---|---|---|---|---|---|---|
| 1 | BP-15 Identity and access (enabling) | Enterprise | High | 4 | 2 | 1 | $60,000 |
| 2 | BP-10 Client payroll processing | CAS | High | 24 | 8 | 1 | $70,000 |
| 3 | BP-01 Individual return preparation and review | Tax practice | High | 24 | 8 | 1 | $142,000 |
| 4 | BP-03 E-file transmission and acknowledgments | Tax operations | High | 24 | 8 | 1 | $60,000 |
| 5 | BP-02 Business, trust, and exempt return preparation | Tax practice | High | 24 | 8 | 1 | $82,000 |
| 6 | BP-13 Client communications | Enterprise | High | 24 | 8 | 24 | $30,000 |
| 7 | BP-18 Security monitoring and incident response (enabling) | Enterprise | High | 8 | 4 | 1 | Not estimated (enabling) |
| 8 | BP-04 Client document intake and scanning | Tax operations | High | 24 | 12 | 24 | $25,000 |
| 9 | BP-05 Client e-signature and return delivery | Tax operations | Moderate | 48 | 24 | 24 | $15,000 |
| 10 | BP-11 Client bookkeeping and bill pay | CAS | Moderate | 72 | 24 | 4 | $20,000 |
| 11 | BP-06 Offshore preparation support | Tax operations | Moderate | 72 | 48 | 24 | $60,000 |
| 12 | BP-14 Billing and collections | Enterprise | Moderate | 72 | 48 | 24 | $10,000 (plus about $1.2 million cash delayed) |
| 13 | BP-17 Practice management, scheduling, and engagement letters | Enterprise | Moderate | 72 | 48 | 24 | $15,000 |
| 14 | BP-08 Audit, review, and compilation engagements | Attest Firm | Moderate | 120 | 72 | 24 | $54,000 |
| 15 | BP-09 SOC examination engagements | Attest Firm | Moderate | 120 | 72 | 24 | $12,000 |
| 16 | BP-07 IRS and state notice response | Tax practice | Low | 72 | 48 | 24 | $5,000 |
| 17 | BP-12 Advisory engagements | Advisory | Low | 120 | 72 | 24 | $20,000 |
| 18 | BP-16 Firm payroll, HR, and recruiting | Enterprise | Low | 120 | 72 | 24 | $10,000 |

**Summary:** 8 High, 7 Moderate, and 3 Low processes (18 in total). The sum of estimated losses at each process's MTD is $690,000.

**Enterprise-wide scenario.** If the whole TCDP were down for 72 hours in the last week before April 15 (for example, ransomware), about $1.59 million of tax work would stop. About $477,000 of it would not be recovered, and overtime to catch up would add about $150,000. CAS payroll would fall back to repeat payrolls through the vendor (BP-10 runs on vendor SaaS, but CAS staff sign in through the identity provider and work from Company endpoints), with about $60,000 of reimbursed client penalties and fees. Attest and advisory losses would add about $40,000. That is about $727,000 in total, plus about $1.2 million of delayed cash. Incident response, legal, and notification costs come on top (see P01 R-001 and R-004).

**What drives the values:**
- **Deadlines, not revenue, drive BP-01 to BP-03.** A day lost in the last week before a deadline cannot be made up. The fallback is to file extensions early for every unfinished client, which moves the risk to the extension deadline but does not remove it.
- **Third-party harm drives BP-10.** If CAS misses a payroll cutoff, about 8,600 client employees may not be paid on payday. That harm lands on people who are not the Company's clients, which is why payroll is recovery priority 2.
- **IRS e-file rules drive BP-05.** The ERO may not transmit a return until the taxpayer signs Form 8879 (IRS Pub. 1345), so a portal outage blocks filing unless clients sign on paper.
- **IRC 7216 drives how BP-06 restarts.** When the offshore pool comes back, the SSN masking and consent checks must come back with it (26 CFR 301.7216-3(b)(4)). Speed is not a reason to skip them.
- **BP-13 carries the BEC risk.** Email is both a critical channel and the attack path in the first P08 scenario.
- **Identity is the first dependency.** Every SaaS system signs in through the identity provider, so BP-15 has the shortest MTD (4 hours).

## 5. Key findings
1. **The tax software vendor's recovery objective has no margin.** The vendor's SOC 2 system description states an RTO of 8 hours and an RPO of 1 hour (P09 vendor review). That just meets the peak-season RTO for BP-01 to BP-03. On 2026-04-14 the vendor's service was degraded for about 3 hours, and the Company had no written procedure for a vendor outage near a deadline (gap 9; P01 R-017; P08 vendor outage variant).
2. **Identity is a single point of failure without a full break-glass design.** Break-glass accounts exist for the cloud organization but not for the identity provider or the productivity suite. An attacker who changes administrator MFA during an incident could stop every process (P01 R-007).
3. **Practice-managed recovery is partly unproven.** The DMS restore was tested in 2025. The audit workpaper server (BP-08) has never been restored, and the CAS payroll fallback (repeat payroll through the vendor) has never been exercised (gap 9; P01 R-018).
4. **CAS payroll is the fastest route to harm outside the Company.** Its 8-hour RTO depends on the payroll vendor (SOC 2 RTO 4 hours) and on CAS staff reaching the vendor through the identity provider (P01 R-019; P09 Availability criteria).
5. **The offshore program adds both capacity and exposure.** It produces about 15% of individual return first drafts. Losing it costs capacity (BP-06), and running it without SSN masking breaches 26 CFR 301.7216-3(b)(4) (gap 4; P01 R-011; P03).

## 6. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Identity provider | SSO, MFA, and conditional access for all SaaS, the VPN, and virtual desktops | All |
| SYS-01 Tax preparation and e-file software (SaaS) | Return preparation, review, e-file, e-signature module, AI extraction (AI-001) | BP-01, BP-02, BP-03, BP-05, BP-06, BP-07 |
| SYS-02 Client portal (SaaS) | Uploads, e-signature, delivery, IRC 7216 consents | BP-04, BP-05, BP-13, BP-17 |
| SYS-03 DMS (in the workloads account) | Scanned documents and prior-year files; daily immutable backups (RPO 24 h) | BP-01, BP-02, BP-04, BP-06, BP-07, BP-12 |
| SYS-04 Cloud landing zone | Workloads, restricted enclave, virtual desktop pool, backup and log archive | BP-04, BP-06, BP-08, BP-09 |
| SYS-06 Productivity suite | Email, files, chat, calendar | BP-07, BP-12, BP-13 |
| SYS-07 Practice management (SaaS) | Time, billing, engagement letters, payment page | BP-14, BP-17 |
| SYS-08 CAS platform (SaaS) | Cloud accounting, bill pay, and payroll processing services | BP-10, BP-11 |
| SYS-09 Audit and SOC engagement platform | Workpaper application and journal entry analytics (AI-004) | BP-08, BP-09 |
| SYS-10 Office networks | 6 offices on SD-WAN; dual ISP at Office 1 (document processing center); single ISP elsewhere | All in-office work |
| SYS-11 Endpoints | 640 laptops (staff can work remotely), 110 desktops, 26 multifunction printers, 18 high-volume scanners | All |
| SYS-12 Security tooling | EDR, SIEM (MSSP), email security gateway | BP-18 and recovery validation |
| SYS-13 HR, payroll, and applicant tracking (SaaS) | Firm payroll and hiring | BP-16 |
| Third parties | Tax software vendor, portal vendor, payroll and accounting vendors, cloud provider, identity vendor, MSSP, offshore preparation support vendor, ISPs | As listed in `bia.csv` |
| People and facilities | Preparers and reviewers, document processing center staff, e-file team, CAS payroll team, IT and security team, MSSP | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 identity provider and administrator access | 2 h | Break-glass accounts for the identity provider and productivity suite (to be created; P01 R-007) |
| 2 | SYS-08 payroll service access for the CAS payroll team | 8 h | Vendor support line runs repeat payrolls; manual checks for terminated employees |
| 3 | SYS-01 tax software access (vendor-hosted) | 8 h | Remote work from any office or home; early extensions |
| 4 | SYS-01 e-file transmission and acknowledgment queue | 8 h | Extensions through the vendor; paper filing with proof of mailing as a last resort |
| 5 | SYS-06 email (or a clean replacement mailbox set after a BEC) | 8 h | Website notice; portal messages; phones |
| 6 | SYS-12 SIEM and EDR console | 4 h | MSSP works from its own platform; needed to validate a clean recovery |
| 7 | SYS-02 portal and SYS-03 DMS | 12 h | Work from paper originals and portal uploads; restore the DMS from the immutable vault |
| 8 | SYS-02 e-signature and delivery | 24 h | Wet-signature Form 8879 |
| 9 | SYS-08 cloud accounting and bill pay | 24 h | Clients pay urgent bills directly |
| 10 | SYS-04 virtual desktop pool for the offshore vendor | 48 h | Reassign drafts to U.S. staff; masking and consent checks verified before reconnection |
| 11 | SYS-07 practice management and billing | 48 h | Manual invoices and paper engagement letters |
| 12 | SYS-09 audit workpaper application | 72 h | Offline engagement files |
| 13 | SYS-13 HR and payroll SaaS | 72 h | Repeat the prior payroll |

## 8. Linkage to regulatory recovery duties
| Requirement | What this BIA supplies | Status |
|---|---|---|
| 16 CFR 314.4(c)(2): manage systems according to their relative importance | Process criticality and recovery priorities (sections 4 and 7) | Supplied; the asset inventory gap remains (P03) |
| 16 CFR 314.4(h)(2) and (h)(5): internal processes to respond and recover | Recovery order and workarounds used by both P08 runbooks | Supplied |
| 45 CFR 164.308(a)(7)(ii)(E): criticality of applications and data that hold ePHI | SYS-03 and SYS-09 hold PHI from health care engagements; both rated for recovery here | Supplied; the enclave move is due 2027-03-31 (P01 R-022) |
| IRS e-file rules (Pub. 1345): signed Form 8879 before transmission | BP-05 workaround keeps wet signatures before e-file | Supplied |
| Client contracts (CAS service commitments) | BP-10 and BP-11 RTOs become the availability commitments in the CAS system description (P09) | To be confirmed with clients by 2027-03-31 |
