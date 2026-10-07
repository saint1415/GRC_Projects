# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory basis | 47 CFR 64.2009(b) (training and an express disciplinary process); 64.2010(a) (reasonable measures); 47 CFR 1.20003(b) (CALEA SSI policies); 17 CFR 229.106(b) (processes described to investors) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. It also gives the CPNI certification (64.2009(e)) a documented basis: each certification statement points to the policy statements, standards, and procedures that make up "operating procedures" for CPNI.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.9: call detail only after a password not prompted by biographical information | POL-01: board risk and technology committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.8: every network element platform must support TACACS+ or be reachable only from jump hosts | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how a care agent authenticates a caller before discussing call detail | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting pretexting calls | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation is stricter than a standard (for example, a state law), the stricter rule applies. The CALEA SSI policies required by 47 CFR 1.20003 are filed with the FCC per carrier subsidiary; they sit under POL-02 4.13 and POL-03 4.6 and are kept by the Director, Lawful Intercept Compliance, with restricted distribution.

## 3. Document inventory
The set has 5 policies, 22 standards, and 17 procedures. Policy statements: 59 (38 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 Network Element Security Standard | Standard | Set by Director of Network Security Engineering | CISO |
| PRC-01.1 Sanctions Procedure (including CPNI misuse) | Procedure | Chief Human Resources Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CIO | Owning director (under POL-01) |
| PRC-01.4 CPNI Certification Evidence Procedure | Procedure | Chief Compliance Officer | Owning director (under POL-01) |
| PRC-01.5 Acquisition Security Integration Procedure | Procedure | Vice President, Integration Management Office | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.4 Customer Authentication Standard (CPNI) | Standard | Set by Chief Customer Officer | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Care Authentication Procedure | Procedure | Chief Customer Officer | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by CIO | CISO |
| PRC-03.1 CPNI Intrusion Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-03) |
| PRC-03.4 PSAP, 988, and NORS Notification Procedure | Procedure | Vice President, Network Operations Center | Owning director (under POL-03) |
| PRC-03.5 CALEA Compromise Reporting Procedure (restricted) | Procedure | Director, Lawful Intercept Compliance | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by CISO | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by CISO | CISO |
| STD-04.3 Backup Standard | Standard | Set by CIO | CISO |
| STD-04.4 CPNI Use and Approval Standard | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| PRC-04.2 Campaign Registration and Supervisory Approval Procedure | Procedure | Vice President, Marketing | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by CISO | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Data Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Network Officer's delegate, Chief Customer Officer's delegate, Chief Human Resources Officer, General Counsel's delegate, and the Director, Lawful Intercept Compliance. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or FCC order, an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal and Regulatory Affairs review regulatory statements; the Privacy Officer reviews anything touching CPNI or customer personal information.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce and vendor agents attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring, the annual Internal Audit plan (P07), and the CPNI certification evidence package (PRC-01.4).
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.11).

**Acquisitions:** acquired carriers adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan. Regulatory duties (CPNI authentication, CALEA filings, PSAP notices) are not exceptions; only the timing of the fix can be risk-accepted, with compensating controls (examples below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Public safety exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | POL-02 4.1 named accounts, for about 7,400 legacy access elements | Reachable only from jump hosts (being enforced); passwords rotated quarterly; element login alerts where logs exist | High | Executive risk committee | 2027-03-31 | R-008; POAM-002 |
| EXC-2026-017 | POL-02 4.6 same-day disablement, at AQ-02 and AQ-03 | Daily HR report reconciliation by the AQ service desks | Moderate | CISO with the Vice President, Integration Management Office | 2027-01-31 | R-004; POAM-001 |
| EXC-2026-020 | STD-01.4 SIEM onboarding, for the AQ-02 and AQ-03 legacy billing systems | Monthly manual CPNI access review by the Privacy Office | Moderate | CISO with the Chief Privacy Officer | 2026-12-31 | R-063; POAM-007 |
| EXC-2026-023 | POL-04 4.5 encryption in transit, for CDR transfers from 41 TDM switches | Management VLAN isolation; collectors accept only listed switch addresses | Low | Vice President, Billing and Revenue Assurance with GRC concurrence | 2027-06-30 | R-017; POAM-017 |
| EXC-2026-026 | STD-01.5 supported releases, for 61 TDM switches | Third-party maintenance; spares pool; management access only from jump hosts | Moderate | CISO with the Chief Network Officer | 2027-09-30 | R-025; POAM-009 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk and technology committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce and vendor agent attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- CPNI certification statements with a complete evidence package (target: 100% of carrier subsidiaries)
