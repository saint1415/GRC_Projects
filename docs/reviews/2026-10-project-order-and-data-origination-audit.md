# Audit of the project order and where the facts come from, October 2026

**Date:** 2026-10-08
**Scope:** the build order of the 10 projects (`docs/how-to-build-the-10-projects.md`) and how each sample's facts originate, across all 216 samples.
**Question asked:** is each project done in a realistic order, and is every conclusion derived from existing data rather than assumed?

## Result

The order was mostly realistic. The way facts originated was not. Every sample's facts file stated the company's security gaps up front, most of them as "found in the 2026 assessments", which are the deliverables themselves. Later projects confirmed conclusions written in advance instead of deriving them from evidence.

## Findings

| # | Issue | Evidence (216 samples, text search) | Realistic approach | Decision |
|---|---|---|---|---|
| 1 | Gaps pre-stated in the facts file | 216 facts files with a posture section; 82 say gaps were "found in the 2026 assessments"; 2 attribute gaps to a dated earlier source | Facts hold who the company is; records go to an intake evidence register; P03 and P07 derive findings | Full rebuild (facts become evidence) |
| 2 | No intake or inventory step | 48 name an inventory source; 17 say how AI tools were found | Step 0 collects exports from systems of record (SP 800-37 Tasks P-10, P-12, P-13, P-15; CSF 2.0 ID.AM, GV.OC-03) | New deliverable `step-00_P00_intake` |
| 3 | Applicability decided at step 5 but needed at steps 1 and 2 | 216 BIAs rate regulatory impact before step 5 | Obligations register at intake; P03 keeps the requirement analysis | Moved to intake |
| 4 | Linear presentation of a loop | 207 risk reports cite P03, built after them | Show pass 1 (risk and gap fieldwork) and pass 2 (after P07) | `assessment_pass` column |
| 5 | Testing policies not yet approved | 0 assessment plans separate design from operating effectiveness | Mark each result operating, design only, or not implemented; follow-up test after a quarter | `test_type` column |
| 6 | BIA limits asserted | 6 BIAs cite interviews; 123 cite financial records | Owner interviews and financial records, cited per process | `source_evidence` column |
| 7 | Likelihood without data | 47 risk reports cite incident history or threat intelligence; 42 cite scans | Likelihood basis cites incident tickets, scans, exports, interviews | `likelihood_basis` column |

Kept as is, because it was realistic: P04 after P02; P08 assembled from P05 and the notification duties; P09 and P10 last with their fit checks; P07 evidence references with sampling.

## Decisions (2026-10-08)

1. Full rebuild: the facts file says who the company is; what its records show lives in step-00 with dated evidence IDs.
2. The guide shows one lifecycle plus the event that usually starts the work at each size.
3. Step folders are renamed only where the order changes. Only step-00 is new, so no existing folder moved.
4. Intake is a real deliverable with five files.
5. Pilot on the six Health Care samples first; the other 210 follow after review.

## Pilot controls

`tools/validate.py` now checks every sample that has a step-00 folder:
- every evidence ID cited anywhere in the sample exists in the register;
- each register row has a source system, owner, phase, and as-of and collected dates in order;
- observations contain no judgment words;
- the facts file has no pre-stated posture section;
- every P07 result has a test type and every risk has a likelihood basis and a pass.

## Rollout log

Industries are converted one at a time after the pilot. Each batch records what the conversion cost and which pre-existing inconsistencies the dated evidence exposed. Findings, counts and risk levels were not changed during conversion; the inconsistencies below are left for a separate fix.

### Healthcare and Public Health (critical infrastructure), 2026-10-08

Six samples, 605 evidence rows in all. Agent cost: about 2.6 million tokens; the longest sample took 31 minutes.

Pre-existing inconsistencies exposed by dating the evidence:
- **Size 2 (independent pharmacy):** the EPCS audit report is treated as on file in P03 and P07 but was obtained on 2026-08-12; two MSP reports labelled July fell inside a fieldwork window that ended in July; a backup console finding called "new from testing" in P07 already appears in pass 1 of the risk register and the SSP.
- **Size 4 (hospital):** the SSP gives 6 legacy VPNs without written terms in one place and 3 in another; a July backup sample is cited by P03 after its fieldwork ended; two pass-1 risks quote P07 results; P07 marks a plan approval Satisfied although the approval came after fieldwork.
- **Size 5 (hospital system):** P07 calls the risk analysis approved before P01 was approved; the 24-hour recovery target is said to come from the BIA, which ran after the restore test it is measured against; one gap row says the unified program has covered all 8 hospitals since 2024, although one hospital joined in 2026.

### Agriculture, 2026-10-08

Six samples, 573 evidence rows in all. Agent cost: about 2.5 million tokens; the longest sample took 29 minutes.

Fixes made to earlier batches during this one:
- **Health Care size 4:** the `assessment_pass` and `last_reviewed` values were swapped on all 50 risks. Swapped back; the validator now requires every pass value to start with "Pass" and checks division risk registers too.
- **Health Care size 6:** three P07 evidence IDs used a trailing hyphen number (EV-C-AC2-3 and two others). Renamed to the parenthesis form used everywhere else.
- **Agriculture size 3:** the Florida Digital Bill of Rights threshold was marked unverified. Fla. Stat. 501.702 was read on 2026-10-08: a controller must have more than $1 billion in global gross annual revenue and meet one further test.

Pre-existing inconsistencies exposed by dating the evidence:
- **Size 2 (micro crop farm):** pass-1 deliverables dated 2026-07-31 rely on the FMIS vendor's SOC 2 report, which arrived on 2026-08-18.
- **Size 4 (mid-market crop farm):** the SSP's backup evidence says 30 of 30 days, P07 says 31 of 31; training completion is 94% in the SSP and 96% in P07; personnel-share readers are 48 in the SSP and R-003 but 46 in P03.
- **Size 5 (enterprise crop farm):** P03 cites board minutes and a budget approval dated after its own approval; the facts say up to 7,300 seasonal accounts while the deliverables count 3,840.
- **Size 6 (crop farm plus two divisions):** the cloud map says the food defense repository is limited to qualified individuals, while the facts and P01 say 140 plant staff can read it.

### Food and Agriculture (critical infrastructure), 2026-10-09

Six samples, 549 evidence rows in all. Agent cost: about 2.4 million tokens; the longest sample took 27 minutes.

Fixes made during this batch:
- **Size 6 (meat processor plus two divisions):** three P07 evidence IDs had lost their parentheses (EV-C-AC23, EV-C-AC65, EV-C-IA21). Renamed to EV-C-AC2(3), EV-C-AC6(5) and EV-C-IA2(1). MT-030's `last_reviewed` moved to 2026-08-15 to match its pass-2 date.

Pre-existing inconsistencies exposed by dating the evidence:
- **Size 2 (micro meat processor):** P07 says the delivery driver was given accounting access, while the facts list three named accounting users; G-046 rests on that later P07 test.
- **Size 3 (small meat processor):** P09, dated 2026-08-21, cites policies published on 2026-09-07 and items approved on 2026-09-04.
- **Size 4 (mid-market meat processor):** the same 23 of 41 Plant 2 OT change records are cited as P03 evidence (EV-065) and as a P07 test sample.
- **Size 5 (enterprise meat processor):** G-045 cites a P01 transmittal dated 2026-09-08, after P03 was approved on 2026-08-21.
- **Size 6 (meat processor plus two divisions):** the Plant 6 walkthrough on 2026-07-14 falls inside the P07 window but is kept as P03 fieldwork; the P04 cloud map's "limited to qualified individuals" wording, logged for Agriculture size 6, does not occur here.

### Administrative and Support Services, 2026-10-09

Six samples, 576 evidence rows in all. Agent cost: about 2.5 million tokens; the longest sample took 31 minutes.

Fixes made during this batch:
- **Size 1 (independent recruiter):** the home office walk-through moved from 2026-07-21, inside the P07 window, to 2026-07-15 at intake.
- **Sizes 1 and 4:** EV-IA-2-1 renamed EV-IA-2(1).
- **Size 6 (staffing firm plus two divisions):** four P07 evidence IDs ran the enhancement number into the control number (EV-C-AC23, EV-C-AC65, EV-C-IA21, EV-G-IA22). Renamed to EV-C-AC2(3), EV-C-AC6(5), EV-C-IA2(1) and EV-G-IA2(2).

Pre-existing inconsistencies exposed by dating the evidence:
- **All sizes:** P03, P08 and P10 cite regulatory text checks dated 2026-09-23 to 2026-10-06, after the deliverables were approved.
- **Size 1:** about 3,400 ATS records "since 2019" does not fit about 1,200 added each year with nothing deleted; P03 cites draft policies during a week when, by the calendar, no draft existed; the 2026-07-23 search is said to cover the mailbox and laptop but its results include phone photos.
- **Size 2 (micro staffing firm):** P07 examined the payroll vendor's SOC 2 report, which arrived two days after fieldwork ended; P07 cites the owner's approval and a policy effective date that come after its own results; P04, prepared 2026-07-31, cites P07 tests and POA&M IDs; the ATS "7 named users" leaves out a former recruiter's account that stayed active until 2026-07-21.
- **Size 3 (small staffing firm):** P03 rates G-062 Met on a TLS scan dated in the P07 window (kept as P03 follow-up); E-Verify users are 6 specialists in the facts, 6 accounts with 2 departed in G-126, and 4 current users in G-127; SSP IA-12 cites an onboarding procedure that G-120 says is not written down.
- **Size 4 (mid-market staffing firm):** P07 cites approvals and audit committee minutes dated 2026-09-22, after fieldwork ended on 2026-09-04; pass-1 risks R-010, R-031 and R-045 cite P07 results; P09 cites minutes dated after it was prepared; the SSP's "I-9 sample of 25" matches neither the P03 nor the P07 sample; AI-002 records a change dated 2026-10-31 as done.
- **Size 5 (enterprise staffing firm):** P03 cites a September budget approval after its own approval; P09 calls the SL-2 system description a draft while its evidence map says it has not started; the P07 plan header and schedule give different fieldwork windows; R-012 lists kiosk EDR that G-079 says is missing.
- **Size 6:** POAM-020 and the P03 roadmap say 2026-12-31 while the division supplement and POL-01 say 2026-11-30; G-150 cites a counsel memo on Staffing's business associate status that the facts do not mention.

### Arts, Entertainment and Recreation, 2026-10-09

Six samples, 614 evidence rows in all. Agent cost: about 2.4 million tokens; the longest sample took 26 minutes.

Fixes made during this batch:
- **Validator:** the evidence register `phase` column now accepts only `Intake`, `Intake follow-up`, `Pnn fieldwork` and `Pnn follow-up`. The one earlier value outside that set (`P09 review`, Healthcare and Public Health size 2) became `P09 fieldwork`.
- **Sizes 1 and 3:** EV-IA-2-1 renamed EV-IA-2(1). **Size 6:** EV-C-AC23, EV-C-AC65 and EV-C-IA21 renamed to the parenthesis form.
- **Size 5:** a sentence the conversion added to P10 ("Discovery found no AI use outside the register") was removed; it was a new conclusion.

Pre-existing inconsistencies exposed by dating the evidence:
- **All sizes:** P03, P08 and P10 cite regulatory text checks dated 2026-09-23 to 2026-10-06, after the deliverables were approved.
- **Size 1 (independent event promoter):** "19 monthly exports" for 2024-12 to 2026-07 covers 20 months; the SSP's AC-11 and P04's laptop encryption cite a P07 walk-through for controls P07 did not test.
- **Size 2 (micro venue):** the BIA, P04 and P03 rest on the ticketing vendor's AOC and SOC 2 report, first read on 2026-08-19, after their fieldwork; the P07 plan lists both as examined during 08-10 to 08-12; R-004 (reviewed 07-24) cites the 08-03 purge.
- **Size 3 (small venue):** pass-1 R-006 states 5 stale accounts that P07 found later; the P07 plan puts network tests on 08-04 while SC-7 says 08-05; POAM-002 cites G-031 for requirement 7.2, which is G-030; G-035 cites EV-IA-2 where the MFA test is EV-IA-2(1); P09 (2026-08-21) cites events of 2026-08-31.
- **Size 4 (mid-market venue):** CM-07a says 31 third-party scripts while its evidence shows 33; P09 (2026-09-04) cites minutes and risk appetite of 2026-09-15; P09 says vendor reviews ended 2026-09-11, the calendar says 2026-09-04; P09 says quarterly committee reporting began 2026-09 while the facts say it is quarterly.
- **Size 5 (enterprise venue):** P03 cites P10 tests that ran after its sampling ended; the BIA cites P01, POA&M and P08 items approved later; P07 findings cite policy sections approved after the report; DEP-19 gives the last MSSP tabletop as 2026-03-19 while the facts and P08 say 2025-10-21.
- **Size 6 (venue plus two divisions):** LV-021 says group venues use rotating barcodes while the facts say 3 still use static ones; GR-05 lists policies effective 2026-10-01 as an existing control in a register prepared 2026-07-31.

### Construction, 2026-10-12

Six samples, 588 evidence rows in all. Agent cost: about 2.5 million tokens; the longest sample took 28 minutes. (A first launch on 2026-10-09 stopped at the usage limit before any edits and was rerun.)

Fixes made during this batch:
- **Validator:** a risk whose `assessment_pass` is Pass 2 may not have a `last_reviewed` date earlier than its Pass 2 date. **Size 6:** PRP-006 and PRP-018 moved from 2026-07-31 to 2026-08-12 to meet it.
- **Sizes 1 to 3 and 6:** trailing-hyphen P07 IDs (EV-IA-2-1, EV-C-AC2-3 and others) renamed to the parenthesis form.
- **Size 5 (enterprise contractor):** payment fraud events EV-2026-04 and EV-2026-06 relabelled INC-2026-04 and INC-2026-06, so incident numbers are not read as evidence IDs.

Pre-existing inconsistencies exposed by dating the evidence:
- **All sizes:** P03 cites regulatory text checks dated after its approval.
- **Size 1 (sole-proprietor contractor):** the P03 header says only G-006 changed after P07 testing, but four more rows cite P07 results; G-028 places the doorbell camera off a work network that does not exist until 2026-09-30; the BIA cites a P09 vendor review dated two days later.
- **Size 2 (micro contractor):** SYS-01 has three administrators in the facts and P07 AC-2 but two in the SSP, P04 and P07 IA-2(1); the BIA and P04 cite reviews and tests dated after they were prepared; R-021 is said to close on 2026-08-31 while its last review is 2026-07-31.
- **Size 3 (small contractor):** P03 G-001 cites a P07 result from August, and G-027 and G-029 cite follow-ups after the P03 update date; G-015 confirms protection on all 20 tablets from a sweep of 2 jobsites; deliverables disagree on which vendor SOC 2 reports are on file.
- **Size 4 (mid-market contractor):** pass-1 R-002 and R-039 quote August P07 samples; R-007 says 45 SP 800-171 requirements are not fully met while P03 says 40; the SSP cites P07 results for AC-6(2), which P07 did not test; P04 and P03 name different reviewers of the enclave log.
- **Size 5 (enterprise contractor):** P03 G-087 and G-146 disagree on whether the enclave SSP maps the provider's responsibility matrix, and G-001 and G-035 disagree on whether the plotters are enrolled; the BIA, P03, P09 and P04 cite POA&M IDs and P07 results issued 2026-09-04.
- **Size 6 (contractor plus two divisions):** pass-1 GR-06 and AE-006 cite P07 findings from August; the P01 report still says CMMC Phase 2 "just begins"; the facts and the findings disagree on whether superintendents use enclave desktops; P03 G-026 samples 30 subcontract awards where P07 SR-6 samples 25.

### Education, 2026-10-12

Six samples, 555 evidence rows in all. Agent cost: about 2.4 million tokens; the longest sample took 27 minutes.

Fixes made during this batch:
- **Validator:** an evidence register ID may not use a hyphen for a control enhancement (EV-IA-2-1); it must be EV-IA-2(1). **Health Care size 4** still had EV-IA-2-1 in three files; renamed.
- **Sizes 1 and 3:** EV-IA-2-1 and EV-IA-2-2 renamed. **Size 6:** EV-C-AC23, EV-C-AC65 and EV-C-IA21 renamed to the parenthesis form; HE-021's `last_reviewed` moved to its Pass 2 date, 2026-08-19.
- **Sizes 1 and 3:** walk-throughs and reviews that the sample dated inside the P07 window but used as evidence of the starting state were re-dated to intake.

Pre-existing inconsistencies exposed by dating the evidence:
- **All sizes:** P03 cites regulatory text checks dated after its approval.
- **Size 1 (tutoring service):** P04 is mapped a day before the P07 results it cites; R-014 says vendor commitments meet the BIA while the vendor review says the 12-hour RTO misses BP-02's 8 hours; POAM-002 cites G-037 rather than G-028.
- **Size 2 (micro tutoring company):** the SSP cites POL-02 A.2 and A.6 where the clauses are A.3 and A.7; the facts say families pay by card while about 20 pay by bank debit; P07 AC-2 counts 21 users across systems where the suite has 7.
- **Size 3 (career college):** P03 G-012 and G-053 describe stale adjunct accounts P07 says it found first; P07 samples termination tickets for adjunct contract ends, which AC-02h says are not sent to IT.
- **Size 4 (private college):** pass-1 R-007, R-012, R-025, R-041 and R-042 quote sample results the SSP credits to P07; G-032 and P07 SR-6 cite P09 vendor reviews dated September; BP-06 lists an identity verification vendor the SSP plans for 2027.
- **Size 5 (enterprise college):** P03 cites the Qualified Individual's report of 2026-09-10, after its approval; the facts say 10 of 16 AI uses were reviewed at intake while the P10 dates show 8; R-001 gives EDR on 98% of endpoints while the SSP says all.
- **Size 6 (college plus two divisions):** SSP AC-6(7) says service accounts are certified while P07 found them excluded; the SSP and P09 disagree on the proctoring contract's notice term; pass-1 SH-001 and GR-06 cite August findings.

### Finance and Insurance, 2026-10-12

Six samples, 545 evidence rows in all. Agent cost: about 2.6 million tokens; the longest sample took 28 minutes.

Fixes made during this batch:
- **Sizes 1, 2 and 6:** trailing-hyphen P07 IDs (EV-IA-2-1, EV-SC-28-1, EV-AT-2-3, EV-C-AC2-3 and others) renamed to the parenthesis form.
- **Sizes 1 and 3:** walk-throughs and reviews dated inside the P07 window but used as evidence of the starting state were re-cited to intake rows.

Pre-existing inconsistencies exposed by dating the evidence:
- **All sizes:** P03 (and in sizes 2 to 4 the P08 notification matrix) cites regulatory checks dated after approval.
- **Size 1 (investment adviser):** P07 SA-9 covers "all 10 vendors" while the vendor register lists 14; the facts and R-006 say statements were pasted into the chatbot through 2026-07-15, after the export behind them.
- **Size 2 (credit union):** the SSP says the requirement list has no NCUA Part 748 row, which N52-R09 now provides; P04 (2026-07-24) relies on a P07 test and a mailbox change from August; POL-04 and POL-05 refer to P10 conditions decided after their approval.
- **Size 3 (community bank):** P04 and P03 cite P07 AC-2 results; P09 (2026-08-20) cites committee minutes, policies and runbooks dated later; R-030 says policies were adopted 2026-08-27 while it was last reviewed 2026-07-24.
- **Size 4 (regional bank):** POAM-009's portal log review is due 2026-09-30 while P07 and R-049 already state its result; P07 SR-6 cites P09 vendor reviews dated after fieldwork.
- **Size 5 (super-regional bank):** P03 and the BIA quote the Q2 asset averages before the Q2 reports were filed; P04 says phishing-resistant MFA is applied to client-service staff while R-005 puts it in its treatment; the facts say 12 AI uses were reviewed at intake while the dates show 11.
- **Size 6 (diversified financial group):** P03 says Colorado SB26-189 deployer duties are under review for the bank while P10 says it does not apply; the SSP says support console views go to the SIEM while P07 says those logs are not collected; P10 cites POL-01 4.13 for the Group AI Standard, which first appears in v2026.

### Financial Services (critical infrastructure), 2026-10-12

Six samples, 583 evidence rows in all. Agent cost: about 2.5 million tokens; the longest sample took 31 minutes.

Fixes made during this batch:
- **Sizes 1, 2 and 6:** trailing-hyphen and run-together P07 IDs (EV-IA-2-2, EV-IA-2-1, EV-C-AC23, EV-M-IA22 and others) renamed to the parenthesis form.
- **Size 1 (insurance agency):** the garage walk-through dated inside the self-assessment window was re-cited to the intake walk-through; G-008 cited an AMS export that was never taken and now cites the intake record.
- **Size 2 (merchant services provider):** P03, P04 and the SSP cited a console audit log sample from before P07, but the facts say the log was first opened in P07; P03 and P04 now cite the gateway's audit log documentation and the SSP cites the P07 test.

Pre-existing inconsistencies exposed by dating the evidence:
- **All sizes:** P03 cites regulatory checks dated after its approval.
- **Size 1:** facts section 7 says the mailbox showed no unknown sign-ins in 30 days of history, while the old posture and P07 AU-6 say the history was never reviewed.
- **Size 2:** P07 SI-2 tested one spare laptop but reports on both; spare terminals are about 40 in the facts, 44 in the spreadsheet and 41 in P07; P04 (2026-07-24) cites a P07 export from August.
- **Size 3 (small payment processor):** four artifacts carry two dates across deliverables (TLS scan, token list, ticket sample, SIEM samples); P02 and P03 disagree on the year of the last developer training; G-057 says no scan followed the March migration while citing Q2 scans.
- **Size 4 (mid-market payment processor):** pass-1 R-009, R-021 and R-023 cite P07 results and a September date; July is counted as 30 days in the backup and reconciliation evidence; the facts list two-person change approval as compensating while P03 and P07 found 4 of 15 changes approved by their authors.
- **Size 5 (enterprise payment processor):** P09 (prepared 2026-08-28) cites the P07 report issued 2026-09-04; R-032 rests on a P07 packet capture but is not listed as added after P07; one population is "2,340 account events" in P07 and "2,340 access grants" in P03.
- **Size 6 (payment processor plus two divisions):** P10 says AI-001 to AI-005 were live before the Group AI Standard while AI-004 launched after it; the SSP names PL-2 where P07 assessed PL-1; POAM-024 is closed with a milestone due 2026-12-31.

### Management of Companies and Enterprises (holding companies), 2026-10-12

Six samples, 565 evidence rows in all. Agent cost: about 2.6 million tokens; the longest sample took 29 minutes.

Fixes made during this batch:
- **Sizes 1 and 6:** trailing-hyphen and run-together P07 IDs (EV-IA-2-1, EV-C-AC65, EV-S-AC67 and others) renamed to the parenthesis form.
- **Size 4 (mid-market holding company):** the SSP's AC-21 cited a P07 data loss prevention test with no results row; it is now registered as P07 fieldwork evidence (EV-072) without adding a result.

Pre-existing inconsistencies exposed by dating the evidence:
- **All sizes:** P03 (and in most sizes the P08 matrix) cites regulatory checks dated after approval.
- **Size 1 (owner of several small businesses):** deliverables say seven SaaS services while six are named; routers are three in the SSP and P04 and two plus home Wi-Fi in the facts; P07 calls two items new findings that the old posture already listed; about 670 people with Florida personal information against 665 by addition.
- **Size 2 (family holding office):** P03 and P02 state the bill pay and vault admin issues that P07 reports as new findings; R-023 stays Open after dual approval was turned on 2026-09-04; P02 and P09 count a family vault user whose account was created 2026-08-20.
- **Size 3 (small holding company):** P01 R-024, R-025 and R-005 cite the wrong BIA processes; BP-01 says approvals use hardware tokens while R-016 says app-based; P09 (2026-09-18) cites minutes and designations of 2026-09-25.
- **Size 4:** July backups are 30 of 30 days in P04 and 31 of 31 in P03 and P07; G-115 says servicing access is reviewed twice a year while P07 says only the ERP is; G-132 counts an intercompany schedule signed after P03 and P07; the facts present the plan Security Official as in place before the 2026-09-22 designation.
- **Size 5 (enterprise holding company):** the facts say the health plan amendment covers 164.314(b) while section 7 and G-056 say it does not; DEP-11 cites R-039 where the field-service risk is R-022; R-042 cites a change dated after its last review.
- **Size 6 (holding company plus two divisions):** P10 cites POL-01 4.14 for a standard adopted before v2026 was approved; HCS-013 and HCS-014 are Closed with a due date after their last review; G-015 and P01 disagree on when the budget was approved.

### Hotels and Restaurants, 2026-10-12

Six samples, 574 evidence rows in all. Agent cost: about 2.5 million tokens; the longest sample took 32 minutes.

Fixes made during this batch:
- **Sizes 1, 3, 4 and 6:** trailing-hyphen P07 IDs (EV-IA-2-1, EV-C-AC2-3, EV-V-IA2-2 and others) renamed to the parenthesis form.
- **Size 1 (bed and breakfast):** a stray copy of the P01 risk register at the sample root, left from an earlier build and identical to the step-04 file, was removed. No other sample has one.

Pre-existing inconsistencies exposed by dating the evidence:
- **All sizes:** P03 cites regulatory checks dated after its approval.
- **Size 1:** R-003 and P09 Part A cite a facilitator email and a P10 chat review dated after them; P03 cites P10 tests from 2026-08-24.
- **Size 2 (small motel):** P04 (2026-07-24) cites five items from August; P03 cites a binder count dated 2026-07-15 while the only count is from 2026-08-04; "all 5 front office users" can display card numbers while 2 former staff accounts stayed active.
- **Size 3 (beachfront hotel):** pass-1 R-031 lists default passwords found by P07; the P07 plan says nothing existed for AC-6, IA-2(1), SC-8 and SC-28 while their own details show those controls tested; 20 PMS users with card access against 22 front office users elsewhere.
- **Size 4 (hotel operator):** the revenue management vendor's report is SOC 2 Type 2 in the SSP and Type 1 in P09 and the facts; P07 RA-3 calls the risk assessment approved before it was; IR-08d is Satisfied while IR-08b says the plan was not distributed.
- **Size 5 (enterprise hotel operator):** firewall rule reviews are six-monthly in G-002 and quarterly in P09; the facts say emailed card forms while G-041 says printed; P02 says POS accounts are vaulted while G-037 says hardcoded; the chatbot result "9 of 20" appears for both the July and August tests.
- **Size 6 (hotel operator plus two divisions):** the P03 method samples 60 adverse action notices while the rows and P10 say 50; P08 says association agreements require 5-day notice while P09 says they have no notice commitment; G-004 and P07 CA-3 disagree on whether interconnection terms exist.
