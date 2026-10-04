# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (Qualified Individual; chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Safeguards Rule | 16 CFR 314.3(a) (written information security program); 314.4(g) (evaluate and adjust) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. Together, these documents are the **written information security program** required by the FTC Safeguards Rule (16 CFR 314.3(a)). The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.6: access disabled the same business day as termination, including adjunct contract ends | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: 14-character minimum workforce passwords; FIDO2 keys for privileged users | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how the help desk verifies identity before an MFA reset | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for faculty on safe use of course announcements | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation is stricter than a standard (for example, a state law), the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 22 standards, and 15 procedures. Policy statements: 57 (41 cite at least one control that Internal Audit tested in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Board risk committee (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging and Monitoring Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Qualified Individual Board Report Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification and Partner Attestation Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 Identity Verification for MFA Reset and Account Recovery Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Ransomware Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Refund Fraud Response Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Records Retention Schedule | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.5 FAFSA and Federal Tax Information Use Standard | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Data Use Register Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| PRC-04.2 FERPA Disclosure Recording Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.4 LTI Tool Review Standard | Standard | Set by Chief Human Resources Officer | CISO |

**Safeguards Rule element map.** Each 314.4 element has a home in the hierarchy, so the compliance auditor can trace it:
| Element | Where it lives |
|---|---|
| (a) Qualified Individual | POL-01 4.2 |
| (b) Risk assessment | POL-01 4.3, 4.4; STD-01.1 |
| (c) Safeguards | POL-02; POL-04; POL-05; STD-01.4, STD-01.5, STD-04.1, STD-04.4 |
| (d) Testing and monitoring | POL-01 4.9; STD-01.2 |
| (e) Personnel and training | POL-05 4.3; STD-05.1 |
| (f) Service providers | POL-01 4.8; STD-01.3 |
| (g) Evaluate and adjust | POL-01 4.5, 4.6; this document section 4 |
| (h) Incident response plan | POL-03; STD-03.1 to STD-03.3; PRC-03.1 to PRC-03.4 |
| (i) Report to the board | POL-01 4.12; PRC-01.4 |
| (j) FTC notification | POL-03 4.5; STD-03.2 |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, University Registrar, Vice President, Financial Aid, Provost and Chief Academic Officer (or delegate), Chief Human Resources Officer, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation, an FSA announcement or audit finding, an incident, a new service line or partner, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Chief Privacy Officer reviews anything touching student data.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce, including adjunct faculty at each new contract, attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**New service lines and partners:** each new SL-2 partner or SL-1 product adopts the hierarchy before launch. Where it cannot comply yet, the business owner files an exception with a dated plan.

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Title IV eligibility and student fraud exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception to the encryption or MFA elements of the Safeguards Rule (314.4(c)(3) and (c)(5)) is valid only if the Qualified Individual also approves the compensating or equivalent control in writing.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-007 | STD-01.5 supported operating system baseline, for the legacy document imaging system | Segmented VLAN; EDR; no internet access; weekly local log review | Moderate | CISO with the CIO | 2027-06-30 | R-007; POAM-008 |
| EXC-2026-011 | POL-02 4.4 MFA for every individual, for student accounts during the rollout | Bot detection; breached-password checks; MFA for aid offers; manual review of bank changes over $5,000; daily bank-change reconciliation. **Not a Qualified Individual approval of equivalent controls under 314.4(c)(5)**; the gap stays open in P03 G-017 | High | Executive risk committee (dated plan: POAM-002) | 2026-12-15 | R-003; POAM-002 |
| EXC-2026-015 | STD-01.4 SIEM onboarding, for the SAIG transmission software and the imaging system | Weekly manual review of local logs by Security Operations | Moderate | CISO with the Vice President, Financial Aid | 2026-12-31 | R-054; POAM-009 |
| EXC-2026-018 | POL-04 4.6 disposal of customer information, until the records schedule is approved | Encryption at rest; access limited to records staff; no new copies outside the SIS | Moderate | CISO with the Chief Privacy Officer | 2027-06-30 | R-020; POAM-010 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter and in the Qualified Individual's annual report.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate, including adjuncts at contract start (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
