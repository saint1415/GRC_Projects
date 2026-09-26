# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | Chief Operating Officer |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, SR-8, SR-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01 |
| Contract and regulatory basis | DFARS 252.204-7012(c) to (g); FAR 52.204-25(d); DFARS 252.246-7008(b)(3)(ii); SP 800-171 3.6.1 to 3.6.3; Fla. Stat. 501.171 |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents and supply chain compromises quickly and lawfully, and meets its DoD reporting clocks.

## 2. Scope
All Cris Santos Company workforce members, the MSP, and all company systems and data. Also covers incidents that start at a supplier or customer but affect the company's systems, orders, payments, or products, including counterfeit, tampered, or covered equipment.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for cyber incidents; coordinates the MSP and forensic firm |
| Purchasing and Supplier Manager | Incident commander for product incidents (suspect counterfeit, tampered, or covered items) |
| Government Contracts Manager | DIBNet, contracting officer, and prime notices; keeps the medium assurance certificate |
| Chief Operating Officer | Engages counsel and the cyber insurer; approves external communications |
| Warehouse and Logistics Manager | Quarantines suspect stock and holds shipments |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with supplier compromise that introduces tampered or counterfeit products (P08). (IR-8; RS.MA-01; SP 800-171 3.6.1)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, to the IT Manager's incident line. Examples: phishing clicks, unexpected supplier bank-change requests, lost devices, CUI outside the lab or CUI share, suspect counterfeit or tampered items, and products that may come from a covered manufacturer. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure in the ticketing system under the Security category. (IR-5; SP 800-171 3.6.2)
4.4 **Suspect products.** Suspect counterfeit, tampered, or covered items must be quarantined at once, must not ship, and must be kept until the prime or contracting officer gives disposition instructions. Shipments already made must be traced by serial number. (SR-11; IR-4)
4.5 **Reporting clocks.** The Government Contracts Manager must meet the deadlines in the P08 notification matrix, including:
- a DIBNet report within 72 hours of discovering a cyber incident that affects a covered contractor information system or the covered defense information in it, with the DoD incident report number sent to Prime B as soon as practicable (DFARS 252.204-7012(c), (m));
- a covered telecommunications equipment report within 1 business day of identification, with further information within 10 business days (FAR 52.204-25(d));
- prompt written notice to the contracting officer, through Prime B, when a DoD job uses electronic parts from a source outside the authorized sourcing order (DFARS 252.246-7008(b)(3)(ii)(A));
- personal information breach notices under Fla. Stat. 501.171 and the law of each state where affected individuals reside.

Legal counsel confirms each external notice. (IR-6; RS.CO-02; RS.CO-03)
4.6 When a cyber incident affects CUI systems, images of affected systems and relevant monitoring data must be preserved for at least 90 days after the DIBNet report. Malicious software is submitted to the DoD Cyber Crime Center as instructed, never to the contracting officer. (IR-4; DFARS 252.204-7012(d), (e))
4.7 The company must keep a DoD-approved medium assurance certificate held by the Government Contracts Manager and one backup, so it can report through DIBNet. (IR-6; DFARS 252.204-7012(c)(3))
4.8 No ransom may be paid without approval from the Chief Executive Officer, legal counsel, and the cyber insurer, and an OFAC sanctions check. The insurer's hotline must be called before incident vendors are engaged. (IR-4)
4.9 The incident response plan must be tested at least annually by tabletop exercise, and after any major incident. (IR-3; SP 800-171 3.6.3)
4.10 Lessons learned must be documented within 30 days of closing an incident and added to the risk register and the C-SCRM plan. (IR-4; ID.IM)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (POL-01 section 4.7). Sanctions range from retraining to termination, depending on intent and harm. Compliance is checked through the annual control assessment (P07) and the annual tabletop exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the Chief Executive Officer for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; POL-04; DFARS 252.204-7012; FAR 52.204-25; DFARS 252.246-7008; Fla. Stat. 501.171
