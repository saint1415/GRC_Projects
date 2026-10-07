# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (and Cris Santos Payouts, LLC, under 23 NYCRR 500.2(d)) |
| Policy ID | POL-01 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | CISO |
| Approved by | Board risk and technology committee (on the recommendation of the executive risk committee) |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, new sponsor banks, or acquisitions |
| Implements (SP 800-53 Rev. 5) | PM-1, PL-2, PM-2, RA-3, PM-9, PL-1, CA-5, PS-8, SA-9, SR-6, CA-2, CA-2(1), CM-12, CM-4, SI-12, CM-8 |
| CSF 2.0 | GV.PO-01, GV.RR-02, GV.RM-01, GV.RM-06, GV.PO-02, GV.RR-04, GV.SC-05, ID.IM-01, ID.AM-03, GV.OV-01, ID.AM-01 |
| Regulatory drivers | See `policy-control-map.csv` (one driver per statement) |

## 1. Purpose
Establish the enterprise information security program, assign accountability from the board to every workforce member, set the policy hierarchy and the exceptions process, and give every other security policy its authority. The program protects the confidentiality, integrity, and availability of cardholder, merchant, partner, and company information and supports the company's PCI DSS, FTC Safeguards Rule, bank service provider, NYDFS Part 500, and SEC obligations.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) in every location, and Cris Santos Payouts, LLC, which adopted this program under 23 NYCRR 500.2(d). Covers all systems and data, including Cloud A, Cloud B, DC-1, DC-2, SaaS, and systems that service providers operate for the company, and the services the company provides to merchants, ISV partners, and sponsor Banks A, B, and C.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk and technology committee | Oversees cybersecurity risk; approves this policy and the risk appetite; receives quarterly reports and the annual written report (16 CFR 314.4(i); 23 NYCRR 500.4(b)) |
| Board audit committee | Oversees Internal Audit, SOX, and disclosure controls |
| CEO and CFO | Accept Very High risks; take part in materiality determinations with the disclosure committee |
| CISO | Program owner; Qualified Individual (16 CFR 314.4(a)); CISO of Cris Santos Payouts, LLC (500.4(a)); holds the PCI DSS executive charter (12.4.1); chairs the policy governance committee |
| President, Cris Santos Payouts, LLC | Senior member designated to oversee the CISO's work for the subsidiary (500.4(a)(2)) |
| Chief Risk Officer | ERM; owns the enterprise risk register |
| Chief Audit Executive | Independent assessment (third line), including the Class A independent audit (500.2(c)) |
| All workforce | Follow policies, standards, and procedures; report incidents |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 The company must maintain an information security program aligned to NIST CSF 2.0 that meets PCI DSS for service providers, the FTC Safeguards Rule, the bank service provider notice rules, Part 500 for the payouts subsidiary, and the SEC disclosure rules, documented in this policy hierarchy and in system security plans for tier-1 systems. (PM-1; PL-2; GV.PO-01)
4.2 The CISO must be designated in writing as the Qualified Individual and as the CISO of Cris Santos Payouts, LLC, and an executive charter signed by the CEO must assign responsibility for the PCI DSS program to the CISO. (PM-2; GV.RR-02)
4.3 An enterprise risk assessment must be performed at least annually and after material changes, using NIST SP 800-30 Rev. 1, rolled up into the enterprise risk register following NIST IR 8286 Rev. 1, with PCI DSS targeted risk analyses for every requirement that allows a flexible frequency. (RA-3; PM-9; GV.RM-01)
4.4 Risk may be accepted only at the authority levels in STD-01.1: risk owner (Low), CISO with the accountable executive (Moderate), executive risk committee (High), CEO and CFO jointly (Very High). Sponsor bank, card network, and regulatory risks (ER-04, ER-06) at Moderate or above must not be accepted without a dated treatment plan. (PM-9; GV.RM-06)
4.5 Policies must be reviewed and approved at least annually; standards and procedures at least annually or when the controls they describe change. (PL-1; GV.PO-02)
4.6 Any deviation from a policy or standard must be approved through the exception process (section 7) before it takes effect, and any use of a rule's written-approval provision must be recorded there. (PL-1; CA-5; GV.PO-02)
4.7 Workforce members who violate security policies must be sanctioned under PRC-01.1 in proportion to intent and harm, and each sanction must be documented. (PS-8; GV.RR-04)
4.8 No service provider may store, process, or transmit account data or customer information, or affect the security of the CDE, until it has been tiered and assessed under STD-01.3 and has signed a contract with security terms and a written acknowledgment of its PCI DSS responsibilities. Its AOC and responsibility matrix must be reviewed at least every 12 months. (SA-9; SR-6; GV.SC-05)
4.9 Security controls for tier-1 systems and common control providers must be assessed at least annually by assessors independent of their operation, and the cybersecurity program must be independently audited each year. (CA-2; CA-2(1); ID.IM-01)
4.10 PCI DSS scope must be documented and confirmed at least every six months and after significant change, including any new sponsor bank program, and significant organizational changes must trigger a documented review of scope and controls. (CM-12; CM-4; ID.AM-03)
4.11 Security documentation, including risk assessments, assessments, exception records, and the records supporting each NYDFS annual filing, must be retained for at least 5 years. (SI-12; GV.PO-02)
4.12 The CISO must report cybersecurity risk to the board risk and technology committee at least quarterly and in writing at least annually, covering the topics in 16 CFR 314.4(i) and, for the payouts subsidiary, 23 NYCRR 500.4(b). (PM-9; GV.OV-01)
4.13 An asset inventory must record each asset's owner, location, classification, support expiration date, and recovery time objective, and must be validated at least quarterly. (CM-8; ID.AM-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-01.1 Risk Assessment Standard (including PCI DSS targeted risk analyses)
- STD-01.2 Security Assessment and System Authorization Standard
- STD-01.3 Third-Party Security Standard
- STD-01.4 Audit Logging and Monitoring Standard
- STD-01.5 Configuration, Vulnerability, and Change Management Standard
- STD-01.6 Maintenance Standard
- STD-01.7 Physical Security Standard
- STD-01.8 PCI DSS Scope Management Standard
- PRC-01.1 Sanctions Procedure
- PRC-01.2 Policy Exception Procedure
- PRC-01.3 Change Management Procedure
- PRC-01.4 Quarterly PCI DSS Review Procedure

## 6. Compliance and enforcement
Compliance is monitored through continuous control monitoring, the PCI DSS quarterly reviews (PCI DSS 12.4.2), access certifications, and the annual Internal Audit assessment (P07). Violations are handled under the sanctions procedure (PRC-01.1, POL-01 statement 4.7), from retraining to termination of employment or contract, in proportion to intent and harm.

## 7. Exceptions
This section defines the exception process for every policy and standard in the hierarchy. Exceptions follow PRC-01.2: requested in the GRC platform, risk-rated with the P01 method, approved at the authority level for the residual risk, recorded in the exception register with compensating controls, and limited to 12 months. Where a rule allows an officer to approve an alternative in writing (16 CFR 314.4(c)(3) and (c)(5); 23 NYCRR 500.7(c)(2), 500.12(b), 500.14(b), 500.15(b)), the exception record is that written approval and names the rule. PCI DSS has no such waiver. Expired exceptions are escalated to the CISO, and the executive risk committee reviews the register monthly. Details are in `policy-hierarchy.md` section 5.

## 8. Related documents
POL-01 to POL-05; `policy-hierarchy.md`; P01 risk register; P02 Core Payment Processing Platform SSP; P03 gap analysis; P08 runbook and notification matrix; P10 AI governance.
