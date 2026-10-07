# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (holding company, Global Business Services, and all subsidiaries) |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-14 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Also supports | Finance's written information security program (16 CFR 314.3(a)); the Item 106 description of risk management processes |

## 1. Purpose
Define how the group's security documents fit together, who approves each level, how they are kept current, how subsidiaries adopt them, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.5: no credential reset without verified identity proofing | POL-01: risk committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: FIDO2 keys for privileged users and payment approvers | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how the service desk verifies identity before a reset | Owning director | Annually or when the process changes |
| **Subsidiary supplement** (optional) | Extra requirements for one subsidiary's regulator or operations | Finance WISP annex; Manufacturing OT annex | Subsidiary President with the CISO | Annually |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure meeting tips for deal teams | Owning director | As needed |

**Rules:**
- A lower level may add detail but may not weaken a higher level.
- Every standard and procedure names its parent policy and statement.
- **Group policies apply to every subsidiary.** A subsidiary may add a supplement but may not adopt a weaker rule. Finance's WISP (16 CFR 314.3(a)) is the group policy set plus the Finance annex.
- Where a regulation is stricter than a standard (for example, a state law or the Safeguards Rule for Finance), the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 22 standards, 15 procedures, and 2 subsidiary supplements. Policy statements: 53 (31 map to controls Internal Audit tested in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 OT Security Standard | Standard | Set by CISO with the Director of OT Security | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Acquisition Cyber Diligence and Integration Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification, Authentication, and Account Recovery Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Identity-Verified Credential Reset Procedure (service desk) | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach and Regulatory Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Shared-Services Compromise Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations, with the General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State and Regulatory Notification Procedure | Procedure | Director of Security Operations, with the General Counsel | Owning director (under POL-03) |
| PRC-03.4 Payment Fraud Response and Bank Recall Procedure | Procedure | Director of Security Operations, with the Treasurer | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Records Retention Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.5 Sensitivity Labeling Standard | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 MNPI and Deal Room Handling Procedure | Procedure | Chief Privacy Officer, with the General Counsel | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer, with the AI governance committee | CISO |
| PRC-05.1 Payment Instruction Verification (Callback) Procedure | Procedure | Chief Human Resources Officer, with the Treasurer | Owning director (under POL-05) |
| SUP-FIN Finance WISP annex | Subsidiary supplement | Finance Information Security Officer | Finance President with the CISO |
| SUP-MFG Manufacturing OT annex | Subsidiary supplement | Director of OT Security | President, Manufacturing with the CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Human Resources Officer, General Counsel's delegate, Chief Accounting Officer, and the four subsidiary BISOs. The Finance Information Security Officer attends for anything touching Finance customer information. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation, an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Chief Privacy Officer reviews anything touching personal information or plan PHI; the Chief Accounting Officer reviews anything touching SOX controls.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**Acquisitions:** acquired businesses adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (PRC-01.4), as for AQ-01 and AQ-02 below.

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems, entities, and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Plant-safety exceptions at High or above are refused without a dated treatment plan. Exceptions that touch Finance customer information also need the Finance Information Security Officer's written agreement, and exceptions to MFA for Finance systems need the Qualified Individual's written approval of equivalent controls (16 CFR 314.4(c)(5)).

**Limits:** 12 months maximum; renewals need fresh approval.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, entity, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | STD-02.2 phishing-resistant MFA, for 448 privileged accounts still on push MFA | Number matching; PAM session approval; conditional access limited to managed devices | Moderate | CISO with the CIO | 2027-03-31 | R-002; POAM-002 |
| EXC-2026-034 | POL-02 4.6 same-day disablement, at AQ-01 and AQ-02 | Daily HR report reconciliation by the GBS service desk | Moderate | CISO with the Vice President, Integration Management Office | 2027-01-31 | R-012; POAM-003 |
| EXC-2026-037 | STD-01.8 supported operating systems, for 140 OT components | Segmented control networks at Plants 1 and 2; no internet access; passive monitoring | Moderate | CISO with the President, Manufacturing | 2027-09-30 | R-039; POAM-014 |
| EXC-2026-040 | POL-04 4.7 payment files only through the hub, for 3 local bank portals | Bank-side dual approval; Treasurer's daily review of local portal activity | Moderate | CISO with the Treasurer | 2027-03-31 | R-003; POAM-008 |
| EXC-2026-042 | STD-01.4 SIEM onboarding, for the AQ-01 and AQ-02 directories | Weekly manual review of privileged group changes by the Security Operations team | Moderate | CISO with the Vice President, Integration Management Office | 2027-01-31 | R-047; POAM-009 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk and subsidiary each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk and subsidiary, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
