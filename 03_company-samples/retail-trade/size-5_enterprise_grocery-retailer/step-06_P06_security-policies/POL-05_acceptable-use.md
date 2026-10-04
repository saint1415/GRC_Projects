# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Hierarchy level | Tier 1 policy (see `policy-hierarchy.md`) |
| Owner | Chief Human Resources Officer |
| Approved by | Executive risk committee |
| Approval date | 2026-09-10 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review by 2027-09-30), and after major changes, incidents, or acquisitions |
| Implements (SP 800-53 Rev. 5) | AC-20, AT-1, AT-2, CM-7, CM-8, IA-5, IR-6, PE-3, PL-4, SA-9, SI-12 |
| CSF 2.0 | DE.AE-02, GV.OC-04, GV.RR-04, PR.AA-01, PR.AA-05, PR.AT-01, PR.DS-01, PR.PS-01, PR.PS-02 |
| PCI DSS v4.0.1 (N44-45-R01) | 3.2, 4.2.2, 8.2.2, 8.3.1, 9.5.1.2, 9.5.1.2.1, 9.5.1.3, 12.2.1, 12.6.1, 12.6.3, 12.6.3.1, 12.10.1 (requirement numbers only; read the text in the company's licensed copy) |

## 1. Purpose
Set the rules every workforce member follows when using company systems, devices, and data, including the store-floor rules that protect cardholders.

## 2. Scope
All Cris Santos Company workforce members (employees, contractors, and temporary staff) at the 112 stores in Florida, Georgia, Alabama, South Carolina, and Tennessee, the 2 distribution centers, and headquarters, including the acquired banner (AB) stores from their acquisition date. Covers all systems and data, including stores, colocation, cloud, SaaS, store operational technology, and systems that third parties operate for the company, and the services the company offers to external business clients (SL-1 retail media and SL-2 supplier collaboration).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Chief Human Resources Officer | Owns this policy, training records, and acknowledgments |
| Managers and store leads | Make sure their teams follow it |
| CISO | Approved tools and technical standards |
| All workforce | Follow this policy and report concerns |

## 4. Policy statements
Each statement is testable and tagged with its SP 800-53 control(s) and CSF 2.0 subcategory. `policy-control-map.csv` traces each statement to its regulatory driver and shows whether Internal Audit tested it in 2026 (P07).

4.1 Company systems must be used only for authorized business purposes, and every workforce member must acknowledge this policy at hire and annually. (PL-4; GV.RR-04)
4.2 Every workforce member must complete security awareness training at hire and annually; cashiers and front-end leads must also complete skimming and PIN pad tampering training; staff with email take part in phishing simulations. (AT-2; PR.AT-01)
4.3 POS operator IDs, PINs, and passwords must never be shared or written down. (IA-5; PR.AA-01)
4.4 Workforce must never ask customers to send card numbers by email, chat, or text, and must never key card numbers anywhere except on the PIN pad or the processor's hosted fields. (SI-12; PR.DS-01)
4.5 Personal devices must not be used to access the CDE or administrative consoles. (AC-20; PR.AA-05)
4.6 Only AI tools on the approved list (STD-05.3) may be used for company work; any new AI use, including an AI feature switched on in an existing product, must be registered with the AI governance committee first. (CM-7; SA-9; GV.OC-04)
4.7 Lost or stolen devices, handhelds, and badges, and any suspicious activity, must be reported immediately. (IR-6; DE.AE-02)
4.8 Unapproved software and browser extensions must not be installed on administrator endpoints. (CM-7; PR.PS-02)
4.9 Store leads must inspect PIN pads for tampering and substitution on the schedule set by the targeted risk analysis and record each inspection. (CM-8; PE-3; PR.PS-01)

## 5. Standards and procedures under this policy
Standards set measurable requirements (approved by the CISO); procedures give step-by-step instructions (approved by the owning director). Both sit below this policy in the hierarchy and cannot contradict it.
- STD-05.1 Security Awareness and Training Standard
- STD-05.2 External Systems and Personal Devices Standard
- STD-05.3 Approved AI Tools List

## 6. Compliance and enforcement
Compliance is measured through training completion, annual acknowledgments, phishing simulation results, PIN pad inspection logs, and endpoint software inventory. Violations follow PRC-01.1, from coaching for a first minor breach to termination for deliberate misuse.

## 7. Exceptions
Exceptions follow POL-01 section 7 and PRC-01.2. A deviation from a PCI DSS requirement also needs the PCI Program Manager's review, because internal exceptions do not change what the QSA must validate.

## 8. Related documents
POL-01; STD-05.1 to STD-05.3; POL-02 (operator IDs); POL-03 (reporting); P10 approved AI tools; P07 AT-2 results.
