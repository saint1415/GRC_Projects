# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Operations Manager (Qualified Individual and security lead) |
| Approved by | Owner, 2026-08-31 |
| Effective date | 2026-09-01 |
| Review cycle | Annually (next review 2027-08-31), and after any incident that required outside notice |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Drivers | PCI DSS v4.0.1 12.10; Visa What To Do If Compromised v10.0; ISO agreement notice clause; 16 CFR 314.4(j); Fla. Stat. 501.171 |

## 1. Purpose
Make sure the company spots, contains, reports, and recovers from security incidents quickly, and meets every notice deadline it owes to the processor partner, the sponsor bank, the card brands, regulators, merchants, and individuals.

## 2. Scope
All employees and outside agents, and every system and copy of card data and merchant information, including systems run for the company by the MSP, the processor partner, and SaaS vendors. A "security incident" includes any attempted or successful unauthorized access to, or change of, a company system or a merchant's gateway settings; suspected card data compromise; card data found where it should not be; fraudulent deposit account change requests; and lost or stolen laptops, phones, or terminals.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Operations Manager | Incident lead; keeps the incident log and clock table; first contact for the MSP and processor partner |
| Owner | Backup incident lead; calls the cyber insurer; decides on money, merchant communications, and any payment demand |
| Merchant Support Lead | Backup for console actions (disabling accounts, freezing changes) |
| MSP | Technical response on laptops, network, and suite: isolate, preserve, rebuild, restore |
| Cyber insurer and panel vendors | Breach counsel and a forensic firm, engaged through the insurer's hotline |
| All employees and agents | Report suspected incidents at once |

## 4. Policy statements
4.1 The company must keep an incident response runbook for its most serious likely incident, a compromise of the payment environment through a company console account (P08), with printed copies of the runbook and contact list at the office and at the Operations Manager's and Owner's homes. (IR-8; RS.MA-01; PCI DSS 12.10.1)

4.2 Employees and agents must report any suspected incident to the Operations Manager **at once, and within 1 hour at most**, by phone. If the Operations Manager cannot be reached, report to the Owner. Examples: a suspicious email or sign-in prompt, a merchant reporting strange refunds or a changed payment page, a caller pushing for a deposit account change, card numbers found in email or tickets, or a lost laptop. (IR-6; RS.MA-02)

4.3 The Owner and the Operations Manager must each keep a company phone on, and answer incident calls, at all times. One of them must be reachable 24 hours a day. (IR-6; PCI DSS 12.10.3)

4.4 The Operations Manager must log every incident, including those that turn out to be harmless, with the time found, what happened, what was done, and the outcome. (IR-5; RS.MA-02)

4.5 On any reasonable suspicion that card data or a merchant's gateway account has been compromised, the Operations Manager must notify the processor partner's and sponsor bank's recorded incident contacts **immediately and no later than 24 hours**, as the ISO agreement requires, and must support the reporting clocks in Visa's What To Do If Compromised (report within 3 calendar days of reasonable suspicion or confirmation). (IR-6; RS.CO-02)

4.6 For any incident that may involve card data or merchant owner information, the Operations Manager must record the time of discovery and the time of determination, and breach counsel must decide on each legal notice: the FTC (16 CFR 314.4(j)), merchants as data owners (Fla. Stat. 501.171(6) and other states' laws), and individuals and the Florida Department of Legal Affairs where the company owns the data (501.171(3) and (4)). Deadlines are in the P08 notification matrix. (IR-6; RS.CO-02; RS.CO-03)

4.7 For any suspected compromise, account takeover, or extortion, the Owner must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; RS.MA-02)

4.8 Evidence must be preserved: affected laptops stay powered on and disconnected; console, suite, and phone logs are exported before they age out; and nobody may sign in to a compromised account or change a compromised system except as the forensic firm directs. (IR-4; RS.AN-03)

4.9 No ransom or extortion payment may be made without the Owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.10 Card data found where it should not be (email, tickets, recordings, files) must be handled under POL-04 4.8 and logged as an incident. (IR-4; PCI DSS 12.10.7)

4.11 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02; PCI DSS 12.10.2)

4.12 Lessons learned must be written up within 30 days of closing any incident that required outside notice or outside help, and fed into the risk register, training, and the runbook. (IR-4; ID.IM-02; PCI DSS 12.10.6)

## 5. Compliance and enforcement
Breaking this policy leads to action under POL-02 A.12. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the quarterly PCI review (POL-02 A.5), the annual tabletop, and the annual assessment (P07).

## 6. Exceptions
Exceptions follow POL-02 A.11. No exception may delay a notice owed under law or contract.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; ISO agreement; cyber insurance policy; Visa What To Do If Compromised v10.0
