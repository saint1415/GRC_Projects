# Risk Register Report: Cris Santos Company | Nuclear Reactors, Materials, and Waste | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radiation safety consulting practice) |
| Size tier | Micro (7 employees) |
| Vertical | Nuclear Reactors, Materials, and Waste |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | Client contract duties to protect Part 37 security information (37.43(d) flow-down); Fla. Stat. 501.171(2) "reasonable measures" |
| Prepared | 2026-08-14 by the Office Manager (Security Officer) with the Part 37 services lead and the MSP lead technician |
| Updated | 2026-08-26 (R-023 added from P07 testing); 2026-09-15 (R-006 treated and closed; R-020 and R-021 accepted) |
| Approved | 2026-09-15 by the Principal Health Physicist (owner) |

## 1. Scope and risk framing
**Scope.** The whole practice and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-08), the office and calibration laboratory, the USB drives staff take to client sites, and the vendors that hold practice or client information: the productivity suite vendor, the calibration system vendor, the accounting and payroll service, the MSP and its backup subcontractor, and the dosimetry processor.

**Whose harm counts.** Two kinds of harm are rated together:
- harm to the practice (lost revenue, lost clients, contract breach), and
- harm the practice could cause its clients: disclosure of a client's Part 37 security information, malware carried into a reactor plant, or a wrong calibration certificate. A 7-person practice cannot survive the loss of trust that would follow any of these, so client harm is rated at least as high as direct harm.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Office Manager may accept.
- Moderate: only the owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The owner approves a dated treatment plan instead. A risk to a client's security information or to a reactor plant is never accepted above Low.

This is the practice's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the April 2026 reactor kiosk event, and interviews with all 7 staff and the MSP lead technician (2026-08-03 to 2026-08-14).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). For a practice with about $4,400 of receipts per business day, the loss of the Part 37 service line or of a reactor client is rated High; losing control of every computer at once is Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 3 |
| Moderate | 15 |
| Low | 5 |
| **Total** | **23** |

Status: 10 In progress, 10 Open, 3 Closed (R-006 treated; R-020 and R-021 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Phished account used to copy client Part 37 security information | High | Restricted per-client folders; MFA number matching; access review; training | Senior Health Physicist (Part 37 services lead) | 2026-12-31 |
| R-003 | Malware on practice USB media carried into a reactor plant | High | Personal media banned; company encrypted drives scanned before every trip | Senior Health Physicist (field services lead) | 2026-10-31 |
| R-013 | MSP tool or shared MSP logins compromised | High | Named MSP accounts with MFA; annual MSP review; 24-hour incident notice in the contract | Principal Health Physicist | 2026-12-31 |
| R-004 | Unapproved staff can open client security information | Moderate | Client approval list; restricted folders | Senior Health Physicist (Part 37 services lead) | 2026-10-15 |
| R-005 | Departed staff keep access and stay on client lists | Moderate | Departure checklist with client notice in 2 working days | Office Manager | 2026-10-31 |
| R-010 | Suite data cannot be restored | Moderate | First restore test; 90-day immutable versions | Office Manager | 2026-10-31 |

**The common theme is that the practice carries other people's secrets.** Two of the three High risks are about harm the practice could pass to clients: a stolen account opens six clients' security plans (R-001), and a USB drive is the practice's only path into a reactor plant (R-003). The third (R-013) is the outside party that holds administrator access to everything. The restricted client library alone also lowers R-004, R-006, R-007, and R-012.

**Risks fixed or found during the work:**
- R-006: the MSP removed 14 "anyone with the link" sharing links on 2026-08-05 and disabled that link type. The client whose Part 37 documents were behind 2 of the links was told on 2026-08-06. The suite's 180 days of log history showed no access by unknown parties; older history does not exist. Closed.
- R-005: the former Health Physicist's SYS-02 account was disabled on 2026-08-04, the day it was found, and the 2 clients that had approved him were told on 2026-08-05. SYS-02 sign-in history showed no use after his last day. The process gap remains open.
- R-007: the client whose implementing procedure was pasted into a public chatbot was told on 2026-08-07. Its RSO assessed the event and recorded it as not suspicious activity under its own procedures. The practice gap remains open.
- R-023: added on 2026-08-26 after P07 testing found an inbound remote desktop port forward to lab workstation 2. The MSP removed the rule on 2026-08-25.

## 4. Treatment summary
- **Funded (2026 Q4, approved by the owner; about $5,600 one-time and $3,600 a year):**
  - MSP-managed EDR with after-hours monitoring on 9 computers: about $1,600 a year
  - Security awareness training with phishing exercises for 7 people: about $500 a year
  - Backup upgrade to 90-day immutable versions: about $600 a year
  - Suite audit log retention add-on (one year): about $400 a year
  - Annual MSP security review: about $500 a year of MSP and owner time
  - 6 hardware-encrypted USB drives for field kits: about $600 one-time
  - Lab network segment, lab workstation encryption, and restore tests by the MSP: about $1,500 one-time
  - Independent assessment and policy work in 2026 (P07, P06): about $3,500 one-time
- **Deferred to the 2027 budget:** replacing or upgrading the gamma spectroscopy software so lab workstation 2 can run a supported operating system (R-009). Until then, the lab network segment and monthly images are the compensating controls.
- **Accepted:** R-020 (Low; laptops encrypted), R-021 (Low; work moves to mobile hotspots).
- **Contract actions:** MSP amendment with named accounts, MFA, 24-hour incident notice, and a subcontractor list (R-013) by 2026-12-31; SYS-02 data-use terms (R-016) by 2026-11-30; the 2 missing client approval letters (R-004) by 2026-10-15.

## 5. Approval
- Principal Health Physicist (owner): approved all treatment plans, the two acceptances, and the budget on 2026-09-15.
- Next full review: August 2027, or sooner after a major change (for example, a new Part 37 client, a new reactor client, or enabling the suite's AI assistant) or an incident.
