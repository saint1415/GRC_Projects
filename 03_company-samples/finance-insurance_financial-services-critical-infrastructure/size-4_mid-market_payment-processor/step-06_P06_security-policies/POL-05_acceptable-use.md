# Acceptable Use Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-05 |
| Owner | HR Director, with the IT Director |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-15 |
| Effective date | 2026-10-01 (replaces the 2024 policy; acknowledgments due 2026-11-30) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | PL-4, AT-2, AT-3, AC-19, SA-11 |
| CSF 2.0 | GV.PO-01, PR.AT-01, PR.AT-02 |
| PCI DSS v4.0.1 | 5.4.1, 12.2.1, 12.6 |
| FTC Safeguards Rule | 16 CFR 314.4(e) |

## 1. Purpose
Set the rules for using company devices, accounts, networks, data, and AI tools, so that everyday work does not put card data or customer information at risk.

## 2. Scope
All workforce members and contractors, on company devices and on any device used for company work.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| HR Director | Owns this policy; collects acknowledgments at hire and each year |
| IT Director | Device management, approved software, and technical blocks |
| Director of Information Security | Training content, phishing simulations, and the approved AI tools list (with the AI and model risk committee) |
| Managers | Make sure their staff follow the policy |
| All workforce | Read, acknowledge, and follow the policy |

## 4. Policy statements
4.1 Company work must be done on company-managed devices with EDR and full-disk encryption. Personal devices may reach email and chat only through the managed app, and may never reach a CDE. (AC-19; PL-4; PCI DSS 12.2.1)

4.2 Card numbers and other Restricted data must never be sent or stored in email, chat, tickets, or shared drives. If a merchant sends card data, the recipient must report it under POL-03 4.10 and must not forward it. (PL-4; PCI DSS 3.2.1, 12.10.7)

4.3 Every workforce member must complete security awareness training at hire and each year, including phishing, social engineering, funding account change scams, and the rules in this policy. Developers must also complete secure coding training each year. (AT-2; AT-3; PR.AT-01; PR.AT-02; PCI DSS 12.6.1, 12.6.3, 6.2.2; 16 CFR 314.4(e))

4.4 Suspected phishing must be reported with the report button. Never approve an MFA prompt you did not start. (AT-2; PCI DSS 5.4.1, 12.6.3.1)

4.5 Remote work is allowed on company devices over home or trusted networks; public Wi-Fi requires the company VPN. Screens must lock when unattended. (PL-4; AC-11)

4.6 **Contact center and support.** Staff must never ask a merchant or cardholder to read out card data except inside the approved secure payment flow, where recording pauses automatically. Funding account changes follow POL-02 4.12; staff must never change a funding account on the strength of a phone call or email alone. (PL-4; PCI DSS 3.3.1)

4.7 **Generative AI tools.** Only tools on the approved AI tools list may be used for work. Restricted data may never be entered into any AI tool. Confidential data may be entered only into tools approved for it, under contract terms that prohibit training on company data. A person must review every AI output before it is sent to a merchant, partner, bank, or regulator. (PL-4; PCI DSS 12.2.1; 16 CFR 314.4(f))

4.8 **AI-assisted code.** Code produced with an AI coding assistant must be labeled as AI-assisted in the pull request and must pass the same review, static analysis, and dependency scanning as other code; changes to CDE repositories also need a security review. (SA-11; PCI DSS 6.2.3, 6.2.4)

4.9 Users must not install unapproved software, disable security tools, or share credentials. (PL-4; CM-11)

4.10 The company monitors use of its systems and networks for security. Users have no expectation of privacy in company systems, subject to applicable law. (PL-4)

## 5. Compliance and enforcement
Compliance is checked through acknowledgments, training completion reports, phishing results, technical blocks, and the annual assessment (P07). Violations are handled under POL-01 section 4.14.

## 6. Exceptions
Exceptions follow POL-01 section 4.13 and must be approved by the IT Director and the Director of Information Security.

## 7. Related documents
POL-01; POL-02; POL-04; STD-10 AI and model risk standard; P10 AI governance assessment and approved tools list
