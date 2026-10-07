# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory hooks | MTSA Cybersecurity Plan sections and audits (33 CFR 101.630); RMP and PSM written procedures for MOC and operating procedures (40 CFR 68.69, 68.75; 29 CFR 1910.119(f), (l)); DOT security plan (49 CFR 172.802(c)) |

## 1. Purpose
Define how the company's security documents fit together for both IT and OT, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. It also connects the security hierarchy to the process safety documents that already govern the plants, so that one change does not need two unrelated approvals.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.6: all remote access to OT goes through the central gateway | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.4: remote OT sessions end after 8 hours or 30 minutes idle; logic downloads only on site | CISO (OT standards with the Director of OT Security and the Vice President, Process Safety and EHS) | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.7: how to open, use, and reseal an OT break-glass account | Owning director or plant manager | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure engineering laptop setup tips for integrators | Owning director | As needed |

**Rules:**
- A lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement.
- Where a regulation is stricter than a standard (for example, the MTSA rule at PLT-01, or a state breach law), the stricter rule applies.
- **Process safety documents are peers, not children.** Operating procedures, MOC procedures, and the emergency response plan are owned by the process safety program. Where a security procedure touches them (for example, the untrusted-DCS safe-state procedure or the OT change procedure PRC-01.3), it is approved jointly by the owning director and the plant's process safety manager, and the process safety document is updated through MOC (40 CFR 68.75(e)).
- **SSI stays out of the hierarchy.** The MTSA Facility Security Plan and Cybersecurity Plan are SSI (49 CFR Part 1520). Policies and standards may refer to them by name but may not reproduce their content.

## 3. Document inventory
The set has 5 policies, 24 standards, and 15 procedures. Policy statements: 56 (36 map to controls tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Policy | Standards | Procedures |
|---|---|---|
| POL-01 Information Security Policy (owner CISO; approved by the board risk committee) | STD-01.1 Risk Assessment; STD-01.2 Network and Communications Security (annex A: OT reference architecture); STD-01.3 Configuration and Change Management (annex B: OT hardening baselines); STD-01.4 Security Awareness and Training; STD-01.5 Personnel Security; STD-01.6 Logging and Monitoring; STD-01.7 Contingency and Recovery; STD-01.8 Security Assessment and Authorization; STD-01.9 Supply Chain and Third-Party Security | PRC-01.1 Sanctions; PRC-01.2 Policy Exception; PRC-01.3 OT Change and MOC Integration |
| POL-02 Access Control Policy (owner Director of Identity and Access Management, with the Director of OT Security) | STD-02.1 Account Management; STD-02.2 Identification and Authentication; STD-02.3 Privileged Access; STD-02.4 OT Access; STD-02.5 Physical Access to OT | PRC-02.1 Access Provisioning; PRC-02.2 Access Certification; PRC-02.3 IT Break-Glass; PRC-02.4 Integrator Onboarding; PRC-02.5 OT Access Certification; PRC-02.6 PLT-01 OT Provisioning; PRC-02.7 OT Break-Glass |
| POL-03 Incident Response and Resilience Policy (owner Director of Security Operations, with the Director of OT Security) | STD-03.1 Incident Classification and Escalation; STD-03.2 Notification; STD-03.3 OT Recovery | PRC-03.1 OT Intrusion Runbook (P08); PRC-03.2 SEC Materiality Assessment; PRC-03.3 Multi-State Breach Notification; PRC-03.4 Release Reporting Checklist |
| POL-04 Data Classification and Handling Policy (owner Chief Data and Analytics Officer, with the PLT-01 FSO for SSI) | STD-04.1 Encryption; STD-04.2 Media Protection and Disposal; STD-04.3 Backup; STD-04.4 SSI and CVI Handling | PRC-04.1 SSI Handling |
| POL-05 Acceptable Use Policy (owner Chief Human Resources Officer, with the CISO) | STD-05.1 Acceptable Use of IT and OT; STD-05.2 External Systems and Personal Devices; STD-05.3 Approved AI Tools List | None |

**How the MTSA Cybersecurity Plan maps to the hierarchy.** The 14 sections required by 33 CFR 101.630(c) draw on these documents: organization (POL-01 section 3), training (STD-01.4), drills and exercises (POL-03 4.11), records (POL-01 4.11), communications (POL-03 and the PLT-01 communications plan), systems and maintenance (STD-01.3), access control (STD-02.4), physical security (STD-02.5), monitoring (STD-01.6), audits (STD-01.8), vulnerability reports and unresolved vulnerabilities (the P07 POA&M and the CySO's register), incident reporting (STD-03.2), and the Cybersecurity Assessment (P01 and the 2027 assessment).

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director of OT Security, Vice President, Process Safety and EHS, Chief Compliance Officer, CIO, Chief Data and Analytics Officer, Chief Human Resources Officer, Senior Vice President, Manufacturing (or a delegated plant manager), and the General Counsel's delegate. The PLT-01 CySO attends for anything that touches the Cybersecurity Plan. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation, an audit finding, an incident, an acquisition, or an MOC that changes an OT security control.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Vice President, Process Safety and EHS reviews anything that touches a process safety element; the FSO reviews anything that touches SSI.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce and integrators attest annually (POL-05 4.1); role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.11).

**Acquisitions:** acquired plants adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the PLT-12 to PLT-14 remote access and segmentation exceptions below).

## 5. Exceptions process and register
**Who can request:** any system, process, or plant owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date. OT requests also state whether the exception touches a safety instrumented system or a PSM or RMP process.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). OT exceptions also need the plant manager's sign-off, and process safety exceptions at Moderate or above need the Vice President, Process Safety and EHS.

**Limits:** 12 months maximum; renewals need fresh approval. An exception cannot waive a regulatory requirement. At PLT-01, where the MTSA rule allows documented compensating controls (for example, default passwords that cannot be changed or MFA that is not feasible, 101.650(a)(2) and (a)(4)), the exception record is that documentation and is copied into the Cybersecurity Plan.

**Register fields:** exception ID (EXC-OT-NNN for OT, EXC-IT-NNN for IT), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), MTSA relevance, status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-OT-002 | POL-02 4.7 MFA, for local console logon to PLT-01 engineering workstations | Badge-controlled engineering office; named accounts; download only on site; session logging | Low | PLT-01 Plant Manager with GRC concurrence | 2027-09-30 | R-001 |
| EXC-OT-003 | POL-02 4.9 account lockout, for PLT-01 operator stations | Staffed control room; failed-logon alerts to the SOC | Low | PLT-01 Plant Manager with GRC concurrence | 2027-09-30 | None |
| EXC-OT-004 | STD-02.2 session lock, for PLT-01 operator stations | Staffed, badge-controlled control room | Low | PLT-01 Plant Manager with GRC concurrence | 2027-09-30 | None |
| EXC-OT-007 | POL-04 4.3 encryption in transit, for DCS controller protocols | Zone firewalls; passive monitoring; physical protection of cabling | Low | CISO with the Director of OT Security | 2027-09-30 | None |
| EXC-OT-011 | POL-02 4.1 unique accounts, for 14 truck rack and terminal panel HMIs | Physical access control; video; role PINs; changes logged in the DCS | Moderate | CISO with the Vice President, Global Logistics | 2027-06-30 | R-051 |
| EXC-OT-014 | STD-03.3 vault backups, for PLT-12 to PLT-14 | Weekly local backup copied to removable media stored off site | High | Executive risk committee | 2027-06-30 | R-010; POAM-015 |
| EXC-OT-015 | POL-02 4.6 gateway-only remote access, for PLT-12 to PLT-14 integrators | Remote tools disabled except supervised call-in sessions | High | Executive risk committee | 2026-12-31 | R-011; POAM-014 |
| EXC-OT-016 | STD-01.3 supported operating systems, for 9 Blend Hall 1 operator stations | Isolated network segment; monitoring; USB disabled | Moderate | CISO with the PLT-01 Plant Manager | 2027-06-30 | R-031; POAM-020 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce and integrator attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- MTSA Cybersecurity Plan sections traced to a current document (target: 14 of 14 by plan submission)
