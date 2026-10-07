# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office and Compliance Manager (Information Security Officer) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, PS-8, SA-9, SR-3, SR-5, CA-2, SI-12, PL-1. Part B: AC-1, AC-2, AC-3, AC-6, AC-17, IA-2, IA-2(1), IA-5, MA-4, PS-4. Part C: PL-4, AC-20, AT-2, AT-3, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-06, ID.RA-01, ID.IM-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01 |
| Customer and legal drivers | County security exhibit (SP 800-53 Rev. 5 Moderate, MFA); city cybersecurity standards; FAR 52.204-21(b)(1), 52.204-23, 52.204-25, 52.204-30, 52.204-9(b) (CT-F); Fla. Stat. 501.171(2), 119.0701(2)(b) |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach the customers' buildings and data and only as far as their job requires, and tell the workforce how to use company systems.

## 2. Scope
All workforce members of Cris Santos Company, and the MSP, vendors, and subcontractors when they use company systems or customer data. It covers the Building Systems Operations Platform (SYS-01 to SYS-08), the company's accounts on customer systems (the city systems and the GSA building), and every copy of customer data, drawings, and CUI.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate and higher risk; approves every new administrator account; decides sanctions |
| Office and Compliance Manager | Information Security Officer; runs this policy; grants and removes access; reviews logs and accounts; runs supplier screening for CT-F |
| Lead Controls Technician | Administers SYS-02 and the gateways under Part B |
| Security Systems Technician | Administers SYS-01 under Part B |
| MSP | Creates and disables suite and laptop accounts on request; operates laptop controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Information Security Officer.** The Office and Compliance Manager is the designated Information Security Officer and CUI program lead. The owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Information Security Officer must update the risk assessment every July, and after any major change such as a new contract, a new platform, or expanding the face verification pilot, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Information Security Officer may accept Low and Very Low risks. Only the owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the owner. A risk to the safety of building occupants at High is never accepted. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The owner decides and the Information Security Officer records each sanction. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendors and the MSP.** No vendor, the MSP, or a subcontractor may receive customer data or administrator access until it has agreed in writing to protect it and to tell the company of any security incident within 24 hours. The Information Security Officer reviews the MSP, the SYS-01 and SYS-02 vendors, and the backup provider once a year (SOC 2 report or questionnaire). (SA-9; GV.SC-05; GV.SC-06; Fla. Stat. 501.171(2))

A.6 **Federal parts screening (CT-F).** Before any equipment, software, or service is supplied to or used at the federal building, the Information Security Officer must confirm it is not a Kaspersky covered article, does not use covered telecommunications or video surveillance equipment, and is not covered by a FASCSA order, and must search SAM.gov for "FASCSA order" before each order and at least every three months. Network, controller, and camera parts may be bought only from authorized distributors. Anything found is reported under POL-03 4.8. (SR-3; SR-5; FAR 52.204-23; 52.204-25(b)(1); 52.204-30(b))

A.7 **Assessment.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; ID.IM-01)

A.8 **Records and public records.** Customer records belong to the customer. The Information Security Officer must keep a retention schedule, send any public records request to the customer's custodian, provide records the custodian asks for within a reasonable time, keep exempt records confidential, and return or destroy customer data at contract end as each contract requires (the county: within 30 days). Security records are kept at least 3 years, or longer where a contract requires. (SI-12; GV.PO-02; Fla. Stat. 119.0701(2)(b))

A.9 **Policy review and exceptions.** The Information Security Officer must review this policy set every August and after any incident or major change. An exception must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01; GV.PO-02)

### Part B. Access control
B.1 **Named accounts only.** Every person must have their own account on SYS-01, SYS-02, the gateways, the suite, the CMMS, and customer systems. Shared or generic accounts, including the SYS-02 "oncall" account, are not allowed. (AC-2; IA-2; PR.AA-01; FAR 52.204-21(b)(1)(v))

B.2 **Least privilege.** Access must match the job. Day-to-day SYS-01 and SYS-02 work uses operator roles; administrator roles are limited to 2 named people per platform, and the owner approves each administrator account in writing. Technicians use a separate local administrator account on laptops only when an engineering tool needs it. (AC-3; AC-6; PR.AA-05; FAR 52.204-21(b)(1)(ii))

B.3 **MFA.** MFA is required for SYS-01, SYS-02, the suite, the CMMS, the gateway VPN, the backup console, and the MSP's remote management tool. MFA push approvals must use number matching where offered. (IA-2(1); PR.AA-03; county security exhibit)

B.4 **Termination.** On or before a workforce member's last day, the Information Security Officer must complete the termination checklist: disable accounts on every platform, gateway, and customer system; change any shared secret the person knew; remove MFA registrations; collect keys, devices, and site badges; return any GSA PIV card through the prime; and remind the person in writing of their confidentiality duty. For an involuntary termination, access is disabled before the person is told. (PS-4; AC-2; PR.AA-05; FAR 52.204-9(b))

B.5 **Monthly reconciliation.** Each month the Information Security Officer must compare the user lists of SYS-01, SYS-02, the gateways, the suite, the CMMS, the backup console, and the city systems with the staff roster, remove anything that does not match, and show the result to the owner. (AC-2; AC-6; PR.AA-05)

B.6 **Remote access to buildings.** Remote access to customer BAS networks is allowed only through the company gateway VPN with MFA from a company laptop, or through the customer's own VPN. Unattended remote-access tools, port forwards, and vendor remote support into customer networks are not allowed without the customer's written approval and the owner's approval. (AC-17; MA-4; PR.AA-05)

B.7 **Passwords and defaults.** Passwords must be at least 14 characters, unique, and stored only in the company password manager. No device may be put into service with a manufacturer default password; the commissioning checklist confirms it. (IA-5; PR.AA-01; FAR 52.204-21(b)(1)(vi))

B.8 **Emergency access.** A sealed break-glass credential for one SYS-01 administrator account is kept by the owner for use when both administrators are unavailable during a lockdown request. Any use is reported to the Information Security Officer and the password changed afterwards. (AC-2; PR.AA-05)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems and customer data are for contract work only. Workforce members must look up cardholder records, video, or drawings only when a work order or customer request requires it. (PL-4; PR.AT-01)

C.2 Workforce members must not store or send customer data, drawings, or CUI with personal email, personal cloud storage, messaging apps, or public AI chatbots. POL-04 section 4.7 lists the approved AI tools. (PL-4; PR.AT-01)

C.3 Company devices must never be connected to the GSA Building Systems Network; GSA work is done only on GSA-furnished equipment. Personal devices may not hold customer data. (AC-20; FAR 52.204-21(b)(1)(iii))

C.4 Workforce members must complete company security training at hire and every year, take part in phishing simulations, and complete every training a customer requires (the county's basic cybersecurity training; GSA annual IT security training for PIV holders). Administrators and CUI handlers also complete role-based training. (AT-2; AT-3; PR.AT-01)

C.5 Workforce members must report suspected incidents at once under POL-03 section 4.2, including their own mistakes. (IR-6; RS.MA-02)

C.6 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. The acknowledgment is also the access agreement for customer data and CUI. (PL-4; PS-6)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Information Security Officer checks compliance through the monthly reconciliation (B.5), the weekly log review, and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; gateway commissioning checklist; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2, IA-5, PS-4, SR-3
