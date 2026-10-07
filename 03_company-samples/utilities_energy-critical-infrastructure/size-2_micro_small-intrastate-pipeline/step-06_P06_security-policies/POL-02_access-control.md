# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Office Manager (security program coordinator); Operations Manager for the SCADA and field device rules |
| Approved by | Owner, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after major changes, incidents, or a TSA designation |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, SA-9, SR-6, CA-2, CM-3, SI-12, PL-1, PS-8. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, AU-6, CM-7, IA-2, IA-2(1), IA-2(2), IA-5, MA-4, PS-4. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-07, ID.RA-01, ID.IM-01, PR.PS-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AT-01, DE.AE-02 |
| Pipeline safety link | 49 CFR 192.605 (O&M procedures, including change of field equipment); 192.631(a)(1)(ii) reduced scope |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people can see or control the pipeline through SCADA, and only as far as their job requires, and tell everyone how to use company systems.

## 2. Scope
All employees, contractors, and vendors with access to company systems: the hosted SCADA tenant, the gas control desk, the controller laptops, the field devices and gateways at all 7 sites, office IT, and business SaaS, including systems the SCADA vendor and the MSP run for the company.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate and higher risk; reviews SCADA users and the command log monthly |
| Operations Manager | SCADA security owner: creates and removes SCADA accounts, approves changes that affect SCADA, keeps the PSGCS inventory |
| Office Manager | Security program coordinator: runs this policy, the risk register, vendor contracts, and office IT accounts with the MSP |
| MSP | Creates and disables office accounts on request; operates office device controls |
| All staff | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Roles.** The Owner is accountable for security. The Office Manager is the security program coordinator, and the Operations Manager is the SCADA security owner. The Owner must record these designations in writing and update them within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Office Manager and the Operations Manager must update the risk assessment every July, and after any major change such as a new SCADA vendor, a new SCADA module, or a TSA designation, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Office Manager (office IT) and the Operations Manager (SCADA and field) may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. (PM-9; GV.RM-01)

A.4 **Suppliers.** No vendor may reach SCADA, a field device, the gas control desk, or Restricted information until a contract with security terms is in place: security incident notice within 24 hours, notice before vendor support sessions and platform changes, and return or deletion of company data at exit. The Office Manager reviews the SCADA vendor's SOC 2 report and an MSP security questionnaire every year. (SA-9; SR-6; GV.SC-05; GV.SC-07)

A.5 **Independent assessment.** Security controls must be assessed at least once a year by someone who does not operate them. (CA-2; ID.IM-01)

A.6 **Changes that affect SCADA.** SCADA display, point, alarm, or role changes; vendor releases and new modules; field device firmware updates; and SIM or gateway replacements must be approved by the Operations Manager and recorded before or, for vendor releases, when they take effect. Field changes also follow the O&M manual. (CM-3; PR.PS-01)

A.7 **Retention.** Security policies, risk assessments, assessments, incident records, vendor reviews, and training records must be kept for at least 3 years, and longer where PHMSA or FPSC record rules require. (SI-12; GV.PO-02)

A.8 **Policy review and access to policies.** The Office Manager must review POL-02, POL-03, and POL-04 every September and after an incident or major change, and keep the current versions in the shared drive where every employee can read them. (PL-1; GV.PO-02)

A.9 **Exceptions.** An exception must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

A.10 **Sanctions.** Breaking a security rule leads to coaching, a written warning, or dismissal, in proportion to intent and harm. The Owner decides. Reporting a mistake in good faith is never sanctioned. (PS-8)

### Part B. Access control
B.1 **Named accounts.** Every person must have their own account in SCADA, the productivity suite, and accounting. Shared or generic logins are not allowed, including at the gas control desk. (IA-2; AC-2; PR.AA-01)

B.2 **Least privilege.** The controller role (command rights) is limited to the 3 qualified controllers. The administrator role is used only to make configuration changes, never for routine monitoring. Everyone else gets the viewer role or no SCADA access. The Owner approves SCADA access in writing before it is granted. (AC-2; AC-3; AC-6; PR.AA-05)

B.3 **MFA.** MFA is required for every SCADA account, the productivity suite, accounting, and every administrator login, including logins held by the MSP. So that MFA never blocks a safety action, the Owner keeps a sealed break-glass credential for one controller account in the office safe; any use is logged and the password changed afterwards. (IA-2(1); IA-2(2); PR.AA-03)

B.4 **Termination.** On or before a person's last day, the Office Manager completes the last-day checklist: SCADA account disabled first, then suite, accounting, and the interstate pipeline portal; MFA registrations removed; laptop, keys, and padlock keys collected; and any password or combination the person knew changed. For an involuntary departure, access is disabled before the person is told. (PS-4; AC-2; PR.AA-05)

B.5 **Monthly review.** Each month the Owner reviews the SCADA user list and the command and sign-in log summary, and the Office Manager compares suite and accounting users with the staff list. Anything that does not match is removed or explained in writing. Every quarter the Owner confirms each SCADA role still fits the job. (AC-2; AU-6; PR.AA-05; DE.AE-02)

B.6 **Where SCADA may be used.** SCADA command rights may be used only from company-managed devices: the gas control desk, the 3 controller laptops, and the spare clean laptop. Never from a personal device. Browsers must not save SCADA passwords. (AC-17; PR.AA-05)

B.7 **Vendor and MSP sessions.** SCADA vendor support staff may enter the tenant only after notice to the Operations Manager, except during a vendor platform emergency, when notice follows within 24 hours. MSP remote-control sessions on the gas control desk need the Operations Manager's approval each time. (MA-4; AC-17; PR.AA-05)

B.8 **Device and field passwords.** No gateway, RTU, flow computer, firewall, or Wi-Fi device may keep a manufacturer default password. Each device gets a unique password, recorded on a sealed list in the office safe and changed when anyone who knew it leaves. (IA-5; PR.AA-01)

B.9 **Gas control desk.** The desk workstations are for SCADA only: no email, no browsing other than the SCADA web client, no personal use. They are exempt from screen lock so alarms stay visible, so the desk must be in view of staff during business hours and the office locked after hours. (CM-7; AC-11; PR.PS-01)

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Limited personal use of office laptops is allowed if it creates no risk; no personal use of any kind is allowed on the gas control desk or the spare SCADA laptop. (PL-4; PR.AT-01)

C.2 Staff must not put Restricted or Internal information (POL-04) into personal email, personal cloud storage, messaging apps, or public AI chatbots. (PL-4)

C.3 Staff must never share passwords or MFA codes, including with the SCADA vendor or the MSP, and must lock laptops when stepping away. (IA-5; PL-4; PR.AA-03)

C.4 Staff must complete security training at hire and every year, and take part in phishing simulations. Controllers also complete the cyber scenarios in emergency plan training. (AT-2; PR.AT-01)

C.5 Staff must report suspected incidents at once under POL-03 4.2, including their own mistakes and lost devices. (IR-6)

C.6 Staff must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.10. The Owner checks compliance through the monthly review (B.5), and the independent assessor through the annual assessment (P07).

## 6. Exceptions
Exceptions follow A.9.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; last-day checklist; O&M manual; emergency plan; P01 risk register; P02 SSP control statements AC-2, AC-17, IA-2(1), IA-2(2), MA-4
