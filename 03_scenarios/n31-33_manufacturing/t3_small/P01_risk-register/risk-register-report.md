# Risk Register Report: Cris Santos Company | Manufacturing | Small

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (connected medical device manufacturer) |
| Size tier | Small (250 employees) |
| Vertical | Manufacturing (NAICS 334510) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | HIPAA risk analysis for the device cloud, 45 CFR 164.308(a)(1)(ii)(A); security risk management expected for cyber devices under FD&C Act section 524B(b)(2) |
| Prepared | 2026-07-24 by the IT Manager with the Product Security Lead |
| Approved | 2026-09-04 by the COO (Moderate and below) and the CEO (High) |

## 1. Scope and risk framing
**Scope.** The whole organization, tied to its key systems and products (`../scenario-facts.md` section 3):
- the device cloud (SSP system, P02) and the PHI it holds for 40 hospitals;
- the fielded PM-2 and PM-1 monitors and the build and code-signing pipeline that produces their firmware;
- the MES and test stations on the factory floor;
- the business processes in the BIA (P05).

Two kinds of harm are rated together. **Enterprise harm** covers data, operations, revenue, and regulatory standing. **Patient harm** comes from a device or device cloud that is compromised. Impact ratings use the BIA categories, and patient safety drives the Very High ratings.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the IT Manager may accept.
- Moderate: the COO may accept, with a treatment plan or a documented reason.
- High and Very High: only the CEO may accept, and only temporarily with a dated treatment plan. A patient-safety risk rated High is never accepted without remediation.

Product security risks are also carried in the design risk management file for each device, as the QMSR requires (21 CFR 820.10(c)). This register is the enterprise view of the same risks.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the P03 gap analysis, the BIA, the PM-2 threat model, and interviews with Engineering, Manufacturing, Quality, and Cloud Operations.
2. **Rate likelihood.** Each risk has a likelihood of initiation (adversarial) or occurrence (non-adversarial) and a likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05).
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 5 |
| Moderate | 21 |
| Low | 6 |
| **Total** | **32** |

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-032 | Same service password on every PM-2 unit lets an attacker change settings | High | Out-of-cycle firmware with unique credentials; customer advisory within 30 days | VP Engineering | 2026-10-11 |
| R-002 | Code-signing key stolen from the build server and used to sign malicious firmware | High | HSM or non-exportable cloud keys; two-person signing; key rotation | VP Engineering | 2026-12-31 |
| R-001 | Exploited vulnerability in fielded PM-2 monitors | High | CVD policy; regular patch cycle; updated threat model; device penetration test | VP Engineering | 2027-01-31 |
| R-005 | Ransomware spreads from the office into Line 2 MES and stops production | High | Segment Line 2; named operator accounts; offline MES backups | Director of Manufacturing Operations | 2026-12-31 |
| R-010 | FDA refuses or delays the AI-001 submission because 524B elements are missing | High | Close the P03 524B roadmap; pre-submission meeting | VP QA/RA | 2027-06-30 |
| R-008 | Support account misuse exfiltrates PHI across all tenants | Moderate | Just-in-time access; quarterly reviews; bulk-query alerts | Cloud Operations Lead | 2026-11-30 |
| R-009 | Log analytics vendor holds PHI without a BAA | Moderate | Mask identifiers; subcontractor BAA | Compliance Manager (Privacy Officer) | 2026-10-31 |

The High risks share one theme: **the company cannot yet show that its fielded devices stay cybersecure after release.** Four of the five come from gaps that section 524B addresses directly: no CVD process, no regular patch cycle, weak protection of the code-signing key, and an out-of-date SBOM. Fixing them also lowers eight Moderate risks (R-003, R-004, R-012, R-013, R-014, R-015, R-024, R-025). R-005 is the one High risk outside the product. It comes from the flat Line 2 network and shared MES logins.

R-032 was added on 2026-08-12, after P07 lab testing found that every PM-2 unit accepts the same service password. The VP QA/RA is treating it as a potential uncontrolled risk under FDA's postmarket cybersecurity guidance (December 2016). The response follows the P08 runbook, including the 21 CFR 806 reporting decision.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 H1 budget, $310,000):**
  - HSM or cloud key management for code signing, and a key ceremony ($45,000)
  - Automated SBOM generation and vulnerability monitoring for device and cloud builds ($38,000 per year)
  - Line 2 OT segmentation and badge-plus-PIN MES login ($62,000)
  - Independent penetration tests of the device cloud and PM-2 ($70,000)
  - SOC 2 Type 2 audit for the device cloud ($55,000)
  - Just-in-time production access and centralized log review ($40,000 per year)
- **Accepted:**
  - R-026: Low; monitors buffer 72 hours of data and resend after an outage
  - R-030: Low; full-disk encryption and remote wipe
- **Contract and policy actions:**
  - Subcontractor BAA or replacement for the log analytics vendor (R-009), due 2026-10-31
  - Published CVD policy and ISAO membership (R-003), due 2026-10-31
  - Approved AI tools list (R-028), due 2026-11-30

## 5. Approval
- COO: approved the Moderate and Low treatments and the two acceptances, 2026-09-04.
- CEO: approved the High-risk treatment plans and the budget, 2026-09-04.
- Next full review: July 2027, or sooner after a new marketing submission, a major change, or an incident.
