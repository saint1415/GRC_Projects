# Security Assessment Plan and Results Memo: Cris Santos Company | Administrative and Support | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent recruiter, sole proprietorship) |
| System assessed | Recruiting and Placement Systems Profile (RPSP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Administrative and Support and Waste Management and Remediation Services |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-recruiter (self-assessment), assisted by the on-call IT support technician after the technician signed a confidentiality agreement on 2026-07-17. **Independence is limited**: the owner designed, operates, and assessed these controls. The technician helped run the tests and read the settings but also supports the laptop and router |
| Assessment window | 2026-07-20 to 2026-07-24 (tests on 2026-07-23) |
| Also supports | The "reasonable measures" duty in Fla. Stat. 501.171(2): evidence that the measures were checked, not just written |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 48 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-004) or a High or Moderate gap in P03.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the owner's administrator accounts (R-001, R-002; G-055) | Basic / email, ATS, partner portal, accounting |
| IA-5 | Password reuse and storage (R-002; G-053) | Focused / every account and the router |
| SI-12 | Retention of SSNs, IDs, and reports (R-004; G-037, G-038) | Focused / mailbox, laptop, phone, ATS |
| MP-6 | Disposal of consumer information and devices (R-006; G-113) | Basic |
| SA-9 | Partner and AI vendor terms (R-003, R-007, R-008; G-026) | Focused / partner, ATS and AI add-on, chatbot |
| CP-9 | ATS data recovery (R-010; G-064) | Basic / ATS and file storage |
| AU-6 | Account monitoring (R-001, R-002; G-077) | Basic |
| IR-6 | Incident reporting and Florida notice (R-014; G-095) | Basic |
| AC-19 | Phone with ID photos and signed-in apps (R-012) | Basic |
| RA-3 | Risk assessment (basis for 501.171(2) reasonableness) | Basic |

## 2. Methods and objects
- **Examine:** account security pages, the account list, the browser password store, the router admin page, phone settings, the partner agreement and SOC 2 report, ATS and AI add-on terms, P01 and P05.
- **Test (2026-07-23):** sign-ins to email, the ATS, the partner portal, and accounting from a new browser; a search of the mailbox, file storage, laptop, and phone camera roll for SSNs, ID images, and consumer reports; a check of the router admin password.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen. A call with the partner's payroll desk (2026-07-22, EV-032) supplied the SA-9 evidence about bank changes.

### What each test could show
No written policy existed during fieldwork. POL-01 was drafted afterward from these results and the gaps, and adopted on 2026-08-31, so none of its new rules had operated yet and none was tested here. The first risk assessment (P01) was completed on 2026-07-24, inside the assessment window, so it could be reviewed for design only. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control existed before the assessment and was tested on the live accounts, devices, mailbox and vendor records | 21 |
| Design | The control is new (the 2026 risk assessment); its design was reviewed. Operation is checked at the July 2027 annual review | 6 |
| Not implemented | Nothing existed to test | 21 |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-RA-3 and so on), with the population each test covered: the owner's accounts (EV-001, EV-008, EV-012, EV-015, EV-031), the laptop and phone (EV-020, EV-021), the router (EV-023), the mailbox (EV-009), and the vendor terms (EV-004, EV-006, EV-013, EV-027). Controls that POL-01 introduces are tested for operation at the 2027-02 follow-up, after at least one quarter of use.

## 3. Rules of engagement
- Search results were counted, not copied: no SSN, ID image, or report left the owner's accounts, and screenshots were cropped to settings and counts only.
- The IT technician worked only under the confidentiality agreement, in sessions the owner started and watched, and never received a password.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 17 |
| Other than satisfied | 31 |
| **Total** | **48** |

**Fully other than satisfied:** IA-2(1), SI-12, AU-6, IR-6.
**Partly satisfied:** RA-3 (the assessment exists; no review cycle yet), IA-5 (device-level protection fine; passwords weak), AC-19 (phone connects safely; ID photos and no rules), MP-6 (paper fine; electronic disposal missing), SA-9 (roles defined; terms missing), CP-9 (vendor encryption fine; no independent ATS copy).
**No control was fully satisfied.** That is expected for a business with no written program before this assessment.

**New findings during testing:**
- The home router's admin password was still the factory default (IA-05e.). The IT technician changed it during the test on 2026-07-23; POL-01 7.3 now requires changing defaults before use.
- The mailbox and device search measured the exposure for the first time: 77 people with an SSN or government ID number in the mailbox (66 in Florida, 11 in 6 other states), 34 start forms in the laptop downloads folder, 9 ID photos on the phone (deleted 2026-07-23), and 2 consumer reports. This count drives P01 R-004 and the P08 notice planning.

The 10 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-010). The High items are POAM-001 (MFA, due 2026-09-15) and POAM-002 (purge and retention, due 2026-10-31).

## 5. Deliverables
`assessment-results.csv` (48 rows), `poam.csv` (10 items), and this memo. Accepted by the owner-recruiter on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside review at least every second year.
