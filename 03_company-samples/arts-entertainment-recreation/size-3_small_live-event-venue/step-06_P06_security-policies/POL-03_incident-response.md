# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | General Manager (2026-08-31) |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, AU-6, AU-11 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, DE.CM-01 |
| PCI DSS v4.0.1 (N71-R04) | 10.4, 10.5, 12.10 |
| Law | Fla. Stat. 501.171 (breach notice); other states' breach laws; FTC Act Section 5 (N71-R05) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly, meets card brand, acquirer, and breach notification deadlines, and keeps shows running safely while it does.

## 2. Scope
All Cris Santos Company employees, owners, and temporary staff, and every contractor with access to company systems. Covers suspected and confirmed incidents involving card data, patron data, ticketing platform accounts or settings, company systems, and systems that service providers run for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander for security incidents; coordinates the integrator and forensic firm |
| Controller | Acquirer and card brand notices; cyber insurer; evidence for the PCI forensic investigator |
| General Manager | Engages counsel; approves external statements; breach notification decisions with counsel |
| Director of Ticketing | Ticketing platform containment (accounts, settings) with the vendor |
| Operations Director | Event-day continuity (manual entry, safety) |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must keep an incident response plan made up of this policy and runbooks for its most likely incidents, starting with a ticketing platform breach (P08). (IR-8; RS.MA-01; PCI 12.10)
4.2 Workforce members and contractors must report any suspected incident **immediately**, and within 1 hour at most, to the IT Manager's incident line. Examples: a phishing click, a strange ticketing setting, a card reader that looks altered, a card number written down. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; PCI 12.10)
4.3 Every incident must be logged, categorized, and tracked to closure. (IR-5)
4.4 Security logs from the ticketing platform, identity provider, cloud tenant, firewall, and PCs must be kept for at least 12 months and reviewed through automated alerts daily and a manual review weekly. (AU-6; AU-11; DE.CM-01; PCI 10.4; 10.5)
4.5 **Suspected card data compromise:** the Controller must notify the acquirer within 24 hours of suspicion (merchant agreement) and follow the acquirer's instructions, including Visa's reporting timelines and any PCI forensic investigation. (IR-6; RS.CO-02; PCI 12.10)
4.6 Evidence must be preserved with chain of custody. Affected systems must be isolated from the network, not switched off or wiped, until forensics approves. (IR-4; RS.AN-03)
4.7 Notices to patrons, the Florida Department of Legal Affairs, other states, and consumer reporting agencies must meet the deadlines in the P08 notification matrix. Counsel must confirm each notice. (IR-6; RS.CO-02; RS.CO-03)
4.8 No ransom or extortion payment may be made without approval from the majority owner, counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.9 The plan must be tested by tabletop at least annually and after any major incident, and staff with incident roles must be trained on it. (IR-3; PCI 12.10)
4.10 Lessons learned must be documented within 30 days of closing an incident and added to the risk register. (IR-4; RC.RP-01)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.10. Compliance is checked through the annual control assessment (P07) and the annual tabletop exercise.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; POL-04; merchant agreement; Fla. Stat. 501.171
