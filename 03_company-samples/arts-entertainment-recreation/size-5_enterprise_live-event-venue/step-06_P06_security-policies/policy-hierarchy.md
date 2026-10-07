# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| PCI DSS v4.0.1 | Requirement 12.1 and the "processes documented, roles assigned" requirement (x.1) that opens Requirements 1 to 11 (N71-R04) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy keeps the five policies short and stable while standards and procedures carry the detail that changes more often, such as the payment page script rules and the fee display rules.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.5: access removed the same business day a workforce member leaves | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.8: every script on a payment page has an owner, a business justification, and an integrity hash | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-03.4: what to do when card numbers turn up in case notes | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting a tampered card reader | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation, card brand rule, or contract is stricter than a standard (for example, a state breach law or a client notice term), the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 23 standards, and 14 procedures. Policy statements: 58 (40 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard (including targeted risk analyses) | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 Payment Page and Checkout Template Standard | Standard | Set by CISO with the Chief Technology Officer | CISO |
| STD-01.9 Pricing and Fee Display Standard | Standard | Set by CISO with the General Counsel and the Chief Marketing Officer | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 PCI DSS Scope Confirmation Procedure | Procedure | Director of Payments and PCI Compliance | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.4 Client User and API Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach, Card Brand, and Client Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Ticketing Platform Breach Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations, with the General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State and Client Notification Procedure | Procedure | Director of Security Operations, with the Chief Privacy Officer | Owning director (under POL-03) |
| PRC-03.4 Card Data Found in Unexpected Places Procedure | Procedure | Director of Payments and PCI Compliance | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection, Retention, and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Phone Payment Handling Standard | Standard | Set by Chief Privacy Officer with the Director of Payments and PCI Compliance | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer with the AI governance committee | CISO |
| PRC-05.1 Card Device Inspection Procedure | Procedure | President, Venue Operations | Owning director (under POL-05) |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, Chief Technology Officer, Director of Payments and PCI Compliance, Chief Human Resources Officer, General Counsel's delegate, and the President, Venue Operations. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or PCI DSS version, a QSA or audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver (a PCI DSS requirement, a statute, or a rule).
3. **Review:** the committee reviews; Legal reviews regulatory and pricing statements; the Privacy Officer reviews anything touching patron data; the Director of Payments and PCI Compliance confirms PCI DSS statements still meet the standard.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually and seasonal staff each season (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring, the annual Internal Audit plan (P07), and the QSA's testing.
7. **Retire or revise:** superseded versions are kept at least 3 years (POL-01 4.11).

**Acquisitions:** acquired venues adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AV-01 to AV-06 exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Safety and card data exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception from a PCI DSS-derived statement does not change PCI DSS: the requirement stays in the Report on Compliance and needs a compensating control the QSA accepts, or it is reported as not in place.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.5 supported operating system baseline, for about 150 AV-01 to AV-06 POS terminals | Interim access lists isolating terminals from office PCs; application allow-listing; daily SOC review of AV firewall logs; weekly reader inspections | Moderate | CISO with the Vice President, Integration Management Office | 2027-03-31 | R-031; POAM-001 |
| EXC-2026-017 | POL-02 4.5 same-day access removal, at AV-01 to AV-06 | Daily HR report reconciliation by the enterprise service desk | Moderate | CISO with the Vice President, Integration Management Office | 2027-01-31 | R-057; POAM-011 |
| EXC-2026-020 | POL-02 4.3 MFA for client users of the client console | Risk-based login throttling; tenant isolation; export logging; MFA offered to every client | High | Executive risk committee | 2027-01-31 | R-005; POAM-004 |
| EXC-2026-023 | STD-01.4 SIEM onboarding, for venue OT and AV POS terminals | Weekly review of venue firewall logs; OT changes only with integrator escorts | Moderate | CISO with the President, Venue Operations | 2027-03-31 | R-034; POAM-012 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more; seasonal staff before first shift)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
