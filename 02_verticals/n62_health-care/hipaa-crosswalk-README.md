# HIPAA Security Rule crosswalk (Health Care vertical)

File: [`hipaa-security-rule-crosswalk.csv`](hipaa-security-rule-crosswalk.csv). Used by every Health Care scenario (P02, P03, P07).

| Column | Source | Authority |
|---|---|---|
| `citation`, `level`, `title`, `type` (Required/Addressable), `requirement_text_nist_sp800_66r2` | NIST SP 800-66 Rev. 2 dataset in the Cybersecurity and Privacy Reference Tool (CPRT), exported 2026-09-26 | Authoritative (NIST restatement of 45 CFR 164 Subpart C) |
| `sp800_53r5_controls`, `csf2_subcategories` | **Author mapping.** Built from the SP 800-66r2 key activities and checked against the official SP 800-53 Rev. 5.2.0 and CSF 2.0 catalogs | Not official |

**Why an author mapping?** SP 800-66r2 Appendix D says NIST moved its official HIPAA-to-SP 800-53 and CSF mapping to CPRT. The published mapping targets CSF 1.1, and NIST states it will be updated for CSF 2.0. The CPRT export available on 2026-09-26 did not include those relationships. Replace the two mapping columns with NIST's official mapping when it is published for CSF 2.0.

**Notes**
- NIST's dataset lists 164.314(a)(3)(i) separately. The current eCFR text places subcontractor requirements at 164.314(a)(2)(iii). Both rows are kept as NIST lists them.
- 164.314(b) (group health plans) is included for completeness and marked not applicable in physician-practice scenarios.
