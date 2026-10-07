# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| 33 CFR Part 101 Subpart F | 101.630(a), (c) (the Cybersecurity Plans describe how each measure is met, and draw on this hierarchy) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, how they feed the Coast Guard Cybersecurity Plans, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.9: vendor and OEM remote access only through the vendor access gateway | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.8: compensating control record for every OT KEV within 10 days of listing | CISO (with the CySO for OT and Subpart F standards) | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-03.4: how the CySO or an alternate reports to the COTP, FBI and CISA under 6.16-1 | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure handling tips for gate clerks | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation is stricter than a standard, the stricter rule applies. Where a Cybersecurity Plan or an FSP sets a facility-specific rule, the Plan or FSP governs at that facility and the standard is updated to match within 30 days.

## 3. Document inventory
The set has 5 policies, 22 standards and 16 procedures. Policy statements: 57 (40 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Chief Risk Officer | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | Director of Security Operations | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | CIO | CISO |
| STD-01.6 Maintenance Standard | Standard | Director of OT Engineering | CISO |
| STD-01.7 Physical Security Standard | Standard | Vice President, Maritime Security | CISO |
| STD-01.8 OT Security Standard | Standard | Director of OT Engineering | CISO with the CySO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief People Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CIO | Owning director (under POL-01) |
| PRC-01.4 Cybersecurity Plan Maintenance and Amendment Procedure | Procedure | Director of Maritime Cybersecurity (CySO) | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Director of Identity and Access Management | CISO with the CySO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 OEM Remote Session Procedure | Procedure | Director of OT Engineering | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | General Counsel | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | CIO | CISO |
| PRC-03.1 Ransomware Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.4 Coast Guard and MTSA Reporting Procedure | Procedure | Director of Maritime Cybersecurity (CySO) | Owning director (under POL-03) |
| PRC-03.5 Manual Terminal Operations Procedure | Procedure | Chief Operating Officer | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Compliance Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | CISO | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Director of Endpoint Engineering | CISO |
| STD-04.3 Backup Standard | Standard | Director of Cloud Platform Engineering | CISO |
| STD-04.4 SSI Handling Standard | Standard | Director of Maritime Cybersecurity (CySO) | CISO |
| STD-04.5 Cargo Data Integrity Standard | Standard | Vice President, Terminal Technology | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Vice President, Data and Analytics | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief People Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Chief People Officer | CISO with the CySO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | Director of Endpoint Engineering | CISO |
| STD-05.3 Approved AI Tools List | Standard | Vice President, Data and Analytics | CISO |
| PRC-05.1 Longshore and Contractor Supervised Access Procedure | Procedure | Vice President, Labor Relations | Owning director (under POL-05) |

## 4. How the hierarchy feeds the Cybersecurity Plans
The Cybersecurity Plans must contain 14 sections (101.630(c)). They are facility documents and SSI; they cite this hierarchy rather than repeat it, and add the facility-specific detail.

| Plan section (101.630(c)) | Source in the hierarchy |
|---|---|
| (1) Cybersecurity organization and identity of the CySO | POL-01 4.2; CySO designation letters |
| (2) Personnel training | POL-05 4.3, 4.4; STD-05.1; PRC-05.1 |
| (3) Drills and exercises | POL-03 4.12, 4.13 |
| (4) Records and documentation | POL-01 4.11 |
| (5) Communications | POL-03 4.4, 4.8; PRC-03.4 |
| (6) Cybersecurity systems and equipment, with maintenance | STD-01.5; STD-01.6; STD-01.8 |
| (7) Access control measures | POL-02; STD-02.1 to STD-02.3 |
| (8) Physical security controls for IT and OT | POL-05 4.10; STD-01.7 |
| (9) Monitoring measures | STD-01.4; POL-04 4.5 |
| (10) Audits and amendments | POL-01 4.9; PRC-01.4 |
| (11) Reports of audits and inspections | POL-01 4.9; P07 reports |
| (12) Unresolved vulnerabilities, including accepted ones | POL-01 4.4; the exception register (section 6) |
| (13) Cyber incident reporting procedures | POL-03 4.4; PRC-03.4 |
| (14) Cybersecurity Assessment | POL-01 4.3, 4.10; STD-01.1 |

## 5. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director of Maritime Cybersecurity (CySO), Chief Compliance Officer, CIO, Vice President, Maritime Security, Director of OT Engineering, Chief People Officer, General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or MARSEC Directive, an audit finding, an incident, an acquisition, or a Cybersecurity Plan amendment.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the CySO reviews anything that changes a Subpart F measure, because the change may need a Plan amendment sent to the Coast Guard at least 30 days before it takes effect once Plans are approved (101.630(e)(2)).
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workers attest annually (POL-05 4.2); role-based attestations for standards; terminal-level briefings by the FSOs and Terminal OT Security Leads.
6. **Monitor:** statements feed continuous control monitoring, the annual Internal Audit plan (P07) and, after approval, the annual Plan audits.
7. **Retire or revise:** superseded versions are kept at least 2 years (POL-01 4.11), or longer under the records schedule.

**Acquisitions:** acquired terminals adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the T-08 identity and logging exceptions below).

## 6. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems, facilities and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Safety exceptions at High or above are refused without a dated treatment plan. The CySO must concur on any exception that touches a Subpart F measure.

**Limits:** 12 months maximum; renewals need fresh approval. An exception to a Subpart F measure is not a regulatory waiver: it must be documented as a compensating control or an unresolved vulnerability in the Cybersecurity Plan (101.630(c)(12)), or handled through a waiver, equivalence determination or temporary deviation notice to the COTP (101.665).

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system and facility, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), Plan section reference, status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | POL-02 4.4 MFA, for T-08 legacy TOS users | Site link limited to named services; daily HR reconciliation; legacy TOS reachable only from T-08 | Moderate | CISO with the Vice President, Integration Management Office and CySO concurrence | 2027-03-31 | R-003; POAM-001 |
| EXC-2026-034 | POL-02 4.1 unique accounts, for RTG HMIs at 4 terminals | Cab access limited to TWIC holders; operator log kept by the superintendent | Moderate | CISO with the Director of OT Engineering and CySO concurrence | 2027-03-31 | R-007; POAM-004 |
| EXC-2026-036 | STD-01.4 SIEM onboarding, for T-07 gate servers and OT | Weekly export of local logs to the SOC; OT firewall alerts | Moderate | CISO with the Director of Security Operations | 2027-01-31 | R-041; POAM-008 |
| EXC-2026-040 | POL-04 4.3 encryption, for OT protocols that cannot support it | OT zones; allow-listed flows through the OT DMZ; monitoring at T-01 to T-05 | Low | Director of OT Engineering with GRC concurrence | 2027-06-30 | R-002; P03 G-037 |
| EXC-2026-042 | POL-02 4.9 vendor gateway, for the T-01 automation vendor tunnel | Firewall allow list to the vendor's address range; OT monitoring alerts at T-01; tunnel disabled outside planned windows from 2026-10-15 | High | Executive risk committee (2026-09-08) | 2026-12-15 | R-004; POAM-002 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 7. Metrics
- Policies, standards and procedures past their review date (target: 0)
- Worker attestation rate (target: 98% or more); hiring halls with training or supervised-access arrangements (target: 6 of 6)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Exceptions touching Subpart F measures that are reflected in the Plans (target: 100%)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
