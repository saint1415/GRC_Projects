# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Contract basis | State cybersecurity exhibits (SP 800-53 Rev. 5 Moderate "-1" controls); customer security addenda |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, including the OT detail that differs by building and customer.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.9: all remote access to customer OT only through the OT remote access gateway | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.6: gateway sessions require an FSP ticket, FIDO2 MFA, and recording; 8-hour maximum | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-03.4: how to put a building into manual mode and restore it | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for working safely on customer networks | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a customer contract or law is stricter than a standard (for example a 1-hour notice for a public safety customer), the stricter rule applies to that customer, and the contract obligations register records it.

## 3. Document inventory
The set has 5 policies, 25 standards, and 17 procedures. Policy statements: 57 (30 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and Supply Chain Security Standard (including FAR 52.204-25 and FASCSA screening) | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging and Monitoring Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard (including controller programs and door schedules) | Standard | Set by CISO | CISO |
| STD-01.6 OT Remote Access and Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard (ROCs and offices) | Standard | Set by CISO | CISO |
| STD-01.8 Personnel Security Standard (including CJIS, school site, and PIV requirements) | Standard | Set by CISO | CISO |
| STD-01.9 Secure Development Standard (FSP and IBOP integrations) | Standard | Set by CISO | CISO |
| STD-01.10 Vulnerability and Patch Management Standard (IT and OT) | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Supplier Screening Procedure (Section 889, Kaspersky, FASCSA) | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.5 Subcontractor Onboarding Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Customer Console and Tenant Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged and OT Remote Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Badge Enrollment and Revocation Procedure (ROC, for customers) | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Customer and Regulatory Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 OT Intrusion Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Building Manual-Mode Procedures | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.5 Ransomware Runbook | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 CUI and Security Records Handling Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.5 Customer Data Retention Standard (cardholder, video, biometric) | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Video Evidence Export Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| PRC-04.2 Public Records Request Routing Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard (including CJIS role-based training) | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 Mobile Devices and Rugged Tablets Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.4 AI, Biometric, and Video Analytics Features Standard | Standard | Set by Chief Human Resources Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Technology Officer, Director of OT Security, Chief Human Resources Officer, Vice President, Government Contracts Compliance, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or contract type, an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory or contract driver.
3. **Review:** the committee reviews; Legal reviews regulatory and contract statements; the Privacy Officer reviews anything touching personal, student, or biometric data.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept at least 3 years, or longer where a contract requires (POL-01 4.11).

**Customer terms:** the contract obligations register (POL-01 4.14) records each customer's stricter terms (notice clocks, CJIS training, FERPA, CUI, retention schedules). Standards point to the register instead of copying 64 sets of terms.

**Acquisitions:** acquired businesses adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AQ-1 and AQ-2 exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems, buildings, and customers involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Exceptions that would leave a physical safety risk (ER-01) at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception can never waive a customer contract term or a law; where a contract term cannot be met, the segment president must notify the customer and agree a plan in writing.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, buildings and customers affected, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), customer notified (yes or no), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-022 | POL-02 4.9 (OT remote access only through the gateway) and POL-01 4.10, for the AQ-1 legacy tool at 142 sites | Agents disabled outside service windows at 61 sites; vendor relay allowlisting; weekly SOC agent inventory | High | Executive risk committee | 2027-01-31 | R-002; POAM-001 |
| EXC-2026-027 | POL-02 4.5 (same-day disablement), for AQ-1 staff on the legacy directory | Daily HR report reconciliation by the AQ-1 service desk | Moderate | CISO with the Vice President, Integration Management Office | 2026-12-15 | R-003; POAM-002 |
| EXC-2026-031 | STD-01.10 supported OS baseline, for 37 engineering workstations needed by legacy BAS tools | Application allowlisting; no internet access; USB scanning | Moderate | CISO with the Vice President, Building Technology Platforms | 2027-06-30 | R-036; POAM-016 |
| EXC-2026-034 | POL-04 4.2 (encryption in transit), for BACnet and legacy reader wiring inside customer buildings | OT VLANs where in place; OT sensors; customer upgrade recommendations | Moderate | CISO with the Director of OT Security | 2027-06-30 | R-059; POAM-018 |
| EXC-2026-036 | POL-02 4.1 (no shared accounts), for the 3 AQ-2 legacy BAS supervisory instances | Campus network isolation; change log kept by the campus lead | Moderate | CISO with the Vice President, Integration Management Office | 2027-03-31 | R-054; POAM-004 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- Customer terms in the contract obligations register with a named owner (target: 100%)
