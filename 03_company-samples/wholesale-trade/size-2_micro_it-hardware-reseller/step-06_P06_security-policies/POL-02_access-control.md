# Access Control Policy (with Program Governance, Supplier Rules, and Workforce Use Rules)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-02 |
| Owner | Operations Manager (security and compliance lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after major changes, incidents, or changes in DoD contract requirements |
| Implements (SP 800-53 Rev. 5) | Part A: PM-2, PM-9, RA-3, PS-8, CA-2, SA-9, SR-3, SR-5, SR-6, SR-8, CM-8, SI-12, PL-1. Part B: AC-2, AC-3, AC-6, AC-11, AC-17, IA-2, IA-2(1), IA-5, PS-4, AU-6, PE-3, PE-8, SC-7. Part C: PL-4, AT-2, AC-20, AC-22, IR-6 |
| CSF 2.0 | GV.RR-02, GV.RR-04, GV.RM-01, GV.PO-01, GV.PO-02, GV.SC-05, GV.SC-06, GV.SC-07, ID.RA-01, PR.AA-01, PR.AA-03, PR.AA-05, PR.AA-06, PR.AT-01 |
| Contract and regulatory basis | FAR 52.204-21(b)(1); 32 CFR 170.15, 170.19, 170.22; FAR 52.204-25 and 52.204-26; DFARS 252.246-7008 |

**Why this policy has three parts.** A 7-person company does not need five separate policies. This policy carries the program governance and supplier rules that would otherwise be in an Information Security Policy (POL-01), and the workforce use rules that would otherwise be in an Acceptable Use Policy (POL-05). POL-01 and POL-05 are short pointer files to Parts A and C.

## 1. Purpose
Set up the company's security program and supplier rules, make sure only authorized people reach FCI and company information and only as far as their job requires, and tell staff how to use company systems.

## 2. Scope
All workforce members of Cris Santos Company: the Owner, employees, part-time and temporary staff, and contractors. It covers every company system and every copy of company information, including systems the MSP and SaaS vendors run for the company, and the purchasing of every product the company resells.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Owner | Approves policies and the security budget; accepts Moderate risk; CMMC Affirming Official; signs SAM representations; decides sanctions |
| Operations Manager | Security and compliance lead; runs this policy; grants and removes access; reviews accounts and logs; manages the MSP |
| Federal Account Manager | Section 889 screening of DoD quotes; clause review on DoD orders |
| Purchasing and Inventory Coordinator | Supplier list, sourcing order, and broker approvals |
| Bookkeeper | Supplier payments and bank-detail verification |
| MSP | Creates and disables suite and laptop accounts on request; operates device and network controls |
| All workforce | Protect credentials; follow Part C; report problems at once (POL-03) |

## 4. Policy statements

### Part A. Program governance and supplier rules (essentials of POL-01)
A.1 **Security lead and Affirming Official.** The Operations Manager is the security and compliance lead. The Owner is the CMMC Affirming Official. Both designations must be in writing and updated within 30 days of any change. (PM-2; GV.RR-02; 32 CFR 170.22(a)(1))

A.2 **Risk assessment.** The Operations Manager must update the risk assessment every July, and after any major change (a new broker, a new system holding FCI, accepting CUI, or changing the AI reorder feature), using NIST SP 800-30 Rev. 1 and including supply chain threats. Every risk must have an owner and a treatment in the risk register. (RA-3; ID.RA-01)

A.3 **Risk acceptance.** The Operations Manager may accept Low and Very Low risks. Only the Owner may accept a Moderate risk. High and Very High risks must not be accepted; they need a dated treatment plan approved by the Owner. A risk that could put counterfeit, tampered, or covered equipment on a DoD order is never accepted. (PM-9; GV.RM-01)

A.4 **Sanctions.** A workforce member who breaks a security rule must be sanctioned in proportion to intent and harm: coaching and retraining, a written warning, suspension, or termination. The Operations Manager records each sanction, and the Owner decides suspension or termination. Reporting a mistake in good faith is never sanctioned. (PS-8; GV.RR-04)

A.5 **Honest affirmations and representations.** No CMMC result or affirmation may be entered in SPRS, and no SAM representation may be made, unless a documented assessment or reasonable inquiry supports it and the Operations Manager has signed it. Counsel reviews any correction of a past entry. The supporting evidence must be kept for 6 years. (CA-2; GV.OV-01; 32 CFR 170.15(c)(2); FAR 52.204-26(c))

A.6 **Assessments.** The company must complete a CMMC Level 1 self-assessment against the SP 800-171A objectives for all 15 FAR 52.204-21 requirements every year, before the annual affirmation. Security controls must also be assessed at least once a year by someone who does not operate them. (CA-2; ID.IM-01; 32 CFR 170.15(a)(1))

A.7 **Service providers.** No vendor may store, process, or transmit FCI for the company until the Operations Manager has approved it, its security evidence (SOC 2 report or equivalent) is on file, and its terms limit use of company data to providing the service. The MSP must provide its technician list and MFA evidence every year. (SA-9; GV.SC-05; 32 CFR 170.19(b)(3))

A.8 **Sourcing order.** Buyers must buy from the original manufacturer or its authorized suppliers first. A broker may be used only when authorized sources cannot supply and only after the broker passes the broker approval checklist in the C-SCRM plan. Products for DoD orders must come from authorized sources unless the Owner approves an exception in writing and the contracting officer is notified as DFARS 252.246-7008(b)(3) requires. (SR-5; SR-6; GV.SC-06; DFARS 252.246-7008(b))

A.9 **Section 889 screening.** Every SKU must have a manufacturer of record in the ERP. SKUs made by a covered manufacturer, including rebranded or white-label units, are blocked on DoD quotes. Every piece of equipment the company buys for its own use must be screened before purchase, and the company's equipment and telecommunications services must be re-screened before each annual SAM update. (SR-5; CM-8; GV.SC-07; FAR 52.204-25(b); 52.204-26(c))

A.10 **Supplier terms.** Purchase orders must flow down the substance of FAR 52.204-25 (excluding paragraph (b)(2)) and DFARS 252.246-7008, and must require suppliers to notify the company of counterfeit, suspect, tampered, or covered items and of any compromise affecting the company's orders. (SR-3; SR-8; GV.SC-05; FAR 52.204-25(e); DFARS 252.246-7008(e))

A.11 **Supplier bank details.** A change to a supplier's bank details must be verified by calling the supplier on the phone number already in the ERP, never a number in the request. The Owner approves the first payment to changed details, and that payment waits 5 business days. (SR-6; GV.SC-07)

A.12 **Retention.** Policies, assessments, SPRS and SAM support, incident records, supplier approvals, and training records must be kept for 6 years from creation or last use, whichever is later. (SI-12; GV.PO-02)

A.13 **Policy review and exceptions.** The Operations Manager reviews this policy set every August and after an incident or major change, and keeps the current version where every workforce member can read it. An exception must be requested in writing, rated on the risk register scale, approved under A.3, recorded in the risk register, and limited to 12 months. No exception may cover a FAR 52.204-21 requirement for a system that handles FCI, because CMMC Level 1 allows no POA&M. (PL-1; GV.PO-01; GV.PO-02)

### Part B. Access control
B.1 **Unique accounts.** Every workforce member must have their own account in the ERP, the suite, every supplier portal, and the carrier account. Shared or generic accounts are not allowed. (IA-2; AC-2; PR.AA-01; FAR 52.204-21(b)(1)(v))

B.2 **Least privilege.** Access must match the person's job. The FCI folder is limited to the Owner, the Operations Manager, the Federal Account Manager, and the Setup and Receiving Technician. ERP administrator roles are limited to the Owner and the Operations Manager. The Operations Manager approves access in writing (the onboarding checklist) before it is granted. (AC-3; AC-6; PR.AA-05; FAR 52.204-21(b)(1)(i)-(ii))

B.3 **MFA.** MFA is required for the ERP, the suite, every supplier portal that offers it, and every administrator login, including logins held by the MSP (backup console, firewall, RMM). (IA-2(1); PR.AA-03)

B.4 **Termination.** On or before a workforce member's last day, the Operations Manager completes the termination checklist: disable ERP, suite, supplier portal, and carrier accounts; ask the MSP to remove laptop access; remove MFA registrations; delete the person's alarm code; collect keys and devices. For an involuntary termination, access is disabled before the person is told. (PS-4; AC-2; FAR 52.204-21(b)(1)(i))

B.5 **Monthly review.** Each month the Operations Manager compares the user lists of the ERP, suite, supplier portals, and backup console with the staff list and removes anything that does not match. In the same 30-minute session the Operations Manager reviews ERP administrator activity, supplier bank-detail changes, suite sign-in alerts, and new mail forwarding rules, and records the result on the checklist. (AC-2; AU-6; PR.AA-05; DE.AE-02)

B.6 **Locking.** Every computer, including the setup bench, must lock after 10 minutes idle. (AC-11; PR.AA-03)

B.7 **MSP and vendor access.** MSP technicians and vendor support staff must use named accounts with MFA. (AC-17; IA-2(1); SA-9)

B.8 **Passwords and shared secrets.** Passwords must be at least 12 characters and never reused from personal accounts. Passwords must never be kept in documents or spreadsheets. Each person has an individual alarm code, deleted when they leave. The staff Wi-Fi password changes every year and when anyone leaves. (IA-5; PE-3; FAR 52.204-21(b)(1)(vi), (ix))

B.9 **Physical access.** The stockroom door stays closed except while a delivery is being handed over. Couriers and visitors are signed in, escorted while inside, and signed out; the sign-in sheets are kept for 1 year. Keys are listed in a key log. (PE-3; PE-8; PR.AA-06; FAR 52.204-21(b)(1)(viii)-(ix))

B.10 **Setup bench.** The setup bench sits on its own network segment, uses named accounts, is encrypted, and accepts only company-issued USB media. Customer devices are connected only to the bench network. (SC-7; AC-6; SC-28; FAR 52.204-21(b)(1)(x))

### Part C. Workforce use rules (essentials of POL-05)
C.1 Company systems are for company work. Workforce members open FCI and customer information only when their job needs it. (PL-4; PR.AT-01; FAR 52.204-21(b)(1)(i))

C.2 Workforce members must not store or send FCI or customer information with personal email, personal cloud storage, personal messaging apps, or public AI chatbots. FCI stays in the ERP, the suite's FCI folder, and company laptops. Suite email on a personal phone is allowed only through the managed suite app. (AC-20; PL-4; FAR 52.204-21(b)(1)(iii))

C.3 Workforce members must lock their screen when stepping away and never share passwords or MFA codes, including with the MSP or a supplier. (AC-11; PL-4)

C.4 Workforce members must complete security training at hire and every year, covering FCI handling, supplier payment fraud, counterfeit and Section 889 awareness, and incident reporting, and must take part in phishing simulations. (AT-2; PR.AT-01)

C.5 Workforce members must report suspected incidents and suspect products at once under POL-03 section 4.2, including their own mistakes. (IR-6)

C.6 Workforce members must sign an acknowledgment of this policy at hire and after each annual update. (PL-4)

C.7 Nothing about DoD customers, delivery locations, or setup orders may be posted on the website, marketplaces, or social media (POL-04 4.10). (AC-22; FAR 52.204-21(b)(1)(iv))

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under A.4. The Operations Manager checks compliance through the monthly review (B.5), the annual Level 1 self-assessment (A.6), and the annual independent assessment (P07).

## 6. Exceptions
Exceptions follow A.13.

## 7. Related documents
POL-01 and POL-05 (pointer files); POL-03; POL-04; onboarding and termination checklist; C-SCRM plan (due 2026-11-30); P01 risk register; P02 SSP control statements AC-2, IA-2, SR-5; P03 gap analysis
