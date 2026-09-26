# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | IT Manager |
| Approved by | General Manager |
| Effective date | 2026-09-04 |
| Review cycle | Annually (next review 2027-09-04), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-2, IR-3, IR-4, IR-5, IR-6, IR-8, AU-6, AU-11, SI-4 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, DE.CM-03, ID.IM-03 |
| PCI DSS v4.0.1 (N44-45-R01) | 12.10 |
| Law and contract | Fla. Stat. 501.171 and other states' breach laws; merchant agreement (acquirer notice within 24 hours of suspecting a compromise) |

## 1. Purpose
Make sure the company detects, contains, reports, and recovers from security incidents quickly and lawfully, meets its merchant agreement, and meets breach notification deadlines.

## 2. Scope
All Cris Santos Company workforce members (owners, employees, and temporary staff) and contractors with access to company systems, including the marketing contractor. Covers the store, online ordering, and all systems and data, including systems that service providers operate for the company (storefront, payment processor, POS vendor, cloud provider, pricing engine vendor). It applies to cardholder data wherever it could appear, customer and loyalty member data, workforce data, and all other company information.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| IT Manager | Incident commander; coordinates the storefront vendor, processor, POS vendor, and forensic firm |
| General Manager | Engages counsel and the cyber insurer; approves external communications |
| Controller | Notifies the acquirer under the merchant agreement; manages the insurer claim |
| E-commerce and Marketing Manager | Storefront and checkout page actions; customer communications |
| Store Manager | Store-side actions (PIN pads, POS back office, building systems) |
| All workforce and contractors | Report suspected incidents immediately |

## 4. Policy statements
4.1 The company must maintain an incident response plan and runbooks for its most likely incidents, starting with e-commerce skimming (P08). (IR-8; RS.MA-01; PCI DSS 12.10)
4.2 Workforce members and contractors must report any suspected incident **immediately**, and within 1 hour at most, by calling the IT Manager's incident line or telling the manager on duty. Examples: a PIN pad that looks altered, an unexpected change or script on the checkout page, customers reporting card fraud after online orders, phishing clicks, lost handhelds, and card numbers received by email. Good-faith reporting is never sanctioned. (IR-6; RS.MA-02; PCI DSS 12.10)
4.3 Every incident must be logged, categorized, and tracked to closure in the help desk tool under the Security category. (IR-5)
4.4 Storefront admin, identity provider, and cloud logs must be kept for at least 1 year and reviewed weekly. Alerts from the payment page monitoring service must be triaged the same day. (AU-6; AU-11; SI-4; DE.CM-03; PCI DSS 12.10)
4.5 **Acquirer notice.** When a compromise of card data is suspected, the Controller must notify the acquirer within 24 hours, as the merchant agreement requires, and follow the acquirer's instructions, including any requirement to engage a PCI forensic investigator. (IR-6; RS.CO-02)
4.6 Evidence must be preserved before cleanup: capture the malicious script, page versions, and logs, and keep a chain of custody. (IR-4; RS.AN-03)
4.7 Notifications to individuals, state authorities, consumer reporting agencies, and law enforcement must meet the deadlines in the P08 notification matrix. Legal counsel must confirm each notification. (IR-6; RS.CO-02; RS.CO-03)
4.8 No ransom or extortion demand may be paid without approval from the majority owner, legal counsel, and the cyber insurer, and an OFAC sanctions check. (IR-4)
4.9 Staff with incident response duties must be trained at hire into the role and annually. The plan must be tested at least annually by tabletop exercise, and after any major incident. (IR-2; IR-3; PCI DSS 12.10)
4.10 Lessons learned must be documented within 30 days of closing an incident, and the risk register, POA&M, and runbooks updated. (IR-4; ID.IM-03)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement in POL-01 section 4.10. Sanctions range from retraining to termination of employment or contract, depending on intent and harm. Compliance is checked through the annual control assessment (P07), the quarterly access reviews (POL-02 4.6), and the PCI DSS self-assessment each year.

## 6. Exceptions
Exceptions follow POL-01 section 4.7. They must be written, risk-rated, approved by the policy owner (or by the majority owner for High risk), recorded in the risk register, and expire within 12 months. No exception may allow card numbers to be entered or stored outside the P2PE devices and the processor's payment form.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-01; merchant agreement; cyber insurance policy; Fla. Stat. 501.171
