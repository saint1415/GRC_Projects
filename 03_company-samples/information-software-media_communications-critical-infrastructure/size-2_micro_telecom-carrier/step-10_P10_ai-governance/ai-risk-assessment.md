# AI Risk Assessment: Customer-Service Chat Assistant with Account Access

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (rural fiber broadband and voice carrier) |
| Tier / Vertical | Micro / Communications |
| AI use case | AI-001: chat assistant in the customer portal and on the website, a BSS vendor add-on built on a large language model platform, with read access to the signed-in customer's account and a few account actions. Live since 2026-05-04 |
| Framework | NIST AI RMF 1.0 (AI 100-1) and the Generative AI Profile (AI 600-1) |
| Assessor / date | Office Manager (security and compliance lead) with one Customer Service Representative and the telecom regulatory consultant, 2026-08-25 |
| Decision | Owner and General Manager, 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Office Manager, who turned the assistant on and administers the BSS. **Decision authority:** the Owner and General Manager.
- **Policies that apply:**
  - POL-02 B.10: online CPNI only after portal sign-in; no account information to anyone who has not signed in (47 CFR 64.2010(c), (e)).
  - POL-02 B.12: change notices to the telephone number or address of record (64.2010(f)).
  - POL-04 4.3: no use of CPNI for marketing without approval; tools that would do so stay off (64.2007(b)).
  - POL-04 4.7: approved AI tools only; the assistant is the one approved entry, under the conditions in section 6.
  - POL-02 A.5: no CPNI to a vendor without CPNI terms.
- **Scale for a Micro company:** there is no AI committee. The Owner and General Manager, the Office Manager, and the Network Operations Lead review AI use at the monthly security meeting.

**How it started.** The BSS vendor offered the assistant free for six months. The Office Manager turned it on in the portal and on the website on 2026-05-04 to give customers after-hours help, because the company has no night staff. The vendor's defaults were left in place, including two that conflict with the CPNI rules (section 2). Nobody reviewed it first, which is the change-review gap in P09 (CC3.4).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Answer common questions (outages, prices, troubleshooting, bills) and handle simple account tasks after hours, so customers do not wait for the next business day |
| Users / operators | Customers using portal or website chat; the Office Manager (configuration); representatives (who receive hand-offs the next business day) |
| Affected people | About 1,420 account holders and anyone who opens the chat. About 1,150 chat sessions from 2026-05-04 to 2026-08-14 |
| Data | Inputs: customer messages; account data from the BSS (balance, plan, bill lines including itemized toll calls, recent call detail for voice accounts, open tickets). Outputs: answers, bill explanations, ticket creation, setting changes. Transcripts kept by the vendor for 180 days. **The add-on terms allow the vendor to use de-identified chat data to improve its models; no term excludes it** |
| Build or buy | Buy: a BSS vendor add-on built on a third-party large language model platform. Configured with the company's knowledge articles |
| Account actions allowed today | Show balance, bills, plan, and recent calls; open a repair ticket; switch paperless billing; **change the email address on the account** |
| Not intended | Password or PIN changes; service changes or disconnection; credits; payment arrangements; number porting. None of these is enabled. Enabling any requires re-assessment |

**What went wrong (found 2026-07-24, P03):**
1. **Guest verification** (vendor default) showed the balance and the last 3 calls after the account number and service address, both printed on every bill. That is account information the CPNI rules forbid as an authenticator for online access (64.2010(c)). It was used in 210 sessions and was turned off on 2026-08-14. The Office Manager and counsel reviewed those sessions: no complaint and no sign of use by someone other than the account holder was found, so no breach was determined. The review is in the incident register.
2. **Personalized offers** (vendor default) suggested faster broadband plans using the account's services and bill lines, including voice usage. Using voice CPNI to market broadband needs approval (64.2007(b); P03 G-007). Turned off on 2026-08-14.
3. **Email address change in chat** lets a signed-in user change the email of record with no notice to the old address. If an account is taken over, the attacker can lock the customer out of reset messages, and the change notice rule is not met (64.2010(f)).

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| FCC CPNI rules, 47 CFR 64.2001-64.2011 (C-COMMUNICATIONS-R01) | **Yes** | The assistant is an online channel that shows CPNI (call detail, voice plan, voice bill lines). Authentication (64.2010(c), (e)), change notices (64.2010(f)), and approval for marketing use (64.2007(b)) apply. An unauthorized disclosure through the assistant is handled under 64.2011. The vendor's handling of CPNI is the company's responsibility (64.2010(a)) |
| Florida breach law, Fla. Stat. 501.171 | Yes, if the assistant exposes Florida-defined personal information | For example, a user name or email with a password, or a driver license number if the BSS returned it (it does not show it today) |
| FTC Act Section 5 | Yes, for statements about the broadband service and data use | The common carrier exclusion (15 U.S.C. 45(a)(2)) does not reach broadband, which is an information service. The assistant's claims about prices, outages, and privacy must be accurate |
| State AI laws | None identified | The company serves only Florida addresses. No Florida AI statute is listed in the repository's cross-sector register (`00_universal-framework/cross-sector/`, verified 2026-09-25), and the assistant makes no consequential decision of the kinds other states' laws cover. It still says it is an AI at the start of every chat |
| Sector AI rules | None identified | The vertical overlay lists no Communications-specific AI rule |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`).
- **Why not High:** the assistant does not make, and is not a substantial factor in, a consequential decision about a person (credit, housing, employment, and so on). Service, credit, and payment decisions stay with staff.
- **Why not Low:** it talks directly to customers, reads CPNI, and can change account settings. Errors can expose call detail, mislead customers about bills, or give unsafe advice during an outage.

**Re-tier to High and re-assess if:** the assistant can change passwords, PINs, or the address of record; decide credits, deposits, or disconnections; take spoken calls; or use CPNI for offers at scale.

## 4. MEASURE
Pilot data 2026-05-04 to 2026-08-14 (about 1,150 sessions). Tests on 2026-07-24 and 2026-08-11 used a test account.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Sample of 40 transcripts graded against the BSS and the knowledge articles. Wrong billing or policy answers must be under 3% | 3 of 40 wrong (7.5%), mostly late fees and toll charges | **No** |
| Safe | 10 prompts about calling 911 during an outage must say to use a mobile phone and never suggest unplugging equipment during a 911 call | 9 of 10 correct; 1 gave modem restart steps with no 911 advice | **No** |
| Secure and resilient | 20 prompt injection and data extraction prompts; no access to another customer's data; no action outside the allowed list | No cross-account data (the BSS limits the session to the signed-in account). 2 of 20 prompts made it change the email address without a confirmation step | **Partial** |
| Accountable and transparent | AI disclosure at the start; hand-off to a person; transcripts available to the company | Disclosure shown; hand-off creates a next-day ticket; the company can view transcripts but not export them | **Partial** |
| Explainable and interpretable | Bill answers point to the bill line used | Shown in about half of billing answers | **Partial** |
| Privacy-enhanced | CPNI only after sign-in; no CPNI marketing; no vendor training on company data; transcripts deleted within 90 days | Guest verification and offers off since 2026-08-14; training use allowed by the terms; 180-day retention | **No** |
| Fair, with harmful bias managed | Compare wrong-answer and hand-off rates for Spanish and English chats; flag a gap over 10 percentage points | Spanish chats are about 5% of sessions. Sample of 8 Spanish chats: 2 wrong (25%); English 3 of 32 (9%). Sample is small, but the gap is flagged | **No (flagged)** |

**Why these groups.** The assistant collects no age, race, or disability data, and the company does not want to start. Chat language is recorded for every session, so the comparison needs no new personal data. Older customers are a known concern in the service area. Because age is not recorded, the monthly sample also tracks how often customers ask for a person after a wrong answer.

**Bias finding.** Spanish-speaking customers got wrong billing answers more often. The sample is too small to be sure, so until the vendor shows better accuracy, Spanish billing questions get a hand-off message with the bilingual representative's callback hours.

## 5. MANAGE
**Data protection:**
- Account information only after portal sign-in; guest verification stays off (POL-02 B.10).
- Personalized offers stay off until the company adopts CPNI approval rules (POL-04 4.3).
- Email address change removed from chat; changes go through the portal with a notice to the old address and the telephone number of record (POL-02 B.12).
- Contract addendum by 2026-12-31: CPNI confidentiality; no use of company data to train or improve models, de-identified or not; 90-day transcript deletion; transcript export on request; incident notice within 24 hours; the list of subservice organizations, including the language model platform (POAM-011).

**Human in the loop:**
- The assistant answers and takes only the allowed actions; every setting change needs a confirmation step.
- Anything about money owed, credits, or service changes goes to a representative the next business day, with the transcript attached.
- Customers can ask for a person at any time.

**Monitoring:**
- Monthly: 20 transcripts graded for accuracy, including every Spanish chat in the month (up to 10), logged against P01 R-019.
- Monthly: the 911 prompt set re-run after any vendor update.
- Complaints that mention the assistant are tagged in the BSS; any complaint about unauthorized release of CPNI is counted for the annual certification (64.2009(e)).

**Incident handling:** any assistant disclosure of CPNI to someone other than the account holder is a suspected incident under POL-03 and follows the P08 notification matrix (64.2011). The Office Manager can switch the assistant to "general questions only" in the BSS settings in minutes.

**Decommissioning:** turn the assistant off and fall back to the portal and next-day callbacks if the addendum is not signed by 2026-12-31, if wrong answers stay above 3% for three months in a row after 2026-12-31, if it ever shows one customer's data to another, or when the free period ends unless the Owner and General Manager approves the cost.

## 6. Decision
**Approve with conditions.** Owner and General Manager, 2026-08-31.

The assistant may continue **only if** these are met by 2026-10-15:
1. Guest verification and personalized offers stay off (done 2026-08-14).
2. Email address change is removed from chat.
3. The 911 answer is fixed in the knowledge articles and passes 10 of 10 prompts.
4. Spanish billing questions get a hand-off message until the fairness check passes.
5. Wrong billing answers are under 3% in the October sample, or billing answers are limited to quoting the bill.

**By 2026-12-31:** the vendor addendum in section 5 is signed (POAM-011).

**Related actions for AI-002 and AI-003.** The Network Operations Lead confirms with the monitoring vendor that its learned alert thresholds use only device data (no customer data). Staff use of public generative AI tools with Restricted data is prohibited (POL-02 C.2; POL-04 4.7) and is covered in the October training.
