# Business Impact Analysis: Cris Santos Company | Finance and Insurance | Micro

**Organization:** Cris Santos Community Federal Credit Union (member-owned federal credit union) | **Tier:** Micro (7 employees; $60.0 million in total assets) | **Method:** NIST SP 800-34 Rev. 1 BIA template
**Prepared by:** Operations Manager (Information Security Officer) with the President and CEO, the Accounting and Compliance Officer, the Lending Manager, the Senior Member Service Representative, and the MSP lead technician, 2026-07-13 to 2026-07-24 | **Approved:** President and CEO, 2026-08-31

## 1. Overview and purpose
This BIA lists every business function of the credit union, how long each can be down, and how much data each can lose. It supports:
- the measures to protect member information against destruction, loss, or damage from environmental hazards or technical failures that the credit union must consider (12 CFR Part 748, Appendix A, III.C.1.h; N52-R01), and the 2019 business continuity plan that will be rewritten from it;
- the security program objective to prevent destruction of vital records (12 CFR 748.0(b)(5)) and the vital records preservation program (12 CFR Part 749, as amended effective 2026-07-16);
- the catastrophic act report: NCUA's regional director must be notified within 5 business days of a disaster that interrupts vital member services for a projected period of more than two consecutive business days (748.1(b));
- the availability rating in the SSP (P02), impact ratings in the risk register (P01), and the recovery order in the incident response runbook (P08).

## 2. System and business description
One Florida office, 7 employees, about 6,400 members, and $60.0 million in total assets. Almost everything runs at vendors: the core processing system at a core processor (SYS-01), online and mobile banking at a digital banking provider (SYS-02), the wire portal at the corporate credit union (SYS-03), the productivity suite (SYS-04), card processing (SYS-07), and the loan origination system (SYS-08). On site are 8 desktops, 3 laptops, and 2 check scanners (SYS-05) and the office network and phones (SYS-06). The MSP runs IT and the document imaging server in a cloud tenant (SYS-09). See `../00_company-facts.md` sections 3 and 7.

## 3. Impact categories and values
Dollar values are scaled to about $1.1 million a year in net revenue (fictional), about $4,400 per business day.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost (direct loss and lost revenue) | More than $25,000 (one fraudulent wire, or about 6 business days of net revenue) | $5,000 to $25,000 | Less than $5,000 |
| Operations | Members cannot reach their money at the office, or no wires can be sent | One service stops; members slowed | Staff slowed but working |
| Regulatory | Reportable cyber incident to NCUA (748.1(c)), member notice under Appendix B, or a catastrophic act report (748.1(b)) | Missed filing or settlement deadline (SAR, Call Report, ACH settlement) | Internal policy deviation |
| Member harm (recorded in the `impact_safety` column) | Members lose funds, or cannot get paychecks, benefits, or closing funds | Member payments delayed but completed the same week | None |
| Reputation | Local media coverage, or members moving accounts in noticeable numbers | Member complaints or online reviews | Internal only |

The credit union has no processes that affect physical safety, so the Safety column records financial harm to members instead.

## 4. Process criticality and downtime
| Process | Criticality | MTD | RTO | RPO |
|---|---|---|---|---|
| BP-01 Teller and member account services | High | 8 h | 4 h | 1 h |
| BP-02 Online and mobile banking | High | 24 h | 8 h | 1 h |
| BP-03 Outgoing member wire transfers | High | 8 h | 4 h | 1 h |
| BP-04 Debit card and ATM services | Moderate | 24 h | 8 h | 1 h |
| BP-05 ACH and share draft processing | High | 24 h | 8 h | 1 h |
| BP-06 Loan origination and underwriting | Moderate | 72 h | 48 h | 24 h |
| BP-07 Member communications and document handling | Moderate | 24 h | 4 h | 24 h |
| BP-08 Accounting, BSA/AML, and regulatory reporting | Low | 72 h | 48 h | 24 h |

Totals: 8 processes, 4 High, 3 Moderate, 1 Low.

**What drives the values:**
- **Teller services (BP-01)** are vital member services under 12 CFR 749.1. An MTD of 8 hours is one business day. Well before two business days the credit union would also owe NCUA a catastrophic act report.
- **Wires (BP-03)** fund home closings and vehicle purchases the same day. The average wire is about $38,000, so one lost or fraudulent wire is a Severe cost by itself.
- **Phones (BP-07)** have a 4-hour RTO although the process is Moderate. Callbacks to the member's phone number on file (the new wire rule in POL-02) need working phones, and the VoIP phones share the single internet line.
- **Lending and accounting (BP-06, BP-08)** have deadlines counted in days (Regulation B notice timing, SAR filing), so 48 hours to recover is tolerable if no data is lost.

## 5. Resource requirements and vendor dependencies
| Resource | Description | Recovery method behind the RPO | Supports |
|---|---|---|---|
| SYS-01 Core processing system | Member accounts, shares, loans, general ledger, teller, ACH, BSA module | Core processor replication between two data centers (SOC 2 system description: RPO 15 minutes) | BP-01, BP-03, BP-04, BP-05, BP-08 |
| SYS-02 Online and mobile banking | Vendor-hosted; integrated with the core | Provider replication (SOC 2 report: RTO 4 h, RPO 15 min) | BP-02 |
| SYS-03 Wire portal | Corporate credit union web service with hardware tokens | Corporate credit union records; alternate phone-initiated wire | BP-03 |
| SYS-04 Productivity suite | Email, the shared Member Services mailbox, shared files | Vendor service resilience and deleted-item retention; **no separate backup** | BP-03, BP-07, BP-08 |
| SYS-05 Endpoints | 8 desktops, 3 laptops, 2 check scanners | No local data by design, except the nightly offline-teller balance file and scans cached at teller stations | All |
| SYS-06 Network and phones | Firewall, Wi-Fi, VoIP phones, one internet line | Firewall configuration backed up by the MSP | All |
| SYS-07 Card processing and ATM | Card processor; one lobby ATM | Card processor stand-in authorization | BP-04 |
| SYS-08 Loan origination system | Vendor SaaS with the AI scoring add-on | Vendor backups (SOC 2 report requested, not yet received) | BP-06 |
| SYS-09 Document imaging server | Virtual server in a cloud IaaS tenant, run by the MSP | Daily snapshots in the same cloud account, 14 days kept; **never restore-tested** | BP-07 |
| People | 7 employees | Cross-training: the Operations Manager and the Accounting and Compliance Officer can both approve wires and work the teller line | All |

**Vendor dependencies:**
| Vendor | Functions that stop without it | Evidence of recovery capability |
|---|---|---|
| Core processor | BP-01, BP-03, BP-04 (partly), BP-05, BP-08 | SOC 2 Type 2: RTO 8 h, RPO 15 min. **The 8-hour RTO exceeds the 4-hour RTO for BP-01.** Offline teller mode covers the gap for up to one business day |
| Digital banking provider | BP-02 | SOC 2 Type 2: RTO 4 h and RPO 15 min, which meet this BIA |
| Corporate credit union | BP-03, BP-05 settlement | Service agreement states wire service availability; alternate phone wire never tested |
| Card processor | BP-04 | Stand-in authorization when the core is down |
| MSP | Recovery of endpoints, network, and the imaging server | No written recovery commitment; the contract has only a 4-business-hour response time |
| Cloud IaaS provider (through the MSP's tenant) | BP-07 (imaging) | Provider platform commitments; the snapshots sit in the same account as the server |
| Productivity suite vendor | BP-03 (wire requests by email), BP-07 | Vendor service commitments (standard terms) |
| Internet provider | Every office function, including phones | None; single line |

**Key findings:**
1. **The core processor's 8-hour RTO does not meet the 4-hour RTO for teller services.** The offline teller mode fills the gap, but its balance file sits on one unencrypted desktop (risk R-012 in P01).
2. **The internet line is a single point of failure for the office, the phones, and callbacks** (R-013).
3. **Imaging and email have no independent backup.** The imaging server's snapshots sit in the same cloud account, and one MSP login without MFA could delete both (R-010). Signature cards and ID copies are needed to verify members.
4. **Vital records need a current program.** Part 749 was rewritten effective 2026-07-16. Under 749.2(b), records kept by an off-site data processor count as stored if the service agreement says the processor protects against losing production and backup data at the same time. The core processor contract has not been checked for that language, and the credit union's own records preservation log dates from 2019 (P03 gap G-006).
5. **The MSP contract has no recovery commitment.** Its 4-business-hour response time is not a recovery time. The P01 treatment for R-014 adds one at renewal.

## 6. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Internet, office network, and phones (SYS-06) | 2 h | Cellular failover router (to be installed by 2026-12-31); forward the main number to a staff cell phone until then |
| 2 | Clean teller and wire-desk endpoints (SYS-05) | 4 h | Laptops as teller stations; MSP reimages desktops |
| 3 | Core access for teller services (SYS-01) | 4 h | Offline teller mode on the nightly balance file |
| 4 | Wire portal (SYS-03) | 4 h | Corporate credit union phone-initiated wire with PIN, with a callback to the member on file |
| 5 | Email and the shared mailbox (SYS-04) | 8 h | Member requests by phone or in person only |
| 6 | Online and mobile banking (SYS-02) | 8 h | Vendor-hosted; website notice and phone service |
| 7 | Card and ATM (SYS-07) | 8 h | Card processor stand-in; ATM out-of-service notice |
| 8 | Document imaging server (SYS-09) | 24 h | Verify identity in person with ID; request re-sent loan documents |
| 9 | Accounting and reporting (through SYS-01) | 48 h | Prior-day core reports |
| 10 | Loan origination (SYS-08) | 48 h | Paper applications; manual underwriting |
