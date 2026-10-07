# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, PT-1, RA-1, SA-1, SC-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| PCI DSS v4.0.1 (N44-45-R01) | 12.1.1, 12.1.2 (requirement numbers only) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, such as PCI DSS testing frequencies, store procedures, and technology settings. It also gives the QSA one place to confirm that PCI DSS Requirement 12.1 policy duties are met.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.5: access disabled the same business day as termination | POL-01: board risk and technology committee. POL-02 to POL-05: executive risk committee | Every 12 months |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: 14-character minimum passwords; FIDO2 keys for privileged users; POS operator PINs changed every 90 days | CISO | Every 12 months or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-03.4: how a front-end lead switches lanes to store-and-forward and issues manual SNAP EBT vouchers during an outage | Owning director | Every 12 months or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting overlay skimmers at self-checkouts | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation, card brand rule, or PCI DSS requirement is stricter than a standard, the stricter rule applies. PCI DSS targeted risk analyses (PCI DSS 12.3.1) live in STD-01.1 and set the frequencies that standards and procedures use (for example, PIN pad inspection and payment page check frequencies).

## 3. Document inventory
The set has 5 policies, 20 standards, and 14 procedures. Policy statements: 62 (42 map to a control Internal Audit tested in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard (including PCI DSS targeted risk analyses) | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and TPSP Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration, Change, and Vulnerability Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security and POI Device Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 PCI DSS Scope Confirmation Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 E-commerce Skimming Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Store Downtime and Manual EBT Voucher Procedures | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Customer Data Use and Clean Room Standard | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| PRC-04.2 Data Protection Assessment Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Digital Officer, Vice President, Payments, Chief Human Resources Officer, Senior Vice President, Store Operations, and the General Counsel's delegate. The PCI Program Manager is secretary. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or PCI DSS version, a card brand rule change, an audit or ROC finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver (for PCI DSS, the requirement number only).
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Chief Privacy Officer reviews anything touching customer personal information; the PCI Program Manager confirms the PCI DSS mapping.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal and in the store operations manual; workforce acknowledge annually (POL-05 4.1); role-based acknowledgments for standards (for example, PIN pad inspection for front-end leads).
6. **Monitor:** statements feed continuous control monitoring, the payments security council metrics, and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept at least 3 years (POL-01 4.15).

**Acquisitions:** an acquired business adopts the full hierarchy on the day of closing. Where it cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AB exceptions below). Since 2026 the deal approval must fund the integration plan (POL-01 4.16).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), the linked P01 risk and P07 POA&M item, and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Food safety exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception does not change PCI DSS: if a PCI DSS requirement cannot be met as written, the PCI Program Manager documents a compensating control worksheet for the QSA, or the requirement is reported as not in place in the ROC. An exception is a time-limited deviation while a dated treatment plan runs; it is never a risk acceptance for a risk outside tolerance.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), PCI DSS impact (yes or no), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | POL-02 4.1 no shared accounts, for the local administrator account on AB store servers | Account usable only from the store server console; password changed after each use by the AB help desk; weekly local log export reviewed by the SOC | Moderate | CISO with the Vice President, Integration Management Office | 2026-12-31 | R-018; POAM-008 |
| EXC-2026-016 | STD-01.4 SIEM onboarding, for AB store servers and the legacy directory | Weekly manual log review by the SOC; processor fraud monitoring on AB merchant IDs | Moderate | CISO with the Vice President, Integration Management Office | 2027-03-31 | R-003; POAM-009 |
| EXC-2026-018 | STD-01.5 30-day patching, for store controller vulnerabilities awaiting POS vendor certification | Payment VLAN segmentation; application allow-listing; EDR; quarterly internal scans | Moderate | CISO with the Director of Store Technology | 2026-11-30 | R-028; POAM-013 |
| EXC-2026-022 | POL-02 4.8 no always-on vendor remote tools, for two refrigeration vendors | Store firewall rules limit the tools to OT controllers; weekly session log review by Facilities Engineering; manual temperature checks | High | Executive risk committee (dated treatment plan in place) | 2026-12-31 | R-007; POAM-004 |
| EXC-2026-025 | STD-05.1 annual skimming training, for 140 AB front-end staff hired before the acquisition | Store lead inspections of PIN pads at each shift change; training scheduled with conversion wave 1 | Low | Senior Vice President, Store Operations with GRC concurrence | 2026-12-15 | R-024; POAM-014 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk and technology committee sees a count of open exceptions by residual risk each quarter; the PCI Program Manager gives the QSA the list of exceptions that touch PCI DSS scope before fieldwork.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce acknowledgment rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- PCI DSS requirements with a current targeted risk analysis where one is required (target: 100%; 8 of 11 at 2026-08, POAM-018)
