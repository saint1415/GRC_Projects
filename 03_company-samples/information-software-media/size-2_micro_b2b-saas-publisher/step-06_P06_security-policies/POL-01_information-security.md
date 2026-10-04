# Information Security Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Status | Merged into POL-02 Part A |
| Owner | CTO (security and compliance lead) |
| Approved by | Chief Executive Officer, 2026-09-15 |

At the Micro tier the company keeps three core policies: access control (POL-02), incident response (POL-03), and data classification (POL-04). A separate Information Security Policy would add little for a 7-person company, so its essential rules live in **POL-02 Part A. Program governance**:

| Essential rule | Where it lives | Driver |
|---|---|---|
| Designation of the security and compliance lead (CTO) and privacy lead (Operations and Finance Manager) | POL-02 A.1 | SOC 2 CC1.3 |
| Annual risk assessment with an owner and treatment for each risk | POL-02 A.2 | N51-R01 (reasonable security); SOC 2 CC3.2 |
| Who may accept risk | POL-02 A.3 | SOC 2 CC3.1 |
| Every security, privacy, and AI statement checked and approved before use | POL-02 A.4 | N51-R01 (deception) |
| No contract, no customer data; sub-processor list and 30-day notice | POL-02 A.5 | Customer DPA; SOC 2 CC9.2 |
| Annual independent assessment and penetration test | POL-02 A.6 | Security exhibit; SOC 2 CC4.1 |
| Retention of security records | POL-02 A.7 | SOC 2 CC2.1 |
| Policy review and availability to staff | POL-02 A.8 | SOC 2 CC5.3 |
| Exceptions process | POL-02 A.9 | SOC 2 CC5.3 |
| Sanctions | POL-02 A.10 | SOC 2 CC1.5 |

Traceability for these rules is in `policy-control-map.csv` under POL-02. Revisit this choice when the company reaches the Small tier (10 or more employees) or prepares for its SOC 2 Type 2, when a separate information security policy is usually expected.
