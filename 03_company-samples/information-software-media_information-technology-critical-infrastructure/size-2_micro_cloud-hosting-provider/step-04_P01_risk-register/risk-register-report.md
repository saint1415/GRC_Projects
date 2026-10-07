# Risk Register Report: Cris Santos Company | Information Technology | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (managed cloud hosting provider) |
| Size tier | Micro (7 employees) |
| Vertical | Information Technology |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also satisfies | The risk assessment both bank contracts expect under the Interagency Guidelines, III.B (identify threats, assess likelihood and damage, assess sufficiency of controls) |
| Prepared | 2026-07-31 by the Lead Systems Engineer (Information Security Lead) with the Operations Manager |
| Updated | 2026-08-19 (R-024 added from P07 testing; R-007 updated); 2026-08-28 (R-013 updated from P10); 2026-09-15 (R-010, R-022, R-023 closed by acceptance) |
| Approved | 2026-09-15 by the Owner |

## 1. Scope and risk framing
**Scope.** The whole business and its key vendors: every system in `../00_company-facts.md` section 3 (SYS-01 to SYS-11), the DC-1 racks, and the vendors that hold or reach customer data: the colocation, public cloud, RMM, PSA, DNS, identity, and MDR providers. Customer VMs and customer servers are not company assets, but the company's tools reach them, so harm to them is counted as impact on the company.

**Risk tolerance and who can accept risk:**
- Very Low and Low: the Information Security Lead (Lead Systems Engineer) may accept.
- Moderate: only the Owner may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The Owner approves a dated treatment plan instead. A risk that can reach every customer at once is never accepted at High or above.

This is the company's first documented risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the cloud mapping (P04), CISA advisories on attacks against managed service providers, and interviews with all 7 staff (2026-07-20 to 2026-07-31).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories. For a company with about $3,000 of revenue a day, an event that reaches every customer at once, or a bank's covered services, is rated Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 4 |
| Moderate | 16 |
| Low | 4 |
| **Total** | **25** |

Status: 16 Open, 6 In progress, 3 Closed (R-010, R-022, and R-023 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Shared RMM account used to push a malicious script to 310 customer servers | Very High | Remove shared accounts (2026-10-15); sign-in restriction; two-person script approval; RMM logs to the MDR | Lead Systems Engineer | 2026-11-30 |
| R-002 | Attacker deletes customer VMs and every backup | High | Separate backup account with object lock; break-glass user; restore tests | Lead Systems Engineer | 2026-12-31 |
| R-003 | Shared hypervisor administrator account used to take over the cluster | High | Named accounts with MFA; BMC jump host; rotate BMC passwords | Lead Systems Engineer | 2026-12-31 |
| R-004 | Portal compromise exposes a full-administrator service credential | High | Least-privilege service account; secret in the cloud secrets service; 7-day critical updates | Systems Engineer | 2026-11-30 |
| R-009 | Hurricane or site failure takes DC-1 offline for days | High | Degraded-mode recovery into the cloud tenant, tested before the 2027 season | Owner | 2027-05-31 |
| R-014 | Banks not notified after a 4-hour disruption | Moderate | Verified bank contacts; determination step in P08; tabletop | Operations Manager | 2026-10-31 |

**The common theme is concentration.** A few credentials and tools reach everything: the RMM tool reaches 310 customer servers (R-001), one hypervisor account reaches 260 VMs (R-003), the portal's service account reaches the same VMs from the internet (R-004), and one cloud account holds both the portal and the off-site backups (R-002). At 7 people the company cannot add many people, so the treatments remove shared accounts, split accounts, and add a second approval where one mistake or one stolen password would reach every customer.

**Risks found or changed during the work:**
- R-007: the former Support Engineer's VPN account was disabled on 2026-07-22, the day it was found. VPN logs (90 days, back to late April) showed no sign-in after he left; RMM logs only cover 30 days, so use of the shared RMM account before late June cannot be ruled out. The shared RMM password was rotated on 2026-07-23. P07 then found him still on the colocation access list; he was removed on 2026-08-18.
- R-024: added on 2026-08-19 after P07 testing found the backup appliance still using the vendor's default administrator password. The password was changed the next day.
- R-013: updated on 2026-08-28 with the P10 test results on the MDR's AI triage.

## 4. Treatment summary
- **Funded (2026 Q4 and 2027 Q1, approved by the Owner; about $8,700 one-time and $7,800 a year):**
  - Hardware security keys for all 7 staff, with spares: about $700 one-time
  - MDR add-on to ingest RMM, cloud, and hypervisor manager logs, with 12-month retention: about $3,600 a year
  - Vulnerability scanning service: about $2,400 a year
  - Separate backup account with object lock: about $1,200 a year
  - Business password manager tier with per-person access and audit: about $600 a year
  - Independent control assessment (P07) and policy work in 2026: about $6,000 one-time
  - Degraded-mode recovery test in the cloud tenant: about $2,000 one-time (cloud resources and outside help)
- **Engineer time:** about 120 hours across Q4 for account clean-up, the portal service account, the change log, and the contingency plan. The Owner moved two customer onboarding projects to Q1 2027 to free it.
- **Accepted:** R-010 (Low; facility redundancy evidenced in the colocation SOC 2 report), R-022 (Low; working abuse process), R-023 (Low; laptops encrypted).
- **Contract actions:** incident notice terms in the RMM contract (R-001, R-019) and a telemetry-use limit in the MDR contract (R-013), both at renewal by 2026-12-31; bank-designated contacts from both banks (R-014) by 2026-10-31.

## 5. Approval
- Owner: approved all treatment plans, the three acceptances, and the budget on 2026-09-15.
- Next full review: July 2027, or sooner after a major change (for example a second site, a new bank customer, or a new RMM vendor) or an incident.
