# Information Security Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Status | Merged into POL-02 Part A |
| Owner | Office Manager (Security and Compliance Coordinator) |
| Approved by | President, 2026-08-31 |

At the Micro tier the company keeps three core policies: access control (POL-02), incident response (POL-03), and data classification and CUI handling (POL-04). A separate Information Security Policy would add little for a 7-person shop, so its essential rules live in **POL-02 Part A. Program governance**:

| Essential rule | Where it lives | Citation |
|---|---|---|
| Designation of the Security and Compliance Coordinator (Office Manager) | POL-02 A.1 | SP 800-171 policy basis (3.x requirements) |
| Annual risk assessment with SP 800-30 | POL-02 A.2 | SP 800-171 3.11.1 |
| Who may accept risk; SP 800-171 gaps never accepted | POL-02 A.3 | 32 CFR 170.24 |
| Where CUI may live; FedRAMP Moderate-equivalent cloud only | POL-02 A.4 | DFARS 252.204-7012(b)(2)(ii)(D); 3.1.20 |
| Service providers: responsibility matrix, named MFA accounts, U.S.-person technicians | POL-02 A.5 | 32 CFR 170.19(c)(2) |
| SSP accuracy; no SPRS score or affirmation without evidence | POL-02 A.6 | 3.12.4; 32 CFR 170.22 |
| Annual assessment and monthly POA&M review | POL-02 A.7 | 3.12.1 to 3.12.3 |
| Records kept 6 years; audit logs 1 year | POL-02 A.8 | 3.3.1 |
| Sanctions | POL-02 A.9 | Company rule |
| Policy review and exceptions | POL-02 A.10 | Company rule |

Traceability for these rules is in `policy-control-map.csv` under POL-02. Revisit this choice if the company grows past the Micro tier (10 or more employees), adds a second site, or a prime requires Level 2 (C3PAO) certification.
