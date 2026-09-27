# Incident Response Runbook: Business Email Compromise and Fraudulent Wire Transfer

| Field | Value |
|---|---|
| Organization | Cris Santos Community Federal Credit Union (member-owned federal credit union) |
| Tier / Vertical | Micro / Finance and Insurance |
| Incident type | Business email compromise (BEC): an attacker takes over a credit union mailbox (the shared Member Services mailbox in the worked example), reads a member's wire conversation, and sends changed wire instructions from a look-alike address; a wire is sent to the attacker |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy; POL-02 B.10 (wire security procedure) |
| Regulatory basis | 12 CFR 748.0(b)(3) and Appendix A III.C.1.g (N52-R01); 12 CFR 748.1(c) (C-FINANCIAL-R03); 748.1(d); Appendix B; Fla. Stat. 501.171 and ch. 670 |
| Runbook owner | Operations Manager (Information Security Officer) |
| Approved | 2026-08-31 by the President and CEO |
| Last tested | Not yet. First tabletop with the MSP due 2026-11-30 (POAM-009) |

## 0. Roles and notification chain (Govern)
The credit union has 7 people and no IT staff. The MSP does the technical work; the cyber insurer supplies breach counsel and forensics; the corporate credit union handles the wire recall. The ISO runs the incident and keeps the log.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident lead | Operations Manager (ISO) | Accounting and Compliance Officer | Cell phone (numbers on the printed contact card) |
| Decision maker (NCUA report, member notice, spending) | President and CEO | Board chair | Cell phone |
| Wire recall and account holds | Operations Manager | Accounting and Compliance Officer | Corporate credit union wire desk (number in the binder) |
| SAR, FBI, and law enforcement | Accounting and Compliance Officer (BSA Officer) | President and CEO | Cell phone |
| Technical response | MSP emergency line (after-hours number in the MSP contract) | MSP lead technician's cell | Phone only |
| Cyber insurer and fidelity bond carrier | Cyber policy 24x7 breach hotline; bond carrier claim line | Insurance agent | Numbers on the policy cards in the binder |
| Breach counsel and forensics | Insurer panel counsel and forensic firm | n/a | Assigned on the first hotline call |
| NCUA | NCUA-designated point of contact for cyber incident reports; Regional Director | n/a | Contacts in the binder, checked each quarter |
| Vendors | Digital banking provider, core processor, and productivity suite support | Account managers | Numbers in the binder |

**Notification chain in the first hour:** staff member → ISO (within 15 minutes for a suspected fraudulent wire) → wire recall and the President and CEO at the same time → BSA Officer (FBI and SAR clock) → MSP (mailbox and account containment) → insurer hotline and bond carrier (President and CEO) → counsel and forensics (through the insurer).

**Out-of-band first.** Assume credit union email is compromised. Coordinate by phone and text on personal phones, using the printed contact card. Never reply to the suspicious email thread.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the vault and at the ISO's and the President and CEO's homes: this runbook, the contact card, the notification matrix, the NCUA report template, the member notice template, and the corporate credit union recall form
- [ ] Wire security procedure in force: callback to the number on file for every wire not requested in person, recorded before keying (POL-02 B.10). **Gap until POAM-006 training and the member agreement update close**
- [ ] Every mailbox, including shared ones, reached only through named accounts with MFA (done for Member Services on 2026-08-12; POAM-004)
- [ ] Suite alerts for new forwarding rules and risky sign-ins; sign-in logs kept one year (SI-4, AU-11). **Gap until POAM-007 closes**
- [ ] Staff trained on BEC red flags and the 15-minute reporting rule (POL-03 4.2). **Gap until POAM-006 and POAM-010 close**
- [ ] Vendor contracts require prompt incident notice to the ISO (POAM-013)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| A member says they did not ask for a wire, or asks where their wire went | Member call or visit | Report to the ISO **within 15 minutes**. Start the recall at once (section 3, step 1) |
| A callback reaches the member, who denies sending the request or the new instructions | MSR | Do not send. Report within 15 minutes. Tell the member their email may be compromised |
| An email changes wire instructions, is urgent, or comes from an address that differs slightly from the one on file | MSR | Hold the request; callback to the number on file; report if the member denies it |
| Suite alert: new forwarding rule, sign-in from an unusual location, or a mailbox rule that hides messages | Suite alert; MSP | MSP disables the session and rule; ISO opens an incident |
| A staff member typed their password into a page reached from an email | Staff report | MSP resets the password, revokes sessions, and checks mailbox rules |
| Beneficiary bank or the corporate credit union flags a wire | Wire desk call | ISO opens an incident and starts the recall |

**Declare a BEC incident when** a wire or other payment was sent, or was about to be sent, on instructions the member did not give, or a credit union mailbox or a member's credentials are confirmed to be in an attacker's hands.

**Record three times in the incident log:**
1. When the credit union first learned of the suspected fraud. This starts the **SAR clock** (748.1(d)(2)(i): 30 calendar days).
2. When the ISO and the President and CEO **reasonably believe a reportable cyber incident occurred**. This starts the **72-hour NCUA clock** (748.1(c)). Write the decision down either way.
3. When the credit union **determined a breach, or had reason to believe one occurred**, under Fla. Stat. 501.171. This starts the **Florida 30-day clock**.

## 3. First hour (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Call the corporate credit union's wire desk to send a recall and ask the beneficiary bank to freeze the funds; follow up in writing | Operations Manager | Recall reference number logged |
| 2. Report to the FBI through IC3 with the wire details (amount, date, beneficiary bank and account) | BSA Officer | IC3 complaint number logged |
| 3. MSP resets the mailbox password, revokes all sessions, removes forwarding and hiding rules, and exports the sign-in and mailbox audit logs before they age out | MSP with the ISO | Rules removed; logs saved |
| 4. Call the affected member at the phone number on file; place a hold on further wires from the account until new instructions are confirmed in person | ISO | Member informed; hold set in the core |
| 5. Check other pending wires and recent wires for the same look-alike address, beneficiary account, or email thread | ISO and Senior MSR | Search logged |
| 6. President and CEO calls the cyber insurer's hotline and the bond carrier | President and CEO | Claim numbers issued; counsel assigned |
| 7. Open the incident log with the three times from section 2 | ISO | Log started |

## 4. Analysis (RS.AN)
Led by the forensic firm through breach counsel, with the MSP supplying access and logs.
1. **Entry point.** Which mailbox, when, and how (phishing page, reused password, or the member's side only)? Sources: suite sign-in log, mailbox audit log, MSP antivirus console.
2. **Bank-side or member-side?** If only the member's own email was compromised, the credit union's systems were not accessed; if a credit union mailbox was accessed, the credit union has a cyber incident of its own. **This drives the 748.1(c) decision.**
3. **What member information was exposed.** List every message and attachment the attacker could read or forward: loan applications, ID copies, account numbers, Social Security numbers. Count members by state. Sensitive member information under Appendix B III.A.1 includes a name with a Social Security number or account number; Florida personal information includes a name with a Social Security number or driver license number (501.171(1)(g)).
4. **Was the callback done?** Check the wire file. If not, record why. This drives the Article 4A analysis (Fla. Stat. 670.202) and the training response.
5. **Other channels.** Check online banking for sign-ins or contact changes on the affected member's account, and the core for other transactions on it.
6. **Preserve evidence.** Keep the emails with full headers, the audit exports, the wire file, the recall correspondence, and call notes with a chain-of-custody log. Supporting documents for the SAR are kept 5 years (748.1(d)(3)).

## 5. Containment and eradication (RS.MI)
1. Keep the affected member's wire hold until the member confirms new instructions in person.
2. Block the look-alike domain and the attacker's IP addresses in the suite; tell the digital banking provider about the IP addresses.
3. If a credit union mailbox was used: reset credentials for every person who had access, confirm MFA, remove app consents and unknown MFA registrations, and have the MSP check the computers used to open the phishing email.
4. Move member documents out of the mailbox to the imaging server (POL-04 4.3) so a repeat intrusion finds less.
5. Send a same-day note to all staff: the red flags seen, and a reminder that every emailed wire request needs a callback to the number on file.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** Counsel reviews each notice before it goes out.

**Reportable cyber incident decision (748.1(c)(1)).** The ISO and the President and CEO answer, and record with the date and time:
- Did an attacker gain access to a credit union member information system (for example a mailbox holding member documents) and expose sensitive data, causing a substantial loss of confidentiality or integrity?
- Did a cyberattack disrupt business operations or vital member services?
- Did the incident come through a CUSO, cloud service provider, other third-party data host, or supply chain compromise? If a vendor told us, the 72 hours may run from its notice.

A fraud against one member through the member's own email, with no credit union system accessed, is usually **not** a reportable cyber incident, but it still needs a SAR and the member notice analysis. A compromised credit union mailbox full of member Social Security numbers usually **is**. The reasons are recorded either way.

| When | Action | Owner |
|---|---|---|
| Hour 0 | Wire recall; IC3 report; insurer and bond carrier notified | Operations Manager; BSA Officer; President and CEO |
| Hour 0 to 4 | Reportable cyber incident decision recorded | ISO and President and CEO |
| Immediately, if the attacker is still active | Telephone notice to law enforcement and NCUA (748.1(d)(2)(i)) | BSA Officer |
| Within 72 hours of the "yes" decision | NCUA notice to the designated point of contact (748.1(c)); the Appendix B notice to the Regional Director in the same contact | President and CEO |
| As soon as misuse is confirmed or reasonably possible | Member notice with the Appendix B III.B content (the member whose wire was diverted, and members whose documents were exposed) | ISO with counsel |
| Within 30 days of the Florida determination | Florida individual notice, or reliance on the Appendix B notice under 501.171(4)(g); copy to the Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000; other states' laws for members living elsewhere | ISO with counsel |
| Within 30 calendar days of initial detection | SAR filed (up to 60 days only if no suspect is identified) | BSA Officer |
| Promptly after filing | Board told of the SAR (748.1(d)(4)) | BSA Officer |

**Plan to the shorter clock.** The 72-hour NCUA clock is the shortest. Make the decision early and write it down. The SAR clock runs from initial detection, not from the end of the investigation.

**Member liability.** Consumer wires sent through Fedwire or a similar wire system are outside Regulation E (12 CFR 1005.3(c)(3)), so the loss question falls under UCC Article 4A. If the member did not authorize the payment order and no agreed security procedure made it effective, the credit union must refund it with interest (Fla. Stat. 670.202, 670.204). Counsel decides. Do not tell the member the loss is theirs before counsel has reviewed it.

**Staff and member communications.** Staff do not discuss the case outside the credit union and never mention a SAR (748.1(d)(5)). Statements to members come from the President and CEO.

## 7. Recovery (RC.RP, RC.CO)
A BEC incident rarely takes systems down. Recovery means safe service for the affected member and confidence that email and wires can be trusted. If a credit union system was compromised, restore in BIA priority order (P05):
1. Internet, network, and phones (callbacks depend on phones)
2. Clean teller and wire-desk computers
3. Core access for teller services
4. Wire portal (the corporate credit union's phone-initiated wire as the alternate)
5. Email and the Member Services mailbox, with rules checked and MFA confirmed
6. Online banking, cards, imaging, accounting, and lending

**For the affected member:** new wire instructions confirmed in person, the member's email treated as untrusted until the member confirms it is secured, and a written record of the agreed callback procedure. Record the amount recovered through the recall and any refund decision.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closing the case; written summary within 30 days (POL-03 4.12).
- Update the risk register (P01, especially R-001, R-002, R-007, R-018), the POA&M (P07), and this runbook.
- Add the case, with names removed, to the next training session (POL-02 C.4).
- Report the incident and management's response in the annual board report (Appendix A III.F).
- Keep incident records at least 5 years (POL-02 A.9).

## 9. Worked example (tabletop script)
The script uses the configuration before the shared mailbox was converted on 2026-08-12.

| Time | Event | Clock or decision |
|---|---|---|
| Day -19 | An MSR types the Member Services mailbox password into a fake "mailbox full" page. The attacker signs in from abroad and adds a rule that forwards messages containing "wire" or "closing" and hides replies | Not yet known |
| Day -1, 16:10 | Email from an address one letter different from a member's: "the title company changed banks; updated wiring instructions attached." The attachment reuses the member's real wire form | Red flags: changed instructions, look-alike address |
| Day 0, 09:20 | Senior MSR keys an $86,400 wire without a callback; the Operations Manager approves at 09:45 because the form matches | Security procedure not followed |
| Day 1, 11:40 | The member calls: the title company never received the funds. The MSR reports to the ISO at 11:50 | **Initial detection: SAR clock starts** |
| Day 1, 12:00 | Recall request through the corporate credit union; IC3 report; hold on the account | |
| Day 1, 13:30 | MSP finds the forwarding rule and foreign sign-ins on the Member Services mailbox | Credit union mailbox compromised |
| Day 1, 15:00 | ISO and President and CEO record that they reasonably believe a reportable cyber incident occurred (member documents with Social Security numbers exposed) | **72-hour NCUA clock starts (deadline Day 4, 15:00)**; Florida 30-day clock tracked from Day 1 |
| Day 1, 16:00 | Insurer hotline and bond carrier notified; counsel and forensics assigned | |
| Day 2, 10:00 | NCUA notified through the designated contact; Regional Director told of unauthorized access to sensitive member information | Well within 72 hours |
| Day 9 | Forensics confirms the attacker could read documents for 412 members (398 in Florida, 14 in other states) | Under 500 Floridians: no Department notice; other states' laws checked |
| Day 14 | Member notices mailed with the Appendix B III.B content, reviewed by counsel; relied on for Florida under 501.171(4)(g) | Florida deadline Day 31 met |
| By Day 31 | SAR filed; board told | 748.1(d)(2), (d)(4) |
| Day 35 | Counsel's Article 4A review: no written callback procedure had been agreed with the member, so the credit union refunds the member and claims under the cyber policy's social engineering sublimit | Lessons learned feed POL-02 B.10 and training |
