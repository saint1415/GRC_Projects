# Acceptable Use Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions |
| Policy ID | POL-05 |
| Owner | Group HR director, with the Group CISO |
| Approved by | Group CISO, under authority of POL-01 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | PL-4, PL-4(1), AT-1, AT-2, AT-3, AC-8, AC-19, AC-20 |
| CSF 2.0 | PR.AT-01, PR.AT-02, GV.PO-01 |
| Regulatory basis | PCI DSS 12.2, 12.6; 16 CFR 314.4(e) |
| Division supplements | Payment Processing: operations floor rules. Software: engineer use of production data. Merchant Consulting: client environments and client data |

## 1. Purpose
Set clear rules for how the workforce uses group systems and information.

## 2. Scope
All workforce members in every division and in corporate shared services, on any device used for group work, including in clients' and merchants' environments.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| All workforce | Follow these rules; complete training; report incidents |
| Managers | Make sure staff complete training and acknowledgments |
| Group HR | Tracks acknowledgments and training completion in every division |

## 4. Policy statements
4.1 Workforce members must access cardholder, merchant, and client information only as needed for their job. (PL-4; AC-8)

4.2 Every workforce member must acknowledge this policy and their division supplement at hire and every year. (PL-4; PR.AT-01; PCI DSS 12.2.1)

4.3 Every workforce member must complete security awareness training at hire and every year, including phishing and social engineering such as MFA code relay. Users of a cardholder data environment, including users from other divisions, must also complete PCI DSS role training before access. (AT-2; AT-3; PR.AT-01; PR.AT-02; PCI DSS 12.6; 314.4(e)(1))

4.4 Suspected incidents must be reported to the group SOC within 1 hour (POL-03 4.1). (IR-6)

4.5 Restricted information may be used only on group-managed devices and approved services. It must not be sent to personal email or stored on personal devices. (AC-19; AC-20)

4.6 **Generative AI.** Only AI tools on the group approved-tools list may be used for group work. Cardholder, merchant, client, and customer information must never be entered into public AI tools. (PL-4; PL-4(1))

4.7 Workforce members must never ask for, accept, or write down card numbers in email, chat, tickets, or notes. Direct merchants and clients to the evidence upload portal. (PL-4; PCI DSS 3.2.1)

4.8 **Client and merchant environments.** Workforce members working in a client's or merchant's systems must follow the client's rules, use per-person credentials stored in the group secret store, and remove local copies of client data at the end of the engagement. (PL-4; AC-20; PCI DSS 8.2.3)

## 5. Compliance and enforcement
Violations are handled under POL-01 section 4.7.

## 6. Exceptions
Exceptions follow POL-01 section 4.10.

## 7. Related documents
POL-01 to POL-04; `division-supplements.md`; Group AI Standard (P10).
