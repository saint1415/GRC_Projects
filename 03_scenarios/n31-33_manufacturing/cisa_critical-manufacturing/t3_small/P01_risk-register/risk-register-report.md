# Risk Register Report: Cris Santos Company | Critical Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (power and distribution transformer manufacturer, Florida) |
| Size tier | Small (200 employees; SBA-small under the 800-employee standard for NAICS 335311) |
| Vertical | Critical Manufacturing |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2), with OT threat sources and predisposing conditions from NIST SP 800-82 Rev. 3 Appendix C |
| Benchmark | NIST CSF 2.0 with SP 800-82 Rev. 3 (voluntary; see P03 section 1) |
| Prepared | 2026-07-24 by the IT Manager with the Controls Engineer; R-034 added 2026-08-15 |
| Approved | 2026-09-04 by the VP Operations (Moderate and below) and the President (Very High and High) |

## 1. Scope and risk framing
**Scope.** The whole company on its one Florida campus:
- the ERP and Production Scheduling Platform (P02);
- the plant control systems, test bay, and historian;
- the PLM vault and TMU firmware library;
- the SaaS and cloud services;
- the suppliers with access to company systems (MSP, OEMs, cloud and AI vendors);
- the obligations the company owes customers: the 12 utility Supplier Cyber Security Addenda and the federal contract clauses.

Business processes and recovery times come from the BIA (P05). Systems are listed in `../scenario-facts.md` section 3.

**What matters most.** The company builds equipment that utilities need to keep the grid running and to restore it after storms. The two things leadership cares about most are:
- keeping the lines producing, especially during hurricane season, when emergency transformer orders arrive;
- keeping the trust of the utilities that buy from it, which now depends on meeting the supplier cyber terms in their contracts.

**Risk tolerance and who can accept risk:**
- Very Low and Low: the IT Manager may accept.
- Moderate: the VP Operations may accept, with a treatment plan or a documented reason.
- High and Very High: only the President may accept, and only temporarily with a dated treatment plan.
- Risks that could affect **worker safety** (drying oven, oil processing, high-voltage test) or **product integrity delivered to utilities** may not be accepted at High or above.

This is the company's first documented cybersecurity risk assessment.

## 2. Method
1. **Identify.**
   - Threat sources and events come from SP 800-30 Appendices D and E and SP 800-82 Rev. 3 Appendix C.
   - The vertical scenario (ransomware disrupting production of grid equipment) and the BIA were also inputs.
   - Interviews covered the Plant Manager, Controls Engineer, Production Planning Manager, Quality Manager, Field Service Manager, and Contracts and Compliance Manager.
   - The gap analysis (P03) supplied the vulnerabilities.
2. **Rate likelihood.** Two ratings were made for each risk: the likelihood of initiation (adversarial) or occurrence (non-adversarial), and the likelihood that the event causes adverse impact. They were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the P05 impact categories: cost, operations, safety, regulatory and contractual, and reputation.
4. **Determine risk.** **Table I-2** gives the risk level. The `overall_likelihood` and `risk_level` columns in `risk-register.csv` were computed by script from the two tables, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 7 |
| Moderate | 16 |
| Low | 10 |
| **Total** | **34** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Ransomware spreads from the office through the dual-homed MES into a flat plant network and stops production | Very High | OT DMZ and zoning; 24x7 managed detection; offline OT backups; runbook and tabletop | Controls Engineer | 2027-03-31 |
| R-002 | Ransomware encrypts the ERP and deletes backups in the same cloud account | High | Immutable separate-account, second-region backups; quarterly restore tests | IT Manager | 2026-12-31 |
| R-003 | Always-on OEM router used to change drying oven setpoints | High | Routers off except approved sessions; remote access gateway with MFA and recording | Controls Engineer | 2026-12-31 |
| R-034 | OEM default password on the drying oven HMI web page (found in P07) | High | Change password; disable web interface; zone ovens | Controls Engineer | 2026-09-30 |
| R-005 | Tampered TMU firmware shipped to utility substations | High | Signature or hash verification on receipt and at final test; hashes to utilities | Quality Manager | 2026-11-30 |
| R-006 | A missed utility addendum duty costs a supply agreement | High | Obligations register; disclose 2 open advisories; notice procedures | Contracts and Compliance Manager | 2026-10-31 |
| R-008 | Covered cameras and an inaccurate SAM representation jeopardize federal work | High | Disconnect and replace cameras; correct representation | Contracts and Compliance Manager | 2026-10-31 |
| R-014 | MSP remote management tool compromise pushes malware everywhere | High | Keep RMM out of OT; MSP activity reports; 24-hour notice term | IT Manager | 2026-12-31 |

**The pattern.** Six of the eight top risks come from **uncontrolled paths into the plant**:
- the office-to-plant network and the dual-homed MES (R-001);
- OEM routers and the oven's default password (R-003, R-034);
- the MSP's remote tool (R-014);
- backups that share the fate of production (R-002).

Closing the IT/OT boundary and the remote access paths also lowers five Moderate risks (R-009, R-010, R-021, R-026, R-027) and one Low risk (R-023).

**The other two top risks are about customers.** R-005 and R-006 are the risks utilities care about under their CIP-013 programs. They are cheap to fix (procedures, hashes, a register) and are due first.

R-034 was added on 2026-08-15 after the control assessment (P07) found the OEM default password on the drying oven HMI's web configuration page.

## 4. Treatment summary
- **Funded (2026 Q4 to 2027 Q2 budget, $186,000, approved 2026-09-04):**
  - OT network segmentation, OT DMZ, and a remote access gateway ($68,000)
  - 24x7 managed detection and response for IT endpoints and the firewall ($38,000 a year)
  - A passive OT network monitoring sensor ($22,000)
  - Immutable, separate-account backups and an offline OT backup store ($9,000)
  - Replacement of the 4 covered cameras ($6,000)
  - A retainer with an OT-capable incident response firm through the insurer ($10,000)
  - A second internet carrier ($8,000 a year)
  - Replacement of the first 4 unsupported HMIs, with OEM support ($25,000)
- **Accepted:**
  - R-015: hardware keys already reduce it to Low.
  - R-025: Low while time-based preventive maintenance continues.
  - R-033: Low; portals and email serve as fallback.
- **Contract and procedure actions (no capital):**
  - The obligations register.
  - Disclosure of the 2 open supplier advisories to utilities by 2026-09-30.
  - Access-revocation notices for the 3 departed field technicians.
  - Firmware hash verification.
  - Correcting the SAM representation.

## 5. Approval
- VP Operations: approved Moderate and Low treatments and acceptances, 2026-09-04.
- President: approved the Very High and High treatment plans and the budget, 2026-09-04. The President did not accept any High risk; all are being mitigated.
- Next full review: July 2027, or sooner after a major change (for example the OT DMZ cutover), an incident, or publication of the CIRCIA final rule.
