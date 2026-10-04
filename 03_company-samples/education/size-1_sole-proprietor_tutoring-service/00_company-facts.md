# Scenario facts: Cris Santos Company | Educational Services | Sole Proprietorship

All 10 deliverables in this folder use the facts below. The company is fictitious. This scenario is independent of the other sizes. Where a fact comes from a regulation, the citation is given.

## 1. The organization
| Item | Fact |
|---|---|
| Legal name | Cris Santos Company (sole proprietorship; the owner files Schedule C) |
| Business | Tutoring and educational support service (NAICS 611710): one-to-one math and reading tutoring for students in grades 2 to 7, SAT and ACT preparation for high school students, study-skills coaching, and learning-plan consultations for families |
| Location | Florida. Home office. Sessions are held online (about 60%), in students' homes, or in a public library study room. Online sessions are offered only to Florida families (a scenario choice that keeps state law to Florida) |
| Workforce | The owner-tutor only (0 employees). No substitute tutor |
| Students | About 55 active students: 36 are under 13 (grades 2 to 7) and 19 are teens (grades 8 to 12). About 32 session hours a week during the school year. Files for about 210 former students (since 2019) are still kept, so the business holds records on about 265 children |
| Sensitive student data | Names, grades, schools, assessment results, progress notes, photos of student work, report cards and test score reports shared by parents, and, for 9 current and about 30 former students, IEP or Section 504 plans and psychoeducational evaluations (disability and diagnosis information) shared by parents. Parent names, emails, phone numbers, and home addresses. No Social Security numbers |
| Revenue | About $180,000 a year (fictional). SBA-small (standard $24.0 million for NAICS 611710; 13 CFR 121.201) |
| Payments | Parents pay by card through the client-management SaaS, which uses a payment processor's hosted payment page. The owner never sees full card numbers (noted only; not analyzed) |
| COPPA status | **Operator of an online service directed to children.** The student practice portal (SYS-03) is a members-only area of the business website built for students in grades 2 to 7. It collects personal information online from children under 13: first and last name, a user name, photos of their work, audio clips of them reading aloud, and messages (16 CFR 312.2 "operator", "personal information", "website or online service directed to children"). The 2025 amendments (90 FR 16918, Apr. 22, 2025) took effect June 23, 2025, with a compliance date of April 22, 2026 for operators, so they apply in full at fieldwork |
| Contrast worth noting | If the owner taught only in person and collected nothing online from children, COPPA would not apply. The applicability test is online collection from children under 13, not size. Information that parents give the owner (intake forms, report cards, IEPs) is not collected "from a child", so COPPA does not reach it; Florida law and the FTC Act still do |
| FERPA status | **Does not apply.** FERPA binds educational agencies and institutions that receive funds under a Department of Education program (34 CFR 99.1). The business receives no such funds and has no contract with a school or district. Records parents share are held under the family's enrollment agreement. Recheck if the owner ever contracts with a school or district |
| GLBA Safeguards Rule status | **Does not apply.** The business does not participate in Title IV and is not a financial institution: it extends no credit and offers no financing; parents pay per session or prepay packages (author's analysis of 16 CFR 314.1 and 314.2) |
| Not in scope | CIPA (not an E-Rate recipient); HIPAA (not a health care provider or covered entity); CIRCIA (proposed only, and the business is not a school district, a Title IV institution, or above the SBA size standard); payment card security (processor-hosted) |
| State law approach | Florida law is cited only where unavoidable: data security and breach notice (Fla. Stat. 501.171) and recording consent for online sessions (Fla. Stat. 934.03) |

## 2. People and contracted services (role titles only)
| Role | Duties |
|---|---|
| Owner-tutor | Every role: owner, tutor, information security program coordinator (16 CFR 312.8(b)(1)), privacy contact for parents, risk acceptor, incident lead |
| On-call IT technician | Hourly help with the laptop, router, and accounts. Remote-support tool on the laptop; no standing access. Signed a confidentiality and data-handling agreement on 2026-07-08, before the self-assessment |
| Tax preparer (CPA firm) | Receives the annual accounting export (parent names and payment totals only) |
| Former freelance web designer | Built the website and portal in late 2024. No current engagement (see section 7) |
| Family members | Use the owner's laptop for personal browsing under the same user account (a gap, not a role) |

## 3. Systems
| ID | System | Hosting | Holds children's or student data? | Notes |
|---|---|---|---|---|
| SYS-01 | Business email and productivity suite: email, calendar, cloud file storage with desktop sync, documents | SaaS (paid business plan) | Yes: student folders (progress notes, assessments, work photos, report cards, IEP and 504 plans, evaluations); a spreadsheet of student portal user names and passwords | **MFA available but off.** File version history kept 30 days (vendor default). Files sync to the laptop |
| SYS-02 | Tutoring client-management SaaS: scheduling, student and parent profiles, session notes, invoices, e-signature, card payments through a processor's hosted page | Vendor SaaS | Yes: student name, grade, school; parent contacts; session note summaries | System of record for clients and billing. **MFA enforced by the vendor.** Vendor provides a SOC 2 Type 2 report on request |
| SYS-03 | Website and student practice portal: public pages, booking link to SYS-02, and a members-only student area (assignments, photo uploads of work, reading-aloud audio clips, messages to the owner) | Website-builder SaaS | Yes: personal information collected online from children under 13 | Launched January 2025. **Admin sign-in is password only.** No children's privacy notice on the site |
| SYS-04 | Video meeting platform for online sessions | SaaS (paid plan) | Yes: live video and audio; cloud recordings | Cloud recording turned on for families who asked for replays. **MFA off** |
| SYS-05 | Laptop | Owner device | Yes: synced copy of SYS-01 files; downloads | **No full-disk encryption. Shared with family members under one user account.** Built-in antivirus and automatic updates on |
| SYS-06 | Mobile phone | Personal device | Yes: texts with parents; photos of student work | Photos sync to a personal photo cloud account. Holds the authenticator app for SYS-02 and SYS-08 |
| SYS-07 | Home network | Internet service provider's router | In transit | **Router admin password still the default.** Family and smart-home devices share the network. Phone hotspot or library Wi-Fi when away |
| SYS-08 | Accounting SaaS | Vendor SaaS | No (parent names and payment amounts only) | MFA on |
| SYS-09 | Consumer generative AI assistant (free tier, personal account) | Vendor app | Yes: student first names, scores, accommodations pasted into prompts | Used since March 2026; see P10 |

**SSP system (P02):** the *Core Business SaaS Stack*: SYS-01 to SYS-09, the owner's email and files, client and billing records, student practice portal, video sessions, and the devices and home network used to reach them.

## 4. Current security posture: early (few formal controls)
**In place today:**
- A paid business plan for email and files (not a personal consumer account), with 30-day file version history
- MFA enforced by the client-management SaaS (SYS-02); MFA on the accounting SaaS (SYS-08)
- Card payments only through the processor's hosted page; no card numbers stored
- Automatic operating system updates and built-in antivirus on the laptop and phone
- Phone passcode with biometric unlock
- A signed enrollment agreement for every family (e-signed in SYS-02), with a photo and recording permission checkbox
- Paper worksheets and printed notes shredded at home with a cross-cut shredder

**Missing:**
1. No risk assessment ever performed (16 CFR 312.8(b)(2)).
2. No written information security program or policies (312.8(b)).
3. No online notice of children's information practices on the portal, and the enrollment agreement does not contain the direct notice content COPPA requires (312.4(c)(1), 312.4(d)).
4. No written data retention policy. Files on about 210 former students since 2019 and 27 inactive portal accounts are kept indefinitely (312.10).
5. No MFA on the email and files suite, the website-builder admin account, or the video platform.
6. The laptop is not encrypted and is shared with family members under one user account.
7. The home router still uses its default admin password, and family devices share the network.
8. No backup independent of cloud sync. Ransomware on the laptop would sync encrypted files into cloud storage, and version history lasts only 30 days.
9. No review of vendors and no written security assurances from the portal, video, or AI vendors (312.8(c)).
10. Cloud recordings of online sessions are kept with no deletion schedule, and recording consent is a checkbox that is not always ticked (Fla. Stat. 934.03).
11. Student information was pasted into a consumer AI assistant (P10).
12. No incident plan, no contact list, and no cyber insurance (general liability policy only).
13. Texts with parents and photos of student work sit on the personal phone and sync to a personal photo cloud.
14. No security training.

## 5. Scenario choices
| Deliverable | Choice |
|---|---|
| P08 incident | Ransomware on the laptop that encrypts the synced student files (the encrypted copies sync to cloud storage) and steals the student folders and the portal password spreadsheet. The client-management SaaS and the portal are not affected. This is the registry default ("ransomware with student record exposure"), which fits this business |
| P09 SOC 2 | Security criteria only, as (a) the owner's self-check and (b) a checklist for reading the client-management SaaS vendor's SOC 2 Type 2 report. Families and the occasional school partner accept a self-attestation |
| P10 AI | The registry default, "AI admissions and student-success risk scoring", is adapted: a tutor has no admissions process. The equivalent use here is the consumer AI assistant (SYS-09) rating each student's "support level" from assessment scores and recommending the starting level for SAT boot camps, then drafting parent progress reports |
| Cloud | SaaS only. No IaaS or PaaS |

## 6. Assessment calendar (fictional)
| Date | Event |
|---|---|
| 2026-07-13 to 2026-07-17 | Self-assessment with the on-call IT technician (summer, light session load). Tests on 2026-07-16 |
| 2026-07-31 | Deliverables adopted by the owner-tutor |
| 2026-08-17 | Fall tutoring term begins |
