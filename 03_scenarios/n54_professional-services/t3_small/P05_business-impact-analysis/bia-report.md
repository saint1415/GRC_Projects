# Business Impact Analysis: Cris Santos Company | Professional, Scientific, and Technical Services | Small

**Organization:** Cris Santos Company, LLC (CPA and tax preparation firm) | **Tier:** Small (60 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** IT Manager (Qualified Individual) with the Tax Partner, Assurance Partner, and Client Services Supervisor | **Approved:** Firm Administrator, 2026-08-31

## 1. Overview and purpose
This BIA identifies which business processes the firm depends on, how long each can be down, and how much data it can lose. It supports:
- the contingency plan due 2027-03-31 (P02 CP-2), including a deadline contingency procedure;
- the recovery sections of the written incident response plan required by 16 CFR 314.4(h) (P08);
- the availability rating in the SSP (P02);
- impact ratings in the risk register (P01), and the asset prioritization in 314.4(c)(2) ("in accordance with their relative importance to business objectives").

## 2. System and business description
The firm runs two Florida offices with 60 employees, plus about 6 seasonal preparers from January to April. It files about 5,750 returns a year and performs about 180 assurance engagements. Tax work runs on the Tax Preparation and Client Portal Platform (TPCP): vendor-hosted tax software, a client portal, a cloud-hosted DMS and workpaper server, an identity provider, the productivity suite, office networks, and endpoints. See `../scenario-facts.md` sections 3 and 4.

**The calendar drives everything.** About 55% of annual receipts are billed from February to April. The April 15 deadline for individual returns and the October 15 extension deadline are the peak risk windows. The values below are **peak-season** values (February 1 to April 15, and October 1 to 15). Outside those windows, the MTD for BP-01 and BP-02 relaxes to 72 hours.

## 3. Impact categories and values
Dollar values are scaled to $15.9 million in annual revenue: about $61,000 per business day on average and about $145,000 per business day in peak season.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $150,000 (about one peak-season day) | $40,000 to $150,000 | Less than $40,000 |
| Operations | Tax teams in both offices cannot prepare or file returns | One office, one service line, or one team stops | Staff slowed but working |
| Regulatory | Missed filing deadlines for many clients, or a reportable data breach (FTC, IRS, states) | Missed deadline for a few clients, or an internal policy breach reported to the Partner Group | Internal procedure deviation |
| Safety | Not applicable. The firm has no processes that affect physical safety; harm to clients is financial and is scored under Regulatory and Reputation | | |
| Reputation | Local media coverage, or loss of referral sources and business clients | Client complaints or online reviews | Internal only |

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-11 Identity and access (enabling service) | High | 8 h | 4 h | 1 h |
| BP-01 Tax return preparation and review | High | 24 h | 8 h | 1 h |
| BP-02 Electronic filing and acknowledgments | High | 24 h | 8 h | 1 h |
| BP-05 Client communications | High | 24 h | 8 h | 24 h |
| BP-03 Client document intake | High | 24 h | 12 h | 24 h |
| BP-04 Client e-signature and return delivery | Moderate | 48 h | 24 h | 24 h |
| BP-09 Billing and collections | Moderate | 72 h | 48 h | 24 h |
| BP-07 IRS and state notice response | Low | 72 h | 48 h | 24 h |
| BP-06 Assurance engagements | Moderate | 120 h | 72 h | 24 h |
| BP-08 Client advisory and tax planning | Low | 120 h | 72 h | 24 h |
| BP-10 Payroll and HR | Low | 120 h | 72 h | 24 h |

**What drives the values:**
- **Deadlines, not revenue, drive BP-01 and BP-02.** A day lost in the last week before April 15 cannot be made up. The fallback is to file extensions early for every unfinished client, which moves the risk to October but does not remove it.
- **IRS e-file rules drive BP-04.** The ERO may not transmit a return until the taxpayer signs Form 8879 (IRS Pub. 1345), so a portal outage blocks filing unless clients sign on paper.
- **BP-05 carries the BEC risk.** Email is both a critical channel and the attack path in the P08 scenario. If email is shut down during an incident, clients must be told through the website and portal where to reach the firm.
- **Identity is the first dependency.** Every SaaS system signs in through the identity provider, so BP-11 has the shortest MTD.

**Key findings:**
1. The tax software vendor's SOC 2 report states an RTO of 8 hours and an RPO of 1 hour for the hosted application (P09 vendor review). That just meets the peak-season RTO for BP-01 and BP-02, with no margin.
2. The workpaper server has never been restore-tested, so the 72-hour RTO for BP-06 is unproven (P01 R-028).
3. There are no break-glass accounts, so an identity provider lockout during an incident (for example, the attacker changes admin MFA) would stop every process (P01 R-010).

## 5. Resource requirements
| Resource | Description | Supports |
|---|---|---|
| SYS-05 Identity provider | Single sign-on and MFA for all SaaS and the VPN | All |
| SYS-01 Tax preparation and e-file software (SaaS) | Return preparation, review, e-file transmission, e-signature module | BP-01, BP-02, BP-04, BP-07 |
| SYS-02 Client portal (SaaS) | Uploads, e-signature, delivery; the vendor retains uploads | BP-03, BP-04, BP-05 |
| SYS-03 and SYS-04 DMS and workpaper servers | Scanned documents and prior-year files; workpapers. Daily immutable backups in a second region (RPO 24 h) | BP-03, BP-06, BP-07, BP-08 |
| SYS-06 Productivity suite | Email, files, calendar | BP-05, BP-07, BP-08 |
| SYS-07 Practice management | Time, billing, payment page | BP-09 |
| SYS-08 Office networks and internet | Firewalls, Wi-Fi; primary and backup ISP at Main office; single ISP at Branch office | All in-office work |
| SYS-09 Endpoints | 62 laptops (staff can work remotely), 12 desktops, 4 printer-scanners | All |
| SYS-10 Payroll SaaS | Firm payroll | BP-10 |
| People | Preparers, reviewers, intake staff, e-file coordinator, IT Manager, MSP | All |

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | SYS-05 Identity provider and administrator access | 4 h | Two break-glass accounts stored offline (to be created; P01 R-010) |
| 2 | SYS-01 Tax software access (vendor-hosted) | 8 h | Staff work remotely if an office is down; early extensions |
| 3 | SYS-01 e-file transmission and acknowledgment queue | 8 h | Paper filing with proof of mailing as a last resort |
| 4 | SYS-06 Email (or a clean replacement mailbox set after a BEC) | 8 h | Website notice; portal messages; phones |
| 5 | SYS-02 portal and SYS-03 DMS | 12 h | Work from paper originals; restore DMS from the immutable vault |
| 6 | SYS-02 e-signature and delivery | 24 h | Wet-signature Form 8879 |
| 7 | SYS-07 Practice management and billing | 48 h | Manual invoices |
| 8 | Notice response tools (SYS-01, SYS-03 read access) | 48 h | Call agencies for more time |
| 9 | SYS-03 Audit workpaper server | 72 h | Offline engagement files |
| 10 | Advisory work files | 72 h | Reschedule |
| 11 | SYS-10 Payroll SaaS | 72 h | Repeat prior payroll |
