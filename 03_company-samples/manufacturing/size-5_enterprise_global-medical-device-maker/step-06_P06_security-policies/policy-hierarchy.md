# Policy Hierarchy and Governance Framework

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Owner | CISO (chair of the policy governance committee) |
| Approved by | Executive risk committee, 2026-09-10 |
| Effective date | 2026-10-01 |
| Implements | PL-1 and every "-1" control (AC-1, AT-1, AU-1, CA-1, CM-1, CP-1, IA-1, IR-1, MA-1, MP-1, PE-1, PS-1, RA-1, SA-1, SC-1, SI-1, SR-1); PM-1 |
| CSF 2.0 | GV.PO-01, GV.PO-02 |
| Regulatory basis | HIPAA 164.316(a), (b) for the business associate services; QMSR document control (21 CFR Part 820, ISO 13485 clause 4.2.4) for the product security documents that are part of the QMS |

## 1. Purpose
Define how the company's security documents fit together, who approves each level, how they are kept current, and how exceptions are handled. The hierarchy lets the five policies stay short and stable while standards and procedures carry the detail that changes more often.

**Two document systems, one hierarchy.** Product security documents that are part of design and production (STD-01.8 Secure Product Development, STD-02.4 Code Signing and Key Management, STD-03.4 Coordinated Vulnerability Disclosure, PRC-01.4 Firmware Release and Signing) are also controlled documents in the QMS, so they follow QMS document control (approval, training, change history) in addition to this framework. The GRC platform links to the QMS record rather than keeping a second copy.

## 2. Hierarchy levels
| Level | What it says | Example | Approved by | Review |
|---|---|---|---|---|
| **Tier 1: Policy** | What must happen and who is accountable. Short, stable, testable "must" statements | POL-02 4.7: firmware signing needs two approvers and no key may exist outside an HSM | POL-01: board risk and technology committee. POL-02 to POL-05: executive risk committee | Annually |
| **Tier 2: Standard** | Measurable requirements that implement a policy | STD-02.4: signing keys generated in a key ceremony with 3 custodians; key backup shares at DC-2 | CISO (with the VP Product Security and the CQRO for product security standards) | Annually or when technology changes |
| **Tier 3: Procedure** | Step-by-step instructions for a role | PRC-01.4: how a release engineer submits a signing request and how approvers check it | Owning director | Annually or when the process changes |
| **Guideline** (optional) | Recommended practice; not mandatory | Secure coding patterns for embedded C | Owning director | As needed |

**Rules:** a lower level may add detail but may not weaken a higher level. Every standard and procedure names its parent policy and statement. Where a regulation is stricter than a standard (for example, a state's agent notice deadline or a BAA term), the stricter rule applies.

## 3. Document inventory
The set has 5 policies, 24 standards, and 13 procedures. Policy statements: 54 (40 tested by Internal Audit in 2026; see `policy-control-map.csv`).

| Document | Level | Owner | Approver |
|---|---|---|---|
| POL-01 Information Security Policy | Policy | CISO | Risk and technology committee of the board (on the recommendation of the executive risk committee) |
| STD-01.1 Risk Assessment Standard | Standard | CISO | CISO |
| STD-01.2 Security Assessment and System Authorization Standard | Standard | CISO | CISO |
| STD-01.3 Third-Party and Supplier Security Standard | Standard | Director of Third-Party Risk Management | CISO |
| STD-01.4 Audit Logging Standard | Standard | Director of Security Operations | CISO |
| STD-01.5 Configuration and Change Management Standard (IT and OT) | Standard | CIO | CISO |
| STD-01.6 Maintenance Standard | Standard | Vice President, Manufacturing Systems | CISO |
| STD-01.7 Physical Security Standard | Standard | Vice President, Facilities | CISO |
| STD-01.8 Secure Product Development Standard (QMS-controlled) | Standard | VP Product Security | CISO with the CQRO |
| STD-01.9 OT Security Standard | Standard | Director of OT Security | CISO |
| PRC-01.1 Sanctions Procedure | Procedure | Chief Human Resources Officer | Owning director (under POL-01) |
| PRC-01.2 Policy Exception Procedure | Procedure | GRC team | Owning director (under POL-01) |
| PRC-01.3 Change Management Procedure | Procedure | CIO | Owning director (under POL-01) |
| PRC-01.4 Firmware Release and Signing Procedure (QMS-controlled) | Procedure | Director of Build and Release Engineering | Owning director (under POL-01) |
| POL-02 Access Control Policy | Policy | Director of Identity and Access Management | Executive risk committee |
| STD-02.1 Account Management Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.2 Identification and Authentication Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.3 Remote and Vendor Access Standard | Standard | Director of Identity and Access Management | CISO |
| STD-02.4 Code Signing and Key Management Standard (QMS-controlled) | Standard | Director of Build and Release Engineering | CISO with the VP Product Security |
| PRC-02.1 Access Provisioning Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.2 Access Certification Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.3 Privileged Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| PRC-02.4 Emergency (Break-Glass) Access Procedure | Procedure | Director of Identity and Access Management | Owning director (under POL-02) |
| POL-03 Incident Response and Product Security Policy | Policy | Director of Security Operations and VP Product Security | Executive risk committee |
| STD-03.1 Incident Classification and Escalation Standard | Standard | Director of Security Operations | CISO |
| STD-03.2 Breach and Regulatory Notification Standard | Standard | Chief Privacy Officer | CISO |
| STD-03.3 Contingency and Disaster Recovery Standard | Standard | CIO | CISO |
| STD-03.4 Coordinated Vulnerability Disclosure Standard (QMS-controlled) | Standard | VP Product Security | CISO with the CQRO |
| PRC-03.1 Fielded-Device Vulnerability Runbook (P08) | Procedure | VP Product Security | Owning director (under POL-03) |
| PRC-03.2 SEC Materiality Assessment Procedure | Procedure | General Counsel | Owning director (under POL-03) |
| PRC-03.3 Breach and Regulatory Notification Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-03) |
| PRC-03.4 Ransomware Runbook | Procedure | Director of Security Operations | Owning director (under POL-03) |
| POL-04 Data Classification and Handling Policy | Policy | Chief Privacy Officer | Executive risk committee |
| STD-04.1 Encryption Standard | Standard | CISO | CISO |
| STD-04.2 Media Protection and Disposal Standard | Standard | Vice President, Facilities | CISO |
| STD-04.3 Backup Standard | Standard | CIO | CISO |
| STD-04.4 Consumer Health Data Standard | Standard | Chief Privacy Officer | CISO |
| PRC-04.1 Data Set Registration Procedure | Procedure | Chief Privacy Officer | Owning director (under POL-04) |
| POL-05 Acceptable Use Policy | Policy | Chief Human Resources Officer | Executive risk committee |
| STD-05.1 Security Awareness and Training Standard | Standard | Chief Human Resources Officer | CISO |
| STD-05.2 External Systems and Personal Devices Standard | Standard | CISO | CISO |
| STD-05.3 Approved AI Tools List | Standard | Chief Medical Officer (AI governance committee chair) | CISO |

## 4. Governance
**Policy governance committee** (meets monthly): CISO (chair), VP Product Security, CQRO, Chief Privacy Officer, Chief Compliance Officer, CIO, Vice President, Manufacturing Systems, Chief Human Resources Officer, and the General Counsel's delegate. The Chief Audit Executive attends as a non-voting observer to keep Internal Audit independent.

**Lifecycle:**
1. **Request:** triggered by the annual review, a new regulation or FDA guidance, an audit finding, an incident, a product launch, or an acquisition.
2. **Draft:** the owner drafts in the GRC platform using the template, maps each statement to SP 800-53 and CSF 2.0, and names the regulatory driver.
3. **Review:** the committee reviews; Legal reviews regulatory statements; the Privacy Officer reviews anything touching PHI or consumer data; the CQRO reviews anything that is also a QMS document.
4. **Approve:** at the level in section 2.
5. **Publish and attest:** published on the policy portal; workforce attest annually (POL-05 4.2); QMS-controlled documents also go through QMS training records.
6. **Monitor:** statements feed continuous control monitoring and the annual Internal Audit plan (P07).
7. **Retire or revise:** superseded versions are kept at least 6 years (POL-01 4.11), and longer where QMS retention applies.

**Acquisitions:** acquired businesses adopt the full hierarchy on the day of closing. Where they cannot comply yet, the Integration Management Office files exceptions with a dated plan (for example, the MN-1 exceptions below).

## 5. Exceptions process and register
**Who can request:** any system, product, or process owner, through the GRC platform (PRC-01.2).

**What a request must contain:** the policy or standard statement affected, the reason, the systems, products, and data involved, the compensating controls, a risk rating using the P01 method (Tables G-5 and I-2), and an end date.

**Who approves:** the authority matching the residual risk (POL-01 4.4): risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO (Very High). Patient-safety and product-integrity exceptions at High or above are refused without a dated treatment plan.

**Limits:** 12 months maximum; renewals need fresh approval. Exceptions for a HIPAA addressable specification must document why the alternative is reasonable and appropriate (164.306(d)(3)). An exception never waives a regulatory deadline (for example, an FDA reporting clock).

**Register fields:** exception ID (EXC-YYYY-NNN), statement, requester, system or product, compensating controls, residual risk, approver, approval date, expiry, linked risk (P01) and POA&M item (P07), status.

**Examples from the current register:**
| Exception | Statement | Compensating controls | Residual risk | Approver | Expires | Link |
|---|---|---|---|---|---|---|
| EXC-2026-031 | STD-01.9 zone segmentation, for the MN-1 plant OT network | Perimeter firewall rules limit office-to-MES traffic to named hosts; weekly review of MN-1 firewall logs by the SOC | High | Executive risk committee | 2027-03-31 | R-020; POAM-006 |
| EXC-2026-034 | POL-02 4.7 and STD-02.4 (no key outside an HSM), for the IV-300 1.x signing workstation | Offline workstation in a locked room; two custodians present by procedure; video recording of each signing | High | Executive risk committee | 2027-01-31 | R-010; POAM-001 |
| EXC-2026-036 | POL-02 4.1 unique identities, for MN-1 operator logins | Supervisor sign-off on paper travelers; camera coverage of stations | Moderate | CISO with the Vice President, Integration Management Office | 2027-03-31 | R-021; POAM-007 |
| EXC-2026-040 | POL-04 4.2 TLS 1.2 minimum, for IV-300 first-generation modules | Separate ingestion listener with rate limits; customer advisory on network restrictions; pharmacist approval of library changes | High | Executive risk committee | 2027-06-30 | R-008; POAM-023 |

**Oversight:** the executive risk committee reviews the register monthly; expired exceptions are escalated to the CISO within 5 business days; the board risk and technology committee sees a count of open exceptions by residual risk each quarter.

## 6. Metrics
- Policies, standards, and procedures past their review date (target: 0)
- Workforce attestation rate (target: 98% or more)
- Open exceptions by residual risk, and expired exceptions (target: 0 expired)
- Policy statements tested by Internal Audit in the last 3 years (target: 100%)
