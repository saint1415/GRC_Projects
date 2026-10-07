# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory drivers | FTC Act Section 5 (written program and accurate statements); CCPA cybersecurity audit (Cal. Code Regs. tit. 11, 7123(b)(1): documentation of the program); SEC Item 106 (processes described to investors); FedRAMP (Government Edition policies inherit from this hierarchy) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. It also gives the CCPA cybersecurity auditor, the SOC 2 service auditor, the ISO/IEC 27001 certification body, and the FedRAMP assessor one set of documents to test.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.10: no long-lived static cloud keys | POL-01: cybersecurity and risk committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.3: tenant access sessions end after 60 minutes or when the ticket closes | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.4: how a support engineer requests, uses, and closes a tenant access session | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Writing customer-facing incident updates | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation, a contract, or the Government Edition's FedRAMP package is stricter than a standard, the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 20 standards, and 14 procedures. Policy statements: 53 (34 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Cybersecurity and risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and Sub-processor Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Public Statement Review Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account and Non-Human Identity Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Tenant Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Tenant Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Customer and Regulatory Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Cloud Credential Compromise Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State and Customer Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Bank Service Provider and FedRAMP Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption and Key Management Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup and Retention Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Tenant Isolation Standard | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Customer Data Export and Interconnection Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| PRC-04.2 Tenant Offboarding and Deletion Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief People Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief People Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief People Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief People Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CTO's delegate, CIO, Chief Data and AI Officer, Chief People Officer, General Counsel's delegate, Director of Trust and Assurance, and the General Manager, Government Edition. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent; Internal Audit staff do not draft policies, standards, or procedures, which also protects the independence the CCPA cybersecurity audit requires (Cal. Code Regs. tit. 11, 7122(a)(2)).

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation, an audit finding, an incident, an acquisition, or a new public statement.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory and contractual statements; the Chief Privacy Officer reviews anything touching personal information.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**Acquisitions:** acquired companies adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AQ-01 exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Exceptions that would leave a tenant isolation or regulatory risk at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. No exception may make a public or contractual statement untrue; if an exception affects a statement, the statement is corrected first (POL-01 4.13).

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | POL-02 4.10 no long-lived keys, for 31 AQ-01 CI keys | Keys scoped to AQ-01 build accounts; weekly key-use review; build logs made private 2026-08-13 | Moderate | CISO with the Vice President, Integration Management Office | 2027-01-31 | R-002; POAM-002 |
| EXC-2026-034 | STD-01.4 SIEM onboarding, for AQ-01 cloud audit logs | Weekly export of AQ-01 audit logs to the archive account | Moderate | CISO with the Director of Security Operations | 2026-12-15 | R-051; POAM-003 |
| EXC-2026-038 | POL-02 4.10, for 9 legacy OCP deploy pipelines | Keys limited to deploy roles; rotated monthly; source restricted to CI runner addresses | Moderate | CISO with the Vice President, Platform Engineering | 2027-01-31 | R-007; POAM-002 |
| EXC-2026-041 | POL-04 4.6 backup deletion within 90 days, for Data Cloud monthly snapshots | Snapshots encrypted; restore requires two approvers; customer notice drafted | Moderate | CISO with the Chief Privacy Officer | 2027-01-31 | R-022; POAM-022 |

**Requests refused in 2026:** a request to keep the trust page statement on support access while the tool is rebuilt was refused under POL-01 4.13; the statement is being corrected instead (POAM-021).

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the cybersecurity and risk committee of the board sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- Public statements reviewed against evidence each quarter (target: 100%)
