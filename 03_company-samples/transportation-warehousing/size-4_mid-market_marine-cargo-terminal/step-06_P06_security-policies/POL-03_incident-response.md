# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-03 |
| Owner | Director of IT and Cybersecurity (CySO) |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 version) |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, incidents or changes to the Coast Guard rule |
| Implements (SP 800-53 Rev. 5) | IR-8, IR-6, IR-5, IR-4, IR-2, IR-3, IR-7, SI-4, AU-6 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MA-03, RS.MI-01, ID.IM-02, PR.AT-02, DE.CM-01, DE.AE-02, ID.IM-03, ID.IM-04 |
| USCG cyber rule (N48-49-R01) | 33 CFR 101.620(b)(6), 101.620(b)(7), 101.625(d)(10), 101.630(b), 101.635(b)-(c), 101.640, 101.645(b), 101.650(d)(1)(iv), 101.650(d)(2), 101.650(g)(1), 101.650(g)(2), 101.650(g)(3), 101.650(h)(2) |
| Other requirements | 33 CFR 101.305; 33 CFR 6.16-1; 49 CFR 1520.9(c); Fla. Stat. 501.171(3)-(5) |
| Supporting standards | See `standards-index.md` (STD-01 to STD-10) |
| Handling | Internal |

## 1. Purpose
Make sure the company detects, contains, reports and recovers from cyber incidents quickly, safely and lawfully at both terminals and the depot, and meets its Coast Guard, SSI and Florida reporting duties. It replaces the 2024 IT-focused incident response policy.

## 2. Scope
All Cris Santos Company workforce members (employees, temporary staff and contractors) at Terminal 1, Terminal 2, the off-dock depot and the headquarters office, plus longshore labor and vendor technicians whenever they use company IT or OT. It covers every system and data set: the cloud landing zone, SaaS services, gate systems, crane and yard equipment controllers (OT), security systems, and systems that vendors operate or support for the company, including any terminal the company acquires, from the day it connects to company systems.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| CySO (Director of IT and Cybersecurity) | Incident commander for cyber incidents; makes the 33 CFR 6.16-1 report; coordinates the MSSP and the forensic firm |
| Alternate CySO (Security Manager) | Incident commander when the CySO is unavailable; runs the technical response with the MSSP |
| FSOs (T1 and T2) | Breaches of security and TSIs under the FSPs (101.305); SSI disclosure reports; incident records |
| Chief Operating Officer | Chairs the crisis management team; decides terminal shutdown or restart with the terminal General Managers |
| General Counsel | Engages outside counsel and the cyber insurer; breach determinations; privilege |
| Director of Maintenance and Engineering | Puts OT in a safe state; signs off OT integrity before restart |
| MSSP | 24x7 detection, triage, host isolation and escalation within 30 minutes |
| All workforce, longshore labor and vendors | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain a Cyber Incident Response Plan covering IT and OT at both terminals and the depot, with runbooks for its most likely incidents: ransomware disrupting the TOS, and unauthorized access to crane controllers through vendor remote access (P08). The full plan is due 2026-12-31. (IR-8; RS.MA-01; 101.620(b)(6); 101.650(g)(2))

4.2 Workforce members, longshore labor and vendors must report any suspected cyber incident **immediately**, and within 1 hour at most, to the CySO line or to the shift superintendent, who calls the CySO line. Examples: a phishing click, a ransom note, a lost device, unusual TOS or release data, or equipment that behaves unexpectedly. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 101.650(d)(1)(iv))

4.3 Every cyber incident must be logged, categorized and tracked to closure, with the date and time of discovery and of each report made. Records are kept per POL-01 4.11. (IR-5; RS.MA-02; 101.640; 101.625(d)(10))

4.4 **Coast Guard reporting.** Evidence of an actual or threatened cyber incident involving or endangering either terminal must be reported **immediately** to the FBI, CISA and the Captain of the Port for that terminal, as required by 33 CFR 6.16-1. The CySO makes the report, or the alternate CySO or the FSO if the CySO cannot be reached. Do not wait for the investigation to finish. A report under 6.16-1 also meets the Subpart F duty to report reportable cyber incidents to the National Response Center. Breaches of security and TSIs are also reported under the FSPs (101.305). (IR-6; RS.CO-02; 101.620(b)(7); 101.650(g)(1); 33 CFR 6.16-1; 33 CFR 101.305)

4.5 **Personal information.** If employee, truck driver or other personal information may have been accessed, the General Counsel must decide whether notice is required under Fla. Stat. 501.171 (individuals no later than 30 days after the breach is determined; the Department of Legal Affairs within 30 days if 500 or more Floridians) or other state law, using the P08 notification matrix, and keep a written decision log. (IR-6; RS.CO-03; Fla. Stat. 501.171(3)-(5))

4.6 **SSI.** If SSI (for example FSP extracts, network maps or this program's vulnerability findings) may have been released to unauthorized persons, the FSO must promptly inform TSA or the applicable DHS component. (IR-6; RS.CO-02; 49 CFR 1520.9(c); 101.630(b))

4.7 No ransom may be paid without approval from the Chief Executive Officer after advice from counsel and the cyber insurer, an OFAC sanctions check, and notice to the audit committee chair. The default position is not to pay while backups are intact. (IR-4; RS.MA-03; OFAC ransomware advisory (2021-09-21))

4.8 **Safety first.** If the integrity of crane, RTG, mobile harbor crane or yard equipment controllers is in doubt, affected equipment must be stopped in a safe state. It may restart only when the Director of Maintenance and Engineering and the terminal General Manager agree that an OT integrity check has been signed off. (IR-4; RS.MI-01; 101.650(g)(2))

4.9 The Cyber Incident Response Plan must be exercised: cyber drills at least twice each calendar year, testing individual Plan elements, and a cyber scenario in the annual exercise at each terminal, with CySO participation. Key personnel must be trained on their incident roles each year. (IR-2; IR-3; ID.IM-02; PR.AT-02; 101.635(b)-(c); 101.650(d)(2))

4.10 **Crisis management and legal.** A severity 1 incident convenes the crisis management team chaired by the Chief Operating Officer. The cyber insurer's hotline is called before incident vendors are engaged, and outside counsel directs the forensic investigation under privilege. (IR-4; IR-7; RS.MA-01; 101.620(b)(6))

4.11 Port partners (both port authorities, affected carriers, the port community systems and the customs data exchange service) must be told promptly when an incident affects shared operations or data exchanged with them, and the carrier alliance as its agreement requires. (IR-4; RS.CO-03; 101.645(b))

4.12 Security events must be monitored 24x7. The MSSP monitors IT sources and must call the Security Manager within 30 minutes of a high-severity alert. OT monitoring alerts from both terminals must reach the MSSP workflow by 2027-01-31 (STD-03). (SI-4; AU-6; DE.CM-01; DE.AE-02; 101.650(h)(2))

4.13 Lessons learned must be documented within 30 days of closing an incident and fed into the risk register, the POA&M and the Cybersecurity Plan. (IR-4; ID.IM-03; ID.IM-04; 101.650(g)(3))

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.8. Sanctions range from retraining to termination of employment or of a contract, depending on intent and harm. For longshore labor, the company may refuse further access to its systems and refer the matter to the hiring hall. Compliance is checked through the annual independent assessment (P07), the Cybersecurity Assessment (33 CFR 101.650(e)(1)), the annual Cybersecurity Plan audit once the Plan is approved (101.630(f)), and the reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved under POL-01 section 4.4, recorded in the risk register (P01), and expire within 12 months. Where a Subpart F measure is not technically feasible (for example MFA on an HMI in a crane cab), the compensating control must be documented for the Cybersecurity Plan, as 101.650 allows.

## 7. Related documents
P08 runbooks and notification matrix; POL-01; Facility Security Plan reporting sections (SSI); STD-03 logging and monitoring; STD-06 contingency and recovery; 33 CFR 6.16-1; 33 CFR 101.305; 49 CFR 1520.9; Fla. Stat. 501.171
