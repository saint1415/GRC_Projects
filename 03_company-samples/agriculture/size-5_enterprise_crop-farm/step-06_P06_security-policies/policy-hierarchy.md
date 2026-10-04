# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| OT guidance | NIST SP 800-82 Rev. 3, section 3.3.4 (OT-specific policies and procedures) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, including the OT detail for irrigation, fertigation, packing, and cold-chain systems.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.9: OT vendor access only through the OT remote access gateway | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.4: integrator sessions approved per session by the control center manager, MFA, recorded, 8-hour maximum | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-01.4: how to propose, bench-test, approve, download, and verify a PLC logic or fertigation recipe change | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for crew leads on tablet care in the field | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation or customer contract is stricter than a standard (for example, a state breach law or a retailer's 24-hour notice term), the stricter rule applies. Safety comes first in OT: no security procedure may require an action that bypasses a fertigation or chemigation interlock or leaves a freeze-protection station without a manual path.

## 3. Document inventory
The set has 5 policies, 23 standards, and 14 procedures. Policy statements: 53 (35 map to controls tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | CISO | CISO |
| STD-01.3 Vulnerability and Patch Management Standard (IT and OT) | Standard | Director of OT Security | CISO |
| STD-01.4 Audit Logging and Monitoring Standard (with the OT logging profile) | Standard | Director of Security Operations | CISO |
| STD-01.5 Configuration and Change Management Standard (with OT change control) | Standard | SCADA Engineering Manager | CISO |
| STD-01.6 Maintenance Standard | Standard | Director of OT Security | CISO |
| STD-01.7 Physical Security Standard | Standard | Vice President, Facilities and Physical Security | CISO |
| STD-01.8 Network Security and OT Segmentation Standard | Standard | Director of Network Engineering | CISO |
| STD-01.9 Third-Party and Supply Chain Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | GRC team | Owning director (under POL-01) |
| PRC-01.3 Acquisition Security Integration Procedure | Procedure | Vice President, Integration Management Office | Owning director (under POL-01) |
| PRC-01.4 OT Change Procedure (PLC logic, setpoints, fertigation recipes) | Procedure | SCADA Engineering Manager | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard (including seasonal accounts) | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Privileged Access Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.4 Remote and OT Vendor Access Standard | Standard | Director of OT Security | CISO |
| PRC-02.1 Access Provisioning Procedure (including the seasonal hiring roster) | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 OT Vendor Session Procedure | Procedure | Director of OT Security | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard (with the OT safe-state annex) | Standard | Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | Chief Privacy Officer | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Chief Information Officer | CISO |
| PRC-03.1 Ransomware Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Manual Irrigation and Freeze-Protection Procedure (one per region) | Procedure | Vice President, Irrigation and Water Resources | Owning director (under POL-03) |
| PRC-03.4 Multi-State Breach Notification Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption and Key Management Standard | Standard | Director of Cloud Platform Engineering | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Director of Endpoint and Mobility Engineering | CISO |
| STD-04.3 Backup Standard | Standard | Chief Information Officer | CISO |
| STD-04.4 Regulatory Records Integrity and Retention Standard | Standard | Chief Compliance Officer | CISO |
| PRC-04.1 Regulator Records Request Procedure (FDA, DOL, EPA) | Procedure | Chief Compliance Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 External Systems, Personal Devices, and Integrator Laptops Standard | Standard | Director of Endpoint and Mobility Engineering | CISO |
| STD-05.3 Approved AI Tools and Imagery Use Standard | Standard | Chief Risk Officer (for the AI governance committee) | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director of OT Security, Chief Privacy Officer, Chief Compliance Officer, Chief Food Safety and Quality Officer, CIO, Chief Human Resources Officer, Vice President, Irrigation and Water Resources, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation, an audit finding, an incident, an acquisition, or a new OT technology.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Director of OT Security reviews anything that touches OT for safety effects; the Chief Privacy Officer reviews anything touching personal information.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); seasonal workers attest at onboarding in English or Spanish; role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.11).

**Acquisitions:** acquired operations adopt the full hierarchy on the day of closing (PRC-01.3). Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AQ-01 and AQ-02 exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Exceptions that would leave a worker safety or food safety risk (ER-05) at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. Exceptions can never waive a binding regulatory requirement (for example, the Produce Safety record requirements or H-2A earnings records); they can only change how the company meets it.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-02.4 gateway-only OT vendor access, for INT-4 and INT-5 | Firewall rules limit each tool to named stations; SOC alert on every session start; control center manager approves by phone | High | Executive risk committee | 2026-12-31 | R-004; POAM-004 |
| EXC-2026-015 | POL-02 4.1 unique identities, for AQ-01 tally tablets | Paper tally cards countersigned by crew leads; payroll variance review | Moderate | CISO with the Vice President, Integration Management Office | 2027-02-28 | R-016; POAM-023 |
| EXC-2026-018 | STD-01.3 supported operating systems, for 31 control center HMIs | Isolated control zone; no internet route; passive OT monitoring; allowlisting planned | Moderate | CISO with the Vice President, Irrigation and Water Resources | 2027-06-30 | R-010; POAM-014 |
| EXC-2026-022 | POL-02 4.4 MFA, for the AQ-02 pivot manufacturer's cloud service | Passwords changed at closing; daily review of the pivot command log by the R6 control center; interim named accounts and MFA due 2026-11-15 | High | Executive risk committee | 2027-06-30 | R-005; POAM-002 |
| EXC-2026-025 | POL-04 4.2 encryption in transit, for legacy pivot panel protocols on the APN | Private APN with no internet route; APN firewall allows only the SCADA masters | Low | Vice President, Irrigation and Water Resources with GRC concurrence | 2027-06-30 | R-008; POAM-009 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more, including seasonal workers)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
