# Incident Response Runbook: Compromise of the Payment Processing Environment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (merchant services provider, an ISO) |
| Tier / Vertical | Micro / Financial Services |
| Incident type | Compromise of the payment processing environment, at the point the company controls: a phishing email captures a support specialist's gateway console password (no MFA). The attacker uses "log in as merchant" to push refunds to prepaid cards and inserts a skimming script into the hosted payment page custom header of e-commerce merchants |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy |
| Runbook owner | Operations Manager (Qualified Individual and security lead) |
| Approved | 2026-08-31 by the Owner |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-009) |

## 0. Roles and notification chain (Govern)
The company has 7 people and no IT staff. The processor partner controls the platform that was misused, the MSP handles laptops and the network, and the cyber insurer supplies breach counsel and forensics. The Operations Manager runs the incident and keeps the log and the clock table.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Operations Manager | Owner | Company phones (on 24 hours a day, POL-03 4.3) |
| Decision maker (money, merchant messages, any payment demand) | Owner | Operations Manager | Company phone |
| Console actions (disable accounts, freeze changes) | Merchant Support Lead | Operations Manager | Company phone |
| Processor partner gateway security and partner risk teams | Recorded incident contacts (POAM-008) | Processor partner 24x7 merchant help line | Phone, then email |
| Sponsor bank | Recorded incident contact (POAM-008) | Through the processor partner | Phone, then email |
| Technical response (laptops, suite, network) | MSP emergency line | MSP lead technician's mobile | Phone only |
| Cyber insurer | Carrier's 24x7 breach hotline | Insurance agent | Number on the policy card in the binder |
| Breach counsel and forensics | Insurer panel counsel and panel forensic firm | n/a | Assigned by the insurer on the first call |
| Law enforcement | U.S. Secret Service field office | FBI through IC3 | Numbers in the binder |

**Notification chain in the first hour:** staff member or merchant → Operations Manager → processor partner gateway security (to freeze the account) and Owner, at the same time → insurer breach hotline (Owner) → breach counsel → processor partner and sponsor bank formal notice (within 24 hours) → MSP if a laptop is involved.

**Out-of-band first.** Assume the support specialist's mailbox is compromised too. Coordinate by phone and text, using the printed contact card.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder at the office and at the Operations Manager's and Owner's homes: this runbook, the contact card, the notification matrix, the P02 boundary diagram, and the console user list
- [ ] MFA required on every console account (IA-2(1)). **Gap until POAM-002 closes (2026-09-15)**
- [ ] Merchant impersonation limited to the two support staff (AC-6). **Gap until POAM-001 milestone 2026-09-15**
- [ ] Payment page script inventory, so an injected script stands out (POL-04 4.9). **Gap until POAM-006 closes**
- [ ] Daily console alert digest for impersonation, refunds, and settings changes (AU-6). **Gap until POAM-005 closes**
- [ ] Processor partner and sponsor bank incident contacts recorded and confirmed this quarter. **Gap until POAM-008 closes (2026-09-15)**
- [ ] Insurer hotline and policy number checked each renewal; MSP contract includes incident notice terms (POAM-011)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A merchant reports refunds it did not make, or customers report fraud after paying online | Merchant call | Ask the processor partner to freeze refunds for that merchant; check the console audit log for impersonation; declare if any company account was used |
| Processor partner's risk team flags a refund spike or a payment page change | Processor partner | Declare |
| Console alert: impersonation or settings change at an odd hour or from an unknown location | Daily alert digest (after POAM-005) | Call the account holder by phone; if they did not do it, declare |
| A staff member reports typing a password into a page from an email | Staff report (POL-03 4.2) | Disable that person's console and suite sessions at once; check the console audit log |
| Card brand or sponsor bank says fraud traces back to several of the company's merchants (common point of purchase) | Sponsor bank, through the processor partner | Declare immediately |

**Declare a payment environment compromise when** any company console account was used by someone other than its owner, any unapproved content appears on a hosted payment page, or the processor partner or sponsor bank reports a common point of purchase among the company's merchants.

**Write down two times.** Several clocks start from them:
- **Reasonable suspicion** (the first evidence that a company account or a payment page was misused): starts the 24-hour ISO agreement notice and Visa's 3-calendar-day reporting clock (WTDIC v10.0 A.1).
- **Discovery** (the first day any employee knew): starts the FTC 30-day clock, if counsel finds 314.4(j) applies (16 CFR 314.4(j)(2)).
- **Determination of a breach** (counsel's call): starts Florida's 10-day third-party agent clock and 30-day individual and Department clocks (Fla. Stat. 501.171(3), (4), (6)).

## 3. First hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log and the clock table (section 6.1). Record the suspicion time | Operations Manager | Log open |
| 2. Call the processor partner's gateway security team: disable the compromised console account, end its sessions, freeze refunds on affected merchants, and export the console audit log | Operations Manager | Account disabled; audit log export received |
| 3. Require MFA on every remaining company console account now, if not already done, and reset their passwords | Merchant Support Lead with the processor partner | All console accounts on MFA |
| 4. Ask the processor partner to restore every affected hosted payment page to its last known-good content. Save a copy of the malicious content as evidence first | Terminal and Integration Technician with the processor partner | Pages match the script inventory; copies saved |
| 5. Call the insurer's breach hotline; get counsel assigned | Owner | Claim number; counsel engaged |
| 6. Send the formal ISO agreement notice to the processor partner's and sponsor bank's recorded contacts. Ask the processor partner to start Visa's report (A.1) and confirm who files it | Operations Manager | Notice sent and acknowledged; time recorded; Visa filer named |
| 7. Reset the phished user's suite password, revoke sessions, and check for forwarding rules; MSP checks the user's laptop for malware and keeps it powered on | MSP with Operations Manager | Suite account clean; laptop isolated if suspicious |

**Keep merchants trading.** Card-present terminals and unaffected merchants are not touched by this attack. Do not ask the processor partner to suspend merchants unless forensics shows they are affected.

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the processor partner supplying platform logs.
1. **Initial access.** Find the phishing email, when the password was captured, and every sign-in by the attacker (console audit log, suite sign-in log). Search all mailboxes for the same email and remove it.
2. **What the attacker did.** From the console audit log, list every impersonation session, refund, and settings change. Compare every hosted payment page's custom header with the script inventory.
3. **Window of exposure.** From the first malicious payment page change to the restore, per merchant. The processor partner needs it to build the at-risk card list within 3 calendar days (WTDIC A.4).
4. **What was taken.** Which data the skimmer captured (name, card number, expiry, security code, billing address), from how many transactions, cardholders, and merchants, and the cardholders' states where known. The refunds are a financial loss to merchants, not a data loss; list them for the processor partner's recovery.
5. **Preserve evidence.**
   - Keep the console audit log export, the malicious script copies, the phishing email, and suite logs.
   - Hash every file and record the chain of custody in the incident log.
   - Do not sign in to the compromised account or change the support laptop except as the forensic firm directs (WTDIC A.7; POL-03 4.8).
6. **Other company data.** Check whether the attacker reached the CRM, portal, or phone system with the same password. If merchant owner data was reached, the company is the covered entity for it (section 6.4).

## 5. Containment and eradication (RS.MI)
1. Block the phishing sender and any attacker domains in the suite; add the skimmer's collection domain to the firewall's DNS filter.
2. Remove any attacker-added forwarding rules, app consents, or MFA registrations from the phished user's suite account.
3. Have the MSP rebuild the phished user's laptop if the forensic firm finds malware; otherwise scan it with the EDR or antivirus.
4. Confirm with the processor partner that no other company console account was used and that all payment pages match the inventory.
5. Confirm with the forensic firm that no persistence remains before returning the user's access, with MFA.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Breach counsel confirms every legal notice before it goes out. The Operations Manager keeps the clock table.

### 6.1 Notice clock table
| Clock starts | Action | Deadline | Owner |
|---|---|---|---|
| Reasonable suspicion | Formal notice to the processor partner and sponsor bank (ISO agreement) | Immediately; no later than 24 hours | Operations Manager |
| Reasonable suspicion or confirmation | Report to Visa (WTDIC A.1), through the processor partner and sponsor bank | 3 calendar days | Operations Manager with the processor partner |
| Notice to Visa | Incident report to Visa and the acquiring bank (A.2) | 3 calendar days after notice | Operations Manager with counsel |
| Window of exposure set (or discovery, or Visa request) | At-risk card numbers to Visa (A.4), by the processor partner | 3 calendar days | Processor partner; company supplies the window |
| Visa formal notice requiring a PFI | Contract a PFI (A.5) | 5 business days | Owner with counsel and the insurer |
| Discovery | FTC notice if counsel finds a notification event of 500 or more consumers (16 CFR 314.4(j)) | As soon as possible; no later than 30 days | Operations Manager with counsel |
| Determination of breach | Notice to affected merchants as their third-party agent, if counsel so finds (Fla. Stat. 501.171(6)(a); other states vary) | As expeditiously as practicable; Florida outer limit 10 days | Operations Manager with counsel |
| Day 0 to 2 | Voluntary report to the U.S. Secret Service or FBI | As soon as practicable | Owner with counsel |
| Other card brands | American Express DSOP Section 3; Mastercard and Discover rules through the sponsor bank | American Express: within 72 hours of discovery. Mastercard and Discover: per brand rules (confirm with the sponsor bank) | Operations Manager |

**Plan to the shortest clock.** The 24-hour contract notice comes first, then Visa's 3 calendar days. Merchants need the company's information early, because their own state-law clocks start when they learn of the breach.

### 6.2 Is this a bank service provider notice? No.
12 CFR 53.4 applies only to services subject to the Bank Service Company Act performed for a bank. The company performs none for the sponsor bank (P03 section 1.3). The ISO agreement notice in step 6 of section 3 is the bank notice. Record the decision in the incident log. The sponsor bank decides on its own 36-hour notice to the OCC under 12 CFR 53.3.

### 6.3 FTC notice decision (16 CFR 314.4(j))
- **Is it a notification event?** Card data typed into a skimmed page is taken before encryption, which is acquisition of unencrypted information without the cardholder's authorization (314.2(m)).
- **Is it the company's customer information?** The page belongs to the processor partner and the data to the merchants' customers. The company's console account was the way in. Counsel decides whether the data was "handled or maintained by or on behalf of" the company (314.2(d)). The company counts affected cardholders toward the 500 if counsel finds it is (conservative reading).
- **What the notice contains (314.4(j)(1)(i)-(vi)):** company name and contact; data types; date range; number of consumers; a general description; whether law enforcement asked for a delay in writing.

### 6.4 Merchant and state-law notices
- **Card data.** The merchants own their customers' card data and are the covered entities under Fla. Stat. 501.171. The processor partner hosts the page. Counsel decides whether the company also acted as a third-party agent; plan as if it did and give each affected merchant the information it needs within 10 days of determination (501.171(6)(a)), coordinated with the processor partner so merchants get one consistent message.
- **What counts.** Under Florida law a card number is personal information only with the person's name and any required security code or password. A payment page skimmer that captures name, card number, and security code meets that test.
- **Merchant owner data.** If the attacker reached merchant owner information in the CRM or portal, the company is the covered entity: notice to individuals within 30 days of determination (501.171(4)), the Department of Legal Affairs if 500 or more Floridians (501.171(3)), and consumer reporting agencies if more than 1,000 (501.171(5)). Other states' laws apply for owners elsewhere.

### 6.5 Earlier event: card data in call recordings (R-003)
On 2026-07-21 the gap analysis found that support call recordings held spoken card numbers, expiry dates, and security codes from about 2,050 keyed-entry calls since May 2025. Recording of the support queue was paused on 2026-07-22. The Operations Manager completed the notice analysis with the insurer's panel counsel on 2026-08-12:
- **Access.** The recordings were reachable only through the phone system's shared administrator login, used by three employees. The phone vendor's administrator audit log for the whole period shows sign-ins only by those three, only from the office or their homes, and no bulk download or export.
- **FTC.** The logs are reliable evidence that there was no unauthorized acquisition, which rebuts the presumption in 16 CFR 314.2(m). **Not a notification event.**
- **State law.** The recordings held personal information (name, card number, security code), but there was no unauthorized access, so there was no breach of security under Fla. Stat. 501.171. Counsel reached the same result for the other states involved. No merchant or individual notice.
- **Card brands and contract.** There was no reasonable suspicion of unauthorized access to account data, so no Visa report was due and the ISO agreement's compromise notice was not triggered. The Owner told the processor partner about it on 2026-08-20 as a PCI DSS compliance matter, together with the 2025 SAQ scope disclosure.
- **PCI DSS.** Handled under 12.10.7 (card data found where not expected): recordings deleted on 2026-08-14 and deletion confirmed by the phone vendor on 2026-08-17; root cause fixed by stopping the keyed-entry service (POAM-012). Disclosed in the 2026 SAQ.

### 6.6 Communications
- Merchants: counsel-approved message and a support script, sent after the processor partner and sponsor bank agree on it.
- Staff and agents: what happened, what not to say, where to send questions.
- No public statement without counsel and the Owner's approval.

**Payment demands:** only the Owner may decide, with counsel's and the insurer's advice and after an OFAC sanctions check (POL-03 4.9).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. Phone and email (SYS-05, SYS-04): clean suite account for the phished user; main line forwarded if needed
2. Clean laptop for the affected support specialist (SYS-06): spare laptop while the MSP checks or rebuilds the original
3. Console access (SYS-01): every company account on MFA with a new password; impersonation limited to the two support staff
4. Fraud filters and merchant risk (SYS-01, SYS-02): review filter settings on affected merchants; help the processor partner recover fraudulent refunds
5. Terminal swaps, CRM, and portal work resume as normal

**Validate before closing:**
- the forensic firm (or PFI) confirms eradication
- every hosted payment page matches the script inventory for 30 days of monthly checks
- the console audit log shows no unknown sign-ins for 14 days
- refunds on affected merchants are back to normal levels

Tell merchants when their payment pages are confirmed clean (RC.CO).

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of recovery, with the MSP, the processor partner, and counsel. Written summary within 30 days (POL-03 4.12).
- Update the risk register (P01: R-001, R-002, R-008, R-009, R-022), the POA&M (P07), POL-02 and POL-04 if needed, and this runbook.
- Give the processor partner the incident report, any PFI report, and the remediation evidence. A compromise may lead the processor partner or the card brands to require validation beyond the SAQ.
- Keep all incident records for at least 3 years (POL-02 A.9), or longer if counsel or a brand requires.
