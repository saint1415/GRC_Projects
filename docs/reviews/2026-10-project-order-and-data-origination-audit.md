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
