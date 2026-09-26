# Security Assessment Plan and Summary: Cris Santos Company | Communications | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (regional broadband and wired telecommunications carrier) |
| System assessed | Network Operations and Customer Billing Platform (OSS/BSS), per the SSP (P02), with its management interfaces to the voice core and access network |
| Tier / Vertical | Small / Communications |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content) |
| Assessor(s) and independence | Contracted independent assessor. Not involved in operating or designing the controls. Escorted by the IT Manager; network tests run with the Network Engineering Manager |
| Assessment window | 2026-08-10 to 2026-08-14 (plan approved by the COO 2026-08-05; walkthrough evidence from 2026-07-28 reused for PE-3) |
| Also supports | The COO's annual CPNI certification (47 CFR 64.2009(e)): the results are evidence for the statement explaining how the company's procedures ensure compliance |

## 1. Scope and controls selected
Small tier scope: 15-25 controls. **20 controls, 140 determination statements.** Controls were chosen because they address the six High risks in P01, the High gaps in P03 (CPNI authentication and the network security benchmark), or the CPNI rules' training, approval, and breach duties.

| Control | Why selected (risk ID or requirement ID) | Depth | Coverage |
|---|---|---|---|
| IA-8 | Customer online authentication (64.2010(c), (e); P03 G-023, G-025); R-003 (High) | Focused | Focused (portal, app, chatbot) |
| SI-2, RA-5 | Unpatched edge routers and unsupported SBC; no internal scanning (P03 G-050, G-051); R-001 (High) | Focused | Focused (edge routers, SBCs, 6 OLTs) |
| IA-2(1), IA-5, AC-2 | Shared and default network element credentials (P03 G-052); R-007 (High), R-019, R-032 | Focused | Comprehensive (all 42 cabinet switches for SNMP) |
| SC-7, AC-6 | Flat management plane; over-privileged mediation account (P03 G-053, G-054); R-002, R-013 (High) | Focused | Focused |
| SI-4, AU-6 | No security monitoring (P03 G-056, G-057); R-010, R-021 | Basic | Basic |
| CP-9, CP-4 | Exposed and untested backups (P03 G-055, G-060); R-008 (High), R-025 | Focused | Focused |
| IR-4, IR-6 | No incident or CPNI breach procedure (64.2011; P03 G-029 to G-034, G-058); R-011 | Focused | Basic |
| AT-3 | CPNI training, including vendor agents (64.2009(b); P03 G-016); R-004 | Focused | Focused (in-house and overflow agents) |
| SA-9 | Unreviewed vendors handling CPNI (P03 G-048); R-022 | Focused | Focused (6 vendors) |
| CM-6 | Network element hardening; R-026, R-032 | Focused | Focused |
| PE-3 | Central offices and remote cabinets; R-026 | Basic | Focused (CO-1, CO-2, 3 cabinets) |
| PT-4 | CPNI approval mechanism (64.2007, 64.2009(a); P03 G-007, G-015); R-006 | Focused | Focused |
| SC-8 | Encryption in transit for CPNI flows; confirms the one strength claimed in P02 | Basic | Basic |

## 2. Methods and objects
- **Examine:** identity provider, BSS, and cloud IAM exports; TACACS+ and device configurations; firewall and route exports; backup and patch reports; scan reports; vendor contracts; the BSS SOC 2 review file; the 2019 CPNI module and training roster; the filed CALEA policies; the draft P08 runbook.
- **Interview:** COO, Vice President of Network Operations, IT Manager, Network Engineering Manager, NOC Manager, Billing Manager, Director of Customer Operations, Regulatory Affairs Manager, CFO, HR Manager, 4 care agents, 3 NOC staff, and 10 randomly selected staff (incident reporting awareness).
- **Test:**
  - portal and app password reset and chatbot authentication with a test account (2026-08-11 retest of the 2026-07-24 P03 tests)
  - reachability of management interfaces from a corporate laptop
  - sign-in to 1 OLT, 1 cabinet switch, and the CO-2 SBC to confirm the absence of MFA
  - SNMP read test with vendor-default community strings against all 42 cabinet switches (2026-08-12)
  - comparison of running software versions with vendor advisories on edge routers, SBCs, and 6 OLTs
  - TLS scan of external endpoints
  - chatbot upsell prompt with an opted-out test account

## 3. Rules of engagement
- No test could interrupt voice, 911, or broadband service. Network element tests ran in the 00:00 to 04:00 maintenance window with the NOC Manager's approval and a rollback plan. SNMP tests were read-only.
- No test touched the lawful-intercept system (SYS-10). Its path was confirmed from routing tables only.
- No CPNI left the company. Test accounts were used for customer-facing tests. Screenshots of real accounts were redacted.
- The assessor would stop and notify the IT Manager and Vice President of Network Operations on finding any critical exposure. **Two were found and reported the same day:** the SBC management interface reachable from the internet edge VLAN (closed 2026-08-14) and the default SNMP strings (reported 2026-08-12; P01 R-032 added 2026-08-13).

## 4. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 51 |
| Other than satisfied | 89 |
| **Total** | **140** |

**Fully other than satisfied (no statement satisfied):** IA-8, IA-2(1), AC-6, AU-6, IR-6, CP-4, PT-4. These controls either had no process at all or, for IA-8 and PT-4, a design that conflicts with the CPNI rules.
**Largely satisfied:** SC-8 (fully), PE-3 at the central offices (9 of 12), AC-2 for workforce identity provider accounts (14 of 26), RA-5 tooling and analysis (5 of 9).

**New findings not known before testing:**
1. Vendor-default SNMP community strings on 11 of 42 cabinet switches (IA-05e., CM-06b.). Added to the risk register as R-032 and to POAM-010.
2. 7 of 64 overflow call center agent accounts belonged to agents who had left the vendor (AC-02h.01). Added to POAM-011.

## 5. POA&M
`poam.csv` has **22 items**: 19 for the controls with weaknesses (every control except SC-8) and 3 carried from P03 gaps that were not tested here (PT-5 opt-out notice, PM-1 certification statement, PM-2 CALEA SSI plan). By risk: **7 High, 14 Moderate, 1 Low**. The High items are POAM-001 to POAM-005, POAM-007, and POAM-008. Status at approval: 14 in progress, 8 open.

## 6. Deliverables and schedule
| Date | Deliverable |
|---|---|
| 2026-08-05 | Plan approved by the COO |
| 2026-08-10 to 2026-08-14 | Fieldwork |
| 2026-08-14 | Out-brief to the COO, Vice President of Network Operations, and IT Manager |
| 2026-08-21 | Draft results and POA&M |
| 2026-09-04 | Results and POA&M accepted by the COO |

Files: `assessment-results.csv` (140 rows), `poam.csv` (22 items), and this plan and summary.
