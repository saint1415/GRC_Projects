# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Related food safety documents | Plant HACCP plans (9 CFR Part 417), Sanitation SOPs (9 CFR Part 416), recall procedures (9 CFR 418.3), the PLT-07 food defense plan (21 CFR Part 121) and food safety plan (21 CFR Part 117) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. It also defines how security documents connect to the food safety documents that FSIS and FDA review, so that a security change and a food safety change are never approved in isolation.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.3: cure, brine, cook, and CIP parameter changes require two people | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.8: every plant has an OT DMZ; no direct cloud-to-PLC path | CISO (with the SVP FSQA for STD-04.4) | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how a vendor requests, starts, and ends an OT gateway session | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for plant supervisors on spotting social engineering | Owning director | As needed |

**Rules:**
- A lower level may add detail but may not weaken a higher level.
- Every standard and procedure names its parent policy and statement.
- Where a regulation is stricter than a standard, the stricter rule applies.
- **Food safety documents are peers, not children.** HACCP plans, SSOPs, the food defense plan, and the food safety plan are owned by FSQA under their own rules (for example, HACCP plans are signed by the responsible establishment official, and the food defense plan by the agent in charge, 21 CFR 121.310). Security documents that change how those plans are carried out (for example, PRC-01.3 OT Change Procedure or STD-04.4 Food Safety Record Integrity Standard) require SVP FSQA concurrence before approval.

## 3. Document inventory
The set has 5 policies, 22 standards, and 13 procedures. Policy statements: 57 (38 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Chief Risk Officer | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | Director of Security Operations | CISO |
| STD-01.5 Configuration and Change Management Standard (IT and OT) | Standard | Vice President, Engineering | CISO, with SVP FSQA concurrence |
| STD-01.6 Maintenance Standard | Standard | Director of OT Security | CISO |
| STD-01.7 Physical Security Standard | Standard | Vice President, Facilities and Corporate Security | CISO |
| STD-01.8 OT Security Standard (plant reference architecture) | Standard | Director of OT Security | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 OT Change Procedure (with FSQA sign-off and food defense screen) | Procedure | Vice President, Engineering | Owning director (under POL-01), with SVP FSQA concurrence |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Director of OT Security | CISO |
| STD-02.4 OT Account and HMI Access Standard | Standard | Director of OT Security | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 OT Vendor Session Procedure | Procedure | Director of OT Security | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | Deputy General Counsel, Privacy | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Vice President, Engineering | CISO |
| PRC-03.1 OT Ransomware Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Product Hold and Regulatory Notification Procedure (FSIS, FDA, EPA) | Procedure | Senior Vice President, Food Safety and Quality Assurance | Owning director (under POL-03) |
| PRC-03.4 Multi-State Breach Notification Procedure | Procedure | Deputy General Counsel, Privacy | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Deputy General Counsel, Privacy | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Director of Cloud Platform Engineering | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Vice President, Facilities and Corporate Security | CISO |
| STD-04.3 Backup Standard (IT and OT) | Standard | Director of Cloud Platform Engineering | CISO |
| STD-04.4 Food Safety Record Integrity Standard | Standard | Senior Vice President, Food Safety and Quality Assurance | CISO, with SVP FSQA concurrence |
| PRC-04.1 Formulation and Food Defense Document Handling Procedure | Procedure | Senior Vice President, Food Safety and Quality Assurance | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security and Food Defense Awareness Training Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Data science lead (for the AI council) | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director of OT Security, CIO, Vice President, Engineering, SVP FSQA, Deputy General Counsel, Privacy, Chief Compliance Officer, Chief Human Resources Officer, and the Director of Refrigeration and Process Safety. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation, an audit finding, an incident, an acquisition, or a food defense reanalysis.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the SVP FSQA reviews anything that touches CCPs, food safety records, or the food defense plan.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal and on plant kiosks in English and Spanish; workforce attest annually (POL-05 4.2); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 3 years (POL-01 4.13).

**Acquisitions:** acquired plants adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the PLT-08 exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems, plants, and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), the linked POA&M item, and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Food safety and worker safety exceptions at High or above are refused unless a dated treatment plan exists.

**Limits:** 12 months maximum; renewals need fresh approval. An exception can never waive a regulatory requirement; it can only govern how the company meets it in the meantime.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system or plant, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-01.8 supported OS baseline, for 118 HMIs and 9 engineering workstations | Application allowlisting; OT DMZ isolation; OT monitoring at 6 plants; no internet access | Moderate | CISO with the Vice President, Engineering | 2027-09-30 | R-007; POAM-004 |
| EXC-2026-017 | POL-02 4.5 remote access only through the gateway, for the PLT-05 refrigeration contractor modem | Modem powered only during supervised, scheduled sessions; hardwired ammonia detection | High | Executive risk committee (with dated plan POAM-003) | 2026-12-31 | R-006; POAM-003 |
| EXC-2026-019 | POL-02 4.1 unique identity, for the PLT-08 legacy eHACCP application and HMIs | Paper sign-off sheets for CCP checks; supervisor review each shift | Moderate | CISO with the Vice President, Integration Management Office | 2027-03-31 | R-062; POAM-007 |
| EXC-2026-022 | STD-01.4 OT log forwarding, at PLT-05 (engine room) and PLT-08 | Weekly local log review by plant controls engineers | Moderate | CISO with the Director of Security Operations | 2027-03-31 | R-028; POAM-011 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate, including plant and agency workers (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
