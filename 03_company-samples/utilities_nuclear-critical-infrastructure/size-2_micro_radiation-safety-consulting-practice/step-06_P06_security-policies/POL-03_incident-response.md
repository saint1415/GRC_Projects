# Incident Response Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-03 |
| Owner | Office Manager (Security Officer) |
| Approved by | Principal Health Physicist (owner), 2026-09-15 |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-15), and after any incident that required notice to a client, a regulator, or individuals |
| Implements (SP 800-53 Rev. 5) | IR-1, IR-3, IR-4, IR-5, IR-6, IR-8 |
| CSF 2.0 | RS.MA-01, RS.MA-02, RS.AN-03, RS.CO-02, RS.CO-03, RC.RP-01, ID.IM-02 |
| Client and legal drivers | Part 37 client contracts (24-hour notice; supports the clients' 10 CFR 37.57(b) assessment); reactor client contracts (4-hour notice); Fla. Stat. 501.171 |

## 1. Purpose
Make sure the practice spots, contains, reports, and recovers from security incidents quickly, and gives its clients the notice they need to meet their own regulatory duties.

## 2. Scope
All staff and every system and copy of practice and client information, including systems the MSP and SaaS vendors run for the practice, laptops and USB drives used at client sites, and paper. A "security incident" includes any attempted or successful unauthorized access, use, disclosure, change, or destruction of information, interference with a system, malware found on practice media at a client site, a lost or stolen device or drive, and client information sent or shared with the wrong person or tool.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Office Manager (Security Officer) | Incident lead; keeps the incident log and the notice clock sheet |
| Principal Health Physicist (owner) | Backup incident lead; calls the cyber insurer; approves client and regulator notices and any spending |
| Senior Health Physicist (Part 37 services lead) | Decides which Part 37 clients' information is involved and makes the client calls with the owner |
| Senior Health Physicist (field services lead) | Lists every device and drive used at each reactor site; makes the plant calls |
| MSP | Technical response: isolate, investigate, rebuild, restore; preserves logs |
| Cyber insurer and its panel vendors | Breach counsel and forensic firm, engaged through the insurer's hotline |
| All staff | Report suspected incidents at once |

## 4. Policy statements
4.1 The practice must keep an incident response runbook for its most likely serious incident, a business-system intrusion with attempted pivots to clients (P08), with a printed copy and contact card in the office and at the owner's and Office Manager's homes. The contact card lists each client's security contact. (IR-8; RS.MA-01)

4.2 Staff must report any suspected incident to the Office Manager **at once, and within 1 hour at most**, by phone. If the Office Manager cannot be reached, call the owner. Examples: entering a password on a suspicious page; an unexpected MFA prompt; a strange pop-up or locked files; a lost laptop, phone, or USB drive; a plant kiosk rejecting a drive; client information sent to the wrong person or pasted into an unapproved tool; a client reporting a strange email from the practice. (IR-6; RS.MA-02)

4.3 The Office Manager must log every incident, including those that turn out to be harmless, with the time found, what happened, what was done, and the outcome. (IR-5)

4.4 **Client notice clocks start at discovery.** The Office Manager must record the time the practice first knew, and start the clock sheet from the P08 notification matrix at once:
- any device or media used at a reactor site may be involved: the field services lead calls the plant **within 4 hours** (contract);
- any Part 37 client's information may have been accessed by someone not approved, copied out, or sent to an unapproved tool: the Part 37 services lead and the owner call the client **within 24 hours** (contract), so the client can assess the event under its own procedures and 10 CFR 37.57(b);
- any other client's information may be involved: tell the client as its contract requires, and in any case without unreasonable delay.
The practice does not decide for a client whether an event is "suspicious activity"; it gives the client the facts quickly and helps it assess. (IR-6; RS.CO-02; RS.CO-03)

4.5 For any incident that may involve personal information (employee records, staff dose reports, or client background pages), the owner, with breach counsel, must decide whether Fla. Stat. 501.171 notice is required and meet the deadlines in the P08 notification matrix. (IR-6; RS.AN-03)

4.6 For any suspected intrusion, ransomware, data theft, or account takeover, the owner must call the cyber insurer's breach hotline before hiring any outside firm, and the MSP must be engaged under its contract. (IR-4; RS.MA-02)

4.7 No ransom may be paid without the owner's approval, advice from breach counsel and the insurer, and an OFAC sanctions check. (IR-4)

4.8 If any material that looks like Safeguards Information arrives, the person who receives it must stop reading, not forward or copy it, and call the field services lead, who calls the sending plant and follows its instructions. (IR-6; 10 CFR 73.21)

4.9 Vendors must report incidents to the Office Manager as their contracts require. The Office Manager must log each report and handle it under this policy. (IR-6; SA-9)

4.10 The runbook must be tested every year with a tabletop exercise that includes the MSP, and after any real incident that used it. (IR-3; ID.IM-02)

4.11 Lessons learned must be written up within 30 days of closing any incident that required client, regulator, or individual notice, and fed into the risk register and training. (IR-4; ID.IM-02)

## 5. Compliance and enforcement
Breaking this policy leads to action under POL-02 A.4. Failing to report is a violation; reporting a mistake in good faith is never sanctioned. Compliance is checked in the annual assessment (P07) and the annual tabletop.

## 6. Exceptions
Exceptions follow POL-02 A.9. No exception may delay a client notice, a plant notice, or a legally required notification.

## 7. Related documents
P08 Incident Response Runbook and notification matrix; POL-02; POL-04; client and reactor contracts; Fla. Stat. 501.171
