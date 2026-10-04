# Risk Register Report: Cris Santos Company | Agriculture, Forestry, Fishing and Hunting | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (precision-agriculture row crop and watermelon farm) |
| Size tier | Micro (7 employees) |
| Vertical | Agriculture, Forestry, Fishing and Hunting |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat sources and conditions from NIST SP 800-82 Rev. 3 |
| Benchmark | NIST CSF 2.0 (ID.RA and GV.RM); no binding federal cybersecurity rule applies to the farm (P03 section 1) |
| Prepared | 2026-07-31 by the Office Manager (Security Coordinator) with the Irrigation and Equipment Technician and the MSP technician |
| Updated | 2026-08-13 (R-023 added from P07 testing; R-002 reviewed); 2026-08-31 (R-012 and R-022 accepted and closed) |
| Approved | 2026-08-31 by the Owner and General Manager |

## 1. Scope and risk framing
**Scope.** The whole farm and its key vendors. That covers the Farm Management and Irrigation Control Platform (FMICP) in the SSP (P02), the eight business processes in the BIA (P05), the systems that hold personal and regulated records (SYS-01 to SYS-10 in `../00_company-facts.md`), and the outside parties that run or reach those systems: the FMIS vendor, the MSP, the irrigation dealer, the equipment dealer, the backup service, the payroll service and H-2A filing agent, and the AI vendor.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager (Security Coordinator) may accept.
- Moderate: only the Owner and General Manager may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner and General Manager approves a dated treatment plan instead. Risks that could injure a worker (fertigation, spray equipment) are never accepted at High.

This is the farm's first documented cybersecurity risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the OT threat sources in SP 800-82 Rev. 3, the BIA (P05), the gap analysis (P03), and interviews with the Owner and General Manager, the Office Manager, the Irrigation and Equipment Technician, the Field Supervisor, the MSP technician, and the irrigation dealer (2026-07-20 to 2026-07-31).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (cost, operations, regulatory, safety, reputation). Season matters: impact was rated for the late-May to mid-July watermelon harvest, when an outage costs the most.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 16 |
| Low | 4 |
| **Total** | **23** |

Treatments: 21 Mitigate and 2 Accept. Status: 16 Open, 5 In progress, 2 Closed (R-012 and R-022 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware via phishing encrypts the office computers and the synced Office folder during harvest | High | Training in English and Spanish; MSP-managed EDR with after-hours alerting; immutable backups | Office Manager | 2026-12-31 |
| R-004 | Backups destroyed with production or not restorable; pump station program held only by the dealer | High | 90-day immutable versions; MFA on the backup console; restore tests; monthly SYS-01 export; farm-held program copy | Office Manager | 2026-11-30 |
| R-023 | Pump station gateway admin page reachable from the internet with the default password | High | Password changed and internet-facing administration off (done 2026-08-14); firmware update and retest | Irrigation and Equipment Technician | 2026-09-30 |
| R-002 | Dealer's always-on remote access used to stop irrigation or change fertigation | Moderate | On-request sessions with named accounts and MFA; session log; dealer security terms | Irrigation and Equipment Technician | 2026-10-31 |
| R-005 | Theft of payroll and H-2A files | Moderate | Restrict and stop syncing the Office folder; encrypt the desktop; mass-download alerts | Office Manager | 2026-10-31 |
| R-007 | Only one person can run irrigation by hand | Moderate | Written procedure in English and Spanish; second person trained and drilled | Owner and General Manager | 2027-02-28 |

**The common theme is that a small farm's irrigation and records sit behind a few passwords nobody manages.** The dealer's gateway (R-002, R-023), the Technician's SYS-01 account (R-003), and the flat shop network (R-020) are three ways to reach irrigation, and none of them has MFA or monitoring. The office side has the same pattern: one phishing email (R-001) could take the payroll and H-2A files (R-005) and the only usable backup (R-004). The treatments for the three High risks also reduce R-002, R-003, R-005, R-008, R-013, and R-020.

**Risks that were fixed or found during the work:**
- R-010: the former bookkeeper's mailbox was disabled on 2026-07-21, the day it was found, and its forwarding rule removed. The Office Manager reviewed the 41 messages forwarded after her departure and documented on 2026-07-24 that none contained personal information as defined in Fla. Stat. 501.171(1)(g), so no breach notice was needed. The process gap remains open.
- R-023: added on 2026-08-13 after P07 testing found the gateway admin page reachable from the internet with the default password. The dealer fixed the password and turned off internet-facing administration on 2026-08-14. The risk stays In progress until the firmware update and retest.
- R-017: the Security Coordinator designation and the three policies were approved on 2026-08-31.

**Food defense note.** R-008 (fertigation changed by an attacker or by mistake) is the only risk where harm to produce through the farm's systems is plausible. 21 CFR Part 121 (N11-R01) does not apply to the farm (P03 section 1), but its vulnerability-assessment approach was used as a voluntary checklist for that risk.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1, approved by the Owner and General Manager; about $3,900 one-time and $3,400 a year):**
  - MSP-managed EDR with after-hours alerting on 3 office computers: about $900 a year
  - Security awareness training with Spanish-language material for 7 people: about $400 a year
  - Backup upgrade to 90-day immutable versions: about $500 a year
  - Firewall segment for the pump station and a guest Wi-Fi network (MSP project): about $1,200 one-time
  - Surge protection on the pump station panel: about $600 one-time
  - Dealer time to set fertigation hard limits, reconfigure the gateway for on-request access, and hand over the program copy: about $900 one-time
  - Annual independent assessment and policy work (P07, P06): about $1,200 a year
  - Annual MSP security review and remaining MSP project time (desktop encryption, mobile device settings, restore tests): about $400 a year and about $1,200 one-time
- **Accepted:** R-012 (Low; irrigation and records do not depend on the shop internet line) and R-022 (Low; FMIS vendor controls evidenced by its SOC 2 report).
- **Contract actions:** irrigation dealer security terms (R-002) by 2026-10-31; AI vendor data terms (R-018) by 2026-10-31; equipment dealer access terms (R-014) and MSP contract amendment (R-021) by 2026-12-31.

## 5. Approval
- Owner and General Manager: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, after the watermelon harvest, or sooner after a major change (for example, connecting the yield model to irrigation, or adding pump station automation) or an incident.
