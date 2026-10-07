# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulations | SDWA section 1433 (42 U.S.C. 300i-2(b)(1)): the policy set is part of the "strategies and resources to improve the resilience of the system, including the physical security and cybersecurity of the system" that each covered system's ERP references |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, and lets 126 water systems in four states, plus acquired systems, work from one set of rules.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.4: all remote OT access through the gateway, approved before the session connects | POL-01: board safety, environmental, and risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.3: vendor sessions limited to 8 hours; phishing-resistant MFA for integrators | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.4: how to open, use, and reseal a control room emergency account | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | AWWA cybersecurity guidance used by OT engineering for implementation detail | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation or a primacy agency rule is stricter than a standard, the stricter rule applies. Plant-level operating procedures (for example, manual-mode procedures for each chemical) are maintained by operations under STD-03.3 and the ERP.

## 3. Document inventory
The set has 5 policies, 20 standards, and 13 procedures. Policy statements: 55 (34 map to controls tested in the 2026 independent assessment; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Safety, environmental, and risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and OT Vendor Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard (IT and OT) | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard (including PLC logic) | Standard | Set by CISO | CISO |
| STD-01.6 OT Asset Lifecycle and Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard (plants and remote sites) | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 OT Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Acquisition Security Integration Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 OT Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Control Room Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Notification Standard (public notice, release reporting, breach, SEC) | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency, Manual Operation, and Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 HMI Compromise Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Tier 1 Public Notice Procedure (cyber trigger) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard (IT and OT) | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Restricted Infrastructure Information Standard | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems, Personal Devices, and Removable Media Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director of OT Security, Chief Privacy Officer, CIO, Vice President, Resilience and Emergency Management, Senior Vice President, Water Quality and Environmental Compliance, Chief Human Resources Officer, a delegate of the Chief Operating Officer (a regional operations vice president, rotating), and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation, an audit finding, an incident, an RRA or ERP review, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; operations reviews anything that could affect plant operation (no OT control may be mandated that would stop an operator from responding to an alarm).
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 5 years (POL-01 4.11).

**Acquisitions:** acquired systems adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AQ-04 to AQ-06 remote access exception below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Public health and safety exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. OT tailoring decisions that SP 800-82 Rev. 3 supports (for example, unlocked operator HMIs in staffed control rooms) are recorded in the system's tailoring record, not as exceptions.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.6 supported operating system, for 3 GCR engineering workstations and the TP-C plant historian | Isolated engineering VLAN; allowlisting in audit mode; OT monitoring; no internet path | Moderate | CISO with the Vice President, Gulf Coast Regional Operations | 2027-06-30 | R-008; POAM-008 |
| EXC-2026-017 | POL-02 4.4 remote access through the gateway, at AQ-04 to AQ-06 | Hardwired chemical feed limits; VPNs restricted to named hosts; SOC review of vendor tool logs daily; AQ-05 agent password rotated monthly | High | Executive risk committee (dated plan: POAM-001) | 2027-01-31 | R-001; R-003; POAM-001 |
| EXC-2026-020 | POL-02 4.1 named accounts, for the 22 TP-C panel HMIs | Badge-controlled reverse osmosis building; video; shift log of panel operators | Low | Vice President, Gulf Coast Regional Operations with GRC concurrence | 2026-12-31 | R-015; POAM-004 |
| EXC-2026-023 | STD-01.4 central logging, for TP-C and 11 GCR booster station HMIs | Weekly local log review by a SCADA technician | Moderate | CISO with the Vice President, Gulf Coast Regional Operations | 2027-01-31 | R-037; POAM-006 |
| EXC-2026-026 | STD-04.1 encryption in transit, for 14 GCR RTUs on licensed radio | Local interlocks; OT monitoring of the radio master; licensed frequency | Low | Director of Network Engineering with GRC concurrence | 2027-12-31 | R-012; POAM-011 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- Acquired systems with open exceptions more than 12 months after closing (target: 0)
