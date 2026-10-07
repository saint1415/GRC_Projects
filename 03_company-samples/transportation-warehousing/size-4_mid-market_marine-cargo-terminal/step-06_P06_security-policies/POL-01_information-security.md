# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | Chief Executive Officer (noted by the board audit committee) |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 version) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, incidents or changes to the Coast Guard rule |
| Implements (SP 800-53 Rev. 5) | PM-1, PL-2, PM-2, RA-3, PM-9, CA-5, PL-1, RA-7, PS-8, SA-4, SA-9, SR-6, SR-8, CA-2, CA-2(1), SI-12, AU-11, CA-3, RA-5, RA-5(11), SI-2, SA-22, SA-11, CM-3, CA-8 |
| CSF 2.0 | GV.PO-01, GV.RR-02, ID.RA-01, ID.RA-05, GV.RM-01, GV.RM-02, GV.OV-01, GV.PO-02, ID.RA-07, GV.RR-04, GV.SC-05, GV.SC-06, GV.SC-07, ID.IM-01, ID.IM-02, PR.PS-04, GV.OC-03, GV.OC-04, ID.RA-08, PR.PS-02, PR.PS-06 |
| USCG cyber rule (N48-49-R01) | 33 CFR 101.620(a), 101.620(b)(1), 101.620(b)(3), 101.625(b), 101.625(d)(15), 101.625(e)(7), 101.630(d)(2), 101.630(e), 101.630(f), 101.640, 101.650(d), 101.650(e)(1), 101.650(e)(2), 101.650(e)(3)(i)-(ii), 101.650(e)(3)(vi), 101.650(f)(1), 101.650(f)(1)-(2), 101.665 |
| Other requirements | 33 CFR 105.225; 33 CFR 105.305(c)(1)(v); 33 CFR 105.415(a)(4); 33 CFR 105.415(b)(4); Fla. Stat. 501.171(6) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |
| Handling | Internal |

## 1. Purpose
Establish the Cris Santos Company cybersecurity program, assign accountability, and give every other security policy and standard its authority. The program protects the safety of people on the terminals, the security of the facilities under their Facility Security Plans, the integrity of cargo and customs data, and the availability of terminal operations, and it is the basis for the Cybersecurity Plan required by 33 CFR Part 101, Subpart F.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary staff and contractors) at Terminal 1, Terminal 2, the off-dock depot and the headquarters office, plus longshore labor and vendor technicians whenever they use company IT or OT. It covers every system and data set: the cloud landing zone, SaaS services, gate systems, crane and yard equipment controllers (OT), security systems, and systems that vendors operate or support for the company, including any terminal the company acquires, from the day it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board audit committee | Oversees cyber risk; receives quarterly reports on top risks, POA&M status, incidents and Subpart F readiness |
| Chief Executive Officer | Approves this policy, the risk appetite and the security budget; accepts High risks |
| Chief Operating Officer | Executive sponsor and TOGP system owner; approves POL-02 to POL-05 and the standards; accepts Moderate risks; approves the Cybersecurity Plan for submission |
| vCISO | Owns this policy and the program strategy; reports to the audit committee; co-chairs AI review |
| Director of IT and Cybersecurity (CySO) | Cybersecurity Officer for both terminals under 33 CFR 101.625; runs the program day to day; owns the SSP and the Cybersecurity Plan |
| Security Manager (alternate CySO), security analysts and GRC analyst | Security operations, vulnerability management, MSSP oversight, GRC, standards and evidence |
| Director of Port Security (T1 FSO) and T2 Security Lead (T2 FSO) | FSPs, FSAs, TWIC and PACS, MTSA reporting, drills and records; SSI custodians |
| Director of Maintenance and Engineering | Owns crane and yard equipment controllers (OT) and OEM relationships |
| General Counsel | Legal and regulatory requirements register; breach determinations; contract terms |
| Procurement Manager | Applies security criteria and contract terms to IT, OT and AI purchases |
| Co-sourced internal audit firm | Independent annual assessment (P07); planned auditor for the Plan and FSP audits |
| All workforce, longshore labor and vendors | Follow the policies and report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain a cybersecurity program documented in this policy set, the supporting standards, the System Security Plan (P02) and, once approved, the Cybersecurity Plan for both terminals. The Cybersecurity Plan must address the specific risks of each terminal. (PM-1; PL-2; GV.PO-01; 101.620(a); 101.620(b)(1); 101.630(d)(2))

4.2 The Chief Operating Officer must designate in writing, by name and title, a Cybersecurity Officer and an alternate, reachable by the Coast Guard 24 hours a day, 7 days a week. The designation must name both terminals, be reaffirmed each year, and be updated in the Plan when the CySO changes. (PM-2; GV.RR-02; 101.620(b)(3); 101.625(b))

4.3 A cybersecurity risk assessment must be performed at least annually and after a change of ownership, an acquisition or another major change, using NIST SP 800-30 Rev. 1. Its results feed the annual Cybersecurity Assessment and both Facility Security Assessments. Every risk must be recorded in the risk register with an owner, a treatment and a due date. (RA-3; PM-9; ID.RA-01; ID.RA-05; 101.650(e)(1); 33 CFR 105.305(c)(1)(v))

4.4 **Risk acceptance authority.** Risk owners may accept Low and Very Low risks. The Chief Operating Officer may accept Moderate risks. The Chief Executive Officer may accept High risks for up to 12 months with a dated treatment plan. Very High risks may not be accepted, except by a CEO exception of up to 90 days after notice to the audit committee chair. Risks that could plausibly injure people on the terminals may not be accepted above Low. (PM-9; GV.RM-01; GV.RM-02; 101.650(e)(1))

4.5 The vCISO must report to the audit committee each quarter on top risks, POA&M status, incidents and progress toward the Cybersecurity Plan submission. (PM-9; CA-5; GV.OV-01; 101.620(a))

4.6 Security policies must be reviewed at least annually and after major changes, incidents or changes to the Coast Guard rule. Supporting standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; 101.630(e))

4.7 **Exceptions** to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and limited to 12 months or less. An exception to a Subpart F measure must document its compensating control for the Cybersecurity Plan. (PL-1; RA-7; ID.RA-07; 101.665)

4.8 **Sanctions.** Workforce members who fail to comply with security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension of access, or termination. HR must document each sanction. Good-faith reporting of incidents or mistakes is never sanctioned. (PS-8; GV.RR-04; 101.650(d))

4.9 **Suppliers.** Cybersecurity capability must be an evaluation criterion when buying IT, OT or AI systems and services. Contracts with vendors that have access to company systems or hold company data must require notice of vulnerabilities and reportable cyber incidents without delay, SSI handling terms where SSI is shared, and, for vendors that hold personal information, breach notice within 10 days. Vendors are tiered and reassessed under STD-04, with an annual SOC 2 (or equivalent) review for Tier 1 vendors (P09). (SA-4; SA-9; SR-6; SR-8; GV.SC-05; GV.SC-06; GV.SC-07; 101.650(f)(1)-(2); Fla. Stat. 501.171(6))

4.10 Security controls must be assessed at least annually by assessors independent of the controls (P07). Once the Cybersecurity Plan is approved, its annual audit must be performed by auditors with no regularly assigned cybersecurity duties, and FSP audits by persons without regularly assigned security duties, unless that is impracticable and documented. (CA-2; CA-2(1); ID.IM-01; ID.IM-02; 101.630(f); 33 CFR 105.415(b)(4))

4.11 **Records.** Records of cybersecurity training, drills, exercises, cyber threats, reportable cyber incidents and Plan audits must be created and kept with the FSO records for at least 2 years, protected against unauthorized deletion, destruction or amendment, and made available to the Coast Guard on request. (SI-12; AU-11; GV.PO-02; PR.PS-04; 101.640; 33 CFR 105.225)

4.12 The General Counsel and the CySO must keep a register of the legal, regulatory and contractual security requirements that apply to the company, including Subpart F, Part 105, 49 CFR part 1520, Fla. Stat. 501.171 and customer requirements such as the carrier alliance SOC 2 commitment. (PL-1; SA-9; GV.OC-03; 101.625(e)(7))

4.13 AI tools that touch company data, support planning, maintenance or security decisions, or face customers must be approved through the AI governance process before use (STD-09; P10). AI used in terminal operations stays advisory: no AI output may move equipment without a human decision. (PM-9; SA-9; GV.RM-01; GV.SC-06; 101.650(f)(1))

4.14 **Acquisitions and ownership changes.** A newly acquired terminal or site must be assessed within 90 days of signing and may connect to company networks only through a segmented, monitored zone until it meets company standards. A change of ownership triggers a new Cybersecurity Assessment and the required Plan and FSP amendments. (CA-3; RA-3; ID.RA-07; GV.OC-04; 101.650(e)(1); 101.630(e); 33 CFR 105.415(a)(4))

4.15 **Vulnerability management.** The CySO must make sure that Known Exploited Vulnerabilities in critical IT and OT systems are identified and mitigated without delay, or covered by documented compensating controls; that vulnerability scans run at the frequencies set in STD-07 (including passive scanning of OT); that systems past vendor support are replaced or isolated; and that the company keeps a public channel to receive reported vulnerabilities. (RA-5; RA-5(11); SI-2; SA-22; ID.RA-01; ID.RA-08; PR.PS-02; 101.625(d)(15); 101.650(e)(3)(i)-(ii); 101.650(e)(3)(vi))

4.16 **Company-built software.** Changes to the customer portal and other company-built applications must be peer reviewed, pass automated dependency and static analysis checks, and be released to production only by company staff who did not write the change. Internet-facing applications must be penetration tested at least annually. (SA-11; CM-3; CA-8; PR.PS-06; 101.650(f)(1); 101.650(e)(2))

## 5. Compliance and enforcement
Violations are handled under section 4.8. Compliance is checked through the annual independent assessment (P07), the Cybersecurity Assessment (33 CFR 101.650(e)(1)), the annual Plan audit once the Plan is approved (101.630(f)), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right authority under section 4.4, recorded in the risk register, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); risk register and appetite statements (P01); gap analysis and roadmap (P03); 33 CFR Part 101, Subpart F; 33 CFR Part 105; 49 CFR part 1520; Fla. Stat. 501.171
