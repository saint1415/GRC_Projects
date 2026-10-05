# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory drivers | N23-R03 (SP 800-171 R2 requires documented policies and procedures for the FPCE through its SSP, 3.12.4); N23-R04 (32 CFR 170.21(a)(2), POA&M limits that shape the exception rules); 17 CFR 229.106(b) (processes described in the Form 10-K) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often (for example, authenticator types, plan room procedures, and payee verification steps). It is the deliverable form for an Enterprise: policies, standards, procedures, and an exceptions process.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.3: no one person may both change a payee and release a payment | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: FIDO2 security keys for privileged users, payment roles, executives, and FPCE users | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-01.5: how Payment Operations verifies a bank change by call-back and records it | Owning director or officer | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting lookalike domains in owner correspondence | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation or contract is stricter than a standard (for example, DFARS 252.204-7012 for CUI, or a state breach law), the stricter rule applies. The FPCE SSP (CMMC Level 2) and the Federal Group plan room procedure (PRC-04.1) sit under this hierarchy and cite it, so a C3PAO sees one chain of authority from the board to the plan room.

## 3. Document inventory
The set has 5 policies, 22 standards, and 16 procedures. Policy statements: 57 (32 tested by Internal Audit in the 2026 PDPP assessment; see `policy-control-map.csv`). The 25 untested statements are covered by other assurance: the FPCE readiness check in P03 (for example POL-02 4.11 and POL-04 4.2), SOX testing, or are scheduled for the 2027 Internal Audit plan.

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and Subcontractor Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 Acquisition Security Integration Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director or officer (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director or officer (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director or officer (under POL-01) |
| PRC-01.4 CMMC Self-Assessment and Affirmation Procedure | Procedure | Director, CMMC Program Office | Owning director or officer (under POL-01) |
| PRC-01.5 Payee and Bank Account Verification Procedure | Procedure | Director of Payment Operations | Owning director or officer (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote, Vendor, and Client-System Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director or officer (under POL-02) |
| PRC-02.2 Access Certification Procedure (including monthly external-user review) | Procedure | Director of Identity and Access Management | Owning director or officer (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director or officer (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director or officer (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Business Email Compromise and Payment Fraud Runbook (P08) | Procedure | Director of Security Operations | Owning director or officer (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director or officer (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | General Counsel | Owning director or officer (under POL-03) |
| PRC-03.4 DoD Cyber Incident Reporting (DIBNet) Procedure | Procedure | Director of Government Contracts | Owning director or officer (under POL-03) |
| PRC-03.5 Ransomware Runbook | Procedure | Director of Security Operations | Owning director or officer (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Compliance Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.4 Payment Data Integrity Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.5 CUI Handling Standard | Standard | Set by Chief Compliance Officer | CISO |
| PRC-04.1 Controlled Plan Room Procedure (Federal Group) | Procedure | President, Federal Group | Owning director or officer (under POL-04) |
| PRC-04.2 Certified Payroll Handling Procedure | Procedure | Chief Human Resources Officer | Owning director or officer (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Compliance Officer, CIO, Chief Human Resources Officer, Vice President, Treasury, Vice President, Project Controls and Systems, Director, CMMC Program Office (for the President, Federal Group), Vice President, Building Technology Services, and a delegate of the General Counsel. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or contract clause (for example, a CMMC phase date or a final FAR rule), an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver (requirement IDs N23-R01 to N23-R04 or the statute or clause).
3. **Review:** the committee reviews; Legal reviews statements that carry a legal or contract duty; the Director, CMMC Program Office reviews anything that touches FCI, CUI, or the CMMC scopes.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); role-based attestations for standards (for example, Payment Operations for PRC-01.5, plan room staff for PRC-04.1).
6. **Monitor:** statements feed continuous control monitoring, the annual Internal Audit plan (P07), and the CMMC self-assessments (P03).
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.11), which also covers CMMC artifact retention (32 CFR 170.16(c)(4)).

**Acquisitions:** acquired businesses adopt the full hierarchy on the day of closing (POL-01 4.10; STD-01.8). Two rules apply from day one with no exception allowed: payee and bank changes go through Payment Operations (POL-01 4.13), and suspected incidents go to the SOC (POL-03 4.2). The 2026-04 AQ-1 loss happened because neither rule reached AQ-1 in time. Where an acquired business cannot comply yet with other statements, the Integration Management Office files exceptions with a dated plan (see the AQ-1 entries below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Federal eligibility (ER-03) and safety (ER-07) exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. **CMMC rule:** an exception never changes how a CMMC requirement is scored. If an exception leaves an SP 800-171 or FAR 52.204-21 requirement not met in a CMMC scope, the requirement is scored NOT MET, the Affirming Official is told the same week, and the POA&M limits in 32 CFR 170.21 apply (no POA&M at Level 1; several Level 2 requirements can never be on a POA&M). **Payment rule:** no exception may allow one person to both change a payee and release a payment.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | POL-02 4.5 same-day disablement, for AQ-1 staff on the legacy directory | Daily HR termination report reconciled by the service desk; AQ-1 accounts removed from SYS-01 and ERP groups on the HR report | Moderate | CISO with the Vice President, Integration Management Office | 2026-12-31 | R-043; POAM-014 |
| EXC-2026-016 | STD-01.4 SIEM onboarding, for the AQ-1 email tenant and ERP | Weekly SOC review of AQ-1 inbox rules and risky sign-ins from the tenant console; all AQ-1 payment files held for Payment Operations review (interim since 2026-05) | Moderate | CISO with the CFO | 2026-11-30 | R-044; POAM-004 |
| EXC-2026-022 | STD-04.4 end-to-end integrity for payment files, for bank 3 | SFTP with key pinning; positive pay; file totals reconciled to the bank acknowledgment before release; dual approval | High | Executive risk committee | 2027-01-31 | R-006; POAM-006 |
| EXC-2026-027 | STD-02.1 device management enrollment, for about 580 rugged jobsite tablets | Tablets limited to the SYS-01 field app with app-level PIN, vendor remote wipe, and no FCI download to device storage | Low | Director of Endpoint Engineering with GRC concurrence | 2027-03-31 | R-032; POAM-013 |
| EXC-2026-030 | POL-02 4.9 remote access through the gateway, for 37 client buildings whose owners mandate their own remote tools | Per-session client approval; MFA; session logs exported weekly to the SIEM; credentials rotated after each session | High (dated treatment plan to 2027-03-31) | Executive risk committee | 2027-03-31 | R-046 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter. Exceptions are disclosed to the C3PAO or a DIBCAC assessor on request; none exists for the FPCE.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more; craft workers attest through the field onboarding kiosk)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- Acquired-business statements still under exception (target: 0 by 2027-03-31)
