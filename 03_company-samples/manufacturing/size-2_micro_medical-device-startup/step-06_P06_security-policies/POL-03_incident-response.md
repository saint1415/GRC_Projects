# Incident Response Policy (including Product Security Incidents and Coordinated Vulnerability Disclosure)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Head of Engineering (Product Security Lead), with the Operations Manager for corporate IT incidents |
| Approved by | CEO, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), before commercial distribution, and after any incident that required outside notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, RA-5(11), PM-15, SR-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-02, ID.RA-08, RC.RP-01, ID.IM-02 |
| Regulatory basis | FD&C Act 524B(b)(1)-(2) (N31-33-R05); after commercial distribution, 21 CFR 820.35(a), Part 803, and Part 806; Fla. Stat. 501.171 for workforce personal information |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents in its own systems and in WM-1 units, handles vulnerability reports from outsiders in a coordinated way, and meets every notification duty on time.

## 2. Scope
All workforce members, contractors, and every company system, WM-1 unit, and release, including systems run for the company by the MSP, SaaS vendors, the cloud provider, and the contract manufacturer. Two kinds of events are covered:
- **Security incidents:** any attempted or successful unauthorized access, use, disclosure, change, or destruction of company information or systems, including lost devices and leaked secrets.
- **Product security events:** a vulnerability report, or evidence that a WM-1 unit, the cloud service, the update path, or the signing key has been attacked or could be.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Head of Engineering | Incident lead for product security events; runs CVD; keeps the vulnerability records |
| Operations Manager | Incident lead for corporate IT incidents; calls the MSP and the insurer's hotline; keeps the incident log |
| CEO | Backup lead for both; approves outside communications, spending, and any ransom decision |
| QA/RA Manager | Regulatory decisions (complaint, MDR, correction) once WM-1 is marketed; FDA communications |
| MSP | Technical response for laptops, the suite, and the network |
| Cyber insurer and its panel vendors | Breach counsel and forensics, engaged through the insurer's hotline |
| All workforce | Report at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most serious likely event, an exploited vulnerability in a fielded WM-1 unit (P08), with a printed copy and contact list in the office and at the CEO's and Head of Engineering's homes. (IR-8; RS.MA-01)

4.2 Workforce members must report any suspected incident or vulnerability **at once, and within 1 hour at most**, by phone: product issues to the Head of Engineering, IT issues to the Operations Manager, and to the CEO if neither answers. Examples: a leaked key or password, a suspicious login alert, a strange message from a hub, a lost laptop, or an email claiming to have found a flaw in WM-1. (IR-6; RS.MA-02)

4.3 The incident lead must log every incident and vulnerability report, including those that turn out to be harmless, with the date found, what happened, what was done, and the outcome. Product security records are kept in the eQMS. (IR-5)

4.4 **Coordinated vulnerability disclosure.** The company must publish a CVD policy and a security contact on its website. The Head of Engineering must acknowledge each report within 3 business days, keep the reporter informed, agree a disclosure date, and credit the reporter if they wish. The company will not take legal action against good-faith research that follows the published policy. (RA-5(11); RS.CO-03; ID.RA-08; 524B(b)(1))

4.5 **Vulnerability assessment.** Each vulnerability must be assessed for exploitability and for its effect on safety and essential performance, and recorded as a controlled or uncontrolled risk, as FDA's postmarket guidance describes. The record links to the threat model and the cybersecurity risk assessment. (RS.AN-03; IR-4)

4.6 **Patches.** Fixes for known unacceptable vulnerabilities go into the regular security maintenance cycle. Critical vulnerabilities that could cause uncontrolled risk get an out-of-cycle fix as soon as possible, through the two-person release process in POL-02 A.11. (RS.MI-02; SI-2; 524B(b)(2)(A)-(B))

4.7 **Regulatory decisions after marketing.** Once WM-1 is in commercial distribution, the QA/RA Manager must screen every product security event as a possible complaint (21 CFR 820.35(a)) and decide, and record, whether it needs a medical device report (Part 803) or a correction or removal report (Part 806), using the P08 notification matrix. (IR-6; RS.CO-02)

4.8 **Company data and extortion.** For suspected data theft, account takeover, or extortion affecting company systems, the Operations Manager must call the cyber insurer's hotline before hiring any outside firm, and engage the MSP. Breach counsel reviews any notice to individuals under Fla. Stat. 501.171. (IR-4; RS.MA-02)

4.9 No ransom or extortion payment may be made without the CEO's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.10 **Suppliers.** The contract manufacturer, the MSP, and the cloud and SaaS vendors must report security incidents affecting company data or WM-1 production to the incident lead as their contracts require (72 hours for the contract manufacturer under POL-02 A.5). Each report is logged and handled under this policy. (IR-6; SR-3; GV.SC-08)

4.11 The runbook must be tested every year with a tabletop exercise that includes the MSP, before commercial distribution, and after any real incident that used it. (IR-3; ID.IM-02)

4.12 Lessons learned must be written up within 30 days of closing any incident that required outside help or notice, and fed into the threat model, the risk register, and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake or vulnerability in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a legally required notification or a patch for a critical vulnerability.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; cybersecurity management plan (planned, P03 G-040); complaint, MDR, and correction procedures (eQMS, drafts)
