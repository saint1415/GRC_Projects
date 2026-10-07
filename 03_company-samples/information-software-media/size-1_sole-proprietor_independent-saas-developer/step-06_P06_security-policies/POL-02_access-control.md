# Access Control Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent B2B SaaS software publisher) |
| Policy ID | POL-02 |
| Status | Merged into POL-01 Information Security Policy (consolidated), effective 2026-09-28 |
| Owner and approver | Owner-developer |

At the Sole Proprietorship tier the company keeps **one** consolidated policy, because one person writes, follows, and checks it (`01_company-sizes/tier-project-scaling.csv`, t1 P06). This file is kept so the folder has the standard policy set names. It holds no separate rules.

**Where the access control rules are:**

- POL-01 section 7 (Access control): individual accounts and no shared credentials (7.1), MFA on every administrator account (7.2), passwords (7.3), super-admin limited to the owner and a named support role for the contractor (7.4), secrets handling and rotation (7.5), sealed emergency access (7.6), monthly log review (7.7).
- POL-01 section 6.4: security terms in contractor agreements.
- SP 800-53 AC-1 and IA-1 (policy and procedures) are met by POL-01 as a whole.

Traceability for every statement is in `policy-control-map.csv`.
