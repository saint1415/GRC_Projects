# Risk Register Report: Cris Santos Company | Government Services and Facilities | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (facilities support contractor operating government buildings) |
| Size tier | Small (60 employees) |
| Vertical | Government Services and Facilities |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2). OT threats informed by NIST SP 800-82 Rev. 3 |
| Also supports | State contract cybersecurity exhibit (risk assessment under SP 800-53 RA-3); FAR 52.204-21 safeguards for the federal contract |
| Prepared | 2026-07-24 by the IT Manager (Information Security Officer) |
| Approved | 2026-08-31 by the Chief Operating Officer (Moderate and below) and the majority owner (High and Very High) |

## 1. Scope and risk framing
**Scope.** The Facility Operations Technology Platform (FOTP) defined in the SSP (P02), the corporate systems that hold customer or federal contract information (identity provider, email, CMMS, HR), and the business processes in the BIA (P05). See `../00_company-facts.md` sections 3 and 4.

**What is out of scope.** GSA's own building systems on the GSA Building Systems Network (SYS-10). GSA owns, authorizes, and monitors them. The register covers only the company's part: its staff, PIV cards, and conduct on those systems.

**What makes this company different.** It does not own the buildings or the field equipment. Its risks come from operating other people's building systems: remote access into government OT networks, holding cardholder data and security system layouts, and meeting three sets of contract terms. A failure can open doors at a government building, not only leak data.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the majority owner may accept, and only temporarily with a dated treatment plan. Risks that could unlock doors or disable life-supporting building services at a customer site are not accepted at High or above.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the OT threat discussion in SP 800-82 Rev. 3, the BIA, the gap analysis (P03), and interviews with the Controls Engineering Manager, Security Systems Supervisor, Site Managers, and Contracts Manager. Site walkthroughs were held 2026-07-15 to 2026-07-17.
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) and the likelihood of adverse impact were rated separately and combined with **Table G-5**.
3. **Rate impact.** Impact uses **Table H-3** with the BIA impact categories (safety and physical security, operations, contract and regulatory, cost, reputation).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 3 |
| Moderate | 19 |
| Low | 9 |
| Very Low | 1 |
| **Total** | **33** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Intrusion through the integrator's remote-support tool unlocks doors and changes HVAC at county sites | Very High | Remove the tool; all remote access through the jump host with MFA, approval, and recording; segment county sites | IT Manager | 2026-10-15 |
| R-006 | Ransomware in the cloud tenant destroys the BAS supervisory server and its backups | High | Immutable, separate-account, second-region backups; quarterly restore tests | IT Manager | 2026-12-31 |
| R-009 | Covered video equipment in use breaches the FAR 52.204-25 representation | High | Confirm manufacturer; report within 1 business day if covered; replace the HQ video system | Contracts Manager | 2026-10-31 |
| R-016 | Exploit of out-of-date edge firewall and VPN firmware at a site | High | Update firmware; monthly firmware review; vulnerability scanning | IT/OT Systems Administrator | 2026-10-31 |
| R-002 | Shared supervisory account used to change BAS programs | Moderate | Named accounts in the identity provider; retire the shared account | Controls Engineering Manager | 2026-11-30 |
| R-011 | Customer notice deadlines missed after an incident | Moderate | IR policy and runbook with notification matrix; customer tabletops | IT Manager | 2026-11-30 |

**Theme of the Very High and High risks: remote access into government OT is the weak point.** The always-on integrator tool (R-001), stale firewall firmware (R-016), and backups that an intruder could delete (R-006) together mean an attacker could get in, act on building systems, and prevent recovery. Fixing the remote access path also reduces R-002, R-003, R-004, R-017, R-019, and R-033.

**R-009 is a contract risk, not a technical one.** FAR 52.204-25(b)(2) prohibits the company from *using* covered video surveillance equipment anywhere, not only on federal work. The origin of the headquarters NVR and 4 cameras is not confirmed. Until it is, the company treats the risk as High because the federal contract is 40% of revenue.

**Added after the control assessment (P07):**
- R-032 was added on 2026-08-05 after testing found 23 undocumented BACnet devices at the county government center.
- R-003 was re-rated on 2026-08-06 after testing found default passwords on 9 controllers and 1 NVR.

## 4. Treatment summary
- **Funded (2026 Q4 budget, $86,000):**
  - Jump host enforcement, privileged session approval, and removal of the integrator tool
  - Backup redesign (separate account, immutable, second region)
  - Central log workspace with 1-year retention
  - Vulnerability scanning service (external, internal, and OT-safe passive discovery)
  - Replacement of the headquarters video system
  - OT VLANs at the 4 county service centers (deferred to 2027 Q1 because it needs county IT change windows)
- **Accepted:**
  - R-021: Low, hardware security keys already in place
  - R-027: Very Low
  - R-030: Low
- **Avoided:** R-014. The company will not configure or operate 1:N face identification of the public (see P10).
- **Shared:** R-028, through contract terms and cyber insurance.
- **Contract actions:** subcontractor security addendum with FAR flow-downs (R-019) by 2026-12-31; 72-hour breach notice clause for the CMMS vendor at renewal (R-028).

## 5. Approval
- Chief Operating Officer: approved Moderate and Low treatments and acceptances, 2026-08-31.
- Majority owner: approved the Very High and High treatment plans and the budget, 2026-08-31. R-001 is not accepted; it is in treatment with a 2026-10-15 deadline and interim weekly checks that the remote-support tool is disabled between vendor visits.
- Next full review: July 2027, or sooner after a major change, a new contract, or an incident.
