# Information Security Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Status | Merged into POL-02 Part A |
| Owner | Operations Manager (Information Security Coordinator) |
| Approved by | CEO, 2026-08-31 |

At the Micro tier the company keeps three core policies: access control (POL-02), incident response (POL-03), and data classification (POL-04). A separate Information Security Policy would add little for a 7-person company, so its essential rules live in **POL-02 Part A. Program governance and secure product development**:

| Essential rule | Where it lives | Driver |
|---|---|---|
| Roles: system owner, Information Security Coordinator, Product Security Lead, 524B owner | POL-02 A.1 | Program governance |
| Risk assessment every July, at design freeze, and before each submission | POL-02 A.2 | FDA premarket guidance V.A.2 |
| Who may accept risk | POL-02 A.3 | Program governance |
| Sanctions | POL-02 A.4 | Program governance |
| Vendor and contract manufacturer security terms | POL-02 A.5 | 21 CFR 820.10(a) (ISO 13485 cl. 4.1.5, 7.4) |
| Annual independent evaluation | POL-02 A.6 | Program governance |
| Retention of security records | POL-02 A.7 | 21 CFR 820.10(a) (ISO 13485 cl. 4.2.5) |
| Policy review and availability to staff | POL-02 A.8 | Program governance |
| Exceptions process | POL-02 A.9 | Program governance |
| Secure product development (security requirements, threat model, SBOM, testing, release record) | POL-02 A.10 | N31-33-R05 (524B(b)(2)-(3)); 820.10(c) |
| Signing and release with an HSM-backed key and two approvers | POL-02 A.11 | N31-33-R05 (524B(b)(2)) |
| No shared, default, or hardcoded device credentials | POL-02 A.12 | N31-33-R05 (524B(b)(2)); FDA premarket guidance App. 1 |

Traceability for these rules is in `policy-control-map.csv` under POL-02. Revisit this choice if the company grows past the Micro tier (10 or more employees) or before the first commercial release, when a stand-alone Information Security Policy and a separate secure development policy become worth the effort.
