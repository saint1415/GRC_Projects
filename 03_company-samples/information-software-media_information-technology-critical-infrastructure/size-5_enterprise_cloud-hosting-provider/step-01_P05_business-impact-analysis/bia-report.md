# Business Impact Analysis: Cris Santos Company | Information Technology | Enterprise

**Organization:** Cris Santos Company, Inc. (publicly traded public cloud and managed infrastructure provider) | **Tier:** Enterprise (12,000 employees) | **Method:** NIST SP 800-34 Rev. 1 BIA template, informed by NIST IR 8286D
**Prepared by:** GRC team with process owners, 2026-06-01 to 2026-07-15 | **Approved:** Chief Technology Officer and Chief Risk Officer, 2026-08-14 | **Reported to:** risk and technology committee of the board, 2026-09-10

## 1. Overview and purpose
This enterprise-wide BIA identifies the business processes the company depends on, how long each can be down, how much data each can lose, and what each depends on, including third parties and the acquired managed services business (AQ-1). For a cloud provider, most processes are also the customers' processes: when the company's data plane stops, about 41,000 customers stop with it. The BIA feeds:
- the availability rating and recovery objectives in the HCP-G System Security Plan (P02);
- impact ratings in the enterprise risk register (P01), per NIST IR 8286D;
- the recovery order in the provider tooling compromise runbook (P08);
- the Availability criteria for the three SOC 2 service lines (P09);
- the contingency planning controls (CP family) in the FedRAMP certifications FR-1 and FR-2 and the Class D upgrade (P03).

**Results in one line:** 18 processes were analyzed; 9 are High criticality, 8 Moderate, and 1 Low. 9 processes need recovery within 2 hours. The dependency map (`dependency-map.csv`) lists 26 dependencies; 17 are single points of failure at some level and 4 have never been tested.

## 2. System and business description
Cris Santos Company runs six commercial regions (R1 to R6, each with three company-operated data centers), a Government region (G1, two data centers), and 41 edge points of presence. It has 12,000 employees, about 41,000 business customers, and about $4.8 billion in annual revenue (about $13.2 million a day). The technology estate is described in `../00_company-facts.md` section 3: the console and API (SYS-01), regional control planes (SYS-02), the workforce identity platform (SYS-03), about 249,000 hosts (SYS-04), storage services (SYS-05), the global network and edge (SYS-06), key management and PKI (SYS-07), the software supply chain (SYS-08), the fleet automation service (SYS-09), the legacy AQ-1 RMM tool (SYS-10), security operations (SYS-11), and about 2,600 vendors (SYS-15).

## 3. Impact categories and values
Dollar thresholds are scaled to about $13.2 million of revenue per calendar day and to the company's materiality framework (P08 section 6). Values are per 24 hours of outage unless stated.

| Category | Severe | Moderate | Minimal |
|---|---|---|---|
| Cost | More than $2 million per day, or more than $20 million cumulative (SLA credits included) | $250,000 to $2 million per day | Less than $250,000 per day |
| Operations | A region's data plane or control plane stops, or a global service (DNS, identity, keys) fails | One service, one zone, or one service line degraded | Staff slowed but working |
| Regulatory | Missed FedRAMP incident or vulnerability timeframe; missed bank notice; missed SEC filing; reportable breach of personal information | Late contractual notice or documentation | Internal policy deviation |
| Safety | Plausible harm through customers' safety-related workloads (for example, public safety or health care systems hosted on the platform) | Customer workloads delayed but safe | None |
| Reputation | National media, analyst or ratings action, loss of FedRAMP certification, or loss of large customers | Regional media; customer complaints; trade press | Internal only |

## 4. Process criticality and downtime (from `bia.csv`)
Ordered by recovery priority, then RTO.

| Process | Criticality | MTD | RTO | RPO | Quantified impact per 24 h |
|---|---|---|---|---|---|
| BP-06 Global network, DNS, and edge | High | 1 h | 30 min | 15 min | $16.00M |
| BP-01 Customer compute and storage data plane (SL-1) | High | 2 h | 1 h | 0 | $24.70M (one region) |
| BP-04 Identity and access | High | 2 h | 1 h | 15 min | $9.50M |
| BP-05 Key management service and PKI | High | 2 h | 1 h | 0 | $12.00M |
| BP-03 Government Cloud data plane and control plane (SL-2, G1) | High | 4 h | 2 h | 15 min | $2.30M |
| BP-12 Customer support, status page, and incident communications | High | 2 h | 1 h | 1 h | $0.45M |
| BP-02 Commercial control plane, console, and public API | High | 4 h | 2 h | 5 min | $6.80M |
| BP-07 Object storage and backup vault services | High | 4 h | 2 h | 0 | $7.40M |
| BP-11 Security monitoring and incident response | High | 4 h | 2 h | 15 min | $0.80M |
| BP-10 Software release and emergency patch deployment | Moderate | 24 h | 8 h | 1 h | $0.60M |
| BP-08 Managed infrastructure services through fleet automation (SL-3) | Moderate | 24 h | 8 h | 4 h | $1.10M |
| BP-09 Legacy RMM operations for AQ-1 customers (SL-3) | Moderate | 24 h | 12 h | 24 h | $0.19M |
| BP-13 Metering and billing | Moderate | 72 h | 24 h | 1 h | $0.35M |
| BP-18 FedRAMP ongoing certification and agency reporting | Moderate | 168 h | 72 h | 24 h | $0.06M |
| BP-16 Payroll and human resources | Moderate | 72 h | 48 h | 24 h | $0.25M |
| BP-14 Financial close and SEC reporting | Moderate | 120 h | 72 h | 24 h | $0.15M |
| BP-15 Capacity planning and hardware supply chain | Moderate | 336 h | 168 h | 24 h | $0.09M |
| BP-17 Sales, contracting, and customer onboarding | Low | 72 h | 48 h | 24 h | $0.12M |

**What drives the values:**
- **Customer dependency** sets the shortest MTDs. The data plane, network, identity, and keys (BP-01, BP-04, BP-05, BP-06) are hours-level because customers' own systems stop when they stop.
- **SLA credits, not lost usage,** dominate the dollar values. Losing the largest region for a day costs about $22.2 million in credits against about $2.5 million of lost usage.
- **Regulation** sets BP-11 and BP-12 to High even though their direct cost is small: FedRAMP Initial Incident Reports are due within 1 hour for the most severe ratings under Class C and within 15 minutes under Class D, and bank notices are due as soon as possible after a four-hour determination (P08).
- **Dollar values understate BP-03.** G1 revenue is small, but losing it puts both the federal business and the FedRAMP certifications at risk, so it is rated Severe on regulatory and reputation impact.
- **Financial close** (BP-14) tightens to a 48-hour MTD at quarter-end because of SEC filing deadlines.

## 5. Dependency mapping and third parties
The full map is in `dependency-map.csv`. Key findings:

1. **Fleet automation blast radius (DEP-21).** One internal service can push software to every host and every enrolled customer guest. Its recovery is fast (8-hour RTO), but its misuse is the most damaging single event in the register. Guest-agent channel releases lack two-person approval (P01 R-001; POAM-001; the P08 scenario).
2. **G1 recovery (DEP-19).** The G1 tenant database restore took 3.4 hours in the 2026-06 disaster recovery test against a 2-hour RTO. The commercial regions met their RTOs in 2026-05 (P01 R-011; POAM-009).
3. **AQ-1 dependencies (DEP-11, DEP-23).** The legacy RMM vendor and the legacy directory are single points of failure for 140 customers, have never been tested for recovery, and the RMM contract has no security or incident notice terms (R-002; POAM-022).
4. **Registrar and HSM concentration (DEP-05, DEP-07).** One registrar for company domains (registry lock enabled, never tested) and one HSM manufacturer (R-024; R-032).
5. **R1 fuel supply (DEP-02).** Florida's R1 region has generators with 72 hours of fuel but only one contracted fuel supplier during hurricane season (R-040).
6. **External Cloud provider X (DEP-09).** The status page and out-of-band recovery vault run outside the company cloud on purpose, so customers and staff keep a source of truth during a company-wide outage. The 2026-05 vault restore of control plane state took 1.2 hours.

## 6. Resource requirements
| Resource / component | Description | Supports process |
|---|---|---|
| SYS-02 Regional control planes | Provisioning, placement, tenant databases, metering | BP-01 to BP-03, BP-07, BP-13 |
| SYS-03 Workforce identity platform | SSO, MFA, PAM, identity governance | All |
| SYS-04 Hypervisor fleet and host management | About 249,000 hosts and BMC networks | BP-01, BP-03 |
| SYS-05 Storage services | Block, object, snapshots, immutable vault | BP-01, BP-03, BP-07 |
| SYS-06 Global network and edge | Backbone, PoPs, DNS, DDoS mitigation | All customer-facing processes |
| SYS-07 Key management and PKI | HSM clusters per region | BP-05; all encrypted resources |
| SYS-08 and SYS-09 Supply chain and fleet automation | Build, sign, deploy | BP-08, BP-10; recovery of all |
| SYS-10 Legacy RMM | AQ-1 managed servers | BP-09 |
| SYS-11 Security operations platform | SIEM, EDR, AI triage | BP-11 |
| SYS-14 External Cloud provider X | Status page, recovery vault, security data lake copy | BP-02, BP-11, BP-12 |
| Facilities | 20 data centers, generators, cooling; 41 PoPs | BP-01, BP-03, BP-06 |
| People | Data center operations, SOC, control plane and network on-call, support, G1 U.S.-person staff | All |

## 7. Recovery priorities
| Priority | Resource | Expected recovery time | Alternate strategy |
|---|---|---|---|
| 1 | Network, DNS, identity, and key management in the affected scope (BP-06, BP-04, BP-05); data plane placement (BP-01, BP-03) | 30 min to 2 h | Anycast failover; break-glass accounts; zone evacuation |
| 2 | Regional control planes and console (BP-02, BP-07), SOC tooling (BP-11), status page and notices (BP-12) | 1 to 2 h | Restore from the immutable vault; status page on Cloud provider X |
| 3 | G1 control plane full capacity (BP-03) | 2 h target (3.4 h demonstrated) | Single-site operation in the surviving G1 data center |
| 4 | Release pipeline for emergency fixes (BP-10) | 8 h | Break-glass build environment with HSM signing |
| 5 | Fleet automation jobs for SL-3 (BP-08) | 8 h | Customer-approved remote access |
| 6 | Legacy RMM for AQ-1 customers (BP-09) | 12 h (vendor-dependent) | Customer-approved remote access |
| 7 | Metering and billing (BP-13) | 24 h | Regional meter buffers (7 days) |
| 8 | FedRAMP reporting (BP-18) | 72 h | Manual export from the GRC platform |
| 9 | Payroll and HR (BP-16) | 48 h | Repeat prior payroll |
| 10 | Financial close (BP-14) | 72 h | Manual close |
| 11 | Capacity planning and hardware supply (BP-15) | 168 h | Spare pools |
| 12 | Sales and onboarding (BP-17) | 48 h | Manual screening |

## 8. Gaps carried to other deliverables
| Gap | Carried to |
|---|---|
| Fleet automation guest-agent channel without two-person approval | P01 R-001; P02 CM-3 and CM-5; POAM-001 |
| G1 tenant database recovery 3.4 h against a 2 h RTO | P01 R-011; P02 CP-10; POAM-009 |
| AQ-1 RMM and legacy directory never recovery-tested; no vendor incident terms | P01 R-002 and R-015; POAM-022 |
| Bank-designated contacts current for 188 of 210 banks | P01 R-016; P03; POAM-023 |
| R3 hypervisor release leaves vendor support 2027-03-31 | P01 R-025; POAM-026 |
| R1 fuel resupply depends on one contracted supplier | P01 R-040 |
| Registrar concentration (registry lock never tested) | P01 R-024 |
