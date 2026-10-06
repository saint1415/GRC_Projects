# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Binding rules served | Form I-9 documentation of business processes (8 CFR 274a.2(f)(1)); reasonable security measures under state law (Florida worked example: Fla. Stat. 501.171(2)) |

## 1. Purpose
Define how the firm's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. It answers P03 rows GV.PO-01 and GV.PO-02 and gives Internal Audit (P07) its test criteria.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.3: every new or changed associate bank account is confirmed out of band and held 3 days | POL-01: risk and technology committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.4: associate sign-in by passkey or app push; 3-day hold; anomaly score threshold for review | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how an Associate Service Center agent verifies a caller through the app before any change | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for recruiters on spotting fraudulent remote candidates | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a law is stricter than a standard (for example, a state's E-Verify or breach law), the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 23 standards, and 17 procedures. Policy statements: 54 (40 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Security Planning and Baseline Standard | Standard | CISO | CISO |
| STD-01.2 Risk Assessment Standard | Standard | Chief Risk Officer | CISO |
| STD-01.3 Configuration, Change, and Maintenance Standard | Standard | CIO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Director of Security Operations | CISO |
| STD-01.5 System Protection and Integrity Standard | Standard | Director of Cloud Platform Engineering | CISO |
| STD-01.6 Security Assessment and Authorization Standard | Standard | CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Vice President, Facilities | CISO |
| STD-01.8 Third-Party, Acquisition, and Supply Chain Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure (including payroll, Form I-9, E-Verify, and AI configuration) | Procedure | CIO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.4 Associate and Client Identity Standard | Standard | Senior Vice President, Payroll and Associate Services | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Associate Bank-Change and Caller Verification Procedure | Procedure | Vice President, Associate Service Center | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Director of Security Operations | CISO |
| STD-03.2 Contingency and Disaster Recovery Standard | Standard | CIO | CISO |
| STD-03.3 Breach Notification Standard | Standard | Chief Privacy Officer | CISO |
| PRC-03.1 Payroll and HR Data Breach Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-03) |
| PRC-03.4 Payroll Engine Recovery Procedure | Procedure | Vice President, Payroll Technology | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption and Tokenization Standard | Standard | Chief Privacy Officer | CISO |
| STD-04.2 Records Retention and Disposal Standard (retention schedule) | Standard | Vice President, Employment Compliance | CISO |
| STD-04.3 Media Protection Standard | Standard | Director of Network and Endpoint Engineering | CISO |
| STD-04.4 Backup Standard | Standard | Director of Cloud Platform Engineering | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| PRC-09.1 Associate Onboarding and Form I-9 Procedure | Procedure | Vice President, Employment Compliance | Owning director (under POL-04) |
| PRC-09.2 Form I-9 Correction and Reverification Procedure | Procedure | Vice President, Employment Compliance | Owning director (under POL-04) |
| PRC-09.3 E-Verify Case and Outage Procedure | Procedure | Vice President, Employment Compliance | Owning director (under POL-04) |
| PRC-09.4 Form I-9 Retention and Purge Procedure | Procedure | Vice President, Employment Compliance | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.3 Personnel Security Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.4 Approved AI Tools List | Standard | CISO, with the AI governance council | CISO |

**Numbering note.** The PRC-09 procedures belong to the employment compliance program, which is common control provider CCP-09 in the ALPP SSP (P02 section 10.3). They sit under POL-04 because they govern the handling, retention, and disposal of Form I-9 and E-Verify records. They also serve as the written description of business processes that 8 CFR 274a.2(f)(1) requires for an electronic I-9 system.

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Human Resources Officer, Vice President, Employment Compliance, Senior Vice President, Payroll and Associate Services, Chief Data Officer, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation (for example, Colorado SB26-189 from 2027-01-01), an audit finding, an incident, a fraud trend, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Chief Privacy Officer reviews anything touching Restricted data; the Vice President, Employment Compliance reviews anything touching Form I-9, E-Verify, or consumer reports.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**Acquisitions:** acquired firms adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the ACQ-1 exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Payroll integrity and patient-safety exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. No exception may waive a legal duty (for example, a Form I-9 retention period or an E-Verify MOU term); an exception can only change how the firm meets it.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | POL-02 4.2 SSO for all workforce systems, for E-Verify (DHS-managed accounts) | Named accounts; tutorial before access; monthly reconciliation to HR from 2026-10 | Moderate | CISO with the Vice President, Employment Compliance | 2026-12-31 | R-008; POAM-006 |
| EXC-2026-016 | STD-01.3 supported operating system baseline, for the DC-1 time clock server | Isolated VLAN; no internet access; firewall allows only the integration platform | Moderate | CISO with the Director of Network and Endpoint Engineering | 2027-02-28 | R-011; POAM-011 |
| EXC-2026-018 | POL-02 4.5 disablement within 4 hours, at ACQ-1 | Daily HR termination report reconciled by ACQ-1 IT from 2026-10 | Moderate | CISO with the Vice President, Integration Management Office | 2027-03-31 | R-057; POAM-002 |
| EXC-2026-022 | STD-01.4 SIEM onboarding, for ACQ-1 systems | Weekly SOC review of ACQ-1 administrator logs; EDR on ACQ-1 laptops | Moderate | CISO with the Vice President, Integration Management Office | 2026-12-31 | R-004; POAM-003 |
| EXC-2026-025 | POL-04 4.2 tokenization outside the payroll engine, for the enterprise data platform | 41 named users; query logging; no export to files; quarterly review | High | Executive risk committee | 2027-03-31 | R-003; R-048; POAM-004 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the risk and technology committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
