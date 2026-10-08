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
