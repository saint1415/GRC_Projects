# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLP |
| Owner | CISO (Qualified Individual; chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-08; POL-01 approved by the Partnership Board, 2026-09-17 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulations | 16 CFR 314.3(a) (written program "in one or more readily accessible parts"); 45 CFR 164.316(a), (b) (business associate role) |

## 1. Purpose
Define how the firm's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. Together, the documents in this hierarchy are the firm's written information security program (WISP) under 16 CFR 314.3(a). The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. An index of all WISP parts is published on the policy portal so that every PTIN holder can find the plan they acknowledge on Form W-12.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.5: access disabled on the recorded end date for seasonal staff | POL-01: Partnership Board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: FIDO2 or platform passkeys for workforce MFA; 14-character minimum passwords | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-04.1: how to release a business return package to the offshore provider | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for spotting refund diversion requests | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation is stricter than a standard (for example, a state law or a client's business associate agreement), the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 20 standards, and 14 procedures. Policy statements: 56 (39 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Partnership Board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Acquisition Security Integration Procedure | Procedure | CISO | Owning director (under POL-01) |
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
| PRC-03.1 Business Email Compromise and Taxpayer Data Theft Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 Incident Disclosure Committee and Client-Impact Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Ransomware Runbook | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Records Retention Schedule | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 IRC 7216 Disclosure and Consent Standard | Standard | Set by Chief Privacy Officer with the National Tax Leader | CISO |
| PRC-04.1 Offshore Release Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| PRC-04.2 Disposal Run Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer with the AI governance committee | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Risk Officer, CIO, General Counsel's delegate, Chief Human Resources Officer, and delegates of the National Tax Leader, the Vice Chair, Assurance, and the Vice Chair, Advisory. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or IRS publication revision, an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; the Office of General Counsel reviews regulatory statements (IRC 7216, state law, business associate terms); the Chief Privacy Officer reviews anything touching personal information.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal with the WISP index; workforce attest annually and seasonal staff before access (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.13).

**Acquisitions:** acquired firms adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Chief Integration Officer files exceptions with a dated plan (for example, the AF-05 and AF-06 identity exception below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and Managing Partner with the CFO (Very High). Exceptions to a regulatory requirement also need the Qualified Individual's **written** approval where the regulation calls for it: an MFA alternative must be "reasonably equivalent or more secure" and approved in writing (16 CFR 314.4(c)(5)), and an encryption alternative must be an effective compensating control reviewed and approved by the Qualified Individual (314.4(c)(3)).

**Limits:** 12 months maximum; renewals need fresh approval. Exceptions that would leave a fraud (ER-05) or regulatory (ER-06) risk at High or above are refused without a dated treatment plan. No exception may permit a disclosure of tax return information that IRC 7216 does not allow.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, Qualified Individual written approval (where required), approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | POL-02 4.4 phishing-resistant authenticators, for about 8,900 non-privileged staff | Number matching; risk-based conditional access; 24x7 SOC alerting on risky sign-ins and inbox rules | High | Executive risk committee; Qualified Individual written approval 2026-09-08 | 2027-01-15 | R-001; POAM-001 |
| EXC-2026-034 | POL-02 4.4 MFA, for 9 service mailboxes still using legacy authentication | Source IP restrictions; no interactive sign-in; SOC alert on any use from new sources | Moderate | CISO with the CIO; Qualified Individual written approval 2026-09-08 | 2026-12-31 | R-024; POAM-001 |
| EXC-2026-036 | POL-02 4.5 timely disablement, at AF-05 and AF-06 (outside identity governance) | Weekly HR termination reconciliation by the acquired firms' providers, checked by the integration office | Moderate | CISO with the Chief Integration Officer | 2027-03-31 | R-003; POAM-005 |
| EXC-2026-040 | POL-04 4.3 encryption in transit, for the legacy SL-2 file transfer endpoint | IP allow lists for 12 clients; file-level encryption of every package | Low | Managing Principal, Tax Compliance Outsourcing with GRC concurrence; Qualified Individual written approval 2026-09-10 | 2027-02-28 | R-059; POAM-016 |
| EXC-2026-042 | POL-04 4.9 disposal at end of retention, deferred until after the 2027 filing season | Restricted access to records past schedule; legal hold review in progress | Moderate | CISO with the Chief Privacy Officer | 2027-09-30 | R-011; POAM-007 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the Audit and Risk Committee sees a count of open exceptions by residual risk each quarter, and the Qualified Individual's annual report to the Partnership Board lists exceptions to regulatory requirements.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more; 100% of seasonal staff before access)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
