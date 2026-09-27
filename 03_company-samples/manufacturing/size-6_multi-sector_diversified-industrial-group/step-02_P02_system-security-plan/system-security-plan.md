# System Security Plan: Device Engineering and Manufacturing System (DEMS)

**Organization:** Cris Santos Company Holdings, Inc. (Medical Devices division, inheriting corporate shared services) | **Tier:** Multi-Sector | **Vertical:** Manufacturing
**Outline:** NIST SP 800-18 Rev. 2, System Security Plan Outline Example (June 2026) | **Version:** 1.0, 2026-09-15

> **Why this system.** At this tier the SSP can cover one system per division or a shared corporate system. The group chose the **Device Engineering and Manufacturing System (DEMS)**, the Medical Devices division's engineering and production system, because it produces the software that runs on about 215,000 fielded devices, it holds the code-signing keys that every device trusts, and it carries the group's top risk (P01 GR-01). It inherits most of its IT controls from corporate (SYS-G1 to SYS-G3) through the group common control catalog (`common-control-catalog.csv`). Distribution (SYS-D4) and Testing (SYS-D6) keep their own division system plans that inherit from the same catalog.

## 1. System Name and Identifier
Device Engineering and Manufacturing System (**DEMS**), identifier CSCH-MD-SYS-D1. SYS-D1 in `../00_company-facts.md`.

## 2. System Overview
DEMS turns device designs into released, signed software and built, tested devices. It supports:
- **Design and development:** requirements, risk management files, and design history files for IX-4, IX-3, PM-7, US-2, and AI-001 (design controls under 21 CFR 820.10(c), which incorporates ISO 13485 clause 7.3).
- **Build and release:** CI/CD builds, security testing, automatic SBOM generation, and code signing for device firmware and DCC software. Signed releases go to the DCC update service (SYS-D2) and to field service.
- **Production:** MES work orders, device history records, and final test at 5 plants, where test stations load signed firmware and device identity certificates.

About 5,200 engineers, 1,100 plant operators and technicians, 164 contract manufacturer and supplier guest users, and 58 pipeline service identities use it.

**Major components:**
- **PLM** (SaaS): requirements, design files, bills of materials, risk files; supplier portal for contract manufacturers
- **Source repositories** (SaaS) with protected branches and signed commits
- **CI/CD build pipeline:** build agents on the group cloud platform (provider A); artifact repository; security testing stages (static analysis, software composition analysis, fuzzing); automatic SBOM generation
- **Code-signing service:** primary HSM at Plant A, backup HSM at Plant B, two-person approval for every production signature. **Exception:** IX-3 firmware is still signed with a software key on a build server at Plant D (gap 1)
- **Release repository:** the only source of production firmware for the DCC update service and field service
- **MES and test stations:** MES servers at each plant and 61 test stations (19 at Plants D and E)

The platform is described by service category and is vendor-agnostic (see P04).

## 3. Laws, Regulations, and Policies Affecting the System
| ID | Requirement | Citation | How it applies to DEMS |
|---|---|---|---|
| N31-33-R05 | FD&C Act section 524B (cyber devices) | 21 U.S.C. 360n-2 | DEMS runs the "processes and procedures to provide a reasonable assurance that the device and related systems are cybersecure" (524B(b)(2)), produces the updates and patches (524B(b)(2)(A)-(B)), and generates the SBOM (524B(b)(3)). The build and signing pipeline is a related system |
| QMSR | Quality management system regulation | 21 CFR Part 820 (incorporates ISO 13485 by reference; effective 2026-02-02) | Design controls (820.10(c)); records including device history and servicing records (820.35). DEMS holds these records |
| N31-33-R04 | EAR | 15 CFR Parts 730-774 | Some device technology in PLM is controlled for export. Access by foreign-national engineers and by foreign contract manufacturers is screened by group trade compliance (deemed exports) |
| N31-33-R03 | ITAR | 22 CFR Parts 120-130 | Not applicable: no defense articles |
| N42-R07 | SEC cybersecurity disclosure | 17 CFR 229.106; Form 8-K Item 1.05 | A compromise of the signing keys could be material to the group (P08) |
| Contracts | Contract manufacturer and supplier agreements; hospital customer security commitments | Contracts | Supplier SBOM and vulnerability notice clauses since 2025; customer security guides describe the update chain |
| Internal | Group policies POL-01 to POL-05 and the Medical Devices supplement | P06 | |

Not applicable to DEMS: the HIPAA Security Rule (DEMS holds no PHI; the DCC, SYS-D2, is the business associate system). DFARS 252.204-7012 and CMMC (no covered defense information or federal contract information in DEMS).

## 4. System Status
### 4.1 System Security Plan Approval
Approved by the Group CISO and the VP Engineering (system owner) on 2026-09-15, after the board risk committee review.

### 4.2 System Authorization Decision
The group is not a federal agency, so there is no formal authorization. The equivalent internal decision:
- **Decision:** authorized to operate with conditions, 2026-09-15, by the Group CISO and the Medical Devices division president, with the Group Chief Risk Officer (acceptance authority for High risks).
- **Conditions:** (1) move the IX-3 signing key into the group HSM service with two-person approval, or retire it with a planned key transition, by 2027-03-31 (POAM-003); (2) no new product line may be signed outside the HSM service; (3) segment Plants D and E and remove shared operator logins by 2027-03-31 (POAM-005, POAM-006); (4) every penetration test of DEMS or its products by the Testing division must carry a signed independence statement (POAM-011).
- **Reauthorization:** annually, or when the IX-3 key transition is complete.

### 4.3 System Operational Status
Operational. **Major modifications planned:** IX-3 signing key transition (P01 GR-01, MD-003), Plants D and E segmentation (MD-005), and supplier SBOM coverage (MD-012), all due by 2027-06-30.

## 5. Role Identification and Responsible Personnel
| Role | Title | Responsibility |
|---|---|---|
| System owner | VP Engineering | Accountable for DEMS and this SSP |
| Authorizing official equivalent | Group CISO with the Medical Devices division president | Authorization decision; the Group Chief Risk Officer co-accepts High risks |
| Product security | Chief Product Security Officer (CPSO) | Threat models, security testing, SBOM program, vulnerability monitoring |
| Regulatory owner | VP Quality and Regulatory Affairs | Design control and record requirements; 524B submissions |
| Production owner | VP Manufacturing Operations | MES and test stations at 5 plants |
| Key custodians | 6 named release engineers (2 per signing ceremony) | HSM operations and key ceremonies |
| Common control providers | Group identity director (SYS-G1), Group SOC director (SYS-G2), Group cloud platform director (SYS-G3) | Operate inherited controls (`common-control-catalog.csv`) |
| Independent assessor | Group internal audit | Assesses common controls once; assessed DEMS in 2026 (P07) |

## 6. System Information Types and System Categorization
Information types were selected from NIST SP 800-60 Vol. 2 Rev. 1 and adjusted for a device manufacturer. Impact levels follow FIPS 199.

| Information type | Confidentiality | Integrity | Availability | Rationale |
|---|---|---|---|---|
| Device software and firmware (source and builds) | Moderate | **High** | Moderate | Unauthorized change could reach about 215,000 fielded devices, including infusion pumps, with possible patient harm |
| Code-signing keys and release credentials | **High** | **High** | Moderate | Every fielded device trusts these keys. Disclosure or misuse would let an attacker sign malicious firmware |
| Design history and risk management files (including export-controlled technology) | **High** | Moderate | Low | Trade secrets and EAR-controlled technology; required records under the QMSR |
| Manufacturing and test records (device history records, final test results) | Low | **High** | Moderate | Falsified test results could release nonconforming devices. The BIA sets production MTD at 72 hours (P05 BP-MD03) |
| **DEMS category (high-water mark)** | **High** | **High** | **Moderate** | Overall **High** |

**Baseline:** the NIST SP 800-53B **High** baseline, tailored. The plan documents **132 controls** in `control-implementation.csv`:
- 129 from the High baseline;
- 3 not in any baseline, added because of the group's structure and the device supply chain: PM-1 and PM-2 (program management inherited from the group) and SR-4 (provenance, which supports the 524B(b)(3) SBOM).

Other High-baseline controls are either fully inherited from the cloud and SaaS providers (for example, most PE controls for provider facilities, evidenced by their SOC 2 Type 2 reports) or tailored out with a reason in the group tailoring register (for example, PE controls for facilities the division does not operate).

## 7. Authorization Boundary Description
- **Inside:** PLM tenant, source repositories, build pipeline accounts in provider A, artifact and release repositories, the HSMs at Plants A and B, the Plant D build server and software key, and the MES servers and 61 test stations at the 5 plants.
- **Outside, inherited (common control providers):** SYS-G1 identity platform, SYS-G2 SOC, SIEM, and EDR, and the SYS-G3 landing zone, WAN, and backup vault.
- **Outside, interconnected:** SYS-D2 DCC update service (receives signed releases), SYS-D3 eQMS (design change and CAPA links), SYS-D6 Testing LIMS (test reports for premarket submissions), SYS-G4 ERP (bills of materials and UDI data), and contract manufacturer systems through the PLM supplier portal.

The diagram is in P04 `cloud-architecture.md` (the DEMS subgraph).

## 8. Information Exchanges Summary
| Connected system / party | Direction | Data | Agreement |
|---|---|---|---|
| SYS-D2 DCC update service | Outbound | Signed IX-4 and PM-7 firmware and hospital drug library packages | Interface agreement; release role only |
| Field service (via release repository) | Outbound | Signed IX-3 packages for USB installation | Interface agreement; IX-3 signed at Plant D (gap 1) |
| SYS-D3 eQMS | Two-way | Design changes, CAPA references, complaint trends | Interface agreement |
| SYS-D6 Testing LIMS | Inbound | Test reports and findings on Medical Devices products | Intercompany testing agreement; **independence statement not required until 2026-10** (POAM-011); information barrier rules (P06) |
| Contract manufacturers and suppliers (PLM supplier portal) | Two-way | Drawings, bills of materials, component data; supplier SBOM entries | Supply agreements with security and SBOM clauses (2025 template); export screening. **Gap:** 164 guest accounts not certified quarterly (POAM-001) |
| SYS-G4 ERP | Outbound | Bills of materials, serial numbers, UDI data | Internal interface |

## 9. System Component Inventory
| Component | Type | Location / provider | Owner |
|---|---|---|---|
| PLM | SaaS | PLM vendor | VP Engineering |
| Source repositories | SaaS | Source hosting vendor | VP Engineering |
| Build agents and artifact repository | IaaS and PaaS | Provider A | VP Engineering |
| Code-signing HSMs (primary and backup) | Hardware security modules | Plants A and B | VP Engineering (key custodians) |
| Plant D build server and IX-3 software key | Server | Plant D | VP Engineering (**transition due 2027-03-31**) |
| Release repository | PaaS | Provider A | VP Engineering |
| MES servers | Servers | 5 plants | VP Manufacturing Operations |
| Test stations (61) | Workstations with test fixtures | 5 plants (19 at Plants D and E) | VP Manufacturing Operations |

## 10. Control Implementation Details
### 10.1 Control implementation status
See `control-implementation.csv` (132 controls) and `common-control-catalog.csv` (89 group common controls that DEMS inherits fully or in part).

| Status | Controls |
|---|---|
| Implemented | 116 |
| Partially implemented | 16 |
| Planned | 0 |
| Not applicable | 0 |
| **Total** | **132** |

| Inheritance | Controls |
|---|---|
| Common/Inherited (from SYS-G1, SYS-G2, SYS-G3, group functions, or providers) | 62 |
| Hybrid (group provides the mechanism; DEMS configures or operates part) | 27 |
| System-specific | 43 |

**The 16 partially implemented controls** cluster in four places:
- **Legacy IX-3 release chain** (scenario gap 1): SC-12, CM-3, CM-8, SR-4, SA-22.
- **Acquired plants D and E** (gap 2): SC-7, AC-4, IA-2, AU-6, AU-12, SI-4, CP-9.
- **Supplier and contract manufacturer access and transparency** (gap 9): AC-2, SR-3.
- **Independence and cross-division response** (gaps 5 and 7): CA-8, IR-8.

### 10.2 Common control inheritance by division
The common control catalog lists 89 controls that corporate provides. Inheritance is **documented for Medical Devices** (2025 inheritance matrix, confirmed for DEMS in this plan) and for Testing's 5 federated laboratories (2026). It is **not documented for Distribution** (scenario gap 3; POAM-013), and the 4 acquired laboratories cannot inherit SYS-G1 controls until they are federated (POAM-015).

### 10.3 Control assessment status
Common controls were assessed once, and DEMS and division controls sampled, from 2026-07-06 to 2026-08-28 by group internal audit. See P07 `assessment-results.csv` and `poam.csv`.

## 11. Digital Identity Acceptance Statement
- **Workforce users** authenticate through SYS-G1 federated sign-in with MFA; **administrators and key custodians** use phishing-resistant hardware keys and just-in-time PAM elevation. This fits a High-integrity system reached by remote engineers.
- **Contract manufacturers and suppliers** use federated guest identities with MFA; export screening applies before access to controlled technology.
- **Plant operators** at Plants A to C sign in to MES with individual badges and PINs linked to SYS-G1 identities. **Plants D and E test stations use shared operator logins** (POAM-006), which the QMSR record requirements and this plan both treat as a weakness because test records cannot be tied to a person.
- **Pipeline service identities** use workload identity with short-lived tokens; signing requests require two human approvals.

## 12. Referenced Artifacts
Scenario facts (`../00_company-facts.md`), group and division risk registers (P01), gap analyses and regulation-by-division matrix (P03), cloud architecture and control map (P04), BIA (P05), group policies and division supplements (P06), assessment and POA&M (P07), incident response runbook and notification matrix (P08), SOC 2 readiness (P09), AI governance (P10).

## 13. Acronym List and Glossary
- **CPSO:** Chief Product Security Officer
- **Cyber device:** a device that includes sponsor-validated software, can connect to the internet, and has characteristics that could be vulnerable to cybersecurity threats (524B(c))
- **DCC:** Device Connectivity Cloud (SYS-D2)
- **DEMS:** Device Engineering and Manufacturing System (SYS-D1)
- **HSM:** hardware security module
- **MES:** manufacturing execution system
- **PLM:** product lifecycle management
- **PSIRT:** product security incident response team
- **QMSR:** Quality Management System Regulation (21 CFR Part 820)
- **SBOM:** software bill of materials

## 14. System Security Plan Review and Change Records
| Version | Date | Change | Author |
|---|---|---|---|
| 0.9 | 2026-08-28 | Draft after P07 fieldwork | VP Engineering |
| 1.0 | 2026-09-15 | Approved with authorization conditions | Group CISO |
