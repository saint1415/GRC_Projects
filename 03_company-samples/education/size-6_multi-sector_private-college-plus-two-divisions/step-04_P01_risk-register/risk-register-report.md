# Risk Register Report: Cris Santos Company Holdings | Educational Services | Multi-Sector

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. (publicly traded holding company; three divisions plus corporate shared services) |
| Size tier | Multi-Sector (45,000 employees; Educational Services, Information, Health Care) |
| Focus division | Higher Education: Cris Santos College (NAICS 611310), a Title IV institution |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2); roll-up to enterprise risk management per NIST IR 8286 Rev. 1 |
| Also satisfies | The college's written risk assessment under the FTC Safeguards Rule, 16 CFR 314.4(b)(1) and (b)(2); Student Health's HIPAA risk analysis, 45 CFR 164.308(a)(1)(ii)(A); Education Software's annual children's information risk assessment, 16 CFR 312.8(b)(2) |
| Registers | `risk-register.csv` (group), `risk-register-higher-education.csv`, `risk-register-education-software.csv`, `risk-register-student-health.csv` |
| Fieldwork | 2026-05-04 to 2026-07-31 (group and division risk analyses) |
| Prepared | 2026-07-31 by the Group CISO and the Group Chief Risk Officer, with the three division security and compliance leads |
| Approved | 2026-09-15 by the board risk committee (group register and all High risks); division presidents approved their Moderate treatments the same week |

## 1. Scope and risk framing
**Scope.** Every system that holds education records, customer information (16 CFR 314.2), children's personal information, or PHI in the three divisions, plus the corporate shared services they depend on: the group identity platform (SYS-G1), the group SOC (SYS-G2), and the group cloud and data platform (SYS-G3). Division systems are SYS-H1 to SYS-H5, SYS-E1 to SYS-E3, and SYS-S1 to SYS-S2 (`../00_company-facts.md` section 3).

**Two levels of register.**
- **Division registers** hold risks that a division owns and can treat itself. Each division security and compliance lead maintains one. Higher Education, the focus division, has the most detailed register.
- **The group register** holds enterprise risks: risks that cross divisions, sit in shared services, or need group funding or a board decision. Each group risk lists the division risks it rolls up in `related_risk_ids`, and each linked division risk points back to its group risk. Group risks are rated on their own group-level likelihood and impact. They are not simply the highest division rating.

**Risk tolerance and who can accept risk** (`../00_company-facts.md` section 7):
| Level | Who may accept |
|---|---|
| Very Low and Low | Division security and compliance lead |
| Moderate | Division president, with a treatment plan or a documented reason |
| High | Group Chief Risk Officer with the Group CISO, reported to the board risk committee; temporary only, with a dated plan |
| Very High | Board risk committee only |

Risks of harm to children or of harm to a student's access to education rated High may not be accepted. They must be treated.

## 2. Method
1. **Identify.** Threat sources and events come from SP 800-30 Appendices D and E, the group and division BIAs (P05), the gap analyses (P03), the common control assessment (P07), and interviews with each division's leadership.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial) was combined with the likelihood of adverse impact using **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3**, scaled to each division's BIA impact categories (P05). Group impact reflects enterprise consequences: several regulators at once (FSA, FTC, HHS, state attorneys general), customer contracts across about 6,300 schools, and SEC disclosure.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in all four registers were computed by script from the two tables, not assigned by hand.
5. **Roll up (NIST IR 8286 Rev. 1).** Division leads propose roll-ups. The Group Chief Risk Officer decides which risks become group risks, using three tests: the risk crosses divisions, sits in a shared service, or needs a group decision.

## 3. Results

| Register | Very High | High | Moderate | Low | Very Low | Total | Rolled up to group |
|---|---|---|---|---|---|---|---|
| Group (`risk-register.csv`) | 0 | 4 | 11 | 5 | 0 | 20 | n/a |
| Higher Education | 0 | 4 | 17 | 9 | 0 | 30 | 25 |
| Education Software | 0 | 2 | 10 | 6 | 0 | 18 | 13 |
| Student Health | 0 | 2 | 10 | 6 | 0 | 18 | 11 |
| **All registers** | **0** | **12** | **48** | **26** | **0** | **86** | **49** |

### Group risks rated High
| Risk ID | Risk | Rolls up | Treatment | Owner | Due |
|---|---|---|---|---|---|
| GR-01 | Customer and college student records exposed through the Education Software support console | ES-001, HE-001 | Ticket-bound, time-limited, customer-approved support access through PAM; share access logs with customers | Education Software CISO | 2026-12-31 |
| GR-02 | Ransomware spreads from on-premises legacy sites through shared services and exfiltrates data from several divisions | HE-005, HE-021, SH-003, SH-004 | Segment legacy sites; unique local admin passwords; restore tests; cross-division tabletop | Group CISO | 2027-03-31 |
| GR-04 | AI used in consequential student decisions or children's products without adequate governance | HE-008, HE-009, HE-029, ES-003, ES-016, SH-012, SH-013 | Group AI program (P10) | Group Chief Risk Officer | 2027-03-31 |
| GR-05 | Student and patient data used or disclosed across divisions beyond its legal purpose on the group data platform | HE-002, HE-011, SH-002 | Purge out-of-scope data; breach risk assessment; role redesign; purpose tags | Group Chief Privacy Officer | 2027-03-31 |

### Higher Education (focus division): risks rated High
| Risk ID | Risk | Treatment | Owner | Due |
|---|---|---|---|---|
| HE-001 | Support console access exposes college tenant records | College approval of support access; monthly review of support access logs (GR-01) | College CISO | 2026-12-31 |
| HE-002 | Warehouse analysts access student and clinic records beyond any legitimate educational interest | Purge clinic tables; role redesign; purpose tags (POAM-005 to POAM-007) | Director of institutional research | 2027-03-31 |
| HE-005 | Ransomware at a legacy campus spreads to the integration hub and exfiltrates student data | Segment legacy campuses; retire the legacy SIS by 2027-06-30 | College chief information officer | 2027-06-30 |
| HE-008 | Admissions applicant scoring disadvantages applicants by protected trait without notice or review | Bias testing, notice, human review rule, Colorado readiness (POAM-022; P10) | Vice president of admissions | 2026-12-31 |

### Other division risks rated High
| Risk ID | Division | Risk | Owner | Due |
|---|---|---|---|---|
| ES-001 | Education Software | Support console account abused to read customer tenants at scale | Education Software support director | 2026-12-31 |
| ES-003 | Education Software | AI tutor gives harmful content to children or leaks their information | Education Software chief product officer | 2026-12-31 |
| SH-002 | Student Health | Nonstudent PHI disclosed to the college warehouse through the utilization extract | Student Health Privacy Officer | 2026-10-31 |
| SH-003 | Student Health | Ransomware encrypts clinic file servers | Student Health security and compliance lead | 2027-03-31 |

### What the results say
The program is defined and largely sound. There are no Very High risks, and the common controls are strong: a 24x7 SOC, PAM, quarterly access certification, immutable backups, and MFA for every federated user and every student. The High risks cluster **where divisions meet**, not in any one division's basics:
1. **One division's tool can open every other's data.** The support console (GR-01) gives Education Software staff standing read access to the college's tenant and about 6,300 customer tenants (scenario gap 1).
2. **Data crossed a legal line between divisions.** The clinic utilization extract (GR-05) moved nonstudent PHI and contract-college student records into the college's warehouse (scenario gap 2). Student Health must now run a HIPAA breach risk assessment under 45 CFR 164.402 for the nonstudent records (SH-002).
3. **AI governance trails deployment** in all three divisions (GR-04; scenario gaps 5 and 6).
4. **On-premises systems at acquired sites** are the most likely ransomware path into shared services (GR-02; scenario gaps 4 and 8).

Governance gaps 3 and 7 (intercompany oversight and the unexercised notification matrix) are Moderate at group level (GR-06, GR-03). They matter because they decide whether the college learns of a platform incident in time to meet FSA's immediate notice and the FTC's 30-day clock (P08).

**Fed back from P07.** The control assessment found one shared local administrator password on 31 legacy campus servers. It was added as HE-021 and rolled into GR-02.

## 4. Treatment summary
- **Group-funded programs (2026 Q4 to 2027 Q2):** support access redesign (GR-01); legacy campus segmentation and retirement, and Student Health identity migration (GR-02, GR-09); warehouse purge, role redesign, and purpose tags (GR-05); group AI governance program (GR-04); egress detection (GR-15).
- **Accepted (all Low):** HE-026 (encrypted laptop loss), ES-018 (denial of service, covered by provider protection), SH-014 (encrypted tablet loss), SH-016 (clearinghouse outage, claims can be queued).
- **Avoided:** SH-013 (the proposed counseling triage chatbot was not approved).
- **Contract actions:** revised intercompany service agreement (GR-06, HE-003, ES-008); district notices and system description update for the AI tutor (ES-004); contract term register for notice clocks (GR-17, ES-010).
- **Treatment status:** 57 risks are In progress, 25 are Open (treatment approved, work not started), and 4 are Closed (the accepted risks).

## 5. Reporting to enterprise risk management
Per NIST IR 8286 Rev. 1, the group register feeds the enterprise risk profile that the Group Chief Risk Officer presents to the board risk committee each quarter. The four High group risks were presented on 2026-09-15. The Higher Education register and the P03 gap analysis also feed the Qualified Individual's written report to the college board of trustees on 2026-10-20 (16 CFR 314.4(i)(2): risk assessment, risk management and control decisions, service provider arrangements, testing results, security events, and recommendations). The Reg S-K Item 106 disclosure in the next annual report draws on the governance described here.

## 6. Approval
- Board risk committee: approved the group register, the four High group treatment plans, and the funding request, 2026-09-15.
- Group Chief Risk Officer and Group CISO: approved treatment plans for the eight High division risks, 2026-09-15.
- Division presidents: approved Moderate and Low treatments and acceptances for their divisions, 2026-09-08 to 2026-09-15.
- Next full review: May to July 2027, or sooner after a major change, acquisition, or incident (314.4(b)(2)).
