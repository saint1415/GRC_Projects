# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| SP 800-171 and CMMC | Policy basis for every family; CMMC assessors examine policies and procedures as evidence for each requirement (SP 800-171A objectives) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, such as CMMC scope rules, export attribute procedures, and the materiality playbook.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.6: access disabled the same business day as a separation, including contractors | POL-01: risk and technology committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: FIDO2 hardware security keys for every CEE user | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.4: how to set and verify export attributes when migrating PLM folders | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Safe use of prime supplier portals | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a contract clause, regulation, or DCSA requirement is stricter than a standard, the stricter rule applies. NISPOM procedures for the classified program are kept by the FSO in the standard practice procedures and follow DCSA guidance.

## 3. Document inventory
The set has 5 policies, 21 standards, and 14 procedures. Policy statements: 53 (37 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Director of Corporate Security | CISO |
| STD-01.8 CMMC Scope Management Standard | Standard | Director, CMMC Program Office | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director or officer (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director or officer (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director or officer (under POL-01) |
| PRC-01.4 CMMC Affirmation Procedure | Procedure | Director, CMMC Program Office | Owning director or officer (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director or officer (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director or officer (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director or officer (under POL-02) |
| PRC-02.4 Export Attribute Procedure | Procedure | Vice President, Trade Compliance | Owning director or officer (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Director of Security Operations | CISO |
| STD-03.2 Breach and Government Reporting Standard | Standard | Vice President, Contracts | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Director of Security Operations | CISO |
| PRC-03.1 CUI Exfiltration Runbook (P08) | Procedure | Director of Security Operations | Owning director or officer (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director or officer (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | General Counsel | Owning director or officer (under POL-03) |
| PRC-03.4 Threat Hunting Procedure | Procedure | Director of Security Operations | Owning director or officer (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Vice President, Engineering (CUI data owner), with the Vice President, Trade Compliance | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | CISO | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Director of Endpoint Engineering | CISO |
| STD-04.3 Backup Standard | Standard | Director of Cloud Platform Engineering | CISO |
| STD-04.4 CUI Marking Standard | Standard | Vice President, Engineering | CISO |
| PRC-04.1 Public Release Review Procedure | Procedure | Vice President, Trade Compliance | Owning director or officer (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | CISO | CISO |
| STD-05.3 Approved AI Tools List | Standard | Chief Data and AI Officer | CISO |
| PRC-05.1 Visitor Escort Procedure | Procedure | Director of Corporate Security | Owning director or officer (under POL-05) |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director, CMMC Program Office, Chief Information Officer, Vice President, Engineering, Vice President, Trade Compliance, Corporate Facility Security Officer, Chief Human Resources Officer, Vice President, Supply Chain, and a delegate of the General Counsel. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or contract clause, an audit or assessment finding, an incident, an acquisition, or a CMMC scope change.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53, CSF 2.0, and the SP 800-171 or CMMC requirement it supports, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; Trade Compliance reviews anything touching export-controlled data.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring, the CMMC readiness checks before each affirmation, and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.11).

**Acquisitions and new sites:** an acquired company or new site adopts the full hierarchy on the day of closing or opening. Where it cannot comply yet, the Integration Management Office or the site director files exceptions with a dated plan (for example, the KS-1 and AZ-1 exceptions below). No exception may permit CUI on a system without the required CMMC status (POL-01 4.10).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), the SP 800-171 or CMMC requirement affected (if any), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High).

**Limits:**
- 12 months maximum; renewals need fresh approval.
- An exception never removes a DFARS 252.204-7012 duty, never permits an unauthorized export, and never covers a requirement that cannot be on a CMMC POA&M (3.1.20, 3.1.22, 3.10.3, 3.10.4, 3.10.5, 3.12.4).
- An exception that leaves an SP 800-171 requirement NOT MET in a certified scope must be closed before the next affirmation; the Director, CMMC Program Office co-signs it.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, SP 800-171 or CMMC requirement affected, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.5 supported operating system, for the 2 GA-1 autoclave controllers (Specialized Assets) | Isolated segment; no remote access; chart recorders; outsourcing agreement | Low | Director of OT Engineering with GRC concurrence | 2027-06-30 | R-044 |
| EXC-2026-017 | POL-04 4.7 removable media, for loading AZ-1 printers | Labeled drive set; kiosk scan; transfer log | Moderate | CISO with the AZ-1 Site Director | 2027-01-31 | R-023; POAM-006 |
| EXC-2026-019 | POL-02 4.1, 4.5, and STD-01.4, for the KS-1 legacy environment | EDR; weekly account reconciliation; no 7021 work at KS-1; migration plan | High | Executive risk committee | 2027-03-31 | R-022; R-046; POAM-020 |
| EXC-2026-022 | POL-02 4.9 vendor access through PAM, for one AZ-1 printer manufacturer | Firewall rule to the manufacturer endpoint only; site staff present during sessions | Moderate | CISO with the Director of OT Engineering | 2026-11-15 | R-027; POAM-008 |
| EXC-2026-024 | STD-03.3 multi-region design, for the SL-2 analytics platform | Daily backups to a second region; documented rebuild | Low | Vice President, Digital Services with GRC concurrence | 2027-03-31 | P09 A1.2 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board committee sees a count of open exceptions by residual risk each quarter. Requests to excuse TX-1 visitor escort lapses were refused because 3.10.3 and 3.10.4 cannot be on a CMMC POA&M (POAM-003).

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Exceptions that affect a certified CMMC scope (target: 0 at each affirmation)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
