# SOC 2 Readiness Summary: Cris Santos Company | Critical Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (power and distribution transformer manufacturer, Florida) |
| Tier / Vertical | Small / Critical Manufacturing |
| Criteria | AICPA 2017 Trust Services Criteria (With Revised Points of Focus, 2022). Criterion IDs and short topic labels only; the criteria text is not reproduced |
| Categories in scope | Security (CC1-CC9) only |
| Target report | None. This is a self-benchmark, not a CPA-issued SOC 2 report |
| Part A | Company Security self-benchmark (`soc2-readiness.csv`) |
| Part B | Review of the MSP's SOC 2 Type 2 report (`vendor-soc2-review.csv`) |
| Prepared | 2026-08-21 by the IT Manager; approved by the VP Operations 2026-09-04 |

## 1. Why SOC 2 (or an alternative) for this organization
**The company is not a SOC 2 service organization.** A SOC 2 report describes a service organization's system and controls for the user entities that rely on its services. Cris Santos Company sells transformers and field service, not hosted or managed services, and no customer's controls depend on company systems. A SOC 2 examination would have no natural audience and would cost far more than any customer has asked for.

SOC 2 still matters here in two ways:

**A. A Security-only self-benchmark to answer utility questionnaires.** The 12 utilities with Supplier Cyber Security Addenda send annual supplier security questionnaires under their CIP-013-2 supply chain programs. In 2026 one of them asked whether the company had a SOC 2 report. The company will answer every questionnaire from one source of truth:
- this self-benchmark against the Security criteria (CC1-CC9);
- the P03 gap analysis, which is organized by CSF 2.0 (the framework most questionnaires use);
- the POA&M (P07), which gives dates.

The self-benchmark uses the Security criteria only, because that is what the questionnaires ask about. Availability, Confidentiality, Processing Integrity, and Privacy are marked N/A. Their substance is covered elsewhere:
- recovery under CC7.5 and CC9.1;
- confidentiality of customer drawings under CC6.5, CC6.7, and POL-04.

Other options considered:
- **A formal SOC 2 or SOC for Supply Chain examination.** Rejected for now: no customer requires one, and the controls are too new to test over a period.
- **ISA/IEC 62443 certification of the plant.** A private OT security standard. Out of proportion for a 200-person plant today; revisit after the OT DMZ is built.
- **CMMC.** Not applicable: no DoD work (P03 G-092).

**B. Third-party risk management.** The MSP holds administrator rights on every IT server and endpoint through its RMM tool (P01 R-014, High). Its SOC 2 Type 2 report is the main evidence that its controls work. The company reviewed it for the first time on 2026-08-21 (Part B).

## 2. System description (scope)
- **Services:** design, manufacture, test, and field service of distribution and power transformers, and the security duties owed to utilities under the addenda.
- **Infrastructure and software:** the ERP and Production Scheduling Platform (SSP, P02), the PLM vault, the plant control systems, the test bay, and the TMU firmware library.
- **People:** 200 employees, including 3 IT staff and the Controls Engineer, plus the MSP.
- **Data:** designs and customer drawings (Restricted), FCI, test reports, supplier data, and employee records.
- **Procedures:** POL-01 to POL-05 and the P08 runbook.

## 3. Readiness results (Part A)
| Category | Ready | Partially ready | Not ready | N/A |
|---|---|---|---|---|
| Security (CC1-CC9, 33 criteria) | 5 | 20 | 8 | 0 |
| Availability (A1, 3) | | | | 3 |
| Confidentiality (C1, 2) | | | | 2 |
| Processing Integrity (PI1, 5) | | | | 5 |
| Privacy (P1-P8, 18) | | | | 18 |

**Ready (5):**
- CC3.1, CC3.2, and CC3.3: objectives, risk analysis, and fraud risk are covered in POL-01 and P01.
- CC4.2: deficiencies are tracked in the POA&M.
- CC6.4: physical access (P07 PE-3 fully satisfied).

**Not ready (8):**
- CC2.3: external communication. The utility notice, vulnerability disclosure, and firmware hash duties are not operating. This is what utilities will ask about first.
- CC6.1 and CC6.6: flat plant network and always-on OEM remote access.
- CC6.3: ERP super users and late account removal.
- CC7.1 and CC7.2: no vulnerability management or monitoring.
- CC7.5: recovery unproven.
- CC9.2: supplier risk not managed.

**How to answer utilities now.** Answer honestly, with dates. For each Not ready item, cite the POA&M item and its milestone. Several fixes are due in September and October 2026, so the company should send its first answers after those milestones:
- routers off between sessions;
- notices in the matrix;
- the 2 open advisories disclosed.

## 4. Findings from the MSP report (Part B)
- **Opinion:** Type 2, unqualified, 12 months ending 2026-03-31. One exception (technician access changes without documented approval), remediated.
- **Security only.** The report does not cover Availability, so the MSP's backup monitoring is not attested. The company must prove recovery itself (POAM-007).
- **The biggest risk is carved out.** The RMM software vendor is a carved-out subservice organization, so the supply chain risk behind R-014 is not covered. Follow-up: ask the MSP how it monitors that vendor.
- **Controls the company must run.** The report lists controls the customer must operate for the MSP's controls to work (complementary user entity controls). Three are open gaps at the company:
  - reviewing MSP activity reports (P03 G-051);
  - restore testing (POAM-007);
  - restricting where the RMM agent runs. It must never reach plant systems.
- **Incident notice:** the MSP commits to 72 hours; the contract has no deadline. Add a 24-hour term at renewal.
- **Next steps:** obtain a bridge letter by 2026-10-31. Request SOC 2 reports from the cloud provider, identity provider, and EDI provider for the P04 inherited controls (P03 G-016).

## 5. Remediation plan and evidence calendar
| Quarter | Criteria addressed | Evidence to start collecting |
|---|---|---|
| 2026 Q4 | CC2.3, CC6.3, CC6.6 (interim), CC7.3, CC7.4, CC2.2 | Utility notice log and advisory disclosures; termination tickets with utility notices; OEM session approvals; tabletop report; policy acknowledgments |
| 2027 Q1 | CC6.1, CC6.6, CC7.1, CC7.2, CC7.5, CC6.8 | Firewall rule reviews; remote access gateway logs; scan reports; MDR tickets; restore test records |
| 2027 Q2 | CC8.1, CC9.2, CC3.4, CC1.4 | OT change records; supplier reviews; training records for production and field staff |

**Next self-benchmark:** April 2027, before the next round of utility questionnaires.
