# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or regulator-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO and, for OT content, the Group OT Security Director |
| Status date | 2026-09-17 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA everywhere, no shared accounts, safe state first, one severity scale, no AI writes to control systems without approval | Board risk committee or Group CISO |
| Group standards | OT security standard (zones, conduits, gateway, monitoring), logging standard, cloud guardrails, Group AI Standard (P10) | Group CISO; Group OT Security Director |
| **Division supplement** | Regulator- and site-specific requirements: RMP and PSM integration, the Terminal T1 Cybersecurity Plan, carrier security plan and ELD rules | Division president, after Group CISO alignment review |
| Facility plans | Plant RMP programs, the Terminal T1 Facility Security Plan and Cybersecurity Plan, hazmat security plans | Facility regulator-facing roles (POL-01 4.14) |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Specialty Chemicals | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Add the AI write rule (POL-01 4.12) explicitly; confirm alignment |
| Distribution | v2026 | 2026-05-15 | Aligned; the Terminal T1 Cybersecurity Plan annex is not written yet (scenario gap 4) | Annex with the Plan (POAM-013, 2027-05-31) |
| Hazmat Transport | v2023 | 2023-04 | **Drifted** (scenario gap 10); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-018) |

## 3. What each supplement adds
### 3.1 Specialty Chemicals supplement (16 plants; RMP Program 3 at Plant C1, Program 2 at 4 plants)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Cyber in process safety | Every PHA and hazard review includes control system compromise as a cause; credited safeguards are checked for common failure with the DCS | POL-01 4.13 | 40 CFR 68.67(c)(4); 68.50 |
| MOC coverage | DCS and SIS logic, alarm limits outside the operating envelope, recipes pushed from the hub, new conduits, and AI operating modes all require plant MOC with an OT security reviewer | POL-01 4.13 | 40 CFR 68.75 |
| Recipe staging | Recipes from SYS-C8 land in an OT DMZ staging share; the plant releases them after MOC screening and two-person verification | POL-01 4.13 | 40 CFR 68.75; 68.65(b)(7) |
| Remote engineering | Each remote session to a plant needs the shift superintendent's approval; remote engineering work counts as contractor work under the safe work practices | POL-02 4.6 | 40 CFR 68.69(d); 68.87(b)(4) |
| SIS protection | SIS keyswitch position shown on the OT monitoring console; two-person verification for program changes; checksum at every proof test | POL-02 4.9 | 40 CFR 68.65(d)(1)(viii); 68.73 |
| Inventory limits | Hydrogen peroxide bought below 52%; flammable liquids under 10,000 lb per process location at Plant C1 | POL-01 4.13 | 29 CFR 1910.119 Appendix A; 40 CFR 68.10(l)(2) |
| Release notification | Notification works without the business network; annual notification exercise run with the network simulated down | POL-03 4.4 | 40 CFR 68.90(b)(3); 68.95(a)(1)(i); 68.96(a) |
| Restart after a cyber restore | Pre-startup safety review and MOC record before restart | POL-03 4.10 | 40 CFR 68.77 |
| Legacy plants | Until migrated (due 2027-12-31): no always-on remote tools, second network cards removed, offline backups kept | POL-02 4.6 | RBPS 8 (voluntary) |

### 3.2 Distribution supplement (64 branches, 3 bulk terminals, the managed inventory service; Terminal T1 under 33 CFR Part 105)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Terminal T1 Cybersecurity Plan | Written Plan in the 14-section format, submitted to the Captain of the Port by 2027-05-31 (rule deadline 2027-07-16) | POL-01 4.14 | 33 CFR 101.630; 101.655 |
| Contractor training gate | No OT access for contractor personnel until trained; untrained personnel accompanied or monitored; new personnel within 5 days of access | POL-05 4.2 | 33 CFR 101.650(d)(3)-(4) |
| Approved list and inventory | Only hardware, firmware, and software on the Terminal T1 approved list may be installed; inventory marks critical IT and OT systems | POL-02; POL-04 4.1 | 33 CFR 101.650(b)(1), (b)(3) |
| Segmentation | Loading rack and tank gauging PLCs behind the terminal OT firewall; all IT-OT connections logged and monitored | POL-02 | 33 CFR 101.650(h) |
| KEVs | Known exploited vulnerabilities in critical terminal systems patched or compensated within 7 days, documented | POL-01 4.3 | 33 CFR 101.650(e)(3)(i) |
| Coast Guard reporting | Actual or threatened cyber incidents reported immediately to the FBI, CISA, and the Captain of the Port; NRC as fallback | POL-03 4.5 | 33 CFR 6.16-1; 101.620(b)(7) |
| Drills | Two cyber drills each calendar year; annual exercise with the CySO taking part | POL-03 4.9 | 33 CFR 101.635 |
| Managed inventory service | MFA on every vendor portal that can change customer gateways; two approvers for gateway firmware; daily reconciliation for utility sites | POL-02 4.3; POL-01 4.8 | SOC 2 commitments (P09) |
| Offeror security plan | Cyber threats to shipping data, rack automation, and the managed inventory order path included in the risk assessment | POL-01 4.3 | 49 CFR 172.802(a) |

### 3.3 Hazmat Transport supplement (motor carrier; about 1,900 tractors and 2,700 drivers)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Carrier security plan | Risk assessment includes cyber threats to dispatch, electronic shipping papers, telematics, and ELDs; fleet technology roles get security duties | POL-01 4.3 | 49 CFR 172.802(a), (a)(3), (b)(2) |
| Dispatch changes | Consignee and route changes for security plan loads need two-person approval and alert the security desk | POL-02 4.2 | 49 CFR 172.802(a)(3) |
| ELD accounts | Unique ELD username for every user, including support personnel; no shared accounts | POL-02 4.1 | 49 CFR 395.22(b)(2)(ii) |
| ELD outage | Fleet-wide outage procedure: paper logs per 395.34(a), stock at every terminal, extension request process | POL-03 | 49 CFR 395.34 |
| Driver records | Drug and alcohol testing results visible only to the safety team and each terminal's own drivers' managers | POL-04 | 49 CFR 382.405 |
| Driver camera AI | AI event scores may not be the sole basis for discipline; a trained reviewer watches the video and documents the decision; drivers get notice of AI use | POL-01 4.12 | State AI employment laws (P10) |
| DOT incident reports | NRC phone report within 12 hours; Form 5800.1 within 30 days | POL-03 4.5 | 49 CFR 171.15; 171.16 |

## 4. Hazmat Transport drift: conflicts with 2026 group policy
The 2023 Hazmat Transport standards were written before the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but drivers, dispatchers, and terminal staff follow the document they know, so the conflicts are real risks (P01 HT-009; P07 PL-01 statements other than satisfied).

| Topic | Hazmat Transport standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Shared accounts | Shared ELD support and terminal front-office accounts allowed | No shared accounts (POL-02 4.1) | Shared ELD accounts at 6 terminals (HT-003; POAM-016) |
| MFA | MFA for email only | MFA for all SYS-G1 applications and remote access (POL-02 4.3) | TMS dispatch accounts at 4 terminals without MFA until 2026-03 |
| Incident severity | Carrier 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation of telematics outages |
| Termination | End of next business day | Within 4 hours (POL-02 4.5) | Longer exposure window for dispatch access |
| AI use | Not addressed | AI inventory and approval (POL-01 4.12) | Driver camera AI scores used in discipline without review (HT-006) |
| Security plan scope | Physical threats only | Risk analysis covers cyber (POL-01 4.3) | Gap 5 (P03 HT-G02) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 7 (POAM-017) |

**Why the drift happened.** The 2023 supplement was owned by the carrier's previous safety director and had no review date after the role changed. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Specialty Chemicals, Distribution) and on re-issue (Hazmat Transport).
