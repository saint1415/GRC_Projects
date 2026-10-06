# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead (Insurance information security officer; Health Care Services HIPAA Security Officer); the group health plan's security official for the plan sponsor procedures. Alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, identity recovery rules, one severity scale, intercompany services treated as third-party services | Board risk committee or Group CISO |
| Group standards | Logging standard, landing-zone guardrails, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Regulator-specific and system-specific requirements (commissioner notices, EHR break-glass, plan sponsor separation) | Division president (or the plan administrator), after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Supplement | Version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Insurance | v2025 | 2025-10 | Aligned; needs the 2026 additions in section 3.1 within 90 days of 2026-10-01 | Update by 2026-12-30 |
| Health Care Services | v2023 | 2023-05 | **Drifted**; conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-024) |
| Group health plan sponsor procedures | v2026 (new) | 2026-09 | Aligned; first edition written during this assessment | Plan document amendment pending (POAM-022) |

## 3. What each supplement adds
### 3.1 Insurance supplement (two Florida-domiciled insurers; licensees in 6 states)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Commissioner notices | List of licensed states that enacted Model #668 (Alabama, South Carolina, Tennessee in part), with commissioner contacts, the 250-resident trigger, and the 72-hour clock; kept current in the notification matrix | POL-03 4.5 | Model #668 sec. 6A-6C |
| Producers of record | Producer of record notice template and agency contact extract for affected policyholders who bought through independent agencies | POL-03 4.5 | Model #668 sec. 6F |
| Holding company as service provider | Annual due diligence on the holding company's shared services using the SCSP affiliate assurance report; security schedule in the intercompany agreement; Group CISO's annual delegate report to Insurance management | POL-01 4.8 | Model #668 sec. 4E(3), 4F |
| Caller verification | Bank-detail changes requested by claimants or repair shops are verified by a call back to contact data on file before they take effect; first payment to a changed account over $10,000 held 5 business days | POL-02 4.13; POL-05 4.3 | Model #668 sec. 4B(3), 4D(2)(a) |
| Surge adjusters | Independent adjusters proofed before hurricane season against adjusting-firm rosters with government ID; accounts pre-staged disabled and activated only from verified rosters; automatic expiry at 90 days | POL-02 4.4, 4.9 | Model #668 sec. 4D(2)(a) |
| Retention | Closed claims purged automatically past the retention schedule | POL-04 4.7 | Model #668 sec. 4B(4), 4D(2)(k) |
| AI in insurance decisions | Insurance AI program annex to the Group AI Standard covering the NAIC AI Model Bulletin elements, applied to all states | POL-01 4.14 | North Carolina Bulletin No. 24-B-19 |
| Agent and policyholder authentication | MFA required for agents; step-up MFA before policyholder payment or contact changes | POL-02 4.13 | Model #668 sec. 4D(2)(g) |

### 3.2 Health Care Services supplement (HIPAA covered entity)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Clinical downtime | Read-only downtime workstations and paper forms at every clinic; a downtime drill in each region every year, including the acquired clinics | POL-03 | 164.308(a)(7)(ii)(C)-(D) |
| Workers' compensation and employer disclosures | Insurer adjusters receive only work-injury encounter reports; no full-chart access. Employer reports use the structured work-status template; written notice to the patient at check-in | POL-02 4.2; POL-04 4.2 | 164.512(l); 164.512(b)(1)(v); 164.514(d)(3) |
| Employee-as-patient | Real-time alert when an employee opens a coworker's record; Privacy Officer review within 2 business days | POL-01 4.7 | 164.308(a)(1)(ii)(D) |
| EHR break-glass | Break-glass access reviewed by the Privacy Officer within 2 business days | POL-02 4.6 | 164.312(a)(2)(ii) |
| Acquired clinics | Within 90 days of closing: inventory, risk analysis, inheritance matrix, SIEM onboarding, unique accounts | POL-01 4.6 | 164.308(a)(1)(ii)(A), (a)(8) |
| Decision support | Every patient care decision support tool inventoried; inputs reviewed for protected traits; mitigation documented | POL-01 4.14 | 45 CFR 92.210 |
| Recording | Consent captured in a required field before any AI scribe recording | POL-05 4.7 | Fla. Stat. 934.03(2)(d) worked example |

### 3.3 Group health plan sponsor procedures (holding company as plan sponsor)
| Topic | Requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Who may access plan PHI | Only the 14-person plan administration unit named in the plan documents | POL-02 4.14 | 164.504(f)(2)(iii)(A)-(B) |
| Where plan PHI lives | Plan administration restricted workspace and the administrator's systems only; no HCM exports elsewhere | POL-04 4.3 | 164.504(f)(2)(iii); 164.314(b)(2)(ii) |
| No employment use | Plan PHI is never used for employment decisions; HR business partners do not see appeal or claim files | POL-04 4.2 | 164.504(f)(2)(ii)(C) |
| Security incidents | Any security incident involving plan PHI is reported to the plan security official the same day | POL-03 4.4 | 164.314(b)(2)(iv) |
| Plan documents | Plan documents amended with the 164.314(b)(2) terms and the sponsor certification re-signed | POL-01 4.2 | 164.314(b); 164.504(f)(2)(ii) |

## 4. Health Care Services drift: conflicts with 2026 group policy
The 2023 supplement was written before the 2025 acquisition and the 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but clinic staff follow the document they know, so the conflicts are real risks (P01 HCS-015; P07 PL-1 finding).

| Topic | Health Care Services supplement (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Front-desk accounts | Shared front-desk logins allowed with a shift log | Unique accounts only (POL-02 4.1) | Shared logins at acquired clinics (HCS-018) |
| Cross-division access | Insurer adjuster access approved by the clinic operations director | Owning data owner approves; minimum necessary; reports, not direct access (POL-02 4.2) | Full-chart adjuster role (HCS-001) |
| Acquisitions | Not addressed | Inventory, risk analysis, and inheritance within 90 days (POL-01 4.6) | Acquired clinics outside the analysis (gap 8) |
| Log retention | 90 days in the EHR | 1 year online, archived per the logging standard | Investigation limited |
| AI use | Not addressed | AI inventory and approval (POL-01 4.14) | AI assistant and scribe pilot ungoverned |
| Termination | Next business day | Within 4 hours (POL-02 4.9) | Longer exposure window |

**Why the drift happened.** The 2024 reorganization moved the division's security function under the Group CISO's governance, but the supplement had no owner or review date. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, tracked in the group policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Insurance; group health plan) and on re-issue (Health Care Services).
