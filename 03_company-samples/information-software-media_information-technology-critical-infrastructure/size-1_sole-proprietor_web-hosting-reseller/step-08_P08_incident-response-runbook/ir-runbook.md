# Incident Response Runbook: Compromise of the Site Management Dashboard Affecting Customer Sites

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller) |
| Tier / Vertical | Sole Proprietorship / Information Technology |
| Incident type | Compromise of provider tooling affecting downstream customers. An attacker takes over a site management dashboard account (SYS-04), most likely the freelance developer's, and pushes a malicious plugin to the 120 connected care-plan sites: a payment-page skimmer on the stores, rogue administrator users, spam pages, or code that reads files in each hosting account |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile), shortened to the first 24 hours |
| Policy basis | POL-01 section 10 |
| Runbook owner and approver | Owner, adopted 2026-09-28 |
| Last tested | Not yet. Walkthrough with the contract security consultant due 2026-11-30 (POAM-010) |

Keep a printed copy at home and a copy in the emergency envelope (POL-01 7.6). Assume the dashboard, and possibly the freelancer's laptop and mailbox, are in the attacker's hands. **Work from the owner's laptop and phone, and do not email the freelancer about the incident until the freelancer's mailbox is confirmed clean.**

## 1. Who to call (Govern)
| Who | Why | When |
|---|---|---|
| Contract security consultant | Second pair of hands: preserve evidence, analyze the plugin, help clean sites | Hour 0 |
| Breach counsel | **None retained today.** The owner names a data breach attorney by 2026-10-31 (P01 R-007) and writes the number on the printed copy. Counsel confirms each breach determination and notice | Hours 0-4 |
| Cyber insurer | **None today.** A technology errors and omissions policy with a cyber endorsement is quoted; decision by 2026-12-31. If bought, call the carrier's hotline *before* hiring any outside firm | Hours 0-4 |
| Dashboard vendor support | Confirm whether the vendor's platform itself is compromised; freeze the account; preserve the activity log beyond its 30 days | Hours 0-2 |
| Upstream hosting provider (abuse and support) | Tell them first, so they treat the company as the victim and do not suspend the whole reseller account for malware (P01 R-004); ask for access logs and pre-incident backups | Hours 1-2 |
| Freelance web developer (by phone) | Ask whether the developer noticed phishing, a new sign-in, or malware; stop use of the personal laptop; do not wipe it | Hours 1-4 |
| Security service vendor | Rescan all 270 sites; turn off auto-dismiss during the incident | Hours 1-4 |
| Affected customers' security contacts | Early warning, then the formal notice (section 6) | From hour 8 |
| FBI (IC3 online report) and CISA | Voluntary report; also a mitigating factor if any payment is ever considered (OFAC) | Day 1 |

Phone numbers live on the printed copy only, not in this file.

## 2. Declare (Detect)
Declare a dashboard compromise when any of these happens:
- the dashboard activity log shows a plugin upload, bulk install, or new user that the owner did not make;
- the security service flags new administrator users or changed executable files on **two or more care-plan sites within a day** (these findings must never be auto-dismissed, POL-01 7.7);
- a customer reports a strange plugin, a new administrator, spam pages, or a changed checkout page;
- the dashboard vendor, the upstream provider, or a card brand warning passed on by a store's processor reports suspicious activity;
- the freelancer reports a phishing click, a lost laptop, or an unexpected sign-in prompt.

**Write down the date and time.** Two clocks matter. The Florida third-party agent clock runs **10 days from the determination of the breach or from having reason to believe it occurred** (Fla. Stat. 501.171(6)(a)). Customers' own 30-day clocks run from their determination (501.171(3), (4)). Record the determination for each customer in the incident log (POL-01 10.3).

## 3. First hour: stop the spread (RS.MA, RS.MI)
| Step | Done when |
|---|---|
| 1. Sign in to the dashboard from the owner's laptop. **Disable the freelancer's account and any account the owner does not recognize.** Change the owner's password and sign out all sessions. Turn on the setting that enforces MFA for every account | Only the owner's account is active |
| 2. **Export the dashboard activity log now** (it is kept only 30 days) and save it with the time of export | Log saved in the incident folder |
| 3. Pause all scheduled bulk updates and backups that could overwrite clean copies | No jobs scheduled |
| 4. Call the consultant, then the dashboard vendor, then the upstream provider | All three engaged |
| 5. Start the incident log: time, what was seen, each action, who was called | Log started |

**Do not** delete the malicious plugin from every site yet. First save one copy of it, and the list of sites and times it was pushed (step 2 and section 4).

## 4. Hours 1-8: scope and contain (RS.AN, RS.MI)
1. **Which sites?** From the exported log, list every site that received the plugin and when. Compare with the security service's findings for the same period.
2. **What does the plugin do?** The consultant reviews the saved copy: card skimming on checkout pages, new administrator users, file reads (including mailbox files in the same hosting account), outbound connections. This answer decides whether personal information was accessed.
3. **Contain on each affected site:**
   - **stores first**: put checkout in maintenance mode until the site is clean;
   - deactivate and remove the plugin, using the dashboard only if the vendor confirms its platform is clean, otherwise site by site through the reseller console;
   - remove rogue administrator users;
   - rotate the site administrator, database, and SFTP passwords from the password manager vault.
4. **The 12 customers that matter most.** For the 9 connected stores (about 31,000 shopper accounts), the two law firms, and the property management company, assume the plugin could read mailbox files in the same hosting account until the consultant shows otherwise.
5. **Other tools.** Check the portal, reseller console, and registrar sign-in history for the same attacker. Change the passwords of any account the freelancer could have stored on the laptop.
6. **Preserve evidence.** Keep the activity log, the plugin copy, the security service findings, the upstream access logs, and the consultant's notes, with a short chain-of-custody note (who, when, where stored). Ask the freelancer to keep the laptop powered on and offline until the consultant has checked it.

## 5. Hours 8-24: restore and prepare notices (RS.CO, RC.RP)
- **Restore** sites that cannot be cleaned with confidence. Use a backup from **before** the first malicious push: the 30-day dashboard backups for the 35 premium sites, and the upstream backups (7 days only) for the rest. **Restore quickly. If the push is more than 7 days old, the upstream backups hold only infected copies.**
- **Rescan** every restored site with the security service before checkout or admin access is turned back on.
- **Early warning.** Send each affected customer a short message from the owner's business email (or by phone if email is in doubt). It says what happened, what was done, and that a formal notice with details follows.
- **Breach determination, one customer at a time.** With counsel, decide for each customer whether personal information was accessed or there is reason to believe so: shopper logins (email and password), card data typed into a skimmed checkout, or Social Security and driver license numbers in mailboxes (Fla. Stat. 501.171(1)(g)). Write the determination and its date in the log. **This date starts the 10-day clock.**
- **Ransom or extortion:** no payment without counsel's advice and an OFAC sanctions check.

## 6. Notice deadlines (from `notification-matrix.csv`)
| Deadline | Notice | Applies when |
|---|---|---|
| As expeditiously as practicable, **no later than 10 days** after the determination | Third-party agent notice to each affected customer, with all the information the customer needs for its own notices (501.171(6)(a)) | Personal information in a customer's site or mailbox was accessed, or there is reason to believe it was |
| Customer's own clock: 30 days after the customer's determination | The customer notifies its Florida individuals (501.171(4)) and, if 500 or more, the Department of Legal Affairs (501.171(3)). Other states' laws apply for residents elsewhere | The customer's duty. The company may send notices on a customer's behalf if asked, but the customer stays responsible (501.171(6)(b)) |
| 30 days after determination | The company's own notices: portal users (about 190 sign-ins) and billing contacts | Only if the attacker also reached the customer portal |

**Plan to the 10-day clock.** It is the company's own legal deadline. Each customer then needs time inside its own 30 days to notify its shoppers, tenants, or clients.

## 7. After day 1 (RC.RP, ID.IM)
- Restore the rest in P05 order: owner access, a clean device, the reseller console and hosting, the registrar and DNS, the portal and customer contacts, the security service. Bring the dashboard back last, only after the vendor confirms it is clean, MFA is enforced, and the freelancer's role is limited to assigned sites (POL-01 7.3).
- The freelancer gets access back only on a checked laptop, with a new password, MFA, and the signed security addendum (POL-01 5.1).
- Send formal notices on time (section 6). Answer customers' questions in writing and keep copies.
- Within 30 days of closing the incident: record lessons learned; update P01 (R-001, R-007, R-012), P07, and this runbook; and correct any public statement the incident made untrue. Keep all incident records and breach determinations at least 5 years (POL-01 8.8).
