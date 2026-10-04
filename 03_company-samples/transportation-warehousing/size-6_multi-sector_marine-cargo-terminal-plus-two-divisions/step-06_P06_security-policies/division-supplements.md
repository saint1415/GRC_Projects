# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead (for Marine Terminals, with the Division CySO); alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, affiliate separation, vendor access only through the jump host | Board risk committee or Group CISO |
| Group standards | Logging standard, standard OT zone design, affiliate data-sharing standard, Group AI Standard (P10) | Group CISO (data-sharing standard: Group General Counsel) |
| **Division supplement** | Regulator-specific and system-specific standards (for example Subpart F measures per facility, CMMC scope rules, building system rules) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks, Cybersecurity Plans (SSI), work instructions | Division security and compliance lead or CySO |

## 2. Supplement status
| Division | Supplement | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Marine Terminals | MT-S1 v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; update for the final 2026 policies and the Gulf terminals due by 2026-12-30 | Confirm alignment; extend to T7 to T9 |
| Freight Trading | FT-S1 v2025, amended 2026-09 | 2026-09-10 | Aligned, but its CMMC scope rule was too narrow (scenario gap 4); amended to POL-01 4.10 | Re-scope Level 1 (POAM-015) |
| Port Real Estate | RE-S1 v2023 | 2023-05 | **Drifted** (P01 RE-004); conflicts listed in section 4 | Re-issue by 2026-12-31 (POAM-019) |

## 3. What each supplement adds
### 3.1 Marine Terminals supplement MT-S1 (9 facilities under 33 CFR Part 105 and Subpart F)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CySO coverage | One Division CySO for all 9 facilities, listed in each Plan; one alternate per terminal on the 24x7 rota; CySO change notified to the Coast Guard within 96 hours once Plans are approved | POL-01 4.2 | 101.620(b)(3); 101.625(b); 101.630(e)(4) |
| Standard OT zone design | IT, gate and OT zones at every terminal; only the TOS equipment interface crosses into OT; IT-OT connections logged to the SIEM. T7 to T9 must meet it by 2027-06-30 | POL-02 4.10 | 101.650(h)(1)-(2) |
| Remote OT access | No modem or internet-reachable OT; vendor sessions through the jump host only, with a written justification per remotely accessible OT system | POL-02 4.10 | 101.650(e)(3)(v); 101.650(f)(3) |
| VMT and gate sign-in | Longshore operator IDs with TWIC tap plus PIN on VMTs; named badge-tap plus PIN sign-in at gate booths | POL-02 4.1, 4.3 | 101.650(a)(4), (a)(6) |
| HMIs and OT devices | Default passwords changed before commissioning; unused ports blocked; approved firmware list per terminal; badge readers at crane electrical houses | POL-02 4.4; POL-05 3.4 | 101.650(a)(2); 101.650(b)(1); 101.650(i) |
| KEVs | OT KEVs patched or compensating controls documented within 30 days; IT KEVs within 14 days | POL-01 4.12 | 101.625(d)(15); 101.650(e)(3)(i) |
| Longshore training | Training at the hiring halls each year; attendance passed to SYS-G5; untrained workers supervised and recorded on the shift log | POL-05 3.2-3.3 | 101.650(d)(1), (d)(3)-(4) |
| Safe state | Equipment stopped in a safe state when OT integrity is in doubt; restart only on joint operations and engineering approval | POL-03 4.7 | 29 CFR part 1917 |
| Dangerous cargo list | Printed at every shift change at every terminal, kept by the FSO | POL-04 5.6 | 33 CFR Part 105 (FSP) |
| Affiliate neutrality | Freight Trading users see only their own shipments; appointment rules the same for all truckers, with any operational exception documented and offered equally | POL-01 4.7; POL-02 4.2 | 46 U.S.C. 41106(2) |
| Equipment-moving AI | No AI system may sequence or command cranes, ASCs or yard equipment without a safety case and Group AI council approval | POL-01 4.14 | 29 CFR part 1917; P10 |

### 3.2 Freight Trading supplement FT-S1 (DoD contractor; importer)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CMMC Level 1 scope | Every system that processes, stores or transmits FCI is listed in the scope before use, including SYS-F2 shipping documents and scale PCs; annual self-assessment and affirmation before each anniversary | POL-01 4.10 | 32 CFR 170.15; 170.19(b); 170.22 |
| CUI | Decline or quarantine CUI until an approved SP 800-171 environment exists; same-day report of any CUI received | POL-04 5.4 | 252.204-7012(b)(2) |
| DoD reporting | Report to DoD within 72 hours of discovering an incident affecting covered defense information; hold a DoD-approved medium assurance certificate; preserve images for 90 days | POL-03 4.5, 4.8 | 252.204-7012(c)-(e) |
| Covered telecommunications | Yard equipment checked against FAR 52.204-25; report within 1 business day of identification | POL-03 4.5 | 52.204-25(d) |
| Scale PCs | Named sign-in; group patching; group disposal service | POL-02 4.1; POL-04 5.7 | 52.204-21(b)(1)(vi), (vii), (xii) |
| Supplier payments | Bank-detail changes only through the vendor portal with callback; dual approval above $1 million | POL-05 3.6 | P01 FT-004 |
| Terminal data | Traders may not request or use other cargo owners' terminal data; annual attestation by all trading staff | POL-01 4.7 | 46 U.S.C. 41106(2) (terminal's duty) |

### 3.3 Port Real Estate supplement RE-S1 (re-issue due 2026-12-31)
| Topic | Division requirement (to be added) | Group policy it builds on | Driver |
|---|---|---|---|
| Integrator access | All integrator access to building systems through the group jump host; no internet-exposed remote access | POL-02 4.10 | FTC Act Section 5 (N53-R02); Safeguards benchmark 314.4(c)(5) |
| Integrator contracts | Security terms, vulnerability and incident notification, return of controller configurations | POL-01 4.9 | Benchmark 314.4(f) |
| Monitoring | Building system remote access and controller logs onboarded to the SIEM | POL-02 4.10; group logging standard | Benchmark 314.4(c)(8) |
| T3 container freight station | CFS reader maintenance under the T3 FSP vendor rules; changes approved by the T3 FSO | POL-02 4.10 | 33 CFR 105.255; 101.650(i)(1) |
| Closings and wires | Closing instructions confirmed through a known number and the title agent's portal; never on email alone | POL-05 3.6 | P01 RE-003 |
| Tenant personal information | Guarantor files restricted to credit staff; listed in the data inventory and the notification matrix | POL-04 5.1 | State breach laws |

## 4. Port Real Estate drift: conflicts with 2026 group policy
The 2023 Port Real Estate standards were written before the 2025 common control catalog and the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but property staff and integrators follow the document they know, so the conflicts are real risks (P01 RE-004; P07 PL-1 results).

| Topic | Port Real Estate standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Building system remote access | "Integrator remote access as agreed with the property manager" | Jump host only; no internet-exposed access (POL-02 4.10) | 31 sites exposed (P01 RE-001) |
| Vendor contracts | Not addressed | Security and notification terms (POL-01 4.9) | 5 integrator contracts without terms (P03 RE-G14) |
| Monitoring | Integrators monitor their own systems | SIEM onboarding (group logging standard; POL-02 4.10 session recording) | No SOC visibility (gap 5) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Gap 6 (POAM-019) |
| Payment changes | Email confirmation acceptable | Callback and portal (POL-05 3.6) | 2026-03 wire redirection attempt |
| Incident severity | Property incident categories | One group scale (POL-03 4.2) | Building incidents not escalated to the SOC |

**Why the drift happened.** The division's security role sat with property operations until 2025, and the supplement had no owner or review date. **Fix:** the Port Real Estate security and compliance lead now owns RE-S1, the Group CISO's policy office tracks supplement versions, and POL-01 4.5 sets the 90-day and annual rules.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Marine Terminals, Freight Trading) and on re-issue (Port Real Estate).
