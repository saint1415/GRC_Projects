# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Payouts, LLC, which adopted this program under 23 NYCRR 500.2(d)) |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-08; POL-01 approved by the board risk and technology committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory basis | PCI DSS 12.1 (policy established, reviewed annually) and the "x.1" requirement in each PCI DSS principal requirement; 23 NYCRR 500.3 (written policies approved at least annually by a senior officer or the senior governing body); 16 CFR 314.4 (written information security program) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. One hierarchy serves PCI DSS, the FTC Safeguards Rule, Part 500 for the payouts subsidiary, and the sponsor banks' due diligence.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.4: MFA for any individual accessing any information system | POL-01: board risk and technology committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: 12-character minimum passwords; FIDO2 keys for privileged users | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-03.3: how to make and record the 4-hour bank notice determination | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure coding tips for payment page developers | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a rule or contract is stricter than a standard (for example, a card brand rule or a sponsor agreement), the stricter rule applies.

**Part 500 coverage.** 500.3 lists 15 areas the policies must address. Each area maps to at least one statement: information security (POL-01), data governance, classification, and retention (POL-04), asset inventory and end of life (POL-01 4.13), access controls (POL-02), BCDR (POL-03 4.9), systems operations and availability (STD-03.3), systems and network security and monitoring (STD-01.4, STD-01.5), awareness and training (POL-05 4.2), application security and development (STD-01.5), physical security (STD-01.7), customer data privacy (POL-04), vendor management (POL-01 4.8), risk assessment (POL-01 4.3), incident response and notification (POL-03), and vulnerability management (STD-01.5).

## 3. Document inventory
The set has 5 policies, 22 standards, and 16 procedures. Policy statements: 54 (31 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Board risk and technology committee (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard (including PCI DSS targeted risk analyses) | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging and Monitoring Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration, Vulnerability, and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 PCI DSS Scope Management Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Quarterly PCI DSS Review Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.4 Merchant and Partner Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Regulatory and Contractual Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Payment Environment Compromise Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Bank Service Provider Notice Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 NYDFS Notice and Annual Filing Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.5 Ransomware Response Runbook | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Data and Analytics Officer | Executive risk committee |
| STD-04.1 Encryption and Key Management Standard | Standard | Set by Chief Data and Analytics Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Data and Analytics Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Data and Analytics Officer | CISO |
| STD-04.4 Data Retention Standard | Standard | Set by Chief Data and Analytics Officer | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Data and Analytics Officer | Owning director (under POL-04) |
| PRC-04.2 PAN Discovery and Unexpected PAN Procedure | Procedure | Chief Data and Analytics Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |
| PRC-05.1 Contact Center Card Data Handling Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-05) |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Compliance Officer, CIO, CTO, Chief Data and Analytics Officer, Chief Human Resources Officer, General Counsel's delegate, PCI Program Director, and the President of Cris Santos Payouts, LLC (for Part 500 matters). The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new rule or card brand requirement, an audit or ROC finding, an incident, a new sponsor bank, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the PCI program office confirms PCI DSS coverage.
4. **Approve:** at the level in section 2. The approval meets 500.3 for the subsidiary because the executive risk committee includes its senior officers and POL-01 goes to the board committee.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring, the PCI DSS quarterly reviews (12.4.2), and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept at least 5 years (POL-01 4.11).

**New sponsor banks and acquisitions:** a new bank program or acquired business adopts the full hierarchy on the day it starts. Where it cannot comply yet, the owner files exceptions with a dated plan.

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Exceptions that leave an ER-04 or ER-06 risk at Moderate or above need a dated treatment plan.

**Regulatory alternatives recorded as exceptions.** Some rules let an officer approve alternatives in writing: the Qualified Individual for MFA (16 CFR 314.4(c)(5)) and encryption (314.4(c)(3)); the CISO for MFA (500.12(b)), EDR and centralized logging (500.14(b)), encryption at rest (500.15(b)), and blocking common passwords (500.7(c)(2)). The CISO holds both roles, so one signed exception record can serve both rules when it names each one. PCI DSS has no such waiver; a PCI DSS gap stays a gap until the QSA accepts a control.

**Limits:** 12 months maximum; renewals need fresh approval. Part 500 compensating control approvals are reviewed at least annually, as the rule requires.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, rules whose written-approval provision it uses, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.5 supported operating system baseline, for 12 midrange settlement servers | Segmented settlement zone; EDR; application allow-listing; added network detection; no internet access | High | Executive risk committee | 2027-06-30 | R-005; POAM-001 |
| EXC-2026-017 | POL-02 4.4 MFA, for about 340 settlement operators on mainframe sessions | Sign-in only from badge-controlled settlement rooms; account lockout; session monitoring by the Cyber Fusion Center. Signed by the CISO on 2026-09-04 as the written approval under 500.12(b) and, as Qualified Individual, under 314.4(c)(5) | Moderate | CISO with the Senior Vice President, Settlement and Treasury Operations | 2026-12-31 | R-026; POAM-004 |
| EXC-2026-019 | STD-01.4 EDR coverage, for the 4 MFT appliances | Network detection on the MFT segments; egress allow-listing; daily integrity check of appliance configuration. Signed by the CISO on 2026-09-04 as the written approval under 500.14(b) | Moderate | CISO with the Director of Settlement Systems | 2027-06-30 | R-003; POAM-009 |
| EXC-2026-022 | POL-02 4.9 vendor access through PAM, for the mainframe vendor | Account limited to the vendor's IP ranges; Cyber Fusion Center alert on every session | Moderate | CISO with the Director of Settlement Systems | 2026-12-31 | R-028; POAM-015 |
| EXC-2026-025 | STD-04.1 encryption of internal transfers, for 2 batch transfers inside DC-1 | Segmented settlement zone; files carry truncated PAN only | Low | Director of Settlement Systems with GRC concurrence | 2027-03-31 | R-032; POAM-017 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk and technology committee sees a count of open exceptions by residual risk each quarter. The QSA receives the register before ROC fieldwork.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- PCI DSS quarterly review completion (target: 4 of 4 quarters)
