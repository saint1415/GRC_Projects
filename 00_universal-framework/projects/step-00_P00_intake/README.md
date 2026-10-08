# P00. Intake: evidence, inventories, and obligations

**Why this step exists.** Every later project needs facts about the company: what systems it runs, what data it holds, who its suppliers are, which rules bind it, and what its records show today. In a real engagement those facts are collected from the company's own systems of record before anyone judges them. This step collects them once, dates them, and gives each one an ID, so every later finding can point to the evidence it came from.

**The rule for this step: observations, not findings.** Intake records what a source shows ("the endpoint console export lists 70 devices; 12 report disk encryption on"). It does not say whether that is good or bad against a requirement. Judgments are made later: the gap analysis (P03) compares observations with the rules, and the control assessment (P07) tests them. A finding that cannot cite an intake evidence ID, or evidence collected during its own fieldwork, is an assumption.

## Universal approach (macro to granular)

1. **Plan the requests (macro).** List the systems of record the company has at this size, and who owns each one. A sole proprietor's systems of record may be a vendor portal, a bank statement, and an email inbox; an enterprise has a CMDB, an HR system, and a contract management system.
2. **Collect exports and documents.** Ask for exports, not summaries: the identity provider user list, the HR roster and terminations, the endpoint console, the cloud account inventory, the accounts payable vendor list, the contract register, prior audit and exam reports, insurer questionnaires, the incident log, scan results, and the current policies. Record the date the data reflects (as of) and the date it was collected.
3. **Hold intake interviews.** Process owners describe what their process does, which systems it uses, and who they rely on. Interviews are evidence too: record who, when, and what was said.
4. **Build the inventories (NIST SP 800-37 Rev. 2, Tasks P-10, P-12 and P-13; CSF 2.0 ID.AM-01, ID.AM-02, ID.AM-04, ID.AM-07).** Assets (hardware, software, services, data, AI tools) and suppliers, each traced to the evidence that lists it.
5. **Build the obligations register (SP 800-37 Task P-15; CSF 2.0 GV.OC-03).** For each candidate law, regulation, standard, and contract: does it bind this company at this size, and why? Cite the fact (with its evidence ID) and the legal text. This is the applicability check; the requirement-by-requirement gap analysis stays in P03.
6. **Record open requests (granular).** Evidence asked for but not yet received is listed, not guessed. Later steps say where a gap in evidence limits their conclusions.

## Outputs

| File | Purpose |
|---|---|
| `evidence-register.csv` | One row per item collected: source system, type, owner, as-of and collected dates, the phase that collected it, and what it shows (observations only). Intake creates the first rows; later fieldwork (BIA interviews, risk and gap interviews, control tests) adds its own rows, so one register backs every deliverable. |
| `asset-inventory.csv` | Hardware, software, services, data stores, networks, and AI tools, each with its owner, hosting, data types, and source evidence. |
| `vendor-register.csv` | Suppliers and service providers, the systems and data they touch, the agreements and assurance reports on file, and the source evidence. |
| `obligations-register.csv` | Each candidate obligation, whether it applies, the factual and legal basis, and which step analyzes it. |
| `intake-report.md` | Scope, sources collected, observations by area, open requests, and what each later step takes from intake. |

## Where the data normally comes from

| Data | System of record (larger companies) | Smaller companies |
|---|---|---|
| Users and access | Identity provider export, HR system roster and termination report | Vendor admin consoles, payroll provider |
| Devices | Endpoint management or EDR console, CMDB | MSP asset report, a walk-through count |
| Cloud and SaaS | Cloud account inventory, SaaS management or SSO app list, expense reports | Card statements and vendor invoices |
| Suppliers and contracts | Accounts payable vendor master, contract management system, BAAs and DPAs | Vendor invoices, signed agreements folder |
| Data | Data map or records of processing, data loss prevention discovery | Interviews and system walk-throughs |
| Obligations | Licenses, contracts, regulator correspondence, counsel memos | Licenses, contracts, payer and customer agreements |
| Current state | Prior audits and exams, insurer questionnaires, incident log, scan and pen-test results, current policies | Insurer questionnaire, MSP reports, the policies folder |
| AI tools | SaaS discovery, procurement, expense reports, browser extension inventory, staff survey | Staff survey and card statements |

## Quality checklist

- [ ] Every evidence row names a source system, an owner, an as-of date, and a collected date, and the collected date is not before the as-of date.
- [ ] `what_it_shows` states observations only. No row says "not compliant", "gap", "weak", or "missing control".
- [ ] Every asset and vendor row cites at least one evidence ID.
- [ ] Every obligation marked Yes or No states the fact and the legal text it rests on.
- [ ] Every evidence ID cited anywhere in the sample exists in `evidence-register.csv`.
- [ ] Open requests are listed instead of filled in with assumptions.

## Sources

SRC-800-37 (Prepare tasks P-10, P-12, P-13, P-15), SRC-CSF2 (ID.AM, GV.OC-03, GV.SC-04), SRC-800-53A (assessment methods and objects: examine, interview, test).
