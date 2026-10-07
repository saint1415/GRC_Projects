# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, new hotels, new management agreements, or significant incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PL-2, PS-8, RA-3, CA-2, CA-3, CA-5, CM-8, SA-9, SR-6, SI-12 |
| CSF 2.0 | GV.OC-03, GV.RM-01, GV.RR-02, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-07, ID.AM-03, ID.RA-05 |
| PCI DSS v4.0.1 | 12.1, 12.3, 12.4 (by policy), 12.5, 12.8 |
| Other drivers | FTC Act Section 5 (15 U.S.C. 45(a), (n)); 16 CFR Part 464; Fla. Stat. 501.171(2) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |

## 1. Purpose
Establish the Cris Santos Company information security program, assign accountability, and give every other security policy and standard its authority. The program protects payment card data, guest and employee information, and the systems that let guests arrive, enter their rooms, and pay safely.

## 2. Scope
All employees, contracted workers supplied by staffing companies, and contractors at the 6 hotels, the central reservations office (CRO), and the corporate office. It covers all company systems and data, the company-managed side of the franchised hotels, systems that vendors and the franchisor operate for the company, and (from 2027-01-01) the hotels the company manages for third-party owners.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber and PCI risk; receives quarterly reports on top risks, POA&M status, PCI status, and incidents |
| Chief Executive Officer | Approves this policy, the risk appetite, and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and PMPS system owner; approves POL-02 to POL-05; accepts Moderate risks |
| Chief Financial Officer | PCI DSS compliance owner; merchant agreement and acquirer; signs the SAQ D |
| General Counsel | Breach determinations; franchise, management, and vendor contract terms; privacy notice |
| vCISO | Owns this policy and the program strategy; reports to the audit committee |
| IT Director | Runs infrastructure; PCI DSS technical lead; owns the SSP and contingency planning |
| Security Manager, security analyst, GRC Analyst | Security operations, vulnerability management, MSSP oversight, risk register, standards, vendor reviews |
| Hotel General Managers and department heads | Apply policies at their hotels; approve access; own downtime and device inspection procedures |
| Co-sourced internal audit | Independent annual assessment (P07) |
| All workforce | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an information security program that meets PCI DSS v4.0.1 for all its merchant accounts and provides reasonable security under FTC Act Section 5 and Fla. Stat. 501.171(2). The program is documented in this policy set, the supporting standards, and the System Security Plan. (PM-1; GV.PO-01; PCI DSS 12.1.1)
4.2 The vCISO leads the program, the IT Director is the PCI DSS technical lead, and the CFO is the PCI DSS compliance owner. These designations are made in writing and reaffirmed each year. (PM-2; GV.RR-02; PCI DSS 12.1.3, 12.1.4)
4.3 An enterprise risk assessment must be performed at least annually and after major changes, using NIST SP 800-30 Rev. 1. Targeted risk analyses must support every PCI DSS requirement whose frequency the company chooses. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-05; PCI DSS 12.3.1)
4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The COO may accept Moderate risks. The CEO may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could stop guests from securing or reaching their rooms may not be accepted above Low. (PM-9; GV.RM-01)
4.5 The vCISO must report to the audit committee each quarter on the top risks, POA&M status, PCI DSS status, incidents, and progress against the program roadmap. (GV.OV-01; CA-5)
4.6 Security policies must be reviewed at least annually and after major changes or incidents. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; PCI DSS 12.1.2)
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **PCI DSS scope.** The IT Director must document the PCI DSS scope (all locations and flows of card data and every connected system) and confirm it at least every 12 months and after any significant change. The CFO must not sign a self-assessment questionnaire answer as "In Place" without evidence. (CM-8; PL-2; ID.AM-03; PCI DSS 12.5.2)
4.9 **Third parties.** No vendor may store, process, or transmit card or guest data for the company without a contract with security and incident notice terms, a security review scaled to its tier, and, for card data, a current PCI DSS attestation of compliance. The GRC Analyst keeps the list of these vendors, a record of which PCI DSS requirements each one manages, and an annual check of each one's compliance status. (SA-9; SR-6; GV.SC-05; PCI DSS 12.8)
4.10 **Franchisor.** For each franchised hotel, the company must hold a written allocation of PCI DSS responsibilities with the franchisor and evidence, at least annually, that the franchisor's controls for the brand PMS, gateway, and property firewalls operate. Until it does, the company treats those controls as unverified in its risk register. (SA-9; CA-3; GV.SC-07; PCI DSS 12.8.5)
4.11 Security controls must be independently assessed at least annually (P07) and after major changes. (CA-2)
4.12 Privacy notices, security statements, and every price display (including chatbot answers and phone scripts) must be accurate. Prices must show the total price including mandatory fees, as 16 CFR 464.2 requires. The General Counsel reviews privacy and security statements before publication; the Vice President of Sales and Marketing checks price displays monthly. (PM-9; GV.OC-03)
4.13 AI tools that use guest, card, or employee data, or that set prices or affect hiring, must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)
4.14 Security records (logs, assessments, risk analyses, incident records, breach determinations) must be kept as the retention schedule in STD-04 requires: at least 12 months for audit logs and at least 5 years for any written Florida no-harm determination. (SI-12)
4.15 **Sanctions.** Workforce members who break security policies must be disciplined in proportion to intent and harm, from retraining to termination. HR documents each sanction. (PS-8; GV.RR-04)

## 5. Compliance and enforcement
Compliance is checked through the annual independent assessment (P07), the QSA-supported PCI DSS assessment, access reviews every 6 months, and the metrics reported to the audit committee. Violations are handled under section 4.15.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); gap analysis (P03); PCI DSS v4.0.1; franchise agreements; REIT management agreement
