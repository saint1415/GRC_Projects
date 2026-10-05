# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| NERC CIP | CIP-003-9 R1 (cyber security policies approved by the CIP Senior Manager at least once every 15 calendar months) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they stay current, and how exceptions are handled. The hierarchy lets the five enterprise policies stay short and stable while standards and procedures carry the detail. It also shows how the NERC CIP documents, which have their own approval rules, sit inside the enterprise hierarchy.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.7: CIP access removed within 24 hours of a termination action | POL-01: risk and reliability committee of the board. POL-02 to POL-05: executive risk committee. CIP Cyber Security Policy: CIP Senior Manager | Annually; the CIP Cyber Security Policy at least once every 15 calendar months |
| **Tier 2: Standard** | Measurable requirements that implement a policy | OT-STD-01: OT remote access only through jump hosts or Intermediate Systems with MFA and session recording | CISO (OT standards jointly with the CIP Senior Manager) | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-03.4: DOE-417 and EOP-004 filing from the DCC and TCC | Owning director | Annually or when the process changes |
| **CIP program documents** | Plans and processes the CIP standards require (for example, the CIP-008 incident response plan, CIP-009 recovery plans, CIP-010 processes, CIP-013 supply chain plan, CIP-014 physical security plan) | CIP-013 supply chain cyber security risk management plan v4 | CIP Senior Manager or delegate where a standard requires it; otherwise the owning director | As each standard requires (for example, 15 calendar months for CIP-013-2 R3) |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure use of tablets in trucks | Owning director | As needed |

**Rules:**
- A lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement.
- Where a regulation or a NERC standard is stricter than a company document, the stricter rule applies.
- The CIP Cyber Security Policy covers the CIP-003-9 R1 topics and points to POL-01 to POL-05 for enterprise-wide rules, so a CIP auditor and an internal auditor see one consistent set.

## 3. Document inventory
The set has 5 enterprise policies, the CIP Cyber Security Policy, 20 standards, and 12 procedures, plus the CIP program documents listed in section 2. Policy statements in POL-01 to POL-05: 60 (38 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk and reliability committee of the board |
| CIP Cyber Security Policy (high, medium, and low impact sections) | Policy | Director, NERC Compliance | CIP Senior Manager |
| STD-01.1 Risk Assessment Standard | Standard | CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | CISO | CISO |
| STD-01.3 Third-Party and Supply Chain Security Standard | Standard | Director, Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | Director, Security Operations | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Director, OT Engineering | CISO |
| STD-01.7 Physical Security Standard | Standard | Director, Corporate Security | CISO |
| OT-STD-01 OT Security Standard (voluntary CIP-equivalent controls for the ADMS, OMS, and distribution substations) | Standard | Director, OT Security | CISO and CIP Senior Manager |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director |
| PRC-01.3 Change Management Procedure (IT and OT) | Procedure | CISO | Owning director |
| POL-02 Access Control Policy | Policy | Director, Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director, Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director, Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard (IT and OT) | Standard | Director, OT Security | CISO |
| PRC-02.1 Access Provisioning and Revocation Procedure (including CIP-004 timelines) | Procedure | Director, Identity and Access Management | Owning director |
| PRC-02.2 Access Certification and CIP Quarterly Verification Procedure | Procedure | Director, Identity and Access Management | Owning director |
| PRC-02.3 Privileged and Emergency Access Procedure (IT and OT PAM) | Procedure | Director, OT Security | Owning director |
| POL-03 Incident Response and Resilience Policy | Policy | Director, Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Director, Security Operations | CISO |
| STD-03.2 Notification and Disclosure Standard (NERC, DOE, SEC, state) | Standard | General Counsel's delegate | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Director, Security Operations | CISO |
| PRC-03.1 OT Intrusion Runbook (P08) | Procedure | Director, Security Operations | Owning director |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Chief Privacy Officer | Owning director |
| PRC-03.4 DOE-417 and EOP-004 Filing Procedure | Procedure | Director, NERC Compliance | Owning director |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | CISO | CISO |
| STD-04.2 Media Protection, Retention, and Disposal Standard | Standard | Chief Privacy Officer | CISO |
| STD-04.3 BES Cyber System Information Handling Standard | Standard | Director, NERC Compliance | CISO and CIP Senior Manager |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Privacy Officer | Owning director |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard (including CIP-004 training) | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 Approved AI Tools List | Standard | Chief Data and Analytics Officer | CISO |
| STD-05.3 Transient Cyber Asset and Removable Media Standard | Standard | Director, OT Security | CISO and CIP Senior Manager |
| PRC-05.1 Control Room Rules Procedure (TCC and DCC) | Procedure | Director, Transmission Operations; Director, Distribution Control Center | Owning director |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director, OT Security, Director, NERC Compliance, Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Human Resources Officer, General Counsel's delegate, and the Vice President, Distribution Operations. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new or revised NERC standard, a new regulation, an audit finding, a self-report, or an incident.
2. **Draft:** the owner drafts in the GRC platform, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the NERC compliance team reviews anything that implements a CIP requirement.
4. **Approve:** at the level in section 2. A change to a CIP-required document also goes to the CIP Senior Manager when the standard requires it.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring, the NERC internal controls program, and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept at least 7 years (POL-01 4.12), which covers NERC evidence retention.

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.5): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Safety exceptions at High or above are refused without a dated treatment plan.

**What cannot be excepted internally:**
- A NERC Reliability Standard requirement. Where a CIP requirement allows "where technically feasible," the company requests a Technical Feasibility Exception from SERC under the NERC Rules of Procedure (Appendix 4D); otherwise it must comply. CIP Exceptional Circumstances are declared under the CIP Cyber Security Policy, not through this process.
- A legal deadline (DOE-417, EOP-004, SEC, state breach law).

**Limits:** 12 months maximum; renewals need fresh approval.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | OT-STD-01 supported operating system baseline, for 22 ADMS consoles and the DCC historian | Vendor-approved EDR; no internet access; jump host allowlisting; console refresh funded | Moderate | CISO with the Vice President, Distribution Operations | 2027-06-30 | R-021; POAM-006 |
| EXC-2026-017 | STD-02.2 device authentication, for 159 legacy serial gateways | Network access lists on private LTE and radio; ADMS alarms on unexpected device state | Moderate | CISO with the Vice President, Distribution Operations | 2027-09-30 | R-006; POAM-003 |
| EXC-2026-022 | STD-04.1 encryption in transit, for DNP3 to the same legacy gateways | Same as EXC-2026-017 | Moderate | CISO with the Vice President, Distribution Operations | 2027-09-30 | R-006; POAM-003 |
| EXC-2026-026 | STD-03.3 recovery time objective, for the ADMS (2 hours) | Paper switching and radio dispatch; failover automation funded | Moderate | CISO with the Chief Operating Officer | 2027-03-31 | R-003; POAM-005 |
| EXC-2026-031 | STD-04.2 retention limits, for SSNs of closed accounts in the CIS | Field-level encryption; export rights being reduced | Moderate | CISO with the Vice President, Customer Operations | 2027-03-31 | R-055; POAM-026 |

The 12 low impact substations without CIP-003-9 Section 6 methods are **not** in the exception register: they are a potential noncompliance, self-reported and under mitigation (P03 section 4).

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the risk and reliability committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, procedures, and CIP program documents past their review date (target: 0; for CIP documents, 0 days past the 15-month limit)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
