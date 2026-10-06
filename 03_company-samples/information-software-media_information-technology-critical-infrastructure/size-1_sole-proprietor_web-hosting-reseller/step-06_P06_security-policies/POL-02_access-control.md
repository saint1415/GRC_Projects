# Access Control Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller) |
| Policy ID | POL-02 |
| Status | Merged into POL-01 Information Security Policy (consolidated), effective 2026-10-01 |
| Owner and approver | Owner |

At the Sole Proprietorship tier the company keeps **one** consolidated policy, because one person writes, follows, and checks it (`01_company-sizes/tier-project-scaling.csv`, t1 P06). This file is kept so the folder has the standard policy set names. It holds no separate rules.

**Where the access control rules are:**

- POL-01 section 7 (Access control): unique accounts (7.1), MFA on every control plane tool and security keys by 2027-03-31 (7.2), least privilege and owner-only bulk pushes (7.3), monthly account review and same-day removal (7.4), credentials only in the password manager vault (7.5), emergency access envelope (7.6), weekly log review (7.7), customer MFA (7.8).
- POL-01 section 5.1: the contractor security addendum (MFA, device, credentials, 24-hour incident reporting, return of credentials).
- SP 800-53 AC-1 and IA-1 (policy and procedures) are met by POL-01 as a whole.

Traceability for every statement is in `policy-control-map.csv`.
