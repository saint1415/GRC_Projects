# Information Security Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (community water system, 2,850 population served) |
| Policy ID | POL-01 |
| Status | Merged into POL-02 Part A |
| Owner | Office Manager (security and compliance coordinator) |
| Approved by | Owner and General Manager, 2026-08-31 |

At the Micro tier the company keeps three core policies: access control (POL-02), incident response (POL-03), and data classification (POL-04). A separate Information Security Policy would add little for a 7-person water system, so its essential rules live in **POL-02 Part A. Program governance**:

| Essential rule | Where it lives | Benchmark or regulation |
|---|---|---|
| Security and compliance coordinator and OT security decision owner designated in writing | POL-02 A.1 | CSF GV.RR-02; SP 800-82 Rev. 3 sec. 6.1.2 |
| Annual risk assessment with SP 800-30, and after major changes | POL-02 A.2 | CSF ID.RA-01; readiness for 42 U.S.C. 300i-2(a)(1) |
| Who may accept risk; public health risks never accepted above Low | POL-02 A.3 | CSF GV.RM-01 |
| Sanctions | POL-02 A.4 | CSF GV.RR-04 |
| Security terms before any vendor gets OT access or company files | POL-02 A.5 | CSF GV.SC-05 |
| Independent assessment every 2 years; self-review in between | POL-02 A.6 | CSF ID.IM-01 |
| 5-year retention of security records | POL-02 A.7 | CSF GV.PO-02; mirrors 42 U.S.C. 300i-2(d) |
| Policy review every August; policies available to staff | POL-02 A.8 | CSF GV.PO-02 |
| Exceptions process | POL-02 A.9 | CSF GV.PO-01 |
| Security changes must keep the engineered safeguards and hand operation | POL-02 A.10 | CSF PR.IR-03; SP 800-82 Rev. 3 sec. 5.3.1 |

Traceability for these rules is in `policy-control-map.csv` under POL-02. Revisit this choice if the company grows past the Micro tier (10 or more employees) or the population served passes 3,300, when SDWA section 1433 would require an emergency response plan and a fuller program.
