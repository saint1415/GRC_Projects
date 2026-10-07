# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| Policy ID | POL-03 |
| Owner | Operations Manager (Compliance Coordinator), with the Lead Systems Engineer (Information Security Lead) as incident commander |
| Approved by | Owner, 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually each September (next review 2027-09-30), and after any incident that required notice to a bank or customer |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8, AU-11, CM-3 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.MA-03, RS.AN-03, RS.CO-02, RS.CO-03, RS.MI-01, RC.RP-01, ID.IM-02 |
| Regulatory drivers | C-IT-R05 (12 CFR 53.4; 12 CFR 304.24); Interagency Guidelines III.C.1.g and Supplement A, II (bank contracts); Fla. Stat. 501.171(6)(a); MSA incident notice clause |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly, and meets every notice duty it owes to banks, customers, and regulators.

## 2. Scope
All workforce members and every company system, including the SaaS tools, the cloud tenant, the DC-1 platform, and the MDR provider's work for the company. A **security incident** is any actual or suspected unauthorized access to, use of, or change to company or customer systems or data, or interference with them. Examples include:
- an unexpected RMM script or session;
- a sign-in the account owner did not make;
- deleted backups;
- a lost laptop;
- a customer report of suspicious activity traced to company tools.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Incident commander: Lead Systems Engineer (backup: the on-call Systems Engineer, then the Owner) | Declares incidents; directs containment; makes the bank 4-hour determination with the Owner; keeps the timeline |
| Owner | Decides on spending, customer-wide shutdowns, and any ransom question; calls the cyber insurer; signs bank notices |
| Operations Manager | Communications lead: bank and customer notices, the bank service register and contacts, the incident log, records |
| MDR provider | 24x7 detection; first containment on laptops and identity accounts; investigation support under its contract |
| Cyber insurer and panel firms | Breach counsel and forensics, engaged through the insurer's hotline |
| All workforce | Report suspected incidents within 1 hour |

## 4. Policy statements
4.1 **Runbook.** The company must keep an incident response runbook for its most serious likely incident, compromise of provider tooling affecting customers (P08). A printed incident kit (runbook, contact list, bank contacts, notification matrix, notice templates) is kept at the office and with the Owner and the Lead Systems Engineer. (IR-8; RS.MA-01)

4.2 **Reporting.** Workforce members must report any suspected incident to the on-call engineer or the Lead Systems Engineer **within 1 hour at most**, by phone. Examples: an MFA prompt they did not start, an unexpected RMM job, a customer saying "your tool ran something on our server," a lost laptop, or a vendor security notice. (IR-6; RS.MA-02)

4.3 **Incident log.** The Operations Manager must log every incident in the PSA incident queue, including those that turn out harmless, with three times recorded: discovery, confirmation, and each determination that starts a legal or contract clock. (IR-5; RS.MA-02)

4.4 **Authority to contain.** The incident commander may, without further approval, pause the RMM tool's scripts and sessions for all customers, disable any account, isolate any system, and revoke any API token. Pausing a service for every customer is acceptable when a tool that reaches every customer may be compromised. (IR-4; RS.MI-01)

4.5 **Bank 4-hour determination.** For any incident that touches a bank's VMs, servers, or the tools that reach them, the incident commander and the Owner must decide, by the 2-hour mark at the latest, whether it has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, the bank's covered services for four or more hours. The decision and its time are recorded. If yes, the Operations Manager notifies the bank's designated point of contact **as soon as possible**, by phone and then email. If the bank has given no designated contact, the notice goes to the bank's CEO and CIO. (IR-6; RS.CO-03; 12 CFR 53.4(a); 12 CFR 304.24(a))

4.6 **Bank contract notice.** If bank customer information may have been accessed without authorization, the Operations Manager must notify that bank within 24 hours, as both bank contracts require, whether or not the 4-hour test is met. (IR-6; RS.CO-03; Interagency Guidelines Supplement A, II)

4.7 **Customer and legal notices.** Notices to customers (MSA: within 72 hours of confirmation), to customers as covered entities under Fla. Stat. 501.171(6)(a) (no later than 10 days after determining a breach), and any notices for the company's own personal information must follow the P08 notification matrix. Counsel reviews each notice before it is sent unless a bank notice cannot wait; in that case the Owner approves and counsel reviews follow-ups. (IR-6; RS.CO-02; RS.CO-03)

4.8 **Bank contacts and maintenance notices.** The Operations Manager must keep a bank service register (each bank, its covered services and systems, its designated contacts, and its CEO and CIO contacts), verify the contacts every quarter, and send planned maintenance affecting a bank's services to its designated contacts at least 5 business days ahead. (IR-6; CM-3; 12 CFR 53.4(a)(1), (a)(2), (b))

4.9 **Insurer and outside help.** For suspected tool compromise, ransomware, or data theft, the Owner must call the cyber insurer's breach hotline before hiring any outside firm. (IR-4; RS.MA-03)

4.10 **Ransom.** No ransom may be paid without the Owner's decision, advice from breach counsel and the insurer, and an OFAC sanctions check. The company never pays on a customer's behalf; customers decide for their own systems. (IR-4)

4.11 **Vendor incidents.** Vendors must report incidents affecting the company under their contracts (POL-02 A.5). The Operations Manager logs each report and the incident commander handles it under this policy. (IR-6; SA-9)

4.12 **Evidence.** At the start of any incident involving company tools, the incident commander must export RMM, cloud, identity provider, and MDR logs before they roll over, and store the exports with a hash and a custody record. (AU-11; IR-4; RS.AN-03)

4.13 **Testing.** The runbook must be tested every year in a tabletop exercise with the MDR provider and a bank scenario, and after any real incident that used it. The first tabletop is due by 2026-10-28. (IR-3; ID.IM-02)

4.14 **Lessons learned.** A written lessons-learned review is due within 30 days of closing any incident that required notice to a bank or customer, or outside help. Findings go into the risk register and the POA&M. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to sanctions under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the yearly assessment (P07) and the yearly tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a notice required by law or contract.

## 7. Related documents
P08 runbook and notification matrix; POL-02; POL-04; bank service register; MSA; bank A and bank B contracts; P03 gap rows G-003 to G-006, G-024, G-034, G-035, G-040
