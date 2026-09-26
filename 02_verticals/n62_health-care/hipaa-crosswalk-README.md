# HIPAA Security Rule crosswalk (Health Care vertical)

Two files, used by every Health Care scenario (P02, P03, P07):

| File | What it is | Authority |
|---|---|---|
| [`hipaa-nist-official-mapping.csv`](hipaa-nist-official-mapping.csv) | **NIST's official mapping.** Each HIPAA Security Rule standard and implementation specification mapped to SP 800-53 Rev. 5.1.1 controls and to CSF **1.1** subcategories | NIST National Online Informative References (OLIR) 110 and 109, final, posted 2024-03-20, developer NIST. These are the online mappings that SP 800-66 Rev. 2 Appendix D points to |
| [`hipaa-security-rule-crosswalk.csv`](hipaa-security-rule-crosswalk.csv) | Working crosswalk. The HIPAA structure and text come from NIST's SP 800-66r2 dataset. `official_sp800_53r5_controls` comes from OLIR 110. `sp800_53r5_controls` and `csf2_subcategories` are an **author mapping** | Mixed; see the columns |

## Why the author mapping is still needed
- **CSF 2.0.** NIST's official HIPAA mapping covers CSF 1.1 only. No HIPAA to CSF 2.0 mapping was published in CPRT or OLIR as of 2026-09-26. The `csf2_subcategories` column is therefore the author's mapping, checked against the official CSF 2.0 catalog.
- **Comparison.** The author's SP 800-53 mapping overlaps NIST's official mapping on 60 of the 68 mapped requirements. The author mapping also includes 29 control choices NIST does not list. Deliverables keep the author mapping (it drove the Phase 1 control selection) and show NIST's official controls next to it in the `nist_official_sp800_53r5_1_1` column of every P03 gap analysis.

## How the official mapping was obtained
1. The public CPRT export for SP 800-66r2 returns structure only. NIST's CPRT metadata lists the HIPAA mapping datasets as non-public in the tool, but points to the OLIR spreadsheets.
2. The OLIR catalog API confirmed status Final, the versions, and the file hashes. The SHA-256 of each downloaded file matched the catalog.
3. `tools/refresh_hipaa_official_mapping.py` downloads both spreadsheets, normalizes control IDs (for example `AC-02(01)` becomes `AC-2(1)`), and rewrites both files. All 108 mapped controls exist in SP 800-53 Release 5.2.0.

## Caveats
- NIST marks the references as not comprehensive, and the relationship-strength columns are blank. Treat mapped controls as related, not as proof of compliance.
- NIST cites the written-contract specification as 164.308(b)(4), the pre-2013 numbering; the current rule uses 164.308(b)(3).
- 164.314(a)(3)(i) appears in NIST's SP 800-66r2 dataset but has no mapping in OLIR 109 or 110.
- 164.314(b) (group health plans) is included for completeness and marked not applicable in physician-practice scenarios.
- The HHS OCR 2016 crosswalk (CSF 1.0 and SP 800-53 Rev. 4) is outdated and is not used.
