# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (Security Coordinator), with the Operations Manager for the batch control system |
| Approved by | Owner and President, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes or incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, PL-1, RA-3, PS-8, SA-9, CA-2, SI-12, CM-3. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, MA-4, IA-2, IA-2(1), IA-5, PS-4, PE-3, MP-7. Part C: PL-4, AT-2 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01, PR.PS-01 |
| Benchmarks and rules | C-CHEMICAL-R01 (6 CFR 27.230(a)(8), (a)(12), (a)(17), voluntary benchmark); CISA RBPS 8 security measures; 49 CFR 172.704 |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach the batch control system, business systems, and formulations, and only as far as their job requires, and tell everyone how to use company systems.

## 2. Scope
All employees, temporary workers, and contractors of Cris Santos Company, including the MSP and the control system integrator when they act for the company. It covers every system in the Blending and Business Platform (P02), the payroll, building, and AI services, and every copy of company information. **It applies to the PLC, the HMI and recipe PC, and the remote access gateway as fully as to the office computers.**

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and President | Approves policies and the security budget; accepts Moderate and higher risk; approves recipe and alarm limit changes; reviews the account list and change log monthly |
| Office Manager (Security Coordinator) | Runs this policy for office and SaaS systems; grants and removes access; keeps the inventory, training records, and incident log |
| Operations Manager | Owns the batch control system; controls the gateway and every integrator session; manages HMI logins, the door code, and DOT hazmat training |
| MSP | Creates and disables suite and device accounts on request; operates device controls |
| Control system integrator | Works only through approved, named, MFA-protected sessions |
| Everyone | Protects passwords and MFA codes; follows Part C; reports problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Named owners.** The Office Manager is the Security Coordinator. The Operations Manager owns the batch control system and the remote access gateway. The Owner records both designations in writing and updates them within 30 days of any change. (PM-2; GV.RR-02; 27.230(a)(17))

A.2 **Risk assessment and oversight.** The Office Manager updates the risk assessment every July, and after any major change, using NIST SP 800-30 Rev. 1. Every risk has an owner and a treatment. The Owner reviews the POA&M, the account list, and the recipe change log at a monthly 30-minute meeting. (RA-3; PM-9; ID.RA-01)

A.3 **Risk acceptance.** The Office Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. A risk that could injure a person is never accepted at High. (PM-9; GV.RM-01)

A.4 **Sanctions.** Anyone who breaks a security rule is sanctioned in proportion to intent and harm: coaching, a written warning, suspension, or termination. The Office Manager records each sanction, and the Owner approves suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Vendor security terms.** No vendor may get remote access to the plant or receive Restricted information (POL-04) until its contract includes: named accounts with MFA, no access without company approval, notice of security incidents affecting the company within 24 hours, and return or deletion of company data at the end of the contract. Existing contracts are updated at renewal and no later than 2026-12-31. (SA-9; GV.SC-05)

A.6 **Evaluation.** Security controls are assessed at least once a year by someone who does not operate them, and after major changes. (CA-2; ID.IM-02)

A.7 **Records.** Security documents, risk assessments, assessments, and training records are kept at least 3 years; incident records at least 5 years. Legal retention periods in POL-04 4.9 take precedence where longer. (SI-12; GV.PO-02)

A.8 **Policy review.** The Office Manager reviews this policy set every August and after an incident or major change, and keeps the current version in the shared drive where everyone can read it. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception to any security policy must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. The shared HMI operator login is recorded as an exception until named logins are live (due 2026-11-30). (PL-1; GV.PO-01)

A.10 **Chemical screening and inventory limits.** Before the first purchase of any new raw material, the Operations Manager checks it against the RMP list (40 CFR 68.130), OSHA PSM Appendix A, CFATS Appendix A, and the DOT security plan list (49 CFR 172.800(b)), and records the result. Hydrogen peroxide is bought only below 52% and no more than 2 totes are kept on site. Any change to these limits needs the Owner's approval and an update of the SSP categorization (P02 section 6). (GV.OC-03; RA-3)

A.11 **Change control for the batch control system.** No recipe, setpoint, or alarm limit is changed without the Owner's written approval on the batch ticket. The integrator changes PLC or HMI logic only with a written change note that the Operations Manager approves before the work and checks after it. The configuration baseline and offline backup are updated after every approved change. (CM-3; PR.PS-01)

### Part B. Access control
B.1 **Unique accounts.** Everyone has their own account in the productivity suite, the accounting service, the SDS service, the integrator portal, and the HMI. Shared or generic accounts are not allowed, except as recorded under A.9. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** Access matches the job. On the HMI, operators may run batches; only the Operations Manager may edit recipes, setpoints, and alarm limits. In the accounting service, only the Owner and Office Manager may change bank details. The Office Manager approves SaaS access in writing on the onboarding checklist. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for the productivity suite, the accounting service, the SDS service, the payroll service, the integrator portal, and every administrator login, including logins held by the MSP (backup console, firewall, remote management). (IA-2(1); PR.AA-03)

B.4 **Onboarding and termination checklist.** The Office Manager and Operations Manager complete the checklist for every start and departure.
- **On the first day:** accounts created only as approved; DOT hazmat training scheduled for completion within 60 days (the legal limit is 90 days, 49 CFR 172.704(c)(1)); a signed acknowledgment of this policy.
- **On or before the last day:** disable SaaS, HMI, and portal accounts; ask the MSP to remove device access; remove MFA registrations; collect keys and devices; **change the door code and any shared OT password the person knew**; remind the person in writing of their confidentiality duty. For an involuntary termination, access is disabled before the person is told.

(PS-4; AC-2; IA-5; PE-3; AT-2)

B.5 **Monthly reconciliation.** Each month the Office Manager compares the user lists of every SaaS service, the HMI, the portal, and the backup console with the staff roster and the integrator's named staff list, removes anything that does not match, and gives the result to the Owner. (AC-2; AC-6; PR.AA-05)

B.6 **Locking.** Computers and tablets lock after 10 minutes idle. The HMI is exempt because operators must see it during a batch; the blend room is staffed whenever a batch runs and locked by keypad otherwise. (AC-11)

B.7 **Emergency access.** The administrator passwords for the HMI, the gateway, and the firewall are kept in a sealed envelope in the Owner's safe. Any use is reported to the Operations Manager, and the password is changed afterwards. (AC-2; IA-5)

B.8 **Remote access to the plant.** The cellular gateway stays powered off. The Operations Manager powers it on only for a scheduled session with a named integrator engineer, watches the session, logs its purpose and every change, and powers the gateway off at the end. Portal accounts are named and use MFA. No other remote access tool may be installed on the HMI PC. The integrator gives the Office Manager a list of its staff with access each year. (AC-17; MA-4; IA-2(1); SA-9; PR.AA-05; 27.230(a)(8))

B.9 **Passwords and shared secrets.** Passwords are at least 12 characters and never reused from personal accounts. The door code, the office Wi-Fi password, and any remaining shared OT password are changed every year and at every departure. (IA-5; PR.AA-01)

B.10 **Removable media.** Only the company USB stick may be connected to the HMI PC, and it is scanned on an MSP-managed laptop before each use. It is kept locked in the blend room control panel. (MP-7; PR.PS-01)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. (PL-4; PR.AT-01)

C.2 Never store or send Restricted information (POL-04) with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. POL-04 4.6 lists the approved AI tools. (PL-4)

C.3 Lock your screen when you step away, and never share passwords or MFA codes, including with the MSP or the integrator. (AC-11; PL-4)

C.4 Complete security awareness training at hire and every year, and take part in phishing simulations. Hazmat employees also complete DOT training, including security awareness, within 60 days of hire and every 3 years. (AT-2; PR.AT-01; 49 CFR 172.704)

C.5 Report suspected incidents at once under POL-03 4.2, including your own mistakes. (IR-6)

C.6 Sign an acknowledgment of this policy at hire and after each yearly update. (PL-4)

C.7 Use the HMI PC only to run batches. Never read email, browse the web, or connect a phone to it. (PL-4; CM-7)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. Compliance is checked through the monthly reconciliation (B.5), the Owner's monthly review (A.2), the session log (B.8), and the yearly independent assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2(1), PS-4, CM-3
