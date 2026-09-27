# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or changes to payment design |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-04 |
| PCI DSS v4.0.1 | Requirement 12.10 |

## 1. Purpose
Make sure the hotel detects, contains, reports, and recovers from security incidents quickly and lawfully, and meets acquirer, card brand, and breach notification deadlines.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, contractors, and staff supplied by the staffing company) at the hotel, its restaurant, and its bars. Covers all systems and data, including services that vendors operate for the hotel (PMS, payment services, booking engine, channel manager, cloud tenant, chatbot, and pricing system). It applies to payment card data, guest personal information, and all other hotel information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander; coordinates the MSP, the forensic firm, and (if required) the PCI Forensic Investigator |
| Controller | Notifies the acquirer; manages card brand requests; engages the cyber insurer |
| General Manager | Engages breach counsel; approves guest and public communications; decides breach notices with counsel |
| Front Office Manager, Food and Beverage Director, Chief Engineer | Run downtime procedures and preserve devices in their areas |
| All workforce | Report suspected incidents immediately |

## 4. Policy statements
4.1 The hotel must maintain an incident response plan and runbooks for its most likely incidents, starting with a POS and reservation system compromise (P08). The plan must cover business recovery (P05) and legal notices. (IR-8; RS.MA-01; PCI 12.10.1)
4.2 Workforce members must report any suspected incident **immediately**, and within 1 hour at most, by calling the IT Manager's incident line or telling their manager. Examples: phishing clicks, a caller asking for card details, a terminal that looks tampered with, card numbers found in email or chat, lost key encoders, unusual PC behavior. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02)
4.3 Every incident must be logged, categorized, and tracked to closure. (IR-5)
4.4 **Suspected card compromise.** The Controller must notify the acquirer within the merchant agreement's deadline (24 hours of suspicion; fictional contract term) and make sure the compromise is reported to Visa within 3 calendar days under Visa's What To Do If Compromised requirements (version 10.0, effective 2026-06-25), and to other brands under their rules. Compromised systems must be isolated but **not powered off, rebuilt, or logged into with administrator credentials** until evidence is preserved. (IR-4; IR-6; RS.CO-02)
4.5 The General Manager and breach counsel must decide whether an incident requires notice under Fla. Stat. 501.171 or other states' laws, document the decision, and meet the deadlines in the P08 notification matrix. (IR-6; RS.CO-02; RS.CO-03)
4.6 No ransom may be paid without approval from the majority owner, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.7 The incident response plan must be tested at least annually by tabletop exercise, and after any major incident. (IR-3; PCI 12.10.2)
4.8 Lessons learned must be documented within 30 days of closing an incident and added to the risk register. (IR-4; ID.IM-04)

## 5. Compliance and enforcement
Violations are handled under the sanctions rule in POL-01 section 4.8. Sanctions range from retraining to termination, depending on intent and harm. For contracted staff, the staffing company is asked to remove the person from the hotel assignment. Compliance is checked through the annual control assessment (P07), the PCI DSS self-assessment, and the access reviews in this policy set.

## 6. Exceptions
Exceptions follow POL-01 section 4.6. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), and expire within 12 months. No exception may allow storage of card security codes after authorization.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; merchant agreements; Visa What To Do If Compromised; Fla. Stat. 501.171
