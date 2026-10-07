# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10; POL-01 approved by the risk committee of the board, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory basis | 10 CFR 73.54(f) (written policies and implementing procedures for the cyber security program); CIP-003-9 R1 (cyber security policies reviewed and approved by the CIP Senior Manager at least once every 15 calendar months) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy keeps the five enterprise policies short and stable while standards and procedures carry the detail that changes more often.

## 2. Three document families, one hierarchy
The company has three sets of security documents. This framework governs the first and defines how it relates to the other two.

| Family | What it covers | Owner | Change control |
|---|---|---|---|
| **Enterprise security policy set (this hierarchy)** | Business IT: corporate, plant business networks, WMS, clouds, data centers, service lines | CISO | This framework |
| **Station cyber security programs** | CDAs at each station: the NRC-approved CSP and its implementing procedures (73.54(f)) | Director, Nuclear Cyber Security; Site Vice Presidents | CSP change process (73.54(d)(3)); license change rules; plant procedure process |
| **NERC CIP program documents** | Generation Dispatch Center (high impact) and station switchyard interface devices (low impact) | Director, NERC Compliance; CIP Senior Manager | CIP-003-9 R1 review and approval at least every 15 calendar months |

**Rules between families:**
- The enterprise policies apply to everything outside the CDA networks and set the minimum for the GDC. Where a CSP or CIP document is stricter, it prevails.
- Enterprise policies may refer to CSP rules (for example, portable media bound for CDAs) but never restate or change them.
- POL-01 to POL-05 are approved by the CIP Senior Manager as the company's CIP-003-9 R1 cyber security policies for low impact assets, together with the GDC program documents. Because the enterprise review cycle is 12 months, it meets the 15-calendar-month limit.

## 3. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.5: access disabled the same business day as a termination, and at badge-out for outage contractors | POL-01: risk committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: 14-character minimum passwords; FIDO2 keys for privileged users | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.1: how outage contractor accounts are requested, end-dated, and removed at badge-out | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure use of outage trailer printers | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation, a CSP, or a NERC standard is stricter than a standard, the stricter rule applies.

## 4. Document inventory
The set has 5 policies, 20 standards, and 11 procedures. Policy statements: 52 (36 map to controls that Internal Audit tested in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and Supply Chain Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard (business facilities) | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure (including the design change cyber screening interface) | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure (including outage contractors) | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director, Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Set by Director, Security Operations | CISO |
| STD-03.2 Regulatory Notification Standard (NRC, NERC, SEC, and state) | Standard | Set by Director, Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director, Security Operations | CISO |
| PRC-03.1 Plant Business Network Cyber Attack Runbook (P08) | Procedure | Director, Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director, Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director, Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Compliance Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.3 Backup Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.4 Security-Related Information Handling Standard | Standard | Set by Chief Compliance Officer | CISO |
| PRC-04.1 Restricted Report and Data Extract Registration Procedure | Procedure | Chief Compliance Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems, Contractor Devices, and Portable Media Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |

## 5. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director, Nuclear Cyber Security, Director, Nuclear Security, Chief Compliance Officer, CIO, Director, NERC Compliance, Chief Human Resources Officer, Export Compliance Officer, and the General Counsel's delegate. The Chief Audit Executive and the Director, Nuclear Oversight attend as non-voting observers to keep the third line and nuclear oversight independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new or changed regulation (including a final NRC rule), an audit or inspection finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Director, Nuclear Cyber Security confirms nothing conflicts with a CSP; the Director, NERC Compliance confirms CIP alignment.
4. **Approve:** at the level in section 3; the CIP Senior Manager also approves for CIP-003-9 R1.
5. **Publish and attest:** published on the policy portal; workforce attest annually and contractors before badging (POL-05 4.2).
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept at least 6 years; documents that are part of the cyber security program records follow 73.54(h) (POL-01 4.11).

**Acquisitions:** an acquired station adopts the full hierarchy on the day of closing. Its CSP and implementing procedures transfer with the license and are moved to fleet procedures through the CSP change process. Where business systems cannot comply yet, the Vice President, Integration Management files exceptions with a dated plan (examples below).

**Pending NRC rules:** the NRC "Modernizing Security Requirements" proposed rule (91 FR 38928, 2026-06-26) is not final. No policy, standard, or procedure is changed for it until a final rule and its effective date are published (P01 R-064).

## 6. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive or Site Vice President (Moderate), executive risk committee (High), CEO and CFO (Very High). Requests in enterprise risk ER-05 (nuclear safety, security, and NRC and NERC compliance) at High or above are refused without a dated treatment plan.

**What cannot be excepted:** a regulatory requirement, a CSP commitment, an SGI requirement, or a NERC CIP requirement. These follow the CSP change process, the SGI program, or the NERC compliance process (POL-01 4.6).

**Limits:** 12 months maximum; renewals need fresh approval.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | POL-02 4.1 and 4.4 (enterprise identity and MFA), for Station 4 users still in the prior owner's directory | Prior owner's MFA for remote access; firewall between Station 4 and DC-1; weekly account reconciliation by the integration team | Moderate | CISO with the Vice President, Integration Management | 2027-03-31 | R-003; POAM-003 |
| EXC-2026-033 | STD-01.4 SIEM onboarding and STD-01.5 EDR baseline, for Station 4 business endpoints and servers | Prior owner's antivirus; daily log export reviewed by the SOC; firewall logging at the Station 4 boundary | Moderate | CISO with the Site Vice President, Station 4 | 2026-12-31 | R-040; POAM-004 |
| EXC-2026-036 | STD-01.5 patching within 30 days, for WMS edge servers during refueling outage change freezes | Edge servers are read-only and reachable only from the work control segment; critical patches still go through the emergency change path | Low | WMS Application Manager with GRC concurrence | 2027-04-30 | R-039; POAM-014 |
| EXC-2026-038 | STD-02.3 vendor access through PAM, for the prior owner's vendor VPN at Station 4 | VPN limited to 14 named vendor accounts with MFA; sessions logged at the Station 4 firewall; no path to CDAs (one-way devices) | Moderate | CISO with the Vice President, Integration Management | 2027-03-31 | R-003; R-030; POAM-009 |

**Not excepted (handled elsewhere):** the Station 4 sensor gateways (a 73.54(b)(1) analysis gap) are in the station corrective action program and POAM-018; the Station 4 vendor access to low impact switchyard devices (CIP-003-9 Attachment 1 Section 6) is in the NERC compliance process and POAM-025.

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 7. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more); contractors badged without attestation (target: 0)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
