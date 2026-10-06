# Security Assessment Plan and Results Memo: Cris Santos Company | Information Technology | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller) |
| System assessed | Hosting Control Plane and Customer Portal (HCP), per the system security plan (P02) |
| Tier / Vertical | Sole Proprietorship / Information Technology |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner (self-assessment), with the contract security consultant for the tests on 2026-08-19. **Independence is limited**: the owner designed, operates, and assessed these controls. The consultant has no standing access and does not run any of the controls, so the consultant ran the sign-in and account tests and challenged the owner's written self-review |
| Assessment window | 2026-08-17 to 2026-08-21 (tests on 2026-08-19) |
| Also supports | The annual control evaluation in POL-01 4.5, and evidence for the reasonable-measures duty of Fla. Stat. 501.171(2) and the FTC reasonable-security expectations (P03) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 43 determination statements.** Controls were chosen because they support the Very High and High risks in P01 or a High gap in P03. Every control in scope reaches many customers at once, which is what makes this business different from an ordinary small office.

| Control | Why selected (risk ID or requirement ID) | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the tools that reach every customer (R-001, R-002; G-005) | Focused / every control plane account |
| AC-2 | Account management for the owner and contractors (R-001, R-012; G-004, G-016) | Focused / all 5 control plane tools |
| AC-6 | Freelancer's administrator role over 120 sites (R-001; G-016) | Focused / dashboard |
| IA-5 | Customer credentials in a spreadsheet and email (R-003; G-007) | Basic / file storage, sent mail, password manager |
| CP-9 | Backups for 270 sites (R-005; G-019, G-037) | Focused / upstream and dashboard backups, one restore |
| SA-9 | Vendor oversight (R-010, R-011; G-021, G-022) | Basic / 5 vendors that hold customer data |
| AU-6 | Log review on the control plane (R-001, R-008; G-014) | Basic / portal, console, registrar, dashboard |
| SI-2 | Patching of care-plan and hosting-only sites (R-004; G-023) | Focused / all 270 sites, 5 sites spot-checked |
| SI-4 | Monitoring, including AI triage (R-008; G-014, G-024) | Focused / security service, 50 dismissed findings |
| IR-6 | Incident reporting and the 10-day customer notice (R-007; G-033) | Basic |

## 2. Methods and objects
- **Examine:** account security and user lists in the portal, reseller console, registrar, dashboard, and security service; dashboard role settings and update history; the password manager report; vendor terms and the reseller terms on backups; the security service vulnerability report of 2026-08-18 and its findings history from May to August 2026; the Terms of Service; P01, P05, and POL-01.
- **Test (2026-08-19, with the consultant):**
  - sign-in to each control plane tool from a new browser, to see whether a second factor is asked for;
  - a sign-in with the freelancer's dashboard account, with the freelancer present, to see what the role can do;
  - a search of file storage and sent mail for customer credentials;
  - restore of one care-plan site from the upstream backup to a test account;
  - a spot check of 5 hosting-only sites for outdated plugins;
  - a review of 50 findings the AI triage had auto-dismissed.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the consultant challenged each answer against what was on screen.

## 3. Rules of engagement
- No changes to customer sites during tests, except the restore, which went to a separate test account and was deleted the same day.
- The consultant signed a confidentiality agreement before the session, worked only in sessions the owner started and watched, and kept no credentials or customer data.
- Screenshots were cropped to settings only. No shopper or mailbox data was copied.
- Any account found that should not exist could be disabled on the spot (this was used once, see section 4).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 10 |
| Other than satisfied | 33 |
| **Total** | **43** |

**Fully other than satisfied (4 controls):** IA-2(1), AC-6, AU-6, and IR-6.
**Partly satisfied (6 controls):** AC-2, IA-5, CP-9, SA-9, SI-2, and SI-4.
**Fully satisfied:** none. What works is mostly what the vendors do: the upstream provider's nightly backups restored a site correctly in 25 minutes, and the security service finds vulnerable plugins on every site every day. What fails is what the owner must do with those tools: protect the logins, limit the contractor, read the logs, and act on the findings.

**New findings:**
- A former freelance designer's dashboard administrator account was still enabled nine months after the engagement ended (AC-02f.[04]). It was disabled during the test on 2026-08-19, and the 30-day activity log showed no use. P01 R-012 was added for it.
- 38 sent emails held customer site or SFTP passwords (IA-05d.).
- The weekly bulk update broke 2 sites in July 2026, because updates go to all 120 care-plan sites at once with no test site (SI-02b.[02]).
- Of 50 auto-dismissed findings, 1 was the real web shell found on 2026-08-05 (SI-04d.[01]). This sample is the main evidence for P10.

The 10 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-010): 1 Very High, 4 High, and 5 Moderate. POAM-001 (MFA on the portal administrator login and every dashboard account) and POAM-003 (the freelancer's role) are due 2026-10-15.

## 5. Deliverables
`assessment-results.csv` (43 rows), `poam.csv` (10 items), and this memo. Accepted by the owner on 2026-09-28. Because independence is limited, POL-01 4.5 requires testing by someone outside the company at least every second year. The next assessment is due in August 2027.
