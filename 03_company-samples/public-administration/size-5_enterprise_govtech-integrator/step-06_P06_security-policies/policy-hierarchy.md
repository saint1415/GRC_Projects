# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Contract and regulatory basis | SP 800-53 Moderate "-1" controls required by agency contracts; CJIS Security Addendum sec. 3.01; Pub. 1075 sec. 4; 45 CFR 164.316 (AG-04 scope) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy keeps the five policies short and stable while standards and procedures carry the detail that changes more often, such as a new CJISSECPOL version or a new agency contract term.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.10: no CJI access before a fingerprint-based check, a signed certification page, and training | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: 14-character minimum passwords; security keys for privileged users; 5 failed attempts in 15 minutes | CISO | Annually, when technology changes, or within 60 days of a new CJISSECPOL version |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.5: how to arrange agency fingerprinting and track certification pages | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Writing agency fact sheets without regulated data | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where an agency contract, CJISSECPOL, Pub. 1075, or a statute is stricter than a standard, the stricter rule applies, and STD-01.8 records the contract-specific values.

## 3. Document inventory
The set has 5 policies, 21 standards, and 13 procedures. Policy statements: 52 (37 tested by Internal Audit in 2026; see `policy-control-map.csv`).

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
| STD-01.8 Regulated Data Contract Flowdown Standard | Standard | Set by CISO | CISO |
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
| PRC-02.4 Break-Glass Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 CJIS and FTI Screening Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Agency and Breach Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Ransomware Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-Agency and Multi-State Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Privacy Officer | CISO |
| STD-04.4 Non-Production Data Standard | Standard | Set by Chief Privacy Officer | CISO |
| PRC-04.1 Contract-End Data Return and Deletion Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 Devices and Alternate Work Site Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Data and AI Officer (with the AI governance committee) | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, Director of Regulated Data Compliance, CIO, Chief Technology Officer, Chief Human Resources Officer, Chief Data and AI Officer, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or CJISSECPOL version, a new agency contract term, an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory or contract driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Director of Regulated Data Compliance reviews anything touching CJI, FTI, or ePHI.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.1); role-based attestations for standards. Agencies receive the current set on request under their contracts.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**Acquisitions:** acquired businesses adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan, except for contract and statutory terms, which cannot be excepted (section 5). For AQ-1, that is why 39 unscreened staff lost CJI access instead of receiving an exception.

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the segment president (Moderate), executive risk committee (High), CEO and CFO (Very High).

**What cannot be excepted:** a CJIS Security Addendum, Pub. 1075 Exhibit 7, or business associate agreement term, or a statutory duty (for example, DPPA, Fla. Stat. 501.171, SEC filing deadlines). Those gaps go straight to the POA&M, and the regulated data or access is removed until they are fixed.

**Limits:** 12 months maximum; renewals need fresh approval.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | STD-01.5 supported operating system baseline, for 64 legacy hosting servers | Host firewalls; EDR on 58 of 64; no internet access; application gateways planned | Moderate | CISO with the President, Systems Integration | 2027-06-30 | R-005; POAM-005 |
| EXC-2026-034 | POL-02 4.2 no standing administrator rights, for 31 AQ-1 engineers | Daily export of AQ-1 administrator actions reviewed by the AQ-1 security lead; peering restriction (POAM-004) | High | Executive risk committee | 2027-01-31 | R-003; POAM-001 |
| EXC-2026-038 | POL-04 4.7 immutable backups, for legacy hosting | Weekly encrypted tape copy to DC-2 | High | Executive risk committee | 2026-12-31 | R-015; POAM-008 |
| EXC-2026-041 | STD-01.6 PAM for vendor maintenance, for 3 legacy hosting vendor accounts | Access windows opened per ticket; VPN MFA; session logs reviewed weekly | Moderate | CISO with the President, Systems Integration | 2027-03-31 | R-039 |

**Refused in 2026:** a request to keep AQ-1 staff with court CJI access while their fingerprint checks were pending (CJIS Security Addendum term; access suspended, POAM-002), and a request to delay the FIPS 140-3 cutover past 2026-09-21 (CJISSECPOL SC-13; tunnels will be shut down instead, POAM-006).

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Days to review a new CJISSECPOL version (target: 60 or fewer)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
