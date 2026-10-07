# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-16 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, no BAA no PHI, vendor access through PAM | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, records schedule, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-, county-, client-, and system-specific standards (for example, state EMS records, manual dispatch, client notices, recording consent, card data) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks, center binders, and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Ambulance Services | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Add vehicle device rules from POL-02 4.10 |
| Urgent Care | v2024 | 2024-02 | **Drifted** (scenario gap 8); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-015) |
| Billing and Dispatch Services | v2025 | 2025-10 | Aligned, but missing the AI mode-change gate in POL-01 4.12 and the client data check in POL-01 4.8 | Add both by 2026-10-31 (POAM-017) |

## 3. What each supplement adds
### 3.1 Ambulance Services supplement (covered entity; Medicare ambulance supplier; state EMS licensee)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Vehicle devices | Every router, MDC, tablet, and cardiac monitor in the group inventory with firmware version; no remote administration on the cellular interface; no default passwords | POL-02 4.10 | 164.308(a)(5)(ii)(D); 164.310(d) |
| Crew sign-in | Crew members sign in to the MDC with their own identity once named sign-in is live; until then, the vehicle assignment log records who staffed each unit each shift | POL-02 4.1 | 164.312(a)(2)(i) |
| Fleet changes | Fleet configuration pushes go through the group change board with a pilot group of vehicles | POL-01 4.6 | 164.308(a)(1)(ii)(B) |
| State EMS records | Patient care record available to the receiving hospital on request within the state's deadline (Florida worked example: 48 hours, Rule 64J-1.014, F.A.C.); retention per the group records schedule | POL-04 4.8 | State EMS rules; Fla. Stat. 401.30 |
| Release of records | All law enforcement and third-party requests go to the Ambulance Privacy Office; stations do not release records | POL-04 4.3 | HIPAA Privacy Rule 164.512(f); Fla. Stat. 401.30(4) (worked example) |
| Medicare documentation | Physician certification statements attached to the billing record before claim release and kept 7 years | POL-04 4.8 | 42 CFR 410.40(e); 424.516(f) |
| County notices | The county notice register (P08) lists each agreement's outage and written report terms | POL-03 4.6 | County ambulance agreements |
| Dispatch protocol settings | Protocol table changes in the CAD require the chief medical officer's approval in the change record | POL-01 4.12 | 164.312(c)(1) |

### 3.2 Urgent Care supplement (covered entity)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Acquired clinics | Until migration, legacy system logs forwarded to the SIEM, unique accounts, weekly access review, and MFA through a proxy | POL-02 4.1, 4.3 | 164.308(a)(1)(ii)(D); 164.312(b), (d) |
| Clinical downtime | Downtime workstations at every clinic; quarterly drill in each state region | POL-03 | 164.308(a)(7)(ii)(C)-(D) |
| AI scribe | Consent captured in a required field before recording; provider attestation on every AI-assisted note | POL-05 4.9 | State recording laws (Fla. Stat. 934.03(2)(d) worked example) |
| Decision support | Every patient care decision support tool inventoried; inputs reviewed; mitigation documented | POL-01 4.12 | 45 CFR 92.210 |
| Records requests | Phone requests routed to the central release-of-information team | POL-05 4.1 | 164.514(h) |

### 3.3 Billing and Dispatch Services supplement (business associate; SOC 2 service organization; PCI DSS)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Manual dispatch | Center binders with incident cards, status boards, county and client call trees; drill each quarter at each center, one multi-day scenario each year | POL-03 4.3 | 164.308(a)(7)(ii)(C)-(D); client contracts |
| Client notices | Notice register by client (dispatch: 15-minute phone call and 24-hour written report; billing: 72 hours for 31 clients, 10 calendar days standard) | POL-03 4.6 | 164.410; 164.314(a)(2)(i)(C); client contracts |
| Client data and AI | No client call audio to the AI triage module until that client consents and the CAD vendor BAA covers it | POL-01 4.8, 4.12 | 164.308(b)(2); 164.502(a)(3) |
| Interfaces | Every county and client interface in the register with a permitted-field list; any law enforcement data handled under POL-01 4.13 | POL-04 4.4 | CJIS Security Policy (if CJI); 164.308(b)(1) |
| Call recording | Recording on dispatch lines as state law allows; counsel confirms which lines and centers each state's rule covers (Florida worked example: Fla. Stat. 934.03(2)(g) names employees of licensed ambulance services and other entities with published emergency numbers); recorded announcement on request lines | POL-05 4.9 | State recording laws |
| Card data | Tone-masked keypad entry; monthly check of recordings for card numbers until then; vendor PCI DSS attestation on file | POL-04 4.5 | PCI DSS v4.0.1 |
| Offboarding | Return or destroy client PHI with a certificate within 60 days of termination | POL-04 4.7 | 164.504(e)(2)(ii)(J) |

## 4. Urgent Care drift: conflicts with 2026 group policy
The 2024 Urgent Care standards were written before the 2026 group policies and before the 2025 acquisition. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 UC-008; P07 PL-01 finding).

| Topic | Urgent Care standard (2024) | Group policy (2026) | Effect |
|---|---|---|---|
| Acquired systems | Not addressed | Unique accounts, MFA, and logging for every system with ePHI (POL-02 4.1, 4.3) | Legacy system runs on shared logins (UC-001) |
| Termination | Clinic manager removes access within 5 business days | Within 4 hours (POL-02 4.5) | Longer exposure window at acquired clinics |
| Incident severity | Urgent Care 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation |
| AI use | Not addressed | AI inventory and approval (POL-01 4.12) | Scribe consent field optional (UC-004) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Acquired clinics not in the 2025 inheritance matrix |
| Records requests | Front desks verify by caller knowledge questions | Central release team (supplement 3.2) | Impostor requests succeed (UC-011) |

**Why the drift happened.** The supplement had no owner after a 2025 reorganization, and the acquisition integration plan did not include policy alignment. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register. Acquisition plans now include a policy alignment milestone.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Ambulance Services, BDS) and on re-issue (Urgent Care).
