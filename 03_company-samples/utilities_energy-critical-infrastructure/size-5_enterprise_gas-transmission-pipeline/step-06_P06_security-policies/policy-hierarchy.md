# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-08 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory drivers | SD Pipeline-2021-02G Sections II.B and IV.A (C-ENERGY-R03): the TSA-approved Cybersecurity Implementation Plan incorporates these documents by reference |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they stay current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable, while standards and procedures carry the detail that changes more often. It also keeps one more relationship clear: the TSA-approved **Cybersecurity Implementation Plan** describes measures by reference to these documents, so a permanent change to a standard or procedure that implements a plan measure is also a plan amendment (POL-01 statement 4.7).

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-03 4.5: Gas Control may close the IT/OT DMZ without waiting for proof of compromise | POL-01: risk committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.4: shared station account passwords changed within 24 hours of a departure; 365-day and 180-day reset schedule | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-03.3: how a control room closes its DMZ connections and confirms the isolation | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure use of satellite phones in the field | Owning director | As needed |

**Rules:**
- A lower level may add detail but may not weaken a higher level.
- Every standard and procedure names its parent policy and statement.
- Where a regulation or a TSA-approved plan measure is stricter than a standard, the stricter rule applies.
- Control room management procedures (49 CFR 192.631) and emergency plans (192.615) are owned by Gas Control and Pipeline Safety and Compliance. They sit beside this hierarchy, and POL-01 4.13 and POL-03 4.1 tie them together.

## 3. Document inventory
The set has 5 policies, 21 standards, and 13 procedures. Policy statements: 59 (39 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk committee of the board |
| STD-01.1 Risk Assessment Standard | Standard | Chief Risk Officer with the CISO | CISO |
| STD-01.2 Security Assessment and Authorization Standard | Standard | Director of OT Security | CISO |
| STD-01.3 Third-Party and Supply Chain Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | Director of Security Operations | CISO |
| STD-01.5 Configuration and Change Management Standard | Standard | Director of SCADA Engineering | CISO |
| STD-01.6 Maintenance Standard | Standard | Director of Compression Engineering | CISO |
| STD-01.7 Physical Security Standard | Standard | Vice President, Corporate Security | CISO |
| STD-01.8 Patch and Vulnerability Standard | Standard | Director of SCADA Engineering | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | GRC lead | Owning director (under POL-01) |
| PRC-01.3 TSA Plan Amendment Procedure | Procedure | Director of OT Security | Owning director (under POL-01) |
| PRC-01.4 Acquisition Security Due Diligence and Integration Procedure | Procedure | Vice President, Integration Management Office | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management; Director of OT Security | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Supplier Access Standard | Standard | Director of OT Security | CISO |
| STD-02.4 OT Access Standard | Standard | Director of OT Security | CISO |
| PRC-02.1 OT Access Request and Review Procedure | Procedure | Director of SCADA Engineering | Owning director (under POL-02) |
| PRC-02.2 Shared Station Account Procedure | Procedure | Director of Compression Engineering | Owning director (under POL-02) |
| PRC-02.3 Break-Glass OT Account Procedure | Procedure | Director of OT Security | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations; Director of OT Security | Executive risk committee |
| STD-03.1 Incident Classification, Escalation, and Reporting Standard | Standard | Director of Security Operations | CISO |
| STD-03.2 Breach Notification Standard | Standard | General Counsel | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | Chief Information Officer with the Vice President, Gas Control | CISO |
| PRC-03.1 Ransomware and Precautionary Shutdown Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 IT/OT Isolation Procedure | Procedure | Director of OT Security | Owning director (under POL-03) |
| PRC-03.4 Multi-State Breach Notification Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | General Counsel with the CISO | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | CISO | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | General Counsel with the CISO | CISO |
| STD-04.3 Backup Standard | Standard | Director of Cloud Platform Engineering; Director of SCADA Engineering | CISO |
| PRC-04.1 SSI Handling Procedure | Procedure | General Counsel | Owning director (under POL-04) |
| PRC-04.2 CEII Filing Procedure | Procedure | Director of Regulatory Affairs | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer with the CISO | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 Transient Device and Removable Media Standard | Standard | Director of OT Security | CISO |
| STD-05.3 AI Use Standard | Standard | Vice President, Digital and Analytics | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Director of OT Security, Chief Compliance Officer, Chief Information Officer, Vice President, Gas Control, Vice President, Pipeline Safety and Compliance, Chief Human Resources Officer, and a General Counsel delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a renewed or new TSA security directive, a PHMSA rule change, an audit finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews. The General Counsel reviews regulatory statements and SSI markings; Gas Control reviews anything that touches the control room.
4. **Plan check:** the Director of OT Security decides whether the change alters a TSA-approved plan measure; if so, PRC-01.3 starts the amendment request.
5. **Approve:** at the level in section 2.
6. **Publish and attest:** published on the policy portal (documents that contain SSI go to the SSI library only); workers attest each year (POL-05 4.2); role-based attestations for standards.
7. **Monitor:** statements feed continuous control monitoring, the Cybersecurity Assessment Plan schedule, and the annual Internal Audit plan (P07).
8. **Retire or revise:** superseded versions are kept 5 years (POL-01 4.11).

**Acquisitions:** an acquired pipeline adopts the full hierarchy on the day of closing. Where it cannot comply yet, the Integration Management Office files exceptions with a dated plan that matches the TSA-approved plan amendment (for PS-3, EXC-2026-015 below).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), whether a TSA-approved plan measure is affected, and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Safety-related (ER-01) exceptions at Moderate or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception never replaces a TSA plan amendment: where a plan measure changes for 45 days or more, the amendment request is filed as well (POL-01 4.7).

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01), POA&M item (P07), plan measure affected, status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-007 | POL-02 4.1 and STD-02.4 unique accounts, for shared operator accounts on legacy HMIs at 31 stations (permitted as critical for operations under SD 02G III.C.4) | Operator functions only; no administrative rights; badge-controlled station control buildings; password change on departure (being automated) | Moderate | CISO with the Chief Operating Officer | 2027-06-30 | R-007; POAM-001 |
| EXC-2026-011 | STD-01.8 patch timelines, for end-of-support HMIs and PLC firmware at 22 stations | Conduit firewalls; no internet path; gateway-only remote access; documented mitigations at 15 stations (7 in progress) | High | Executive risk committee | 2027-06-30 | R-004; R-006; POAM-003 |
| EXC-2026-015 | POL-02 4.1, 4.4, and 4.5 and STD-02.4, for PS-3 local accounts, PS3-CR console controls, and weekly disablement of legacy SCADA accounts | Locked control room; weekly account reconciliation; migration schedule in the TSA-approved plan amendment (2027-06-30) | High | Executive risk committee | 2027-06-30 | R-005; POAM-016 |
| EXC-2026-018 | STD-01.4 log forwarding and 12-month retention, for 22 compressor stations | Local logs kept 90 days; logs exported for any investigation; sensors and forwarding funded | Moderate | CISO with the Chief Operating Officer | 2027-03-31 | R-036; POAM-006 |
| EXC-2026-022 | POL-02 4.8, for 7 always-on supplier cellular modems at 5 stations | Modems limited to read-only turbine monitoring ports; carrier-side IP allowlist; weekly session review | High | Executive risk committee | 2026-12-15 | R-008; POAM-004 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the risk committee of the board sees open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Worker attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Permanent changes to plan measures without an amendment request within 50 days (target: 0; 2 in 2026, P03 G-065)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
