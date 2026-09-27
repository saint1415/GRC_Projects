# Incident Response Runbook: Exploited Vulnerability in a Fielded WM-1 Hub

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (medical device startup) |
| Tier / Vertical | Micro / Manufacturing (NAICS 334510) |
| Incident type | A vulnerability in a fielded WM-1 hub (for example the shared maintenance password or the shared API key) is exploited, or credibly exploitable, in a way that could change monitoring or alarms, impersonate hubs, or tamper with the update path |
| Where "fielded" means | **Today:** the 8 evaluation hubs at the partner hospital's simulation center (no patients). **After clearance:** every hub at hospital customers. Steps marked **[after clearance]** apply only once WM-1 is in commercial distribution |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy (product security incidents and CVD) |
| Regulatory basis | FD&C Act 524B(b)(1)-(2) (N31-33-R05); after clearance, 21 CFR 820.35(a), Part 803, Part 806, and FDA's postmarket cybersecurity guidance (December 2016, nonbinding) |
| Runbook owner | Head of Engineering (Product Security Lead); QA/RA Manager for regulatory steps |
| Approved | 2026-08-31 by the CEO |
| Last tested | Tabletop exercise 2026-08-27 with the MSP lead technician and the insurer's panel counsel (section 9) |

This runbook is also the response part of the cybersecurity management plan that section 524B(b)(1) requires in the 510(k) (P03 G-003, G-040).

## 0. Roles and notification chain (Govern)
The company has 7 people. The Head of Engineering runs product incidents; the Operations Manager runs the IT side and the outside calls. The MSP handles laptops, email, and the network; the cyber insurer supplies breach counsel and forensics if company systems are involved.

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Incident commander | Head of Engineering | CEO | Cell phone (printed contact card) |
| Technical lead, hub firmware | Firmware Engineer | Head of Engineering | Cell phone |
| Technical lead, cloud service and update path | Cloud Software Engineer | Head of Engineering | Cell phone |
| IT response (laptops, email, network) | MSP incident line (number in the MSP contract) | MSP lead technician's cell | Phone only |
| Outside calls, incident log, insurer | Operations Manager | CEO | Cell phone |
| Regulatory decisions and FDA | QA/RA Manager | Regulatory consultant | Cell phone |
| Decisions (money, disclosure, advisories, ransom) | CEO | Head of Engineering | Cell phone |
| Cyber insurer | Carrier's 24x7 hotline | Insurance agent | Policy card in the binder |
| Breach counsel and forensics | Insurer panel firms | n/a | Assigned by the insurer on the first call |
| Partner hospital | Simulation center manager and hospital security team | Hospital CISO office | Numbers in the development agreement |
| Contract manufacturer | Program manager | Quality manager | Numbers in the quality agreement |
| External coordination | ISAO (after membership); CISA for coordinated disclosure (voluntary); FBI field office if criminal activity | n/a | Numbers in the binder |

**Notification chain in the first hour:** whoever sees it → Head of Engineering → CEO and Operations Manager (same call) → partner hospital security team (today) or affected hospitals' clinical engineering **[after clearance]** → MSP incident line if any company system may be involved → insurer hotline (Operations Manager) if company systems, data theft, or extortion are involved.

**Out-of-band first.** If the repository, cloud tenant, or email may be compromised, coordinate by phone and text on personal phones.

## 1. Preparation checks (Identify / Protect)
- [ ] Printed binder in the office and at the CEO's and Head of Engineering's homes: this runbook, `notification-matrix.csv`, contact card, advisory template
- [ ] CVD policy and security contact published; acknowledgment within 3 business days (POL-03 4.4). **Gap until POAM-006 closes (2026-10-31)**
- [ ] ISAO membership active. **Gap until POAM-006 closes.** Without it the FDA enforcement-discretion path in section 4 is not available **[after clearance]**
- [ ] Current SBOM for every firmware version in the field (POAM-005)
- [ ] Signing key in an HSM-backed service with two approvers, so a fix can be signed when the Head of Engineering is unavailable (POAM-003). **Until then, only the Head of Engineering can sign**
- [ ] Hub API key can be rotated and a single hub's credential revoked (POAM-004). **Until then, rotation means reflashing every unit**
- [ ] Cloud activity logs kept long enough to investigate. **Today 90 days: export at declaration**
- [ ] Lab units running every firmware version in the field, for reproduction
- [ ] Inventory of fielded units by serial number, firmware version, and site (POAM-005)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | First action |
|---|---|---|
| Hub settings (alarm defaults, network) changed without anyone doing it | Partner hospital or customer report; hub event log | Head of Engineering opens an incident; ask the site to isolate the hub's network segment |
| Researcher or ISAO reports a WM-1 vulnerability, with or without exploit code | Security contact; CVD form; ISAO bulletin | Acknowledge within 3 business days; triage the same day if exploitation is claimed |
| Many hubs authenticating from unexpected networks, or one hub identity used from two places | Cloud ingestion logs | Cloud Software Engineer exports logs and calls the incident commander |
| Hub secret found outside the company (paste site, public repository, CI log) | Monitoring, partner report, staff | Treat as exploitable; rotate (section 5) |
| CISA advisory or KEV entry for a component in the hub SBOM | Vulnerability monitoring (POAM-006) | Match the SBOM; assess exploitability in the WM-1 context |
| Evaluation or returned unit with modified configuration or firmware | Simulation center; lab | Quarantine the unit; chain of custody |

**Declare a product security incident when** exploitation of a WM-1 vulnerability is confirmed or credibly reported, a vulnerability with a working exploit could affect monitoring or alarms, or the update path (update service, signing key, CI pipeline) may have been tampered with.

**Severity:**
- **SEV-1:** exploitation with possible patient harm **[after clearance]**, or any tampering with the update path or signing key.
- **SEV-2:** exploitation of evaluation units, or an uncontrolled risk with no evidence of exploitation.
- **SEV-3:** controlled risk, handled in the regular security maintenance cycle.

**Record these dates in the incident log. Each starts a different clock:**
| Date | Why it matters |
|---|---|
| Date the company **learned of the vulnerability** | FDA postmarket guidance: customer communication within 30 days and fix within 60 days for uncontrolled risk **[after clearance]** |
| Date the company **became aware** of a possibly reportable event | 21 CFR 803.50 (30 calendar days) or 803.53 (5 work days) **[after clearance]** |
| Date a correction was **initiated** | 21 CFR 806.10(b): 10 working days **[after clearance]** |
| Date the company **confirmed** an incident affecting the evaluation units | Partner hospital agreement: 72 hours |
| Date a breach of workforce personal information was **determined** | Fla. Stat. 501.171(4)(a): 30 days |

## 3. First 24 hours (RS.MA, RS.MI)
| Step | Who | Done when |
|---|---|---|
| 1. Open the incident log and a security record in the eQMS (and a complaint record **[after clearance]**); assign severity | Head of Engineering | Records open |
| 2. Export cloud activity, ingestion, and repository audit logs to protected storage; hash the exports | Cloud Software Engineer | Hashes recorded |
| 3. Reproduce on a lab unit with the same firmware version | Firmware Engineer | Reproduced, or reason it cannot be |
| 4. List affected units by serial number, firmware version, and site | Cloud Software Engineer | Affected-unit list |
| 5. Safety assessment: what could an attacker change (alarm limits, displayed values, network settings), and how likely is it? | Head of Engineering with the QA/RA Manager | Initial controlled or uncontrolled call documented |
| 6. Call the partner hospital security team (today) or affected hospitals' clinical engineering **[after clearance]** with interim steps (section 5) | Operations Manager | Calls logged; 72-hour contract clock met |
| 7. If the update path or signing key may be involved, **pause the update service** | Cloud Software Engineer | Update service paused |
| 8. If any company system may be compromised, call the MSP incident line and the insurer hotline | Operations Manager | Claim number; MSP engaged |

## 4. Analysis (RS.AN)
1. **Exploitability and harm.** Rate exploitability (network access needed, physical access, credentials) and the worst patient effect if exploited. Decide **controlled or uncontrolled risk** to safety and essential performance, as FDA's postmarket guidance describes. Record the decision in the design risk management file and the cybersecurity risk assessment.
2. **Scope.** Which firmware versions and sites? Is the cloud service a path in (for example, settings pushed through the update service)? Could the shared API key let an attacker send false data for other hubs?
3. **Evidence of exploitation.** Settings changed outside normal use, unexpected maintenance logins, one hub identity seen from two networks, units returned with changed configuration. Image affected units and keep a chain-of-custody log.
4. **Signing key and pipeline.** Confirm the key was not used outside a recorded release. If misuse is possible, treat as SEV-1 and plan a key rotation with the fix.
5. **Data.** Today no patient data exists. **[after clearance]** If patient data in the cloud service was accessed, the company's business associate duties to hospitals apply (planned HIPAA program; see the notification matrix).

**Regulatory decision points (QA/RA Manager, recorded in the eQMS):**
| Question | If yes | When it applies |
|---|---|---|
| Is the device on the market yet? | If no: no MDR or correction report exists for pre-production units. Record the vulnerability, fix it in the design, and **include it with its risk assessment in the 510(k)** (guidance V.A.2 and V.A.4) | Now |
| Does a report allege the device failed to meet specifications? | Complaint record and investigation (820.35(a)) | After clearance |
| Does information reasonably suggest a death or serious injury, or a malfunction likely to cause one if it recurred? | MDR within 30 calendar days; 5 work days if remedial action is needed to prevent an unreasonable risk of substantial harm (803.50, 803.53) | After clearance |
| Is the risk **controlled**? | Fix in the regular cycle (524B(b)(2)(A)); keep an 806.20 record | After clearance |
| Is the risk **uncontrolled**? | Out-of-cycle fix as soon as possible (524B(b)(2)(B)). Report the correction under 806.10 within 10 working days of initiating it, **unless all four** enforcement-discretion conditions are met: no known serious adverse events or deaths; customers told within 30 days; fix within 60 days; active ISAO member sharing the communication | After clearance |
| Does the fix change the device so much that a new 510(k) is needed? | Regulatory assessment before release; a new 510(k) is also subject to 524B (21 CFR 807.81(a)(3)) | After clearance |

## 5. Containment and eradication (RS.MI)
**Interim compensating controls (sites apply them; the company writes them):**
1. Put the hubs on a network segment reachable only from clinical engineering; block the maintenance port from other networks.
2. Where available, push a configuration that disables the maintenance page on affected hubs (done on the 8 evaluation hubs on 2026-08-14).
3. **[after clearance]** Increase clinical checks of alarm limits on affected units until the fix is installed.

**Company-side containment:**
1. Rotate the hub API key in the affected environment; until per-device certificates exist this means reflashing every affected unit (POAM-004).
2. Block attacker sources at the cloud ingestion endpoint; disable any cloud account that may be compromised; switch daily work off the shared owner account.
3. If the update path was involved, keep the update service paused and plan a signing key rotation before any release.

**Eradication:**
1. Fix the flaw; verify with regression tests and a security test by someone who did not write the fix.
2. Sign through the release process (today the Head of Engineering alone; two approvers once POAM-003 closes).
3. Release in stages: lab units, then one site, then all sites. Confirm each unit's new version through the cloud service.

## 6. Reporting and communication (RS.CO)
**Follow `notification-matrix.csv`.** The QA/RA Manager confirms regulatory notices; breach counsel reviews any notice about personal information.

| When | Action | Owner |
|---|---|---|
| Day 0 | Log the dates in section 2; insurer hotline if company systems, data theft, or extortion are involved | Head of Engineering; Operations Manager |
| Day 0-3 | Acknowledge the reporter (CVD) and agree a disclosure timeline | Head of Engineering |
| Within 72 hours of confirmation | Partner hospital notice with interim steps (contract) | Operations Manager |
| Before submission | Add the vulnerability, its risk assessment, and the fix to the 510(k) cybersecurity documentation | QA/RA Manager |
| Within 5 work days / 30 days **[after clearance]** | MDR decision and report if reportable (803.53, 803.50) | QA/RA Manager |
| Within 30 days of learning of an uncontrolled risk **[after clearance]** | Customer advisory with compensating controls and the fix plan; copy to the ISAO | CEO approves; Operations Manager sends |
| Within 10 working days of initiating a correction **[after clearance]** | 806.10 report, unless all enforcement-discretion conditions are met (then the 806.20 record) | QA/RA Manager |
| Within 60 days of learning of an uncontrolled risk **[after clearance]** | Validated fix distributed; follow up with sites that have not installed it | Head of Engineering |
| Agreed disclosure date | Public advisory crediting the reporter; optionally coordinated through CISA | Head of Engineering |

**Plan to the shortest clock.** Today the shortest clock is the partner hospital's 72 hours. After clearance it will usually be the 5-work-day MDR decision, then the 30-day customer advisory.

**No ransom or extortion payment** without the CEO, counsel, the insurer, and an OFAC sanctions check (POL-03 4.9).

## 7. Recovery (RC.RP, RC.CO)
Restore in BIA priority order (P05):
1. **Signing key and release tooling (BP-01):** confirm the key is intact and uncompromised; if not, restore from the safe copy onto a clean laptop and plan a re-key.
2. **Identity and email (SYS-03):** MSP restores access if affected.
3. **eQMS (BP-02) and submission work (BP-03):** records current; the incident is recorded as a design input for the threat model.
4. **Repository and CI (BP-04):** secrets rotated; build logs clean.
5. **Cloud service and update service (BP-05):** redeploy from the repository, restore the newest clean snapshot, resume the update service only after the fix is signed.
6. **Evaluation units:** reflash with the fixed firmware; confirm versions.

**Close the incident** when the fix is on every affected unit, no new indicators appear for 14 days, and compensating controls are withdrawn only after the fix is installed. Tell the partner hospital (and customers **[after clearance]**) when it is closed.

## 8. Post-incident (ID.IM)
- Lessons-learned meeting within 14 days of closure; written summary within 30 days (POL-03 4.12). Open a CAPA in the eQMS.
- Update the threat model, cybersecurity risk assessment, SBOM, and design risk management file.
- Update the risk register (P01, especially R-001, R-002, R-005, R-010, R-021, R-023), the POA&M (P07), and this runbook.
- Record time from identification to fix and from fix to installation on every unit (P03 G-031 metrics).
- Keep incident and CVD records as POL-02 A.7 requires.

## 9. Tabletop exercise, 2026-08-27
**Participants:** CEO, Head of Engineering, Firmware Engineer, Cloud Software Engineer, QA/RA Manager, Operations Manager, the MSP lead technician, and the insurer's panel counsel (by video). Facilitated by the independent P07 assessor.

**Scenario (set in 2027, after clearance):** a hospital's clinical engineering team reports that alarm limits on 3 hubs were lowered overnight. A researcher's blog post the same week shows how to log in to the WM-1 maintenance page with the shared default password.

**What worked:** the team declared SEV-1 within the first discussion round; the QA/RA Manager separated the MDR decision from the correction decision; the compensating controls (segment and disable the maintenance page) were clear.

**What failed:**
1. Only the Head of Engineering could sign the fix. When the facilitator made that person unavailable, no fix could be released (POAM-003).
2. Rotating the shared API key meant reflashing every hub in the field, which nobody had planned (POAM-004).
3. Nobody knew which hubs ran which firmware version (POAM-005).
4. The MSP assumed it had no role; counsel noted the cyber policy covers company systems, not incidents at customer sites, so the product liability carrier must also be notified.
5. Without ISAO membership, the enforcement-discretion path was not available, so an 806.10 report would have been needed (POAM-006).

**Actions:** add the product liability carrier to the contact list (done 2026-08-28); the other four are already in the POA&M. Next tabletop before commercial distribution.
