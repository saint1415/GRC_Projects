# SOC 2 Readiness Summary: Cris Santos Company Holdings | Defense Industrial Base | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Tier / Vertical | Multi-Sector / Defense Industrial Base |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022) |
| Scoping | Per division (section 1). One readiness report: the Defense Software industry edition (`soc2-readiness.csv`). Aircraft Parts and Engineering Services are out of scope; the DoD edition relies on its FedRAMP and DoD authorizations |
| Primary assurance for DoD work | CMMC Level 2 (C3PAO) for the Enterprise CUI Environment (target window 2026-12-07 to 2026-12-18) and Level 3 (DIBCAC) for Program H later; SPRS assessments under DFARS 252.204-7019 and 252.204-7020 |
| Prepared | 2026-09-15 by the Group Chief Risk Officer's assurance team with the Defense Software security and compliance lead |

## 1. Scoping decisions per division
SOC 2 reports on controls at a **service organization** for the **user entities** that rely on its service. For each division the question is whether it provides a service that other organizations build their own controls on, and whether a SOC 2 report is the assurance those customers recognize.

| Division | Service line | Service organization? | Decision | Categories | Report |
|---|---|---|---|---|---|
| Defense Software | Industry edition (SYS-D4): sustainment analytics for 14 defense contractor tenants and 63 commercial airline and MRO tenants | **Yes, a true service organization.** Tenants rely on its controls for their maintenance data | **In scope (full).** Existing annual Type 2 | Security, Availability, Confidentiality | Type 2, 12 months ending September 30 |
| Defense Software | DoD edition (SYS-D3) for 5 DoD program offices | Yes, but for a federal customer | **Out of scope.** Its assurance is the FedRAMP Moderate authorization and the DoD provisional authorization under DFARS 252.239-7010 | n/a | n/a |
| Aircraft Parts | Manufacture of parts and spares | **No.** Customers buy parts, not a hosted service | **Out of scope.** CMMC is the assurance for DoD and primes; commercial customers receive the group security program description and P03 and P07 results | n/a | n/a |
| Engineering Services | Engineering and test services | **No for SOC 2 purposes.** Customers rely on the work product, and for CUI on CMMC and, at cleared centers, DCSA oversight | **Out of scope** | n/a | n/a |

**Why Aircraft Parts and Engineering Services are out of scope:**
1. **The recognized assurance is CMMC.** For DoD and primes, the evidence that matters is a CMMC status in SPRS (32 CFR 170.17, 170.23) and the SP 800-171 DoD Assessment (DFARS 252.204-7019, 252.204-7020). A SOC 2 report does not replace either one, and the vertical overlay names CMMC as the assurance for DoD contracts with SOC 2 as secondary.
2. **No user entities.** Primes and DoD do not build their control environments on these divisions' systems; they buy parts and engineering work.
3. **Commercial questionnaires** are answered with the group program description, CMMC evidence, and this sample's P03 and P07 results.
4. **Revisit trigger:** if either division starts hosting systems or data for customers (for example, a hosted engineering data service), assess whether a SOC 2 report is needed.

**Why SOC 2 still matters for a defense group.** The industry edition serves commercial airlines and MROs that ask for SOC 2, and defense contractor tenants use the report alongside the FedRAMP evidence they need under DFARS 252.204-7012(b)(2)(ii)(D). **A SOC 2 report is not FedRAMP Moderate equivalency.** It does not cover the full Moderate baseline and is not a 3PAO assessment against it. The division must not present the SOC 2 report as meeting the DFARS cloud requirement (P03 DS-G14, DS-G20).

**Other assurance options considered.** ISO/IEC 27001 certification (some commercial airline customers accept it; not requested enough to justify it now) and FedRAMP Moderate authorization for the industry edition (chosen, but for the DFARS equivalency need, not as a SOC 2 substitute).

## 2. System description (scope)
- **Services:** maintenance planning, component reliability analytics, and the predictive maintenance score for defense contractor and commercial operator tenants.
- **Infrastructure and software:** SYS-D4 on cloud provider A's government-community offering (container platform, managed databases, separate cluster for CUI tenants since 2026-04, warm standby region); built through the SYS-D5 software factory; group identity (SYS-G1) and SOC (SYS-G2) carved in as internal shared services.
- **Subservice organizations (carve-out):** cloud provider A; the source control and pipeline SaaS provider.
- **People:** about 4,700 Defense Software employees plus group SOC and identity teams; support staff with CUI tenant access are U.S. persons.
- **Data:** tenant maintenance and reliability data (CUI for 14 tenants; commercial confidential data for 63), maintainer work contact details.
- **Complementary user entity controls:** tenant single sign-on and MFA, tenant user provisioning and removal, tenants' own DoD reporting for their CUI, review of the SOC 2 report.

## 3. Readiness results (`soc2-readiness.csv`)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 27 | 5 | 1 | 0 |
| Availability (A1, 3) | 2 | 1 | 0 | 0 |
| Confidentiality (C1, 2) | 2 | 0 | 0 | 0 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |
| **Total (61)** | **31** | **6** | **1** | **23** |

**Why most criteria are Ready:** control environment, risk, monitoring, identity, network, and SOC criteria are met by group common controls already assessed once in P07, and the division has issued Type 2 reports since 2023.

**Not ready:** CC2.3. The draft system description for the period ending 2026-09-30 does not describe the 2026-05 change in the predictive model's data sources, and public material describes the edition as "FedRAMP-ready" and "CMMC compliant" without evidence.

**Partially ready:**
- CC3.4 and CC8.1: the 2026-05 model change was not risk-assessed for data use and bypassed the data-use step of the release board (it also breached DFARS 252.239-7010(c)(2) on the DoD edition side; P03 DS-G05).
- CC6.1: support access to tenant data is approved without a linked customer ticket.
- CC7.2: model service logs are not yet in the SIEM.
- CC9.2: two subcontracts lack required flowdown terms.
- A1.3: warm standby failover was not tested in 2026.

**The immediate issue is the report now being prepared.** The observation period ended 2026-09-30, and the model change operated for about four and a half months of it. Management must describe the change in the system description and evaluate it; expect the service auditor to consider CC2.3, CC3.4, and CC8.1 for exceptions. The division should also correct its public claims before the report is issued, because the report will be read by the same defense contractor tenants who need accurate FedRAMP status information (POAM-015, POAM-016, POAM-018).

**Processing Integrity** is out of scope today because the edition makes no processing integrity commitments. It is under evaluation for 2027, because customers now ask whether predictive maintenance scores are accurate and complete (P10).

## 4. Remediation plan and evidence calendar
| Quarter | Criteria | Evidence to collect |
|---|---|---|
| 2026 Q4 | CC2.3 | Corrected system description; withdrawn claims; written FedRAMP status notices to the 14 CUI tenants |
| 2026 Q4 | CC3.4, CC8.1 | Change gate with mandatory data-use step; retrained model record; release board minutes |
| 2026 Q4 | CC6.1, CC7.2 | Ticket-linked PAM approvals; model service logs in the SIEM |
| 2027 Q1 | CC9.2, A1.3 | Amended subcontracts; failover test report |
| 2027 Q1 to Q3 | All in-scope criteria | Operating evidence for the period ending 2027-09-30 |

**Communication:** the industry edition general manager briefs the top 20 tenants (all 14 CUI tenants included) on the model change, the corrected claims, and the FedRAMP Moderate plan before the 2026 report is issued.
