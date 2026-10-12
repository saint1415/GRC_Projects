# Scenario facts: Cris Santos Company | Financial Services | Sole Proprietorship

All 11 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a statute or regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner-agent files Schedule C and is the agency's only licensed person) |
| Business | Independent property and casualty insurance agency (NAICS 524210). Personal lines (auto, homeowners, condominium, flood, umbrella) and small commercial lines (business owners policies, general liability, commercial auto, workers compensation) for Florida households and small businesses. Appointed by 9 insurers; 2 more markets through a wholesale broker for hard-to-place risks (EV-003, EV-021). The agency sells and services policies; the insurers underwrite, bill most policies directly, and pay claims |
| Location | Florida. A home office in the owner's house is the agency's place of business: a separate room used only for the agency and open to the public by appointment (Fla. Stat. 626.749; EV-014, EV-024) |
| Workforce | The owner-agent only (0 employees). Uses contracted services instead of staff. No unlicensed assistant: only a licensed agent may solicit, quote, or advise (Fla. Stat. 626.112(1); EV-024, EV-025) |
| Clients | About 640 client accounts: about 510 personal lines households and about 130 small businesses, with about 1,150 policies in force. Customer records name about 1,900 individuals (current and former clients, listed drivers, and business owners). About 60 of them are seasonal residents whose primary home is in another state; the rest live in Florida (EV-003) |
| Revenue | About $180,000 a year in commissions (fictional), about $720 per business day (EV-025). SBA-small (standard $15.0 million, NAICS 524210) |
| Premium handling | Most policies are billed by the insurer directly; clients pay the insurer online or by bank draft. About 60 commercial policies are **agency-billed**: the agency emails an invoice, the client pays by check or bank transfer into the agency's **premium trust account**, and the agency remits net premium to the insurer. About $240,000 of premium passes through the trust account each year. Premiums received are trust funds held in a fiduciary capacity (Fla. Stat. 626.561(1)). The agency accepts no payment cards (EV-003, EV-017, EV-019) |
| Licensing | The owner holds a Florida resident general lines (property and casualty) agent license. The agency trades under a name other than the owner's individual name, so it also holds a Florida insurance agency license (Fla. Stat. 626.112(7)(a), 626.172; EV-024). Licensing and agent conduct: Florida Department of Financial Services (ch. 626) |
| GLBA status | Determined in the intake [obligations register](step-00_P00_intake/obligations-register.csv) (GLBA-V, FTC-314). A **financial institution** under GLBA: acting as agent for insurance is financial in nature (12 U.S.C. 1843(k)(4)(B)). GLBA enforcement for "any person engaged in providing insurance" sits with the **state insurance authority** (15 U.S.C. 6805(a)(6)); the FTC covers only institutions not under another authority (6805(a)(7)). **The FTC Safeguards Rule, 16 CFR Part 314, therefore does not bind the agency** (314.1(b) limits it to institutions under FTC jurisdiction). Florida implemented the GLBA privacy provisions for insurance licensees through Fla. Stat. 626.9651 and Rule 69O-128, F.A.C. (privacy notices and disclosure limits) |
| Insurance data security law | Recorded in the intake obligations register (NAIC-668, FL-501.171). **Florida has not enacted the NAIC Insurance Data Security Model Law (#668).** The 2026 Florida Statutes chapters 624, 626, 627, and 628 contain no "cybersecurity event", information security program, or other cyber provision (searched 2026-10-05). The binding state security duty is Fla. Stat. 501.171(2): "reasonable measures to protect and secure data in electronic form containing personal information" |
| Contract duties | 4 of the 9 insurer agency agreements, including the lead insurer's (about 40% of the book), carry a **data security addendum**: safeguards consistent with GLBA section 501(b) (15 U.S.C. 6801(b)); MFA for access to insurer systems and to agency systems that hold the insurer's policyholder information; notice to the insurer within 72 hours of discovering a security incident involving its policyholders' information; cooperation, and no notice to its policyholders without coordinating; an annual security questionnaire (EV-021; CARRIER-DSA in the obligations register). The agency uses the elements of 16 CFR 314.4 as its yardstick for these addenda and for 501.171(2) |
| Contrast worth noting | The same one-person business would be under the FTC Safeguards Rule if it were, for example, a mortgage broker or a tax preparer (16 CFR 314.2(h)(2)), and under NYDFS Part 500 if it held a New York agent license (23 NYCRR 500.1 "covered entity"). The applicability test is the regulator of the activity and the license, not headcount |
| Not in scope | Decided in the intake [obligations register](step-00_P00_intake/obligations-register.csv): 12 CFR Part 53 and parallels (not a bank or a bank service provider); 12 CFR 30 App. B (not a bank); NCUA 12 CFR 748.1(c); SEC Regulation SCI and Form 8-K (not an SCI entity or SEC registrant); NYDFS Part 500 (no New York license; seasonal clients' New York property is referred to a New York agent); HIPAA (no health or group health lines); payment cards (none accepted); CIRCIA (proposed only) |
| State law approach | Florida law is cited only where a Florida duty is unavoidable: data security, disposal, and breach notice (Fla. Stat. 501.171), premium trust funds and records (626.561, 626.748), privacy (626.9651; Rule 69O-128). Seasonal clients in other states are handled generically ("each state where affected individuals reside") |

**Driver labels used in this folder.** None of the vertical requirement IDs C-FINANCIAL-R01 to R06 applies to this agency (intake obligations register; P03 section 1). Rows cite the governing source directly, the way the Small sample cites PCI DSS: "Fla. Stat. 501.171(2)", "Fla. Stat. 626.748", "Rule 69O-128", "Carrier DSA" (the insurers' data security addenda), and "16 CFR 314.4(c)(5) benchmark" where the FTC element is used as the yardstick. "C-FINANCIAL-R05 (not applicable)" and "C-FINANCIAL-R06 (proposed)" appear only where those rules are tracked.

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-agent | Every role: owner, licensed agent, information security coordinator (the "designated individual" the carrier addenda ask for), privacy contact, risk acceptor, incident lead |
| Outsourced bookkeeper | Remote contractor, about 6 hours a month. Reconciles the operating and premium trust accounts, reconciles commission statements, prepares quarterly reports for the owner's tax preparer. Own user in the accounting SaaS (EV-018). **Signs in to online banking with the owner's credentials. Engagement letter has no confidentiality or security terms** (EV-012, EV-016, EV-020, EV-IA-2) |
| On-call IT consultant | Hourly help with the laptop, router, printer-scanner, and SaaS settings. No standing access. A services agreement with confidentiality and security terms was signed on 2026-07-27 (none before; EV-020) |
| Appointing insurers (9) | Underwrite, bill, and pay claims. Provide agent portals. 4 of 9 impose data security addenda (section 1; EV-021) |
| Wholesale broker | Places hard-to-place risks with 2 more insurers; receives submissions with client information through its portal or email |
| Premium finance company | Finances some commercial premiums; the agency submits finance agreements through its portal |
| Owner's attorney | General business counsel; holds the owner's will and business papers. No breach counsel retained (EV-020) |

## 3. Systems

The full inventory, with the evidence behind each entry, is in [`step-00_P00_intake/asset-inventory.csv`](step-00_P00_intake/asset-inventory.csv).

| ID | System | Hosting | Holds client personal information? | Notes |
|---|---|---|---|---|
| SYS-01 | Agency management system (AMS): client and policy records, scanned documents, activity notes, insurer policy downloads, commission accounting, client upload portal, built-in AI drafting assistant | Vendor SaaS | Yes (system of record) | The vendor enforces MFA (authenticator app on the owner's phone). Vendor provides a SOC 2 Type 2 report. Contract includes breach notice to the agency and data export on request or termination. Client upload portal available but **not used** (EV-001, EV-002, EV-020, EV-027) |
| SYS-02 | Business email, calendar, and file storage suite | SaaS (business plan) | Yes (applications, loss runs, payroll reports, bank draft forms as attachments; invoices for agency-billed policies) | **MFA by text message code only.** Forwarding to outside addresses allowed (default). Deleted items and file versions kept 30 days. Vendor data protection addendum in the terms (EV-005, EV-006) |
| SYS-03 | Insurer agent portals (9), comparative rater, premium finance portal, wholesale broker portal | Insurer- and vendor-hosted | Yes | 7 insurer portals enforce MFA. **2 insurer portals are password only; the comparative rater offers MFA but it is off.** Passwords are saved in the browser and some are reused (EV-009, EV-011) |
| SYS-04 | E-signature service | Vendor SaaS | Yes (signed applications, bank draft authorizations) | Signing links go to the client's email on file (EV-010) |
| SYS-05 | Accounting SaaS and online banking for the operating and premium trust accounts | Vendor SaaS; bank-hosted | Limited (client names, premium amounts, client payment details) | Online banking sends a text code to the owner's phone. **The bookkeeper uses the owner's banking credentials; the owner texts the code to the bookkeeper on request.** The bank offers separate sub-users; none set up (EV-012, EV-016, EV-018) |
| SYS-06 | Laptop, mobile phone, and multifunction printer-scanner | Owner devices | Yes (synced files, downloads, texted ID photos, scans) | Laptop full-disk encryption on. Phone passcode on; holds the authenticator app and **driver license photos clients texted**. The printer-scanner keeps scanned images on internal storage and scans to email. **A retired laptop (replaced 2025) with client files is in a closet, not wiped** (EV-011, EV-012, EV-013, EV-014, EV-MP-6) |
| SYS-07 | Home office network | Internet provider's router in the home | Yes (in transit) | **Default router admin password; one network shared with family phones, a game console, and a smart TV; firmware never updated** (EV-015) |
| SYS-08 | Consumer generative AI chatbot | Consumer plan (web) | Yes (pasted declarations pages and applications) | Used since 2026-04 to compare quotes and draft coverage summaries and renewal emails. **Consumer terms let the vendor use chats to improve its models unless the user opts out; not opted out.** Paused 2026-08-05; see P10 (EV-028, EV-029, EV-033) |

Paper: current signed forms are scanned into the AMS and shredded. Client files from 2014 to 2021 are in boxes in the garage (EV-014).

**SSP system (P02):** the *Agency Systems Profile*: SYS-01 to SYS-08 as one boundary, the owner's core SaaS stack (AMS, email and files, insurer portals, e-signature, accounting and banking) plus the devices and home network used to reach it.

## 4. Where the evidence is
This file says who the company is. It does not say how well its security works. That is established from evidence:
- **What the records show** is in the [intake report](step-00_P00_intake/intake-report.md) and the [evidence register](step-00_P00_intake/evidence-register.csv). Every item has a source system, an owner, and as-of and collected dates. For a one-person agency the sources are the AMS and the other vendors' admin settings and reports, the insurer and rater portals, the device and router settings screens, the inbox and file storage, the signed agreements folder, bank and card statements, the accounting SaaS, the tax files, the licensee records, the E&O insurer's portal, and the lead insurer's security questionnaire.
- **Which rules and contracts apply** is in the [obligations register](step-00_P00_intake/obligations-register.csv).
- **Gaps against Fla. Stat. 501.171, the Florida Insurance Code duties, the insurers' addenda and the 16 CFR 314.4 benchmark** are judged in the gap analysis (P03), and **whether controls work** is tested in the control assessment (P07). Both cite evidence IDs.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | **Business email compromise of the agency mailbox and the premium payment flow.** A phishing page relays the owner's sign-in and text code, the attacker sets a hidden forwarding rule, harvests attachments with client personal information, and sends agency-billed commercial clients invoices with new "premium trust account" bank details. The registry default ("Compromise of payment processing environment") is adapted: a one-person agency runs no payment processing environment; its payment flow is email invoicing into a premium trust account, and that is what an attacker would compromise |
| P09 SOC 2 | The agency is not a service organization and would not obtain a SOC 2 report. Security criteria only: (A) the owner's self-check, which also feeds the insurers' annual security questionnaires, and (B) a review of the AMS vendor's SOC 2 Type 2 report |
| P10 AI | AI-001: the consumer generative AI chatbot (SYS-08). AI-002: the AMS's built-in AI drafting assistant. The registry default ("Transaction fraud-detection model") does not fit a one-person agency that processes no transactions; fraud scoring is done by the insurers and banks. The tier scope is "one third-party AI tool the owner uses" |
| Cloud | SaaS only. No IaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-06-15 | Lead insurer's annual agency security questionnaire received; response with a remediation plan due 2026-09-30 (EV-022) |
| 2026-07-08 | Near miss: a commercial client reports a fake invoice from a lookalike domain (EV-008) |
| 2026-07-27 | IT consultant signs a services agreement with confidentiality and security terms (EV-020) |
| 2026-07-27 to 2026-07-31 | Intake: the owner collects the AMS, email, portal, e-signature, banking and accounting settings and reports, the mailbox review, device and router settings, the home office and garage walk-through, agreements and addenda, the questionnaire, statements, tax and license records, the E&O policy, the AMS vendor's SOC 2 report, and the AI chatbot history and terms; inventories; obligations register |
| 2026-08-03 to 2026-08-07 | Self-assessment with the IT consultant (BIA 2026-08-03; SaaS mapping 2026-08-04; control tests 2026-08-05; AMS vendor SOC 2 review 2026-08-06; risk register and gap analysis 2026-08-07) |
| 2026-08-10 to 2026-09-11 | POL-01 drafted from the gaps and the test results |
| 2026-08-19 to 2026-08-21 | AI use review (2026-08-19) and AI use assessment completed |
| 2026-09-14 | Deliverables and POL-01 adopted by the owner-agent |
| 2026-09-30 | Questionnaire response and remediation plan due to the lead insurer |
| 2027-03 (planned) | Follow-up check: operating effectiveness of the controls POL-01 introduced, after at least one quarter of operation |

## 7. Facts added while building the deliverables
These facts were added so the deliverables agree with each other. They do not change sections 1 to 6.

| Topic | Added fact | Used in |
|---|---|---|
| Near miss details | On 2026-07-08 a small-business client forwarded an email that looked like the agency's renewal invoice for an $18,400 workers compensation deposit premium, sent from a domain one letter different from the agency's, with new bank details. The client called the owner before paying. The agency's own mailbox showed no unknown sign-ins in the 30 days of history kept, and no forwarding rules. The lookalike domain was reported to its registrar (EV-005, EV-008) | P01, P08 |
| Test findings | During the 2026-08-05 tests: a sign-in from a new browser to email needed only the text code; the comparative rater and 2 insurer portals signed in with a password only; the browser held 23 saved agency passwords, 6 of them reused; the retired laptop booted to the owner's old account with client files present; 9 client driver license photos were still in the phone's messages (EV-IA-2(2), EV-IA-5, EV-MP-6, EV-SC-8) | P04, P07 |
| Printer-scanner and old phone | The printer-scanner is leased; the lease ends and the device goes back to the dealer on 2026-11-30. The owner's previous phone (encrypted) was factory reset and handed to a family member in 2025 (EV-013, EV-MP-6) | P07 |
| AMS vendor assurance | The AMS vendor provided its SOC 2 Type 2 report (Security and Availability) under a nondisclosure agreement. Received at intake (EV-027); reviewed on 2026-08-06 | P02, P09 |
| E&O endorsement | The E&O policy's cyber and social engineering endorsement has sublimits of $50,000 (incident response costs) and $25,000 (social engineering fraud loss). It requires notice to the insurer as soon as practicable and use of the insurer's panel vendors (EV-026) | P01, P08 |
| AI chatbot use | Used about twice a week from 2026-04-06 to 2026-08-04 for about 40 client accounts. Pasted text included names, addresses, vehicle identification numbers, prior claims, and, for 7 clients, driver license numbers. No Social Security numbers were found in the chat history. One coverage comparison sent to a client in July 2026 stated the wrong windstorm deductible; the owner corrected it before the policy was bound (EV-028, EV-033) | P01, P03, P10 |
| AMS AI assistant | The AMS vendor added an AI assistant (draft emails, summarize activity notes) in a 2026-06 release, on by default. The vendor's AI terms say customer data is not used to train shared models and prompts are kept 30 days. The owner had used it a few times for renewal emails (EV-004) | P10 |
| Bookkeeper | Works from the bookkeeper's own computer, which the agency has never seen. Has had the owner's banking credentials since 2023 (EV-031, EV-IA-2) | P01, P03, P07 |
