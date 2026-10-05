# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Benchmark (N21-BM) | SP 800-82 Rev. 3 section 3.3.4 (OT security policies and procedures) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, including the OT-specific rules that differ between the enterprise SCADA platform, the Florida control room, and the acquired AQ-MC assets.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.5: access, including SCADA accounts, disabled the same business day as termination | POL-01: board risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-01.8: OT DMZ required between any SCADA network and any other network; the OT tailoring register (TR-01 to TR-07) | CISO (OT standards with the Director of OT Security) | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.6: how a shift lead approves, watches, and ends an OT vendor session | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure use of field tablets in vehicles | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation is stricter than a standard (for example, a state breach law or a PHMSA reporting deadline), the stricter rule applies. Regional operating procedures (manual operations, shut-in criteria) are operations documents owned by the regional Vice Presidents; where they touch security, they cite the security procedure they implement.

## 3. Document inventory
The set has 5 policies, 21 standards, and 15 procedures. Policy statements: 54 (36 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party and Supply Chain Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard | Standard | Set by CISO | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 OT Security Standard (SP 800-82 Rev. 3 overlay and tailoring register) | Standard | Set by CISO | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure (IT and OT change boards) | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.4 Acquisition Security Integration Procedure | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management (with the Director of OT Security for OT access) | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard (includes OT domain and local SCADA accounts) | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard (IT and OT) | Standard | Set by Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.5 SCADA Account Management Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.6 OT Vendor Session Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard (with OT roles) | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard (includes regional manual operations) | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Ransomware Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.4 Regulatory Release Reporting Procedure (PHMSA and EPA) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Compliance Officer (with Privacy Counsel for personal information) | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.3 Backup Standard (IT and OT) | Standard | Set by Chief Compliance Officer | CISO |
| STD-04.4 Production Data Integrity Standard | Standard | Set by Chief Compliance Officer | CISO |
| PRC-04.1 Data Extract Registration Procedure | Procedure | Chief Compliance Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems, Wireless, and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Human Resources Officer | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director of OT Security, Chief Compliance Officer, CIO, Vice President, Operations Technology and Automation, Vice President, Health, Safety, and Environment, Chief Human Resources Officer, Privacy Counsel, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation, an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver (`N21-BM` with the SP 800-82 Rev. 3 section, or the binding rule).
3. **Review:** the committee reviews; Legal reviews regulatory statements; Privacy Counsel reviews anything touching personal information; the Vice President, Operations Technology and Automation and the Vice President, HSE review anything that could change how the field is operated.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); contractors attest through their onboarding; role-based attestations for standards.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.11).

**Acquisitions:** acquired assets adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (PRC-01.4), for example the AQ-MC exceptions below.

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). OT exceptions also need the Director of OT Security's sign-off. Process safety or environmental exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception can never waive a binding legal duty (for example, a PHMSA or EPA notice deadline).

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-007 | POL-02 4.1 unique identity, for shared HMI operator logins at the Florida control room and AQ-MC | Badge-controlled rooms; shift sign-in log; monthly event review by the Director of OT Security | Moderate | CISO with the Vice President, Operations Technology and Automation | 2026-12-31 | R-023; POAM-014 |
| EXC-2026-011 | POL-02 4.11 OT DMZ, for the Florida control room (one firewall between corporate and SCADA) | Rule set reduced to 14 named flows; quarterly rule review; allowlisting on HMIs | High | Executive risk committee | 2027-03-31 | R-001; POAM-003 |
| EXC-2026-012 | STD-01.5 supported operating system baseline, for 2 Florida SCADA servers and 26 HMIs (18 Florida, 8 AQ-MC) | Allowlisting; no internet access; restricted firewall rules | Moderate | CISO with the Vice President, Operations Technology and Automation | 2027-06-30 | R-015; POAM-009 |
| EXC-2026-016 | POL-02 4.9 vendor access through the gateway, for the ESP vendor monitoring cloud (read-only after remote write is disabled) | Remote write disabled on all drives by 2026-10-31; vendor change notices; drive trip protections | Moderate | CISO with the Chief Operating Officer | 2026-12-31 | R-003; POAM-002 |
| EXC-2026-019 | POL-02 4.5 same-day disablement of OT accounts, at AQ-MC (seller directory) | Daily HR termination report reconciled by the AQ-MC site lead | Moderate | CISO with the Vice President, Integration Management Office | 2027-01-31 | R-006; POAM-001 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce and contractor attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
- OT tailoring register entries reviewed this year (target: 100%)
