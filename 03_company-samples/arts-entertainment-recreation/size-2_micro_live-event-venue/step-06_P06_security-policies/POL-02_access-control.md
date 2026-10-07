# Access Control Policy (with Program Governance and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Venue Manager (Security and Privacy Lead) |
| Approved by | Owner and General Manager, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes such as a new payment channel, ticketing platform, or website, or after incidents |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, PS-8, CM-3, CM-7, CM-8, PL-1, PL-2, SA-9, SR-6, CA-2, PT-5, SI-7. Part B: AC-1, AC-2, AC-3, AC-6, AC-11, AC-17, AC-18, IA-2, IA-2(1), IA-5, PS-4, SC-7. Part C: PL-4, AT-2, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.OC-03, GV.SC-05, GV.SC-07, ID.RA-01, ID.AM-03, PR.PS-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.IR-01, PR.AT-01 |
| PCI DSS v4.0.1 (N71-R04) | 1.3, 2.2, 2.3, 6.4.3, 6.5, 7.2, 8.2, 8.3, 8.4, 8.6, 11.6.1, 12.1, 12.2, 12.3, 12.5, 12.6, 12.8 |
| Law (N71-R05) | FTC Act Section 5, 15 U.S.C. 45(a) and 45(n); Rule on Unfair or Deceptive Fees, 16 CFR Part 464 |

**Why this policy has three parts.** A 7-person club does not need five separate policies. This policy carries the program governance rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program, make sure only authorized people reach patron data, card devices, and company systems, and only as far as their job requires, and tell the workforce and contractors how to use company systems.

## 2. Scope
All Cris Santos Company employees and owners, and every contractor with access to company systems or card devices: the MSP, the freelance web designer, and event-night workers from the staffing contractors. It covers every system and copy of company information, including systems run for the company by the ticketing vendor, the payment partner, the POS vendor, the MSP, and other SaaS providers.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner and General Manager | Approves policies and the security budget; accepts Moderate risk; approves dated plans for High risk; signs the SAQs and AOCs; decides sanctions |
| Venue Manager | Security and Privacy Lead; runs this policy; keeps the inventory, service provider list, and change log; runs the monthly account check with the system owners |
| Box Office and Ticketing Manager | Grants and removes ticketing access; owns ticketing settings, price tiers, and demand tools |
| Marketing Coordinator | Owns website content and scripts and the price displays in marketing |
| MSP | Creates and disables suite and computer accounts on the Venue Manager's request; runs the network and device controls |
| All workforce and contractors | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance (essentials of POL-01)
A.1 **Security and Privacy Lead.** The Venue Manager is the designated Security and Privacy Lead and PCI DSS contact. The Owner must record the designation in writing and update it within 30 days of any change. (PM-2; GV.RR-02)

A.2 **Risk assessment.** The Venue Manager must update the risk assessment every July, and after any major change such as a new payment channel, ticketing platform, or website, using NIST SP 800-30 Rev. 1. Every risk must have an owner and a treatment in the risk register. Where PCI DSS lets the company choose how often a control runs, the choice and its reason must be recorded in the risk register (targeted risk analysis). (RA-3; PM-9; ID.RA-01; PCI 12.3)

A.3 **Risk acceptance.** The Venue Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. Risks to attendee safety at High are never accepted. (PM-9; GV.RM-01)

A.4 **Sanctions.** Anyone who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, termination, or removal of a contractor's access. The Owner decides suspension, termination, or contractor removal. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **PCI DSS scope.** The Venue Manager must keep a scope document for each merchant account and payment channel, with a card data-flow diagram. It must be confirmed every year and before any new payment channel, card device, payment link, or website change that touches buying tickets. Every SAQ answer must have evidence in the Bookkeeper's SAQ folder before the Owner signs. (CM-8; PL-2; ID.AM-03; PCI 12.5)

A.6 **Service providers.** Before any provider stores, processes, or sends card or patron data for the company, or can affect their security, it must be on the service provider list with the Owner's approval and a written agreement that covers security duties and breach notice. Providers that touch card data or the payment pages must supply a current PCI DSS AOC and a responsibility matrix, checked at least once a year. (SA-9; SR-6; GV.SC-05; GV.SC-07; PCI 12.8)

A.7 **Assessment.** Security controls must be assessed at least once a year by someone who does not operate them, and after major changes. (CA-2)

A.8 **Prices and privacy claims.** Every ticket price the company shows or advertises (website, email, social media, posters, phone scripts) must show the total price including the mandatory service and facility fees, more prominently than any other price, and fee names must say what each fee is for. The privacy notice must match actual data practices. The Marketing Coordinator checks both before publication. (PT-5; GV.OC-03; 16 CFR 464.2 and 464.3; 15 U.S.C. 45(a))

A.9 **Policy review, acknowledgment, and records.** The Venue Manager must review this policy set every August and after an incident or major change, and keep the current version in the shared suite folder. Every employee must acknowledge the policies at hire and each year. Security records (risk assessments, assessments, incident records, SAQ evidence) must be kept at least 5 years. (PL-1; GV.PO-02; PCI 12.1)

A.10 **Change control.** Changes to the website (pages, plugins, scripts), ticketing settings (checkout widget, users and roles, price tiers, demand tools, API tokens), payment settings, and firewall rules must be requested, approved by the Owner or the system owner named in section 3, and recorded in the change log before they go live. (CM-3; PR.PS-01; PCI 6.5)

A.11 **Payment pages.** No script, tag, pixel, or plugin may run on a page that hosts the checkout widget unless it is on the approved script list with its owner and business reason, approved by the Owner. The web designer must compare those pages with the approved list every week and record the result, and website change alerts must go to the Marketing Coordinator and Venue Manager. (CM-7; CM-8; SI-7; PR.PS-01; PCI 6.4.3; 11.6.1)

A.12 **Exceptions.** An exception to any security policy must be requested in writing, rated with the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months or less. (PL-1; GV.PO-01)

### Part B. Access control
B.1 **Named accounts.** Every person must have their own account in the ticketing platform, the website, and the productivity suite. Shared or generic logins are not allowed, including for door staff and shared mailboxes. Shared mailboxes are reached only through named accounts. (IA-2; AC-2; PR.AA-01; PCI 8.2)

B.2 **Least privilege.** Access must match the job, using the ticketing role list. The Box Office and Ticketing Manager approves ticketing access in writing (the onboarding checklist). No more than 2 people hold the ticketing administrator role. Patron export and refund rights are given only to roles that need them; door staff accounts can sell and scan but not refund. (AC-6; AC-3; PR.AA-05; PCI 7.2)

B.3 **MFA.** MFA is required for every ticketing account, the website, the productivity suite, the acquirer portal, and every administrator login, including logins held by the MSP (backup console, firewall, remote management tool). (IA-2(1); PR.AA-03; PCI 8.4)

B.4 **Last day.** On or before a person's last day, the system owners must disable their ticketing, website, suite, and other accounts, the MSP must remove device access, keys and devices must be collected, and any shared secret the person knew (staff Wi-Fi password, alarm code) must be changed. For contractor door staff, the door login is disabled at the end of each season or when the staffing agency reports the person has left. (PS-4; AC-2; PCI 8.2.5)

B.5 **Monthly account check.** Each month the Venue Manager, with the Box Office and Ticketing Manager and the Marketing Coordinator, must compare the ticketing users and API tokens, website users, and suite users with the staff and contractor roster, and remove anything that does not match. The check is recorded on a one-page checklist. (AC-2; AC-6; PR.AA-05; PCI 7.2)

B.6 **API tokens and integrations.** Every API token or connected app must have an owner, a purpose, the narrowest access that works, and an end date, and must be listed in the inventory (POL-04 4.5). Tokens no longer used are revoked the same day. (IA-5; AC-6; PR.AA-01; PCI 8.6)

B.7 **MSP and vendor access.** MSP technicians and vendor support staff must use named accounts with MFA. The MSP must give the Venue Manager a current list of technicians with access every year. (AC-17; IA-2(1); SA-9; PCI 8.4.3)

B.8 **Networks.** Office computers and door tablets must be on a staff network separate from the bar POS, touring crews, and patrons. Crews get an internet-only Wi-Fi. Wi-Fi passwords must not be posted and must change each season and when staff leave. (SC-7; AC-18; PR.IR-01; PCI 1.3; 2.3)

B.9 **Passwords.** Passwords must be at least 12 characters, never reused from personal accounts, and never written down at the door or bar. Vendor default passwords must be changed before a device or service is used. (IA-5; PR.AA-01; PCI 8.3; 2.2)

B.10 **Locking.** Office computers lock after 10 minutes idle. Door tablets need a passcode and lock after 5 minutes. (AC-11; PR.AA-03)

### Part C. Workforce and contractor use rules (essentials of POL-05)
C.1 Company systems are for company work. Look up only the patrons you are serving. (PL-4; PR.AT-01)

C.2 **Never take a card number** by phone, email, text, chat, social media message, or on paper. Help the patron buy online, at the door, or with a payment link. If a card number arrives anyway, do not use it: delete it, tell the Venue Manager, and reply that card numbers must never be sent by email. (PL-4; SI-12; PCI 3.2; 12.2)

C.3 Do not store or send patron or card data with personal email, personal cloud storage, messaging apps, or public AI tools. POL-04 4.7 lists the approved AI tools. (PL-4; PCI 12.2)

C.4 Lock your screen when you step away, and never share passwords or MFA codes with anyone, including the MSP or someone who says they are from the ticketing vendor. (AC-11; PL-4)

C.5 Employees complete security training at hire and every year and take part in phishing simulations. Contractor door and bar leads get a 10-minute card reader and card handling briefing at the start of each season. (AT-2; PR.AT-01; PCI 12.6; 9.5)

C.6 Report suspected incidents at once under POL-03 4.2, including your own mistakes. (IR-6)

C.7 Employees sign an acknowledgment of this policy at hire and after each annual update. (PL-4; PCI 12.1)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Venue Manager checks compliance through the monthly account check (B.5), the weekly log check (POL-03 4.4), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.12.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and last-day checklist; approved script list; change log; service provider list; PCI DSS scope document; P01 risk register; P02 SSP control statements AC-2, IA-2(1), IA-5, PS-4, SC-7
