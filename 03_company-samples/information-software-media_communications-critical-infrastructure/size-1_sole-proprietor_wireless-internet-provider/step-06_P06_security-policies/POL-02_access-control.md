# Access Control Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operated wireless internet service provider) |
| Policy ID | POL-02 |
| Status | Merged into POL-01 Information Security Policy (consolidated), effective 2026-09-01 |
| Owner and approver | Owner-operator |

At the Sole Proprietorship tier the company keeps **one** consolidated policy, because one person writes, follows, and checks it (`01_company-sizes/tier-project-scaling.csv`, t1 P06). This file is kept so the folder has the standard policy set names. It holds no separate rules.

**Where the access control rules are:**

- POL-01 section 7 (Access control and customer authentication): named accounts and no shared accounts (7.1), MFA (7.2), passwords and device defaults (7.3), same-day removal and quarterly review (7.4), management plane reachable only from the management VLAN and VPN (7.5), monthly sign-in review (7.6), emergency access envelope (7.9).
- POL-01 7.7 and 7.8: customer authentication before any CPNI is disclosed by phone, in person, online, or through the AI support assistant (47 CFR 64.2010(b), (c), (e), (f)).
- POL-01 6.4: approved, named VPN sessions for the network consultant.
- SP 800-53 AC-1 and IA-1 (policy and procedures) are met by POL-01 as a whole.

Traceability for every statement is in `policy-control-map.csv`.
