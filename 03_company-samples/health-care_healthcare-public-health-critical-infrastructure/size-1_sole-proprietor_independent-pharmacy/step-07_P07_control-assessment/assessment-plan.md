# Security Assessment Plan and Results Memo: Cris Santos Company | Healthcare and Public Health | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent community pharmacy) |
| System assessed | Pharmacy Core SaaS Stack (PCSS), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Healthcare and Public Health |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The pharmacist-owner (self-assessment), assisted by the on-call IT consultant, who signed a BAA on 2026-07-31. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant ran the network scan and read the settings, and had no prior access to the pharmacy's systems except the 2021 network setup |
| Assessment window | 2026-08-03 to 2026-08-07 (tests on 2026-08-06 after closing) |
| Also satisfies | HIPAA evaluation, 45 CFR 164.308(a)(8) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 39 determination statements.** Controls were chosen because they support the High risks in P01 (R-001, R-002, R-005), a Required HIPAA specification with a gap in P03, or a DEA EPCS duty the pharmacy itself must perform.

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2 | Shared PMS and desktop accounts (R-003; 164.312(a)(2)(i); 21 CFR 1311.200(e)) | Focused / all accounts and a sample of 10 EPCS records |
| IA-2(1) | MFA for the PMS administrator account (R-007; 164.312(d)) | Basic / store and remote sign-in |
| SC-28 | Desktop encryption (R-005; 164.312(a)(2)(iv)) | Basic / all 3 devices |
| AC-17 | Vendor remote-support path into the desktop (R-002) | Focused / remote-support agent and PMS remote access |
| SC-7 | Shared store network (R-004; 164.312(e)(1)) | Basic / router and network scan |
| AU-6 | Daily EPCS audit report and activity review (Required, 164.308(a)(1)(ii)(D); 21 CFR 1311.215(c)) | Focused / 90 retained daily reports |
| IR-6 | Incident reporting (Required, 164.308(a)(6)(ii)) | Basic |
| SA-9 | Vendors and BAAs (R-006, R-009; 164.308(b)) | Focused / all vendors |
| CP-9 | Backups (164.308(a)(7)(ii)(A); 21 CFR 1311.205(b)(17)) | Basic / PMS and compounding records |
| RA-3 | Risk analysis (Required, 164.308(a)(1)(ii)(A)) | Basic |

## 2. Methods and objects
- **Examine:** PMS user list, role and security settings, the daily EPCS audit report screen, the remote-support agent's settings and session history, desktop accounts and encryption status, the router settings, the BAA folder, the PMS vendor's SOC 2 Type 2 report and EPCS certification report, P01 and P05.
- **Test (2026-08-06, after closing):** PMS administrator sign-in from the counter desktop and from the laptop over the phone hotspot; a sample of 10 EPCS dispensing records from the last 12 months, 2 of them from relief days; retrieval of controlled substance records by patient, prescriber, drug, and date; a network scan by the IT consultant; encryption status on each device.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT consultant challenged each answer against what was on screen. The relief pharmacist confirmed by phone how sign-in works on relief days.

### What each test could show
No written policy existed during fieldwork (EV-030). POL-01 was drafted afterward from these results and the gaps, and adopted on 2026-09-04 (effective 2026-09-08), so none of its new rules had operated yet and none was reviewed or tested here. The first risk analysis (P01) was completed on 2026-08-07, the last day of the assessment window, so it could be reviewed for design only. The `test_type` column in `assessment-results.csv` says which kind of conclusion each determination statement supports:

| Test type | Meaning | Statements |
|---|---|---|
| Operating effectiveness | The control existed before the assessment and was tested on the live accounts, devices, network, records and vendor reports | 17 |
| Design | The control is new (the 2026 risk analysis); its design was reviewed. Operation is checked at the August 2027 annual review | 6 |
| Not implemented | Nothing existed to test | 16 |

Evidence for every statement is listed in the [evidence register](../step-00_P00_intake/evidence-register.csv) under the `evidence_ref` IDs (EV-RA-3 and so on), with the population each test covered: the PMS, email and fax accounts (EV-001, EV-012, EV-013), the 3 devices (EV-014, EV-015), the store network (EV-016), and the vendors in the intake vendor register (EV-019). Controls that POL-01 introduces are tested for operation at the 2027-03 follow-up, after at least one quarter of use.

## 3. Rules of engagement
- No testing during business hours. No patient data copied off the systems; screenshots were cropped to settings only, and the EPCS record sample was reviewed on screen.
- The IT consultant worked only under the BAA signed 2026-07-31, on site with the owner.
- Any setting changed during testing is recorded: the remote-support agent was switched to attended mode, and the PMS password card in the counter drawer was destroyed and the password changed, both on 2026-08-06.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 14 |
| Other than satisfied | 25 |
| **Total** | **39** |

**Fully other than satisfied:** IA-2, IA-2(1), SC-28, AU-6, IR-6.
**Partly satisfied:** RA-3 (the analysis exists; no review cycle yet), CP-9 (PMS backups inherited; compounding records have no separate copy), SC-7 (the router is a sound outer boundary; the inside is one flat network), AC-17 (both remote access types were authorized; nothing is written and the agent was unattended), SA-9 (customer responsibilities are defined; two vendors hold PHI with no BAA in effect).
**No control was fully satisfied.** The strongest results are the ones the PMS vendor operates (backups, the outer firewall).

**Pharmacy-specific findings.**
1. 2 of the 10 sampled EPCS dispensing records name the owner although the relief pharmacist dispensed them (IA-02[02]). That breaks the DEA requirement that the record carry the name or initials of the person who dispensed (21 CFR 1311.205(b)(10)(iii)) and the pharmacy's duty to set access by person (1311.200(e)).
2. The first review of the 90 retained daily EPCS audit reports found 3 failed sign-ins, all explained by the owner, and no alteration or access-control events. No DEA report was needed, but none would have been made if one had been (AU-06b.).

**Changes made during the assessment:** remote-support agent switched to attended mode (AC-17a.[02]); PMS password card destroyed and password changed. P01 R-002 and R-003 reflect both.

The 10 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-010). The High item is POAM-001 (desktop encryption), due 2026-09-15.

## 5. Deliverables
`assessment-results.csv` (39 rows), `poam.csv` (10 items), and this memo. Accepted by the pharmacist-owner on 2026-09-04. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.
