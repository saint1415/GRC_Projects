# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-08 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Binding requirements served | None binding for the hierarchy itself; CSF 2.0 benchmark (P03 G-017, G-018). It is the structure through which the SEC, FAR, DOE, EAR, state law, and utility addendum duties in P03 are assigned and tested |

## 1. Purpose
Define how the company's security documents fit together across IT, plant OT, and the products and services supplied to utilities; who approves each level; how documents are kept current; and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, such as OT zone rules and per-utility notice clocks.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.9: OEM remote access to plant systems only through the OT remote access gateway | POL-01: risk committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.8: OT zones and conduits per plant, deny-by-default IT/OT firewall rules, controller program backups weekly | CISO (OT standards also need the Vice President, Manufacturing Engineering) | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how the spares and services desk sends a utility access-revocation notice within 1 business day | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure travel tips for field service technicians | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation or a customer contract is stricter than a standard (for example, a utility addendum with a 24-hour incident notice term, or a state breach law), the stricter rule applies, and the obligations register (POL-01 4.11) records which rule controls.

**OT and safety precedence:** in plant control systems, a security standard never overrides a process safety requirement. Where they conflict, the Vice President, Environmental Health and Safety and the Director of OT Security agree a compensating control, recorded as an exception (section 5).

## 3. Document inventory
The set has 5 policies, 24 standards, and 15 procedures. Policy statements: 56 (37 tested by Internal Audit in 2026; see `policy-control-map.csv`).

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
| STD-01.8 OT Security Standard (zones, OT DMZs, plant changes) | Standard | Set by CISO | CISO |
| STD-01.9 Product Security and Secure Development Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Obligations Register Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard (including the OT remote access gateway) | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Utility Access-Revocation Notice Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Notification Standard (contract and regulatory notices) | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.4 OT Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Ransomware Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Plant Safe-State and Manual Operations Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Compliance Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.3 Backup Standard (including OT program backups) | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.4 Test Data and Certification Records Integrity Standard | Standard | Set by Chief Compliance Officer | CISO |
| PRC-04.1 FCI Handling Procedure | Procedure | Chief Compliance Officer | Owning director (under POL-04) |
| PRC-04.2 Export Screening Downtime Procedure | Procedure | Chief Compliance Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.4 Removable Media and Plant Floor Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Compliance Officer, CIO, Director of OT Security, Vice President, Manufacturing Engineering, Director of Product Security, Chief Human Resources Officer, Corporate Director of Quality, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or contract term (for example a new utility addendum or federal clause), an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory or contractual driver.
3. **Review:** the committee reviews; Legal reviews regulatory and contract statements; the Vice President, Environmental Health and Safety reviews anything that touches plant equipment.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal and, for production workers, through shift briefings; workforce attest annually (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.12).

**Acquisitions:** an acquired site adopts the full hierarchy on the day of closing. Where it cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AQ-01 identity, OT remote access, and logging exceptions below).

## 5. Exceptions process and register
**Who can request:** any system, process, or plant owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Process safety exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. A contract or regulatory requirement (for example a utility addendum term or a FAR clause) cannot be waived internally; the General Counsel must obtain the counterparty's written agreement.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.5 supported operating system baseline, for 148 HMIs and engineering workstations (61 at AQ-01) | Zone firewalls; application allowlisting where the OEM supports it; no internet access; passive OT monitoring at P1 to P6; funded refresh | Moderate | CISO with the Vice President, Manufacturing Engineering | 2027-06-30 | R-006; POAM-009 |
| EXC-2026-017 | POL-02 4.5 same-day disablement, at AQ-01 (legacy directory) | Daily HR termination reconciliation by the service desk | Moderate | CISO with the Vice President, Integration Management Office | 2026-12-31 | R-004; POAM-001 |
| EXC-2026-018 | POL-02 4.9 OT remote access only through the gateway, for the 5 AQ-01 OEM cellular routers | Routers powered off except during scheduled OEM sessions, with plant controls staff present and a session log; to be removed | High | Executive risk committee (process safety exception with a dated treatment plan) | 2027-03-31 | R-007; POAM-008 |
| EXC-2026-021 | STD-01.4 SIEM onboarding, for the AQ-01 legacy ERP and MES and the P3 and P4 MES application logs | Weekly manual log review by the plant IT lead; EDR on AQ-01 office endpoints (installed 2025-09) reports to the SOC | Moderate | CISO with the Director of Security Operations | 2026-12-31 | R-029; POAM-005 |
| EXC-2026-024 | POL-02 4.1 unique identities, for shared operator logins on HMIs that support only shared accounts | Badge-controlled areas; shift logs; OT monitoring of program changes | Low | Vice President, Manufacturing Engineering with GRC concurrence | 2027-06-30 | R-053 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate, including production workers through shift briefings (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%; 2026: 37 of 56)
- Obligations register entries with an owner and a tested notice template (target: 100% of utility addenda and federal clauses)
