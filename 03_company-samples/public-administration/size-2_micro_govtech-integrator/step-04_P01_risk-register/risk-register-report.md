# Risk Register Report: Cris Santos Company | Public Administration | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (GovTech systems integrator) |
| Size tier | Micro (7 employees) |
| Vertical | Public Administration |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | SP 800-53 RA-3, required by the AC-02, AC-03, and AC-04 contracts; the risk assessment the CJIS Security Policy expects of contractors (CJISSECPOL v6.1 RA-3) |
| Prepared | 2026-08-07 by the Operations Manager (Security and Compliance Officer) with the Lead Platform Engineer and the MSP lead technician |
| Updated | 2026-08-19 (R-024 and R-025 added from P07 testing); 2026-08-31 (R-018 and R-021 accepted; R-024 closed) |
| Approved | 2026-08-31 by the owner |

## 1. Scope and risk framing
**Scope.** The whole company and its key vendors: the Hosted Case Management Service (SYS-01, SYS-02, SYS-09), the laptops and SaaS services that administer it (SYS-03 to SYS-06), the MSP and its remote tool (SYS-08), and the company's access to the revenue agency's virtual desktop (SC-01). The vendors in scope are the platform vendor (with its AI add-on), the IaaS provider, the MSP, the productivity suite vendor, the helpdesk vendor, and the repository vendor. See `../00_company-facts.md` sections 1 to 3.

For this company, contract risk counts as much as outage risk. A failed CJIS audit can end the AC-01 contract, and the revenue agency may void the subcontract if the company fails the Exhibit 7 terms (Pub. 1075 Exhibit 7, I(13)).

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Operations Manager may accept.
- Moderate, High, and Very High: only the owner may accept. High and Very High risks are not accepted; the owner approves a dated treatment plan instead.
- A risk that would breach a CJIS Security Addendum or Exhibit 7 term may not be accepted at all. It must be treated, or the regulated data or access removed.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the SSP (P02), the cloud mapping (P04), the gap analysis fieldwork (P03), the 2026-07-29 data inventory, and interviews with all 7 staff and the MSP lead technician (2026-07-27 to 2026-08-07).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. Harm to the agencies and the people in their records counts, not only harm to the company.
4. **Determine risk.** Risk level comes from **Table I-2**. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 6 |
| Moderate | 12 |
| Low | 6 |
| **Total** | **25** |

Status: 12 In progress, 10 Open, 3 Closed (R-024 treated the day it was found; R-018 and R-021 accepted). Treatment: 22 Mitigate, 1 Avoid (R-013), 2 Accept.

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware through a phished administrator laptop encrypts SYS-02, deletes the exports, and alters agency records | Very High | Write-once exports in a separate account; separate administrator accounts; EDR with after-hours alerting; phishing training | Lead Platform Engineer | 2026-12-31 |
| R-002 | Theft of CJI and applicant Social Security numbers, then extortion | High | Bulk-export and sign-in alerts; delete CHRI working files after each load; limit export rights | Lead Platform Engineer | 2026-10-31 |
| R-004 | Records cannot be restored within the 24-hour and 4-hour contract terms | High | 4-hourly write-once exports; quarterly record-level restore tests; contingency plan | Lead Platform Engineer | 2026-11-30 |
| R-005 | Agencies told too late for their CJIS, IRS, or Florida 12-hour clocks | High | POL-03 and the P08 runbook; staff briefing on the 1-hour rule; tabletop | Operations Manager | 2026-11-30 |
| R-012 | MSP remote tool compromise reaches every laptop, cached CJI, and the SSH keys | High | MSP contract amendment; SSH keys off laptops; no CJI on laptops | Owner | 2026-12-31 |
| R-015 | Caseworkers adopt wrong AI pre-screening suggestions | High | Add-on switched off from 2026-09-01 until the P10 conditions are met | Owner | 2026-12-31 |

**Two themes run through the top risks:**
- **An attacker who gets one administrator laptop gets everything** (R-001, R-002, R-004, R-012). The same people read email and administer the tenant and the server on one laptop, the server's SSH keys sit on those laptops, the backup copy sits next to the server, and nobody watches after hours. Fixing these four also lowers R-008, R-009, R-020, and R-025.
- **The company is out of step with the agency terms that let it touch CJI and FTI** (R-003, R-005, R-006, R-007, R-013). Each is rated Moderate or High today, but each can end a contract. That is why the treatment dates for them are the earliest in the register.

**Risks that were found or changed during the work:**
- R-006: the data inventory on 2026-07-29 found a defect log in the suite with 14 taxpayer identification numbers typed in from the agency virtual desktop in May 2026. The Operations Manager reported it by phone to the prime's security officer and the revenue agency's disclosure officer the same day. The agency could not rule out that the values were FTI within 24 hours, so it reported the spill to TIGTA and the IRS Office of Safeguards on 2026-07-30 (Pub. 1075 sec. 1.8.2). The file was purged on 2026-07-30 under the agency's direction, and the MSP purged the suite backup copies on 2026-08-05. The agency's review is open.
- R-003 and R-007: the support role was narrowed to exclude AC-01 on 2026-08-12, and the Lead Platform Engineer was suspended from SC-01 on the same day until recertified.
- R-024 and R-025 were added on 2026-08-19 from P07 testing. R-024 (SSH open to any address) was closed on 2026-08-18; R-025 (the sheriff's file-drop password in a script) is in progress after sheriff IT rotated the password on 2026-08-20.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the owner; about $4,800 one-time and $5,300 a year):**
  - MSP-managed endpoint detection and response with after-hours alerting on 8 laptops: about $2,400 a year
  - Security awareness training with phishing exercises for 7 staff: about $500 a year
  - Write-once export storage in a separate account, 4-hourly exports, and a 1-year log archive: about $1,000 a year
  - MFA-protected session service, automatic patching, and monthly scanning for SYS-02: about $1,200 a year
  - Helpdesk plan change to allow attachment blocking: about $200 a year
  - Independent assessment and policy support in 2026 (P07, P06): about $4,500 one-time
  - Fingerprint-based check fees and MSP project time for re-encryption and clean-up: about $300 one-time
  - Lead Platform Engineer time: about 120 hours over 2026 Q4, taken from project work
- **Accepted (owner):** R-018 (Low; platform vendor outage beyond 24 hours), R-021 (Low; hurricane closes the office).
- **Avoided:** R-013, by keeping CJI out of the helpdesk.
- **Agency and prime disclosures:** the FTI spill (R-006) was reported 2026-07-29; the June connections from an unapproved laptop (R-007) were disclosed to the prime and the revenue agency on 2026-08-14; the AC-01 LASO was told about CJI in helpdesk tickets (R-013) and about the unscreened support role (R-003) on 2026-08-14.

## 5. Approval
- Owner: approved all treatment plans, the two acceptances, and the budget on 2026-08-31.
- Next full review: July 2027, or sooner after a major change (for example, restarting AI suggestions, a new agency customer, or a new CJISSECPOL version) or an incident.
