# Information Security Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Status | Merged into POL-02 Part A |
| Owner | Store Manager (Security and PCI Lead) |
| Approved by | Owner, 2026-08-31 |

At the Micro tier the store keeps three core policies: access control (POL-02), incident response (POL-03), and data classification (POL-04). A separate Information Security Policy would add little for a 7-person store, so its essential rules live in **POL-02 Part A. Program governance**:

| Essential rule | Where it lives | PCI DSS v4.0.1 (N44-45-R01) |
|---|---|---|
| Designation of the Security and PCI Lead (Store Manager) | POL-02 A.1 | 12.1 |
| Yearly risk assessment with SP 800-30 | POL-02 A.2 | 12.3 |
| Who may accept risk | POL-02 A.3 | 12.3 |
| Written PCI DSS scope before signing any SAQ; P2PE devices only | POL-02 A.4 | 12.5 |
| Service provider list, agreements, and yearly AOC check | POL-02 A.5 | 12.8 |
| Approval and change log for online store scripts and custom code | POL-02 A.6 | 6.4.3; 6.5 |
| Yearly independent assessment | POL-02 A.7 | (FTC Act Section 5 reasonable security, N44-45-R02) |
| Records kept at least 3 years | POL-02 A.8 | 12.1 |
| Yearly policy review and written, time-limited exceptions | POL-02 A.9 | 12.1 |

SAQ P2PE for PCI DSS v4.0.1 asks for an information security policy that is published, reviewed yearly, and defines security roles (12.1.1 to 12.1.3). POL-02 Part A, together with POL-03 and POL-04, is that policy for this store. Traceability for these rules is in `policy-control-map.csv` under POL-02. Revisit this choice if the company grows past the Micro tier (10 or more employees) or opens a second store.
