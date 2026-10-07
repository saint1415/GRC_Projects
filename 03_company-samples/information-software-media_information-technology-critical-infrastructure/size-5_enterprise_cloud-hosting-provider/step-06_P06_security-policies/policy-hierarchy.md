# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-08 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory drivers | FedRAMP (C-IT-R01): the "-1" controls in the Class C and Class D lists, and the Security Decision Record rules for recording decisions (SDR-CSO-FRR); HIPAA 164.316 (business associate); SOC 2 CC5.3 (P09) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy keeps the five policies short and stable while standards and procedures carry the detail that changes more often. It serves three audiences with one set of documents: FedRAMP (FR-1 and FR-2), SOC 2 examinations for three service lines (P09), and the company's own engineering teams.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-01 4.10: every fleet automation release approved by two people from teams other than the author | POL-01: risk and technology committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.9: guest-agent releases go to 1% of enrolled VMs for 24 hours before wider rollout | CISO | Annually or when technology or a FedRAMP rule changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-01.4: how a second approver verifies and signs a release | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure coding tips for AI-assisted code | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation or a FedRAMP rule is stricter than a standard, the stricter rule applies, and the standard is updated within 30 days.

## 3. Document inventory
The set has 5 policies, 22 standards, and 14 procedures. Policy statements: 54 (40 tested by Internal Audit in 2026 through the controls they implement; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk and technology committee of the board |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment, Authorization, and FedRAMP Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and Supply Chain Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration, Change, and Vulnerability Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 Landing Zone and G1 Enclave Standard | Standard | Set by CISO | CISO |
| STD-01.9 Software Release and Provider Tooling Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Release Approval Procedure (fleet automation) | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.5 Acquisition Security Integration Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote, Privileged, and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access (Just-in-Time) Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Provider Tooling Compromise Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Customer, Bank, and Multi-State Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 FedRAMP Incident Reporting Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Cryptography and Key Management Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Sanitization Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Customer Content Handling Standard | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Customer Access Request Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Technology Officer's delegate, Chief Privacy Officer, Director of FedRAMP Compliance, Chief Human Resources Officer, General Counsel's delegate, and the Senior Vice Presidents for Government Cloud and Managed Infrastructure Services. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or FedRAMP rule version, an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the FedRAMP compliance group checks the statement against the current rules file.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring, the annual Internal Audit plan (P07), and the FedRAMP independent assessment.
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.16).

**FedRAMP rule changes:** FedRAMP publishes rules in a machine-readable file with a version number. The FedRAMP compliance group checks it monthly (last 2026-10-05, version 2026.10.05.01) and opens a policy change request when a rule affects a statement or standard.

**Acquisitions:** acquired businesses adopt the full hierarchy on the day of closing. Where they cannot comply yet, the integration lead files exceptions with a dated plan (for example, the AQ-1 identity exception below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.3): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), Chief Executive Officer and Chief Financial Officer (Very High). Exceptions that would leave a provider tooling or federal certification risk at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. For a FedRAMP offering, an exception to a FedRAMP rule or control is also recorded in the Security Decision Record with the reason and the resulting risk to customers, and may need agency notice.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | POL-02 4.3 phishing-resistant MFA, for about 180 AQ-1 technicians on the legacy directory | App-based MFA with number matching; conditional access to company networks only; daily review of RMM script runs | Moderate | CISO with the Senior Vice President, Managed Infrastructure Services | 2026-12-31 | R-015; POAM-022 |
| EXC-2026-034 | POL-01 4.10 two-person release approval, for the guest-agent channel until the workflow change ships | SOC reviews each channel release before ring 1; ring 0 limited to company-owned test VMs for 24 hours | High | Executive risk committee (dated treatment plan: POAM-001) | 2026-12-15 | R-001; POAM-001 |
| EXC-2026-037 | STD-04.1 validated modules, for two G1 services on a library update stream with validation pending | Algorithms and key lengths per STD-04.1; module under CMVP review; recorded in the FR-2 decision record | Moderate | CISO with the Senior Vice President, Government Cloud | 2027-02-28 | R-012; POAM-004 |
| EXC-2026-040 | POL-03 4.2 human approval for automated actions, for automatic isolation of crypto-mining free-tier VMs in SL-1 | Alert class limited to free-tier accounts; automatic restore on analyst reversal | Low | Director of Security Operations with GRC concurrence | 2027-06-30 | R-019; POAM-013 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the risk and technology committee of the board sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- Days from a FedRAMP rule version change to the related policy or standard update (target: 30 or fewer)
