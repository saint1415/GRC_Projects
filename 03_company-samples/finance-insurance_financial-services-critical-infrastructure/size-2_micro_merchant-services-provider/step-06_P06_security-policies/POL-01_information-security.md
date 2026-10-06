# Information Security Policy (pointer)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC |
| Policy ID | POL-01 |
| Status | Merged into POL-02 Part A |
| Owner | Operations Manager (Qualified Individual and security lead) |
| Approved by | Owner, 2026-08-31 |

At the Micro tier the company keeps three core policies: access control (POL-02), incident response (POL-03), and data classification (POL-04). A separate Information Security Policy would add little for a 7-person company, so its essential rules live in **POL-02 Part A. Program governance**:

| Essential rule | Where it lives | Driver |
|---|---|---|
| Qualified Individual and PCI DSS lead designated in writing (Operations Manager) | POL-02 A.1 | 16 CFR 314.4(a); PCI DSS 12.1.3 |
| Owner's executive responsibility for PCI DSS; review of the SAQ before signing | POL-02 A.2 | PCI DSS 12.4.1 |
| Annual risk assessment and targeted risk analyses | POL-02 A.3 | PCI DSS 12.3.1 |
| Who may accept risk | POL-02 A.4 | PCI DSS 12.3 |
| Quarterly PCI review | POL-02 A.5 | PCI DSS 12.4.2 |
| Scope confirmation every six months and after change | POL-02 A.6 | PCI DSS 12.5.2.1, 12.5.3 |
| Service provider list, AOCs, responsibility matrix | POL-02 A.7 | PCI DSS 12.8; 16 CFR 314.4(f) |
| Testing calendar (scans, penetration test, independent assessment) | POL-02 A.8 | PCI DSS 11.3, 11.4; 16 CFR 314.4(d)(1) |
| Record retention | POL-02 A.9 | PCI DSS 12.1 |
| Policy review and availability | POL-02 A.10 | PCI DSS 12.1.2 |
| Exceptions process | POL-02 A.11 | PCI DSS 12.1 |
| Sanctions | POL-02 A.12 | 16 CFR 314.4(e) |

Traceability for these rules is in `policy-control-map.csv` under POL-02. Revisit this choice if the company grows past the Micro tier (10 or more employees), adds a second processor partner, or starts storing card data.
