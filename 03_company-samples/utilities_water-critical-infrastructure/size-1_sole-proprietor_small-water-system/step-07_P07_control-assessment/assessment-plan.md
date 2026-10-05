# Security Assessment Plan and Results Memo: Cris Santos Company | Water and Wastewater Systems | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (small community water system) |
| System assessed | Water System Operations Profile (WSOP), per the system profile (P02) |
| Tier / Vertical | Sole Proprietorship / Water and Wastewater Systems |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | The owner-operator (self-assessment), assisted by the on-call IT technician under a confidentiality agreement signed 2026-07-15. **Independence is limited**: the owner designed, operates, and assessed these controls. The IT technician ran the external router check and read the settings, but also supports the laptop |
| Assessment window | 2026-07-20 to 2026-07-24 (tests at the well house and on the devices on 2026-07-23) |

## 1. Scope and controls selected
Sole Proprietorship scope: 6-10 controls. **10 controls, 51 determination statements.** Eight controls were chosen because they support the High and Moderate risks on the treatment control path in P01 (R-001 to R-005, R-008) and the High gaps in P03. SC-28 and SI-3 were added because they are cheap to test and protect the laptop that holds customer and compliance data (R-006).

| Control | Why selected | Depth / coverage |
|---|---|---|
| IA-2(1) | MFA on the portal, which can change setpoints (R-001; P03 G-027) | Basic / all portal, billing, and email accounts |
| IA-5 | Default, shared, and reused passwords on the control path (R-001, R-013; G-026) | Focused / portal, router, PLC, HMI |
| MA-4 | Integrator remote maintenance (R-002; G-028) | Focused / 90 days of portal sessions |
| AC-17 | Remote access rules and the router (R-003; G-030) | Focused / portal and router |
| CP-9 | PLC program and record backups (R-004, R-014; G-029) | Basic |
| AU-6 | Review of portal sign-ins and setpoint changes (G-033) | Basic |
| IR-6 | Incident reporting and the Ground Water Rule clock (R-008; G-014) | Basic |
| RA-3 | Risk assessment (voluntary 300i-2 elements; G-018) | Basic |
| SC-28 | Encryption of customer and compliance data at rest | Basic / laptop and phone |
| SI-3 | Malware defense on the laptop (R-006) | Focused / laptop |

## 2. Methods and objects
- **Examine:** portal user list, security settings, and 90-day audit log; router settings; PLC and HMI password checks at the panel; laptop and phone settings; the integrator and relief agreements; P01 and P05.
- **Test (2026-07-23):** sign-ins to the portal, billing SaaS, and email from a new browser; an external check of the cellular router by the IT technician from the internet side; a standard antivirus test file on the laptop; encryption status on each device.
- **Interview:** replaced by a written **self-review**, because the only person to interview is the assessor. The owner answered the SP 800-53A interview questions in writing, and the IT technician challenged each answer against what was on screen.

## 3. Rules of engagement
- No test changed a treatment setpoint or PLC setting. The router check stopped at the sign-in page once the label password was accepted; the owner then turned off remote administration at the panel.
- Tests at the well house were done after the morning grab sample, with the owner on site and the plant in normal automatic operation.
- Screenshots were cropped to settings; no customer data was copied.

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 21 |
| Other than satisfied | 30 |
| **Total** | **51** |

**Fully satisfied:** SC-28 (laptop and phone encrypted) and SI-3 (the antivirus caught and quarantined the test file).
**Fully other than satisfied:** IA-2(1), AC-17, AU-6, IR-6.
**Partly satisfied:** RA-3 (the assessment exists; no review cycle yet), IA-5 (vendor verification and device keychains only), MA-4 (the portal is documented and ends idle sessions; nothing else), CP-9 (documents and SaaS data backed up; the PLC program and residual spreadsheet are not).

**New finding:** the cellular router's remote web administration was on and accepted the password printed on its label from the internet side (AC-17b.). The owner turned remote administration off during the test on 2026-07-23, and the rule is now POL-01 9.4. The default password stays until the firmware update (POAM-003, POAM-004), and the finding was added to the risk register as R-003.

The 8 controls with weaknesses each have one POA&M item in `poam.csv` (POAM-001 to POAM-008): 3 High, 4 Moderate, and 1 Low. The High items are POAM-001 (portal MFA, due 2026-09-15), POAM-002 (integrator access, due 2026-10-31), and POAM-004 (default and shared passwords, due 2026-11-30).

## 5. Deliverables
`assessment-results.csv` (51 rows), `poam.csv` (8 items), and this memo. Accepted by the owner-operator on 2026-08-31. Because independence is limited, POL-01 4.5 requires an outside reviewer at least every second year.
