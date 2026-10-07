# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| NERC CIP | CIP-003-9 R1 (policies for medium impact topics in Part 1.1 and low impact topics in Part 1.2, approved by the CIP Senior Manager every 15 calendar months) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they stay current, and how exceptions are handled. The hierarchy keeps the five policies short and stable while standards and procedures carry the detail that changes more often. It also shows where each NERC CIP and FERC Security Program duty lives, so an auditor or inspector can find it.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.7: vendor remote access approved per session and able to be disabled at once | POL-01: board safety, risk, and reliability committee. POL-02 to POL-05: executive risk committee. CIP-003-9 R1 content: also the CIP Senior Manager | Annually (CIP content within 15 calendar months) |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.8: Section 9 enhanced measures for every Critical cyber asset; STD-02.3: Intermediate System settings | CISO (CIP standards also by the CIP Senior Manager or delegate) | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-03.4: how to take each river system's gates to local control | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure remote work tips for engineers | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation is stricter than a standard (for example, a CIP time limit), the regulation applies.

## 3. Document inventory
The set has 5 policies, 22 standards, and 14 procedures. Policy statements: 52 (34 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Safety, risk, and reliability committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and Supply Chain Security Standard (includes the CIP-013-2 plan) | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging and Monitoring Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 OT Security Standard (Section 9 baseline and enhanced measures) | Standard | Set by CISO | CISO |
| STD-01.9 NERC CIP Program Standard | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 OT Change Management Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 CIP Exceptional Circumstances Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management (OT identity domain: Director, OT Security) | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management (OT identity domain: Director, OT Security) | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management (OT identity domain: Director, OT Security) | CISO |
| STD-02.3 Remote and Vendor Access Standard (Intermediate Systems; CIP-005-7 R2 and R3; CIP-003-9 Section 6) | Standard | Set by Director of Identity and Access Management (OT identity domain: Director, OT Security) | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management (OT identity domain: Director, OT Security) | Owning director (under POL-02) |
| PRC-02.2 Access Verification Procedure (quarterly CIP verification) | Procedure | Director of Identity and Access Management (OT identity domain: Director, OT Security) | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management (OT identity domain: Director, OT Security) | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management (OT identity domain: Director, OT Security) | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Recovery Standard (CIP-009-6; Rapid Recovery) | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 OT Intrusion Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Regulatory Reporting Procedure (CIP-008, CIP-003 Section 4, 18 CFR 12.10, FERC, EOP-004, DOE-417) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Local Control Fallback Procedure (by river system) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Information Classification and Handling Policy | Policy | Chief Compliance Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.3 Backup and Logic Copy Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.4 CEII and BCSI Handling Standard | Standard | Set by Chief Compliance Officer | CISO |
| PRC-04.1 Restricted Information Access Authorization Procedure | Procedure | Chief Compliance Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 Removable Media, Transient Cyber Asset, and Personal Device Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools and AI Intake Standard | Standard | Set by Chief Human Resources Officer | CISO |
| PRC-05.1 Personnel Risk Assessment Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-05) |

**Where the regulatory duties live:**
| Duty | Document |
|---|---|
| CIP-003-9 R1 policy topics (medium and low impact) | POL-01 to POL-05 with STD-01.9 cross-reference table |
| CIP-003-9 R2 low impact plan (Attachment 1 Sections 1 to 6) | STD-01.9, STD-02.3, STD-05.2, PRC-03.3 |
| CIP-013-2 supply chain plan | STD-01.3 |
| FERC Cyber/SCADA Security Plan (Section 9 baseline and enhanced) | STD-01.8 plus the P02 SSP |
| FERC Security Plans, Internal Emergency Response, Rapid Recovery | Site Security Plans (outside this hierarchy, under the Vice President, Corporate Security) referencing POL-03 and PRC-03.4 |
| 18 CFR 12.10 and EAP duties | Owner's Dam Safety Program (outside this hierarchy, under the Chief Dam Safety Engineer) referencing PRC-03.3 |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Compliance Officer, Director, NERC Compliance, CIO, Senior Vice President, Hydro Operations (CIP Senior Manager) or delegate, Vice President, Dam Safety, Vice President, Corporate Security, Chief Human Resources Officer, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new or revised NERC standard (for example, the 2028 virtualization revisions), a FERC program revision, an audit or inspection finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; the NERC compliance team checks CIP wording; Legal reviews regulatory statements.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring, the NERC internal controls program, and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept for the NERC audit period and at least 7 years (POL-01 4.12).

**Acquisitions:** acquired plants adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan. A CIP requirement cannot be excepted; gaps against CIP are mitigated and, where required, self-reported (as for the Piedmont BES plants in 2026).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), confirmation from the NERC compliance team that no CIP requirement is affected, and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Public safety exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-007 | STD-01.8 supported operating system, for 64 plant HMIs and 9 gate control workstations | Dam safety zone isolation; application allowlisting; no internet or email; monthly logic comparison where copies are current | Moderate | CISO with the Senior Vice President, Hydro Operations | 2027-06-30 | R-006; R-022; POAM-005 |
| EXC-2026-011 | POL-02 4.7 and 4.8 at the 9 Piedmont plants (non-BES plants only; BES plants are handled as CIP mitigation, not exception) | Vendor connections disabled outside approved windows; firewall allow-list on the VPN concentrator; night staffing at PD-04 and PD-06 | High | Executive risk committee | 2026-12-31 | R-003; POAM-001 |
| EXC-2026-015 | POL-02 4.1 shared accounts at the Piedmont plants | Shift logs; password change after every departure; PD plants not connected to the HOC | Moderate | CISO with the Vice President, Integration Management Office | 2027-01-31 | R-033; POAM-002 |
| EXC-2026-019 | POL-03 4.11 quarterly logic copies, at 14 plants | Vendor original logic on file; change freeze on gate logic until copies are taken | Moderate | CISO with the Director, Hydro Control Systems Engineering | 2026-12-31 | R-013; POAM-008 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0; CIP content: 0 past 15 calendar months)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
