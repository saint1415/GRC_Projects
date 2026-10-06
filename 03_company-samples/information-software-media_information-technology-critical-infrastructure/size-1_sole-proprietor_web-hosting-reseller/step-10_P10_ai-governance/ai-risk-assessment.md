# AI Use Assessment: AI Alert Triage in the Website Security Service (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (web hosting reseller) |
| Tier / Vertical | Sole Proprietorship / Information Technology |
| AI use case | AI-001: the AI alert triage feature in the website security service (SYS-05). The vendor turned it on for the owner's plan on 2026-05-04, and the owner left it on. Registry default "AI-driven security operations (alert triage)", adapted to the one third-party tool the owner actually uses. AI-002 (consumer chat assistant) is in section 7 |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form; NIST AI 600-1 for the generated explanations |
| Assessor / date | Owner, 2026-09-10, using the P07 sample of 50 dismissed findings (2026-08-19) |
| Decision | Approved with conditions by the owner, 2026-09-28 (section 6) |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** the owner, who controls every setting in the security service.
- **Policies:** POL-01 9.4 (AI tools and AI features that dismiss findings), 7.7 (weekly review of protected categories), 6.3 (vendor review), 8.2 (where Restricted data may be). POL-02 to POL-05 are pointers to POL-01 at this tier.
- **Approval:** the owner approves every AI feature that touches customer data, after a written assessment like this one. A feature a vendor turns on by default counts as a new tool (POL-01 4.3).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Cut the daily scan noise for one person. The feature scores each finding, writes a short explanation, and **auto-dismisses** findings it rates as false positives or low risk |
| Users / operators | The owner only |
| Affected people | About 150 customers, and the shoppers, tenants, and clients whose data sits on their sites. A missed compromise is the harm |
| Data | Inputs: site files and file changes on all 270 sites, scan findings, visitor IP addresses, site user names. Outputs: scores, explanations, dismissals. **Unknown:** where the vendor stores this data, and whether its terms let it train models on customer site files (P03 G-039) |
| Build or buy | Configure: a vendor feature. The owner cannot see or retrain the model, but can turn off auto-dismiss, by category where the vendor allows |
| Volume | July 2026: 412 findings, **239 (58%) auto-dismissed** with no human review |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules (IT sector) | None identified | The vertical profile lists no AI-specific rule |
| FTC Act Section 5 (15 U.S.C. 45) | **Yes** | The website claims "enterprise-grade malware protection on every site" (deception, P03 G-038). Unreviewed dismissals also weaken reasonable security (unfairness, 45(n)) |
| Fla. Stat. 501.171(2), (6)(a) | **Yes** | Reasonable measures. A compromise the AI hides delays the breach determination, and with it the 10-day notice to the customer. Counsel to advise whether a dismissed alert can count as "reason to believe" |
| State AI laws (for example Colorado SB26-189, Texas HB 149) | No | No duty is triggered: the tool makes no consequential decision about a person, is not used in any consumer interaction, and does none of the practices Texas HB 149 prohibits |

## 3. Risk tier
**Tier: High, as configured today**, under the repository rubric. The rubric's High tier includes AI that "can affect ... critical infrastructure operations". Here the AI alone decides which security findings no person will ever see, for the hosting service of about 150 businesses in an IT-sector company. One such decision hid a web shell for 15 days (2026-07-21 to 2026-08-05). **Path to Medium:** once a person reviews every protected-category finding before it is closed, the AI ranks findings but no longer makes the final call. Re-tier after 8 consecutive weeks with no protected-category miss and under 1% real findings among sampled dismissals.

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Random sample of 50 dismissed findings (P07). Target: under 1% real, none in protected categories | 1 of 50 (2%) real: the web shell. 1 new administrator user needed a check with the customer and was legitimate | **No** |
| Valid and reliable (generated explanations) | 20 explanations checked against the raw finding. Target: none wrong about what changed | 2 of 20 called a changed executable file a "routine plugin update". This is confabulation, a risk named in AI 600-1 | **No** |
| Safe | No auto-dismiss for new administrator users or changed executable files | Auto-dismiss applies to all categories | **No** |
| Secure and resilient | Security service account protected by MFA; only the owner can change AI settings | MFA on (P07); owner is the only user | Yes |
| Accountable and transparent | Feature approved before use; claims to customers accurate | Turned on by the vendor with no review; website overstates protection | **No** (improving) |
| Explainable and interpretable | Each dismissal shows a score and reason, and the raw finding can be opened | Yes for single findings; no bulk view of dismissals | Partial |
| Privacy-enhanced | Customer site files used only to provide the service; U.S. storage | Vendor terms unclear on training use; data location unconfirmed | **No** |
| Fair, with harmful bias managed | See plan below | Miss fell on a hosting-only site | Flagged |

**Bias and fairness testing plan.** The tool makes no decision about a person, so "fairness" here means **equal protection for every customer**. A tool that misses more on one group of sites leaves that group's shoppers and clients less protected.
- **Groups compared:** hosting-only sites versus care-plan sites; the 12 online stores versus all other sites.
- **Metric:** the share of sampled dismissed findings that were real, per group.
- **Threshold:** flag if any group's share is more than 1 percentage point above the comparison group's, or if any protected-category finding is missed in any group.
- **Result (August sample):** hosting-only 1 of 31 (3.2%); care-plan 0 of 19 (0%). **Flagged.** A miss on a hosting-only site also lasts longer, because nobody else looks at those sites (P01 R-004).
- **Fix:** each monthly sample of 50 is split 25 hosting-only and 25 care-plan, with every store dismissal in the period added.

## 5. MANAGE
- **Human-in-the-loop:** findings in the protected categories (new administrator users, changed executable files) are never closed without the owner's review (POL-01 7.7, 9.4). If the vendor cannot do this by category, auto-dismiss is turned off entirely and the score is used only to sort the queue. About 13 findings a day (412 in July) is a workload one person can handle.
- **Monitoring:** Monday review of protected-category findings; monthly sample of 50 dismissals logged in the security log; any vendor change to the feature triggers a re-assessment.
- **Incident handling:** a real finding discovered after dismissal is logged as an incident with its discovery time (POL-01 10.2) and handled under P08. The breach determination date is written down (POL-01 10.3).
- **Decommissioning:** turn off AI triage if a protected-category finding is auto-dismissed after the conditions are in place, if the vendor's terms allow training on customer site files with no opt-out, or if the weekly review is missed for three weeks in a row. The underlying scans stay on.

## 6. Decision: approve with conditions (owner, 2026-09-28)
1. By 2026-10-15: no auto-dismiss in the protected categories, and human review before closing (POAM-009).
2. From 2026-10-05: weekly review on Mondays, together with the log review (POAM-007).
3. By 2026-11-30: first stratified monthly sample of 50 (POAM-009).
4. By 2026-10-15: replace the website claim with an accurate description of daily scanning and of what each plan includes (P03 G-038).
5. By 2026-12-31: written vendor answers on data location and training use of site files (POAM-006). If training cannot be turned off, decommission.

## 7. AI-002: consumer AI chat assistant (SYS-09)
The owner pasted server log excerpts with shopper emails and IP addresses, suspicious files, and one configuration file with a database password into a free consumer chat account. The consumer terms allow use of inputs to improve the service. **Decision: stop.** No customer data, logs, site files, or credentials go into it (POL-01 9.4). The exposed database password is rotated, and laptop copies are deleted, by 2026-09-30 (P01 R-011). A business-tier tool with no-training terms may be assessed later, and redacted excerpts with no customer identifiers are the only permitted input even then.
