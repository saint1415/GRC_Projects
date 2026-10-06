# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Other requirements | PCI DSS v4.0.1 12.1 (policy maintained and reviewed); HIPAA 164.316(a), (b) for SL-2 |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often, such as what a technician may open on a customer's phone or how a sanitization is verified.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-04 4.3: passcodes only in the restricted field, purged at release | POL-01: risk and technology committee of the board. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-04.3: SP 800-88 Rev. 2 methods, verification of 100% of SL-2 devices and 5% of recycling devices, certificate fields | CISO | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-04.2: how a store employee inspects a PIN pad and logs it | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Tips for explaining the device access notice to customers | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a law, regulation, or contract is stricter than a standard (for example, a state breach law or a manufacturer notice term), the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 22 standards, and 14 procedures. Policy statements: 51 (37 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | CISO | CISO |
| STD-01.3 Third-Party Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | Director of Security Operations | CISO |
| STD-01.5 Configuration, Network, and Change Management Standard | Standard | Director of Network Engineering | CISO |
| STD-01.6 Maintenance Standard | Standard | Director of Store Technology | CISO |
| STD-01.7 Physical Security Standard | Standard | Vice President, Asset Protection | CISO |
| STD-01.8 Acquisition Integration Standard | Standard | Chief Risk Officer | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | CISO | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CIO | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Director of Identity and Access Management | CISO |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Resilience Policy | Policy | Director of Security Operations | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Director of Security Operations | CISO |
| STD-03.2 Breach and Contract Notification Standard | Standard | Chief Privacy Officer | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | CIO | CISO |
| PRC-03.1 Customer Device Data Exposure and POS Compromise Runbook (P08) | Procedure | Director of Security Operations | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Multi-State Breach Notification Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-03) |
| PRC-03.4 Card Compromise Procedure (acquirer, card brands, forensic investigator) | Procedure | Vice President, Payments | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | Director of Cloud Platform Engineering | CISO |
| STD-04.2 Customer Data Access Standard | Standard | Senior Vice President, Store Operations | CISO |
| STD-04.3 Media and Device Sanitization Standard (NIST SP 800-88 Rev. 2) | Standard | Director of Sanitization and Asset Recovery | CISO |
| STD-04.4 Payment Data Handling Standard | Standard | Vice President, Payments | CISO |
| STD-04.5 Retention Schedule | Standard | Chief Privacy Officer | CISO |
| PRC-04.1 Data Recovery Case Handling Procedure | Procedure | Director of Data Recovery | Owning director (under POL-04) |
| PRC-04.2 PIN Pad Inspection Procedure | Procedure | Senior Vice President, Store Operations | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | CISO | CISO |
| STD-05.3 Approved AI Tools List | Standard | Chief Data and Analytics Officer | CISO |
| PRC-05.1 Bench Workstation Use Procedure | Procedure | Senior Vice President, Store Operations | Owning director (under POL-05) |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), Chief Privacy Officer, Chief Compliance Officer, CIO, Chief Human Resources Officer, Vice President, Payments, Senior Vice President, Store Operations, Senior Vice President, Depot and Lab Operations, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new law or contract, an audit or ROC finding, an incident, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory and contractual statements; the PCI Program Manager reviews anything touching card data; the Chief Privacy Officer reviews anything touching personal data.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal and in the store task app; workforce attest annually (POL-05 4.1); role-based attestations for standards (for example, technicians attest to STD-04.2).
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept 6 years (POL-01 4.11).

**Acquisitions:** an acquired business adopts the full hierarchy on the day of closing. Where it cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the AC exceptions below). STD-01.8 sets the 90-day interim card data controls and the 12-month integration target (POL-01 4.10).

## 5. Exceptions process and register
**Who can request:** any system or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Exceptions that leave a risk to customer data or card data at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. An exception never waives a legal or contractual duty; where PCI DSS is affected, the PCI Program Manager decides with the QSA whether a compensating control is needed in the ROC.

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | STD-04.4 encryption at the point of interaction, at the 160 AC stores | Interim card data VLANs, EDR on POS PCs, browsing blocked, unique admin passwords, MSSP monitoring of VPNs | Very High until interim controls are verified, then High | CEO and CFO (treatment plan approved 2026-09-08) | 2027-03-31 | R-001; POAM-001 |
| EXC-2026-033 | POL-02 4.1 no shared accounts, at AC stores (legacy ticketing, POS, Manufacturer C portal) | Daily reconciliation of staff lists; CCTV at counters; passcode purge in the legacy service | High | Executive risk committee | 2027-03-31 | R-007; R-058; POAM-004; POAM-011 |
| EXC-2026-036 | STD-04.3 per-device verification, at Depot West | Depot East team verifies a 5% sample weekly; SL-2 health care client lots routed to Depot East | Moderate | CISO with the Senior Vice President, Depot and Lab Operations | 2026-12-31 | R-006; POAM-006 |
| EXC-2026-040 | POL-04 4.5, phone payments keyed into the virtual terminal | Agent PCs in PCI DSS scope with EDR; recordings paused by agents; quarterly recording search | Moderate | CISO with the Vice President, Contact Center | 2027-03-31 | R-016; POAM-013 |
| EXC-2026-042 | STD-01.4 SIEM onboarding, at AC stores | MSSP monitoring of AC VPN concentrators; weekly local log review by the AC managed service provider | Moderate | CISO with the Vice President, Integration Management Office | 2026-12-31 | R-045; POAM-012 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the risk and technology committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more); technician attestation to STD-04.2 (target: 100%)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
