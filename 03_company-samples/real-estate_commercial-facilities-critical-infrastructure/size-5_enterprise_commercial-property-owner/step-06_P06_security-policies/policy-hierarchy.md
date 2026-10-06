# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory drivers | CPG 2.0 goal 1.B (C-COMMERCIAL-FACILITIES-R05); PCI DSS Req. 12.1 (C-COMMERCIAL-FACILITIES-R01); 11 CCR 7123(b)(1), which asks the cybersecurity auditor to assess the written program documentation (C-COMMERCIAL-FACILITIES-R03) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, including the OT detail that differs between BAS platforms.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.9: all vendor and remote access to OT systems goes through the OT remote access gateway | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.4: integrator sessions approved by the chief engineer on duty, recorded, and kept 1 year | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how a lobby officer verifies and issues a tenant credential | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting tailgating without stereotyping | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a law is stricter than a standard (for example, a state retention or notice rule), the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 24 standards, and 14 procedures. Policy statements: 55 (36 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 OT Security Architecture Standard | Standard | Set by Director of OT Security | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure (including emergency OT changes) | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.4 OT Account and Remote Access Standard | Standard | Set by Director of OT Security | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Tenant Credential Lifecycle Procedure | Procedure | Vice President, Corporate Security | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach and Disclosure Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.4 OT Incident and Degraded-Mode Operations Standard | Standard | Set by Director of OT Security | CISO |
| PRC-03.1 BAS Ransomware Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations, with the General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations, with the Chief Privacy Officer | Owning director (under POL-03) |
| PRC-03.4 Tenant and Contractual Notice Procedure | Procedure | Director of Security Operations, with the Vice President, Leasing | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Retention Schedule | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.5 Card Handling Standard | Standard | Set by Chief Accounting Officer | CISO |
| PRC-04.1 CPPA Risk Assessment Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Information Officer | CISO |
| PRC-05.1 POI Terminal Inspection Procedure | Procedure | Chief Accounting Officer | Owning director (under POL-05) |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director of OT Security, Chief Privacy Officer, CIO, Senior Vice President, Engineering, Vice President, Corporate Security, Chief Human Resources Officer, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer and does not draft or recommend content, which keeps Internal Audit independent for the P07 assessment and the CPPA cybersecurity audit (11 CCR 7122(a)(2)). This rule was adopted in 2026 after Internal Audit had advised on the 2025 OT security standard (P03 G-070).

**Lifecycle:**
1. **Request:** triggered by the annual review, a new rule (for example the 2026 CPPA regulations), an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Chief Privacy Officer reviews anything touching personal information; engineering reviews anything that can affect building operations.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.1); integrators attest to STD-02.4 before gateway access.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**Acquisitions:** acquired properties adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the Platform C and Integrator C exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Occupant-safety exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.5 supported OS baseline, for 19 Platform C servers, 23 Platform C workstations, and 31 Platform B workstations | Interim access lists; no internet access; weekly manual log review at sampled sites; replacement funded | High | Executive risk committee | 2027-06-30 | R-006; POAM-007 |
| EXC-2026-017 | POL-02 4.9 (no always-on vendor tools), for Integrator C at the 19 acquired properties | Tool restricted to two subnets; property staff watch the tool console; weekly session review; removal date fixed | High | Executive risk committee | 2026-11-30 | R-003; POAM-003 |
| EXC-2026-022 | POL-02 4.5 same-day disablement, for local OT accounts at Platform B and C | Weekly reconciliation of local accounts with HR terminations | Moderate | CISO with the Senior Vice President, Engineering | 2027-01-31 | R-004; POAM-001 |
| EXC-2026-026 | STD-01.4 OT log onboarding, for Platform B, Platform C, and the legacy PACS | Weekly manual log review at sampled sites; passive monitoring where installed | Moderate | CISO with the Senior Vice President, Engineering | 2027-06-30 | R-008; POAM-005 |
| EXC-2026-031 | POL-04 4.2 encryption in transit, for BACnet traffic inside OT zones | Zone isolation with deny-by-default conduits | Low | Director of OT Security with GRC concurrence | 2027-06-30 | R-048 (accepted) |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more; 98.4% in 2026)
- Integrator attestation to STD-02.4 before gateway access (target: 100%)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
