# Risk Register Report: Cris Santos Company | Public Administration | Sole Proprietorship

| Field | Value |
|---|---|
| Organization | Cris Santos Company (independent GovTech consultant) |
| Size tier | Sole Proprietorship (owner-consultant only, 0 employees) |
| Vertical | Public Administration |
| Method | NIST SP 800-30 Rev. 1 (qualitative 5-level scales; Tables G-5 and I-2) |
| Also satisfies | RA-3 for the county contract's SP 800-53 Moderate clause, and the risk basis for the security program the CJIS Security Addendum (sec. 3.01) requires. This is the consultancy's first risk assessment |
| Prepared | 2026-08-14 by the owner-consultant, with the on-call IT technician (under NDA since 2026-08-07). R-015 added 2026-08-26 from P07 testing |
| Risk owner and approver | Owner-consultant (owner, security officer, and risk acceptor for every risk) |
| Approved | 2026-09-15 |

## 1. Scope and risk framing
**Scope.** The whole business as one system: the Consulting Delivery Environment (SYS-01 to SYS-04, SYS-06 to SYS-09), the owner's use of the three agency accounts (SYS-05), paper in the locked file box, and the on-call IT technician. Processes come from the BIA (P05).

**What makes this business different.** The consultancy hosts nothing, so most of its risk is **risk it carries into other people's systems**: the agencies' data on the owner's devices, and the owner's access as a path into the agencies' case management systems. Impact ratings reflect harm to the agencies and the people in their records as well as to the business.

**Risk tolerance.** The owner owns and accepts every risk. Because the same person proposes and approves, three fixed rules apply (POL-01 4.4):
- Low and Very Low: may be accepted, with the reason written in the register.
- Moderate: may be accepted only with a dated treatment plan or a written reason.
- High and Very High: must be treated with a dated plan, never accepted as they are. Any risk that could expose CJI is treated, whatever its level.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the missing-controls list in `../00_company-facts.md` section 4, the SaaS mapping (P04), the gap analysis (P03), and a walk through the laptop, phone, home network, and each SaaS account with the IT technician.
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (other sources), and likelihood of adverse impact, each on the 5-level scale, combined with **Table G-5**.
3. **Rate impact.** Table H-3 levels, using the BIA impact categories (cost, operations, regulatory and contract, reputation).
4. **Determine risk.** **Table I-2.** The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results
| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 8 |
| Low | 4 |
| **Total** | **15** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware on the laptop with theft of county extracts and city exports | High | Standard daily account, delete old extracts, encrypted backup, training, runbook | Owner-consultant | 2026-10-31 |
| R-002 | Stolen credentials or session used to reach the sheriff's or county's system | High | Standard daily account, sign out of agency systems, phishing training | Owner-consultant | 2026-10-31 |
| R-015 | CJI copied out of the sheriff's virtual desktop (found in P07) | High | CJIS refresher by 2026-09-24, data location rule, quarterly search | Owner-consultant | 2026-11-30 |
| R-003 | County extracts kept past the contract deletion date | Moderate | Delete everywhere and certify to the county | Owner-consultant | 2026-09-30 |
| R-004 | Unencrypted USB drive with driver license numbers | Moderate | Encrypt the drive and remove county data | Owner-consultant | 2026-09-30 |
| R-005 | City applicant data put into a consumer-grade AI assistant | Moderate | Avoid: no agency data in AI tools; support the city's notice decision (P10) | Owner-consultant | 2026-09-30 |
| R-009 | Owner unavailable or phone lost; agency clocks missed | Moderate | Contact sheet, sealed recovery codes, peer backup | Owner-consultant | 2026-12-31 |

The three High risks share one cause: **the owner's laptop is both a store of agency data and a doorway into agency systems, and it is run with administrator rights every day.** A standard daily account and deleting data the contracts no longer allow cost nothing and reduce R-001, R-002, and R-003 within two weeks of adoption. R-015 is the proof that "CJI never leaves the virtual desktop" was an assumption, not a control.

## 4. Treatment summary
- **Free fixes first (by 2026-09-30):** standard daily laptop account, deletion and certification of county extracts, encrypted USB drive, website builder MFA, printed agency contact sheet, and the P08 runbook.
- **Budgeted (about $300 a year):** a yearly security course, two hardware security keys, and an encrypted USB drive. The router changes use the existing hardware.
- **Agency actions:** the city disables the 2024 account and is asked for contractor MFA (R-011); the city's attorney decides on resident notice for the AI proof of concept (R-005); the sheriff closed clipboard and drive mapping on 2026-08-26 (R-015).
- **Accepted (Low):** R-013 (productivity suite outage) and R-014 (hurricane), because every agency system and file is reachable from any clean device.

## 5. Approval
Owner-consultant, 2026-09-15: approved all treatment plans and the two acceptances. Next full review August 2027, or sooner after a new agency client, a new system or AI tool, or an incident.
