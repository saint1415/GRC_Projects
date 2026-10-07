# Data Classification and Handling Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher) |
| Policy ID | POL-04 |
| Status | Merged into POL-01 Information Security Policy (consolidated), effective 2026-09-28 |
| Owner and approver | Owner-developer |

At the Sole Proprietorship tier the company keeps **one** consolidated policy, because one person writes, follows, and checks it (`01_company-sizes/tier-project-scaling.csv`, t1 P06). This file is kept so the folder has the standard policy set names. It holds no separate rules.

**Where the data classification and handling rules are:**

- POL-01 section 8 (Data handling): three classification levels (8.1), approved locations (8.2), synthetic data for development (8.3), encryption (8.4), expiring export links (8.5), scrubbing of error reports (8.6), deletion within 30 days of account closure and device disposal (8.7), 5-year retention of security records (8.8).
- POL-01 sections 6.1 and 6.2: no subscriber data to a service provider without terms and a sub-processor list entry.
- POL-01 Appendix A: where Restricted data may live.
- SP 800-53 MP-1 and SC-1 are met by POL-01 as a whole.

Traceability for every statement is in `policy-control-map.csv`.
