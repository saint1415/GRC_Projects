# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| PCI DSS | 12.1 (policy established, published, reviewed); the "x.1" requirement in each of Requirements 1 to 11 (processes and roles defined) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. It also defines a separate set of **brand technology standards** that franchisees must follow, because the company is responsible for the systems it provides to them.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.5: access disabled the same business day as termination | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: 12-character minimum passwords; FIDO2 keys for privileged users | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-04.1: how to find, confirm, and purge card numbers found outside the vault | Owning director | Annually or when the process changes |
| **Brand technology standard** (franchisee-facing) | Minimum technology and security rules in the franchise system, enforced through the franchise agreement | BS-TECH-04: annual PCI DSS validation and AOC submission | Executive Vice President, Franchise Operations and Development, with the CISO | Annually |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting tampered payment terminals | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a law or PCI DSS is stricter than a standard, the stricter rule applies. Brand technology standards may not be weaker than what the company itself requires for systems it provides to franchisees.

## 3. Document inventory
The set has 5 policies, 22 standards, 12 procedures, and 6 brand technology standards. Policy statements: 58 (36 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment, Authorization, and Assessor Independence Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and Franchise Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance and Vendor Remote Support Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security and Payment Device Inspection Standard | Standard | Set by CISO | CISO |
| STD-01.8 PCI DSS Program Standard (scope, validation, targeted risk analyses) | Standard | Set by CISO | CISO |
| STD-01.9 Public Statements and Price Display Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard (workforce and franchisee accounts) | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach and Card Brand Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 POS and Reservation System Compromise Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Franchise Incident Coordination Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer (with the Director of Payments and PCI Compliance for cardholder data) | Executive risk committee |
| STD-04.1 Encryption and Tokenization Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Records Retention Schedule (guest, card, and employee data) | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Card Data Discovery and Purge Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |
| BS-TECH-01 Brand Systems Use (PMS, CRS, approved payment solutions) | Brand technology standard | Director of Franchise Technology Compliance | Executive Vice President, Franchise Operations and Development, with the CISO |
| BS-TECH-02 Franchisee User Accounts (named users, hotel administrator, quarterly attestation) | Brand technology standard | Director of Franchise Technology Compliance | Same |
| BS-TECH-03 Hotel Network Minimums (segmentation, firewall, remote access) | Brand technology standard | Director of Franchise Technology Compliance | Same |
| BS-TECH-04 PCI DSS Validation and AOC Submission | Brand technology standard | Director of Franchise Technology Compliance | Same |
| BS-TECH-05 Front Office Security Training | Brand technology standard | Director of Franchise Technology Compliance | Same |
| BS-TECH-06 Incident Reporting to the Brand | Brand technology standard | Director of Franchise Technology Compliance | Same |

BS-TECH-03 is being rewritten (POAM-012) to add technical minimums for the 230 franchised hotels that do not use the managed property network.

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Director of Payments and PCI Compliance, CIO, Chief Commercial Officer's delegate, Chief Human Resources Officer, General Counsel's delegate, Executive Vice President, Hotel Operations, and the Director of Franchise Technology Compliance. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or PCI DSS version, an audit or QSA finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory and franchise statements; the Privacy Officer reviews anything touching personal information; the Director of Payments and PCI Compliance reviews anything touching card data.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); franchisee administrators accept brand technology standards annually through the franchise portal.
6. **Monitor:** statements feed continuous control monitoring, the annual Internal Audit plan (P07), and the QSA's testing.
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**Acquisitions:** acquired hotels adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the resort exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date. If the statement maps to a PCI DSS requirement, the request must also say whether a PCI DSS compensating control worksheet is needed for the next ROC.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Card data and guest safety exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), PCI DSS compensating control worksheet reference, status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.5 supported operating system baseline, for legacy POS workstations at 6 hotels | Isolated POS segment; application allow-listing; no internet access | Moderate | CISO with the Executive Vice President, Hotel Operations | 2027-06-30 | R-048; POAM-001 |
| EXC-2026-017 | STD-02.3 vendor access through PAM, for 5 vendors at 37 hotels | Vendor tools disabled except in approved windows; hotel firewall source restriction | Moderate | CISO with the Vice President, Hotel Technology | 2026-12-31 | R-003; POAM-005 |
| EXC-2026-022 | POL-02 4.5 same-day disablement, at the 9 resorts on the seller's directory | Daily HR report reconciliation by the service desk | Moderate | CISO with the Vice President, Integration Management Office | 2027-03-31 | R-004; POAM-003 |
| EXC-2026-026 | STD-01.4 SIEM onboarding, for legacy POS servers and the resort systems | Weekly local report review by hotel controllers | Moderate | CISO with the Director of Security Operations | 2026-12-31 | R-052; POAM-011 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more); franchisee administrator acceptance of brand technology standards (target: 100%)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
