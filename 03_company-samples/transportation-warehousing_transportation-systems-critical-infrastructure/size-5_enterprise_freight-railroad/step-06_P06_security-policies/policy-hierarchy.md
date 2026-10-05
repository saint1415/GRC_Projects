# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-08 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| TSA basis | SD 1580/82-2022-01E Sec. II.B and IV.C.2.d (policy and procedural documents that inform and document the CIP, CIRP, and assessment program) |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often. It also gives TSA inspectors one indexed set of documents behind the CIP.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.5: access disabled the same business day as termination | POL-01: board safety, security, and risk committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.2: 14-character minimum passwords; FIDO2 keys for privileged users | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-02.4: how to open, use, and reseal a break-glass account | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure radio and phone practices for dispatchers | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a TSA Security Directive, the TSA-approved CIP, or another regulation is stricter than a standard, the stricter rule applies. A change to a document that the CIP incorporates by reference triggers a CIP amendment check (SD 1580/82-2022-01E Sec. VI.B).

## 3. Document inventory
The set has 5 policies, 23 standards, and 15 procedures. Policy statements: 55 (34 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Board safety, security, and risk committee (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | Set by CISO | CISO |
| STD-01.2 Security Assessment and Cybersecurity Assessment Plan Standard | Standard | Set by CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Set by CISO | CISO |
| STD-01.4 Audit Logging Standard (including OT log sources) | Standard | Set by CISO | CISO |
| STD-01.5 Configuration, Change, and Patch Management Standard (section 5 is the patch standard) | Standard | Set by CISO | CISO |
| STD-01.6 Maintenance Standard | Standard | Set by CISO | CISO |
| STD-01.7 Physical Security Standard | Standard | Set by CISO | CISO |
| STD-01.8 Network Zone and Segmentation Standard | Standard | Set by Director of OT Security | CISO |
| PRC-01.1 Security Sanctions Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure (including PTC configuration control) | Procedure | CISO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.3 Remote, Vendor, and External System Access Standard | Standard | Set by Director of Identity and Access Management | CISO |
| STD-02.4 OT Access, Shared Account, and Trust Relationship Standard | Standard | Set by Director of OT Security | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification, Escalation, and Regulatory Reporting Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.2 Breach Notification and SSI Release Standard | Standard | Set by Director of Security Operations | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Set by Director of Security Operations | CISO |
| PRC-03.1 Ransomware Runbook for Dispatch and Train Control Back-Office Systems (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.4 RSSM Location Request Fallback Procedure (draft) | Procedure | Assistant Vice President, Rail Security | Owning director (under POL-03) |
| PRC-03.5 Manual Dispatch and CTC Local Control Procedure | Procedure | Vice President, Network Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Assistant Vice President, Rail Security | Executive risk committee |
| STD-04.1 Encryption and Key Management Standard | Standard | Set by CISO | CISO |
| STD-04.2 Media Protection, Marking, and Disposal Standard (including SSI) | Standard | Set by Assistant Vice President, Rail Security | CISO |
| STD-04.3 Backup Standard | Standard | Set by CISO | CISO |
| STD-04.4 Operational Data Integrity Standard | Standard | Set by Director of Train Control Systems | CISO |
| PRC-04.1 SSI Handling Procedure | Procedure | Assistant Vice President, Rail Security | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard (including the TSA security training program) | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.2 External Systems, Mobile Devices, and Personal Devices Standard | Standard | Set by Chief Human Resources Officer | CISO |
| STD-05.3 Approved AI Tools List | Standard | Set by Chief Safety Officer (AI governance committee chair) | CISO |
| STD-05.4 Collective Bargaining Notice Standard for Monitoring Technology | Standard | Set by Chief Human Resources Officer | CISO |
| PRC-05.1 Training Assignment and Grace Period Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-05) |
| PRC-05.2 Lost Device Reporting Procedure | Procedure | Director of Endpoint Engineering | Owning director (under POL-05) |

Counts: 5 policies; 23 standards (STD-01.1 to 01.8, STD-02.1 to 02.4, STD-03.1 to 03.3, STD-04.1 to 04.4, STD-05.1 to 05.4); 15 procedures (PRC-01.1 to 01.3, PRC-02.1 to 02.4, PRC-03.1 to 03.5, PRC-04.1, PRC-05.1 to 05.2).

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Assistant Vice President, Rail Security, Director of OT Security, CIO, Chief Safety Officer's delegate, Chief Human Resources Officer, General Counsel's delegate, Director of Train Control Systems, and Vice President, Network Operations. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, an SD renewal or new regulation, an audit or TSA inspection finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Director of OT Security reviews anything that touches Critical Cyber Systems; the CISO checks whether the change affects a CIP measure.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal and, for SSI content, in the SSI library; employees attest annually (POL-05 4.2); role-based attestations for standards. Changes that affect union-represented crafts follow STD-05.4.
6. **Monitor:** statements feed continuous control monitoring, the Cybersecurity Assessment Plan, and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 7 years (POL-01 4.11).

**Acquisitions:** acquired railroads adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AQ-04 to AQ-06 identity and network exceptions below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, whether a CIP measure is affected, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Rail safety exceptions at Moderate or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception to a CIP measure needs the CISO's written decision on whether to request a CIP amendment or notify TSA; an exception never changes the TSA-approved CIP by itself.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, CIP measure affected (yes or no), compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-011 | STD-02.4 shared accounts, for 3 CTC code server administrator accounts (CIP measure: yes) | Passwords rotated 2026-09-02; use only from the OT enclave through PAM-monitored sessions; vital field logic | High | Executive risk committee | 2026-11-30 | R-006; POAM-004 |
| EXC-2026-017 | STD-01.5 patch timelines, for PTC back office servers awaiting vendor certification (CIP measure: yes) | Enclave isolation; allowlisting; no internet path; heightened monitoring while compensating measures are documented | High | Executive risk committee | 2026-12-31 | R-005; POAM-003 |
| EXC-2026-022 | POL-02 4.5 same-day disablement, at AQ-04 to AQ-06 | Daily HR report reconciliation by the service desk | Moderate | CISO with the Vice President, Integration Management Office | 2027-05-31 | R-063; POAM-001 |
| EXC-2026-026 | STD-01.4 SIEM onboarding, for CTC code servers and PTC message brokers (CIP measure: yes) | Local retention extended to 90 days; weekly manual log review by the OT security team | Moderate | CISO with the Director of Train Control Systems | 2027-03-31 | R-008; POAM-007 |
| EXC-2026-029 | POL-04 4.4 protection of OT traffic, for CTC code line circuits on 3 Class II railroads (CIP measure: yes) | Carrier private circuits; vital field logic rejects conflicting routes; dated treatment plan | Moderate | CISO with the Vice President, Network Operations | 2027-06-30 | R-036; POAM-013 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board safety, security, and risk committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Employee attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit or the Cybersecurity Assessment Plan in the last 3 years (target: 100%)
