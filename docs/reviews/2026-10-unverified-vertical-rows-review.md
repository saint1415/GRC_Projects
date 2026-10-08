# Review of the unverified vertical rows, October 2026

**Date:** 2026-10-08
**Scope:** the 19 rows in `02_industry-rules/` marked `verified=false`, which `tools/validate.py` reported as its one warning (`PLAN.md`, open item 1). There were 16 incident notification rows and 3 requirement rows.
**Method:** each row was checked against a primary source. If a source could not be reached from this environment, the row stays unverified and the reason is recorded. Secondary summaries were used only to find the primary text.

## Result

17 rows are now verified. 2 stay unverified. The validator warning count fell from 19 to 2.

| Rows | Before | After | Primary source |
|---|---|---|---|
| Generic state breach notification (10): Administrative and Support, Arts and Entertainment, Education, Hotels and Restaurants, Information, Real Estate, Commercial Facilities, Repair and Personal Services, Retail Trade, Wholesale Trade | "Varies by state"; some cited a California URL that returns HTTP 403 here | Florida worked example with its actual clocks. Each other state is still named as applying its own statute, not reviewed here | Fla. Stat. 501.171(3)-(5), leg.state.fl.us |
| Card brand compromise (3): Hotels and Restaurants, Repair and Personal Services, Retail Trade | "Per contract" | Report immediately, in the format in Visa's What To Do If Compromised. The acquirer (the Visa Member) reports, and in the US a merchant may report for it. Visa may require an investigation with PCI Forensic Investigator access. The merchant gets these duties through its merchant agreement, not by law | Visa Core Rules and Visa Product and Service Rules, 18 April 2026, rules 10.3.1.1 and 10.3.1.2 |
| FedRAMP incident communications (Information Technology) | "Not verified" | Initial report clocks by Potential Agency Impact N-rating (PAIN) and certification class. Optional from 2026-07-04, required from 2027-01-01, grace period ends 2027-06-01 | FedRAMP Consolidated Rules for 2026, Rev5 Incident Evaluation and Communication, fedramp.gov |
| State and local government reporting (Public Administration) | "Varies" | Florida worked example: 12 hours for ransomware, 48 hours for other severity 3-5 incidents, after-action report within 1 week. The samples are contractors, so the row says the contractor supplies facts to the county or city rather than reporting itself | Fla. Stat. 282.3185(5)-(6) |
| Federal agency reporting (Government Facilities) | "Not re-verified" | Within 1 hour, to CISA as the federal incident center. Contractors report to their agency as the contract requires | 44 U.S.C. 3554(b)(7)(C)(ii) on govinfo (USCODE-2023); CISA Federal Incident Notification Guidelines, effective April 1, 2017 |
| N54-R07, ABA Model Rules 1.1 and 1.6(c) (Professional Services) | ABA site HTTP 403 | Re-anchored to Florida's adopted rules: 4-1.6(e) reasonable efforts to prevent unauthorized disclosure or access, and the 4-1.1 comment on technology competence, including generative AI (amended effective October 28, 2024) | Rules Regulating The Florida Bar, Chapter 4 (October 2026 PDF) |

### FedRAMP initial report clocks

| Class | PAIN-5, 4, 3 | PAIN-2 | PAIN-1 |
|---|---|---|---|
| D | 0.25 hours | 1 hour | 1 hour |
| C | 1 hour | 24 hours | 1 business day |
| B | 6 hours | 1 business day | 1 business day |
| A ("should", not "must") | 6 hours | 1 business day | 1 business day |

## Still unverified (2)

| Row | Why |
|---|---|
| N72-R05, Illinois BIPA, 740 ILCS 14 (Hotels and Restaurants) | ilga.gov returned HTTP 503 and failed certificate checks on every attempt, including Public Act 103-0769 (the 2024 per-person violation amendment) |
| N54-R08, AICPA Code ET 1.700 (Professional Services) | The AICPA Code is published in an interactive viewer that could not be read from this environment |

## Not verified within the changed rows

- **Other states.** The breach rows name Florida as the worked example. Other states' statutes, and California's 1798.82 (leginfo returned HTTP 403), were not reviewed.
- **Other card brands.** Only Visa's rules were read. Mastercard's site returned HTTP 403.
- **ABA model text.** It was not fetched, so the row now relies on Florida's adopted text.
- **FedRAMP legacy procedure.** The pre-2026 FedRAMP Incident Communications Procedures were not re-read. The FedRAMP row says so.
- **FedRAMP class mapping.** Which certification class a given cloud offering holds was not mapped here.

## Follow-up, not in this change

The sample notification matrices (`step-08_P08_incident-response-runbook/notification-matrix.csv`) carry 914 rows marked unverified across 215 samples. Most are contractual or voluntary duties with no public primary source, such as cyber insurance claim notice (188) or voluntary reports to law enforcement. About 30 are card brand rows, which could now cite the Visa rules above.
