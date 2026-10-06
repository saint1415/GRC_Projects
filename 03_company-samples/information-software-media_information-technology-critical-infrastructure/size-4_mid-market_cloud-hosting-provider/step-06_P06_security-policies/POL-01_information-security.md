# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | Director of Security |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, a FedRAMP rules release that changes obligations, an acquisition, or a significant incident |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PL-10, PS-1, PS-8, RA-1, RA-3, CA-1, CA-2, CA-5, CA-7, SA-1, SA-9, SR-1, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07 |
| Regulatory drivers | C-IT-R01 (FedRAMP Consolidated Rules for 2026; Rev5 Class C control list); C-IT-R03 (252.204-7012(b)(2)(ii)(D)); C-IT-R04 (28 CFR Part 202); C-IT-R05 (12 CFR 53.4) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of customer data and the platform that hosts it, including federal customer data in the Government Cloud.

## 2. Scope
All employees and contractors, every service line (managed private cloud, Government Cloud, managed services, backup and DR, DNS and edge), both partitions of the Hosting Control Plane and Customer Portal (HCP), the three data centers, corporate IT, and systems that vendors operate for the company. **One program, two partitions:** controls written for the Government Cloud apply to the commercial partition unless a documented exception says otherwise (section 4.3).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk and FedRAMP status; receives quarterly reports |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Technology Officer | Executive sponsor; HCP system owner; approves POL-02 to POL-05; accepts Moderate risks |
| Director of Security | Owns this policy; senior security official for FedRAMP; reports to the CTO and the audit committee |
| GRC Manager | Risk register, FedRAMP package and continuous monitoring, SOC 2, policies and standards, vendor risk |
| Security Operations Manager | Security monitoring and incident command; federal incident response coordinator |
| Federal Program Director | Government Cloud business owner; agency communications and significant change notices |
| General Counsel | Legal review of notices, contracts, government contract clauses, and AI use |
| VPs and directors | Apply policies in their areas; own the controls assigned in the SSP (P02) |
| Co-sourced internal audit firm | Independent annual assessment (P07); reports to the audit committee |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 **Program.** The company must maintain an information security program documented in this policy set, the supporting standards, and the System Security Plan, using the FedRAMP Rev5 Class C control list as the baseline for both partitions. (PM-1; PL-10; GV.PO-01; C-IT-R01)
4.2 **Senior security official.** The Director of Security is the senior security official and must receive FedRAMP Emergency messages. The designation must be in writing and reaffirmed each year. (PM-2; GV.RR-02; C-IT-R01)
4.3 **One standard for both partitions.** A control that is required in the government partition must also be applied in the commercial partition and at every data center unless the CTO approves a written exception under section 4.8. (PL-2; GV.PO-01; C-IT-R01)
4.4 **Risk assessment.** An enterprise and system risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1, and must include supply chain risk. Every risk must have an owner, a treatment, and a due date in the risk register. (RA-3; PM-9; ID.RA-01; C-IT-R01)
4.5 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The CTO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. No risk that lets one compromise reach many customers at once may be accepted above Moderate. (PM-9; GV.RM-01; C-IT-R01)
4.6 **FedRAMP rules.** The GRC Manager must track every FedRAMP ruleset that applies to the Government Cloud, plan to meet each by its maintaining date, check the FedRAMP changelog monthly, and keep the Security Decision Record and certification package current at least once a year. (CA-7; PL-2; GV.OC-03; C-IT-R01)
4.7 **Reporting.** The Director of Security must report to the audit committee each quarter on the top risks, POA&M status, incidents, FedRAMP transition status, and vendor review status. (CA-5; GV.OV-01; C-IT-R01)
4.8 **Exceptions.** Exceptions to any policy or standard must be requested in writing, risk-rated, approved under section 4.5, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-02; C-IT-R01)
4.9 **Policy review.** Policies must be reviewed at least annually and after major changes or incidents. Standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; C-IT-R01)
4.10 **Independent assessment.** Controls must be independently assessed at least annually (P07), and the Government Cloud must complete its FedRAMP independent assessment each year with the controls FedRAMP lists for Class C. (CA-2; ID.IM-02; C-IT-R01 (IVV-CSF-AIA))
4.11 **Vendors.** Before a vendor receives access to customer data or production systems, it must be tiered, reviewed, and approved by the GRC Manager, and its contract must include security and incident notice terms. Services used by the government partition must hold their own FedRAMP certification or be assessed as third-party information resources. (SA-9; SR-6; GV.SC-05; C-IT-R01 (MAS-CSO-TPR))
4.12 **Tier 1 vendors.** Tier 1 vendors must be reviewed each year, including their SOC 2 report or FedRAMP package, with exceptions followed up in writing (STD-09; P09). (SR-6; GV.SC-07; C-IT-R01)
4.13 **Data security program check.** No vendor, employment, or investment agreement may give a country of concern or covered person access to customer data or government-related data without General Counsel review under 28 CFR Part 202. (SA-9; PS-7; GV.SC-04; C-IT-R04)
4.14 **Contract flow-downs.** Security duties that customers flow down (DFARS 252.204-7012 for defense customers, the bank addendum, agency terms) must be recorded in the SSP and the incident runbooks before the contract is signed. (PL-2; GV.OC-03; C-IT-R03; C-IT-R05)
4.15 **Sanctions.** Workforce members who break security policies must be sanctioned in proportion to intent and harm, from retraining to termination. HR must document each sanction. (PS-8; GV.RR-04; C-IT-R01)
4.16 **Records.** Policies, risk assessments, assessments, FedRAMP deliverables, and incident records must be kept for at least 6 years, or longer where a contract requires. (SI-12; GV.PO-01; C-IT-R01)
4.17 **AI.** AI tools that process customer data, act on security alerts, write production code, or support employment decisions must be approved through the AI governance process before use (STD-10; P10). (PM-9; SA-9; GV.RM-01; C-IT-R01)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), the FedRAMP annual assessment, quarterly access reviews, and the metrics reported to the audit committee. Violations are handled under section 4.15.

## 6. Exceptions
Exceptions follow section 4.8. They must be written, risk-rated, approved by the right authority under section 4.5, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); FedRAMP transition gap analysis and roadmap (P03); FedRAMP Consolidated Rules for 2026
