# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory drivers | SP 800-171 R2 requirements that call for documented policies and the SSP (3.12.4) in the FSCE; FAR 52.204-21; DFARS 252.204-7012(b) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. CMMC assessors accept only final, approved documents as evidence (32 CFR 170.24(b)(1)), so the approval and version rules below also protect the FSCE certification.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.1: shared accounts are prohibited, including kiosk accounts | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.3: reseller API credentials expire within 24 hours and rotate at least every 90 days | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-04.2: how to contain, purge, and report a CUI spill | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting lookalike supplier domains | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation or contract clause is stricter than a standard (for example, a DFARS reporting clock), the stricter rule applies. The FSCE CMMC SSP may add enclave-specific requirements but may not relax enterprise policy.

## 3. Document inventory
The set has 5 policies, 21 standards, and 15 procedures (41 documents). Policy statements: 57 (41 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | Director of Security Operations | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Vice President, Enterprise Applications | CISO |
| STD-01.6 Maintenance Standard | Standard | CIO | CISO |
| STD-01.7 Physical Security Standard | Standard | Vice President, Corporate Security and Facilities | CISO |
| STD-01.8 Supply Chain and Product Integrity Standard (C-SCRM plan) | Standard | Chief Supply Chain Officer | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | Vice President, Enterprise Applications | Owning director (under POL-01) |
| PRC-01.4 Product Authentication Procedure | Procedure | Director, Product Authentication Lab | Owning director (under POL-01) |
| PRC-01.5 Section 889 and Kaspersky Screening Procedure | Procedure | Director, Government Contracts | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Remote, Vendor, and API Access Standard | Standard | Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Director of Security Operations | CISO |
| STD-03.2 Breach and Federal Reporting Standard | Standard | Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | CIO | CISO |
| PRC-03.1 Supplier Compromise Runbook (P08) | Procedure | Director of Security Operations with the Chief Supply Chain Officer | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-03) |
| PRC-03.4 Federal Incident and Covered Equipment Reporting Procedure | Procedure | Director, Government Contracts | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Director of Cloud Platform Engineering | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Vice President, Lifecycle Services | CISO |
| STD-04.3 Backup Standard | Standard | Director of Cloud Platform Engineering | CISO |
| STD-04.4 CUI and FCI Handling Standard | Standard | Director, CMMC Program Office | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Data and Analytics Officer | Owning director (under POL-04) |
| PRC-04.2 CUI Spill Procedure | Procedure | Director, CMMC Program Office | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Director of Endpoint Engineering | CISO |
| STD-05.3 Approved AI Tools List | Standard | Chief Data and Analytics Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Supply Chain Officer, Chief Human Resources Officer, Director, CMMC Program Office, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or contract clause, an audit or C3PAO finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the CMMC Program Office reviews anything that touches the FSCE or the FCI scope.
4. **Approve:** at the level in section 2. Only approved, final versions are published (drafts are not evidence for CMMC).
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.11).

**Acquisitions:** acquired companies adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AQ-1 exception below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High).

**Limits:** 12 months maximum; renewals need fresh approval. **No exception is possible** for CUI outside the FSCE, a shared account in the enterprise FCI scope, or a covered manufacturer's product on a federal order, because those are contract and regulatory requirements, not company choices.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.5 supported operating system baseline, for 112 OT HMIs and engineering workstations | Segmented OT networks at FL-2, GA-1, TX-1; no internet access; hardware safety interlocks | Moderate | CISO with the Vice President, Distribution Operations | 2027-06-30 | R-014; POAM-009 |
| EXC-2026-017 | POL-02 4.10 API credential rotation, for about 430 reseller integrations | WAF rate limits; IP allow lists for 40% of integrations; order anomaly review | Moderate | CISO with the Vice President, E-commerce | 2027-03-31 | R-013; POAM-011 |
| EXC-2026-022 | POL-02 4.5 and STD-01.4 SIEM onboarding, for the AQ-1 legacy directory and ERP | Daily HR reconciliation; weekly local log review by the AQ-1 IT lead | Moderate | CISO with the Vice President, Integration Management Office | 2027-03-31 | R-044; R-050; POAM-002; POAM-013 |
| EXC-2026-026 | POL-02 4.9 always-on vendor tools, for OT vendors at OH-1 and TX-1 | Tools disabled outside scheduled maintenance windows by the site OT lead; SOC alerting on tool sessions | High | Executive risk committee | 2026-12-31 | R-015; POAM-008 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more, including temporary workers)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
