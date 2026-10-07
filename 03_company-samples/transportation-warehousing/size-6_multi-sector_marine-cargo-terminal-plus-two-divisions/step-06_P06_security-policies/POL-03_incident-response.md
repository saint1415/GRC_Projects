# Incident Response Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-03 |
| Owner | Group CISO (operated by the Group SOC director) |
| Approved by | Group CISO and Group General Counsel, under authority of POL-01, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after every major incident or exercise |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-7, IR-8, CP-2 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-04 |
| Regulatory drivers | N48-49-R01 (33 CFR 101.620(b)(6)-(7), 101.635, 101.640, 101.650(g)); 33 CFR 6.16-1; 33 CFR 101.305; N42-R03 (252.204-7012(c)-(e)); N42-R05 (52.204-25(d)); N48-49-R08 (Form 8-K Item 1.05); state breach laws |
| Division supplements | Marine Terminals: per-terminal Cyber Incident Response Plans and OT safe-state rules. Freight Trading: DFARS reporting. Port Real Estate: building system lockout and tenant notices |

## 1. Purpose
Make sure the group detects, contains, reports and recovers from cyber incidents quickly, safely and lawfully, across divisions, and meets every regulator's and customer's clock.

## 2. Scope
All workforce members, longshore workers and vendor technicians when they use group IT or OT, and every system and data set in every division and in corporate shared services, including systems operated by vendors and integrators.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Group SOC director | Group incident commander for incidents in shared services or spanning divisions; establishes the facts every notice depends on |
| Division CySO (alternates at each terminal) | Incident commander for incidents affecting a terminal; makes the 33 CFR 6.16-1 report for each affected facility |
| Facility Security Officers | Breaches of security and TSIs under each FSP (101.305); physical safety of the terminal |
| Freight Trading federal contracts compliance manager | DFARS 252.204-7012 report and FAR 52.204-25 reports |
| Group General Counsel | Runs the notification matrix; engages breach counsel and the insurer; ransom decision process |
| Disclosure committee | SEC materiality determination |
| Division presidents | Decide with operations leads on shutdown and restart of division operations |
| All workforce, longshore workers and vendors | Report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain a group incident response plan with division annexes, and Marine Terminals must maintain a Cyber Incident Response Plan for each facility (101.650(g)(2)). Runbooks must exist for the most likely incidents, starting with ransomware spreading through shared services (P08). (IR-8; RS.MA-01)

4.2 **One severity scale.** All divisions use the group severity scale (Severity 1 to 4). Any incident that affects a shared service, more than one division, OT, or a regulated facility is Severity 2 or higher and is run by a group incident commander. (IR-4; RS.MA-02)

4.3 Anyone who suspects a cyber incident must report it **immediately**, and within 1 hour at most, to the SOC hotline or to the shift superintendent, who calls the SOC and the CySO. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; 101.650(d)(1)(iv))

4.4 **Coast Guard reporting.** Evidence of an actual or threatened cyber incident involving or endangering any terminal must be reported **immediately** to the FBI, CISA and the Captain of the Port for each affected facility (33 CFR 6.16-1). The CySO or an alternate makes the report without waiting for the investigation to finish. A 6.16-1 report also meets the duty to report reportable cyber incidents to the NRC (101.620(b)(7)). Breaches of security and TSIs are reported under the FSP (101.305). (IR-6; RS.CO-02)

4.5 **All other notices** follow the group notification matrix (P08), owned by the Group General Counsel: DoD within 72 hours of discovery for incidents affecting covered defense information (252.204-7012(c)); contracting officers for covered telecommunications within 1 business day (52.204-25(d)); state breach notices for each state where affected individuals reside (Florida worked example: no later than 30 days after determination of the breach, Fla. Stat. 501.171); customers, carriers, tenants and partners under their contracts. (IR-6; RS.CO-03)

4.6 **SEC disclosure.** The SOC and division leads must give the disclosure committee the facts it needs to determine materiality without unreasonable delay after discovery. If the incident is material, the Form 8-K Item 1.05 filing is due within four business days of that determination. (IR-6; RS.CO-03)

4.7 **Safety first.** If the integrity of crane, ASC, RTG or yard equipment controllers, or of building life-safety systems, is in doubt, the affected equipment must be stopped in a safe state. It may restart only when the operations lead and the engineering lead for that site agree it is safe. (IR-4; RS.MI-01)

4.8 **Evidence.** Images of affected systems and relevant monitoring data must be preserved; where covered defense information may be involved, for at least 90 days from the DoD report (252.204-7012(e)). (IR-4; AU-11)

4.9 No ransom may be paid without approval from the board risk committee chair, the Group General Counsel and the insurer, after an OFAC sanctions check and notice to law enforcement. (IR-4)

4.10 **Exercises.** Each terminal must run cyber drills at least twice each calendar year and a cyber exercise at least once each calendar year, with no more than 18 months between exercises (101.635). The group must run a cross-division tabletop each year that tests the notification matrix. (IR-3; IR-2)

4.11 Every incident must be logged and tracked to closure. Records of cyber threats, reportable cyber incidents, drills and exercises must be kept at least 2 years (101.640; 33 CFR 105.225). (IR-5)

4.12 Lessons learned must be documented within 30 days of closing a Severity 1 or 2 incident and fed into the risk registers and the Cybersecurity Plans. (IR-4; ID.IM-04)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.8. Compliance is checked through the P07 assessment of the SOC's incident handling, the annual cross-division tabletop, and terminal drill records.

## 6. Exceptions
Exceptions follow POL-01 section 4.12. Statements 4.4 and 4.5 implement legal duties and cannot be waived.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; Facility Security Plans and draft Cybersecurity Plans (SSI); 33 CFR 6.16-1; 33 CFR 101.305; DFARS 252.204-7012; Form 8-K Item 1.05.
