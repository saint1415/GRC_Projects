# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (with Cris Santos Bank, N.A. and Cris Santos Investment Services, LLC) |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-18 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory basis | 12 CFR 30 App. B II.A (written program) and III.A (board approval); App. D II.A (written risk governance framework with delegations of authority) and II.C.1.(b) (front line unit policies) |

## 1. Purpose
Define how the group's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. It sits inside the enterprise risk governance framework that independent risk management designs and the board risk committee approves (App. D II.A).

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.11: every new wire beneficiary in treasury channels is confirmed out of band | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.4: callbacks use only the phone number on file, never one supplied in the request | CISO, with second-line review by the Director of Technology and Operational Risk | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how the callback team verifies and records a payment instruction | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting look-alike email domains | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation is stricter than a standard (for example, a state breach law), the stricter rule applies. Broker-dealer supplements (for example, the Regulation S-P notice procedure) sit under the enterprise policies and may only add requirements.

## 3. Document inventory
The set has 5 policies, 22 standards, and 13 procedures. Policy statements: 55 (37 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Board risk committee (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO with the Director of Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 Model and AI Risk Standard | Standard | Set by the Head of Model Risk Management with the Chief Data and Analytics Officer | CISO and Chief Risk Officer |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard (workforce and customer) | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.4 Payment Instruction Verification Standard | Standard | Set by Head of Payments Operations | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Callback Procedure | Procedure | Head of Payments Operations | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Cyber Defense | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Cyber Defense | CISO |
| STD-03.2 Customer and Regulator Notification Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Enterprise Resilience | CISO |
| PRC-03.1 BEC and Wire Fraud Runbook (P08) | Procedure | Director of Cyber Defense | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Notification Incident Determination Procedure | Procedure | Director of Cyber Defense | Owning director (under POL-03) |
| PRC-03.4 Destructive Attack Runbook | Procedure | Director of Cyber Defense | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Payment and Ledger Integrity Standard | Standard | Set by Chief Privacy Officer with the Head of Core Banking Technology | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Data and Analytics Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Data and Analytics Officer, Chief Human Resources Officer, the broker-dealer's Chief Compliance Officer, and General Counsel's delegate. The Director of Technology and Operational Risk attends as the second-line challenger and must sign off on any change that affects a risk limit. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or guidance (for example SR 26-2 or the amended Regulation S-P), an audit or examination finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Chief Privacy Officer reviews anything touching customer information; independent risk management reviews risk limits.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**Acquisitions:** acquired institutions adopt the full hierarchy on the merger date. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the legacy commercial platform exception below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive and second-line concurrence (Moderate), executive risk committee (High), CEO and CFO (Very High). Exceptions that would leave a regulatory or disclosure risk above Low are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception can never waive a rule's text (for example, the 36-hour notice in 12 CFR 53.3); it can only change how the bank meets it.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-027 | POL-02 4.8 privileged access through PAM, for 41 mainframe IDs | MFA at mainframe sign-in; daily forwarding of privileged command logs; weekly review by the Director of Data Center and Mainframe Operations | High | Executive risk committee | 2027-03-31 | R-007; POAM-002 |
| EXC-2026-031 | POL-01 4.10 integration within 12 months, for the acquired bank's legacy commercial platform | Daily vendor report of beneficiary changes reviewed by treasury support; callback for every new beneficiary; lower default limits | Moderate | CISO with the Vice President, Integration Management Office | 2027-02-26 | R-004; POAM-004 |
| EXC-2026-033 | POL-02 4.10 SMS only as a fallback, for consumer users not yet migrated | Risk-based authentication; SIM-swap signals from carriers; step-up for high-risk actions | Moderate | CISO with the Head of Consumer and Small Business Banking | 2027-03-31 | R-003; POAM-005 |
| EXC-2026-035 | STD-01.5 supported operating systems, for 4 core middleware servers | Vendor extended support; segmented network; EDR | Low | Head of Core Banking Technology with second-line concurrence | 2027-03-31 | R-031; POAM-008 |
| EXC-2026-038 | POL-04 4.7 isolated immutable copy of core data | DC-2 replica; virtual tape with separate administrator group; annual failover test | High | Executive risk committee | 2027-06-30 | R-002; POAM-020 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
