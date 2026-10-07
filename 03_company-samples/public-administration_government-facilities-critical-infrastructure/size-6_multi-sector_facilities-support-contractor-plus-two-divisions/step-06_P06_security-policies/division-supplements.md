# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-15 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for everyone, one severity scale, CUI only in approved locations, OT remote access only through the jump service | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, OT reference architecture, Group AI Standard (P10) | Group CISO |
| **Division supplement** | Customer-, agency-, and regulator-specific standards (state contract exhibits and federal building rules, DFARS and CMMC, FCRA and post orders) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks, post orders, work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Government Facilities Support | v2026 | 2026-06-30 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after effective date) | Confirm alignment |
| Construction and Renovation | v2025 | 2025-10 | Aligned to 2025 group policy, but has **no CUI handling standard aligned to SP 800-171** and no rule against CUI in commercial SaaS (scenario gap 8) | Add the CUI standard by 2026-11-30 (POAM-019, POAM-021) |
| Janitorial and Security Services | 2022 legacy policy set (pre-acquisition) | Never aligned | **Drifted** (scenario gap 8); conflicts listed in section 4 | Re-issue as a group supplement by 2026-12-31 (POAM-027) |

## 3. What each supplement adds
### 3.1 Government Facilities Support supplement (SUP-FS)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| State and local customer security terms | A contract security register for every state, county, municipal, and education contract (control set, notice term, assessment duty) | POL-01 4.8; POL-03 4.4 | State agency contract exhibits (Florida worked example: Fla. Stat. 282.318(4)(h)); county addenda (282.3185(4)) |
| Building recovery procedures | Manual-operation procedures for every site, exercised with the customer each year; at GSA buildings, as the BTTRG requires | POL-03 4.2 | GSA BTTRG v3.0 section 1.6.2; CP-2 |
| Federal buildings | Staff reach agency building systems only through agency virtual desktops with PIV cards; PIV cards returned on the last day; agency IT policies followed | POL-02 4.5 | FAR 52.204-9(b); BTTRG v3.0 section 1.1 |
| Customer tenant administration | Per-customer administrator roles with just-in-time elevation by 2027-03-31; no new tenant onboarded with the standing global role | POL-02 4.2 | AC-5; AC-6 |
| University cardholder records | Use only for access control; no export without the university's written authorization; FERPA briefing for tenant administrators | POL-04 4.5 | C-GOVERNMENT-R05 (34 CFR 99.31(a)(1)(i)(B); 99.33(a)) |
| Buildings housing FTI or criminal justice agencies | Maintenance in restricted areas only with the customer's escort; staff complete the customer-required training topics | POL-05 4.4, 4.6 | C-GOVERNMENT-R02 (Pub. 1075 2.B.3.3); C-GOVERNMENT-R03 (CJISSECPOL v6.1 AT-3) |
| Face verification | Operate only at approved entrances, only for consenting enrollees, with the badge always required | POL-01 4.13; POL-04 4.10 | P10 AI-001 conditions |

### 3.2 Construction and Renovation supplement (SUP-CN)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| CUI locations | CUI only in SYS-C2; no CUI in SYS-C1, the IBOP commissioning workspace, email, or AI services | POL-04 4.3 | N23-R03 (DFARS 252.204-7012(b)(2)(ii)(D)); N23-R04 (252.204-7021(d)(2)) |
| CUI marking and plan rooms | Mark derivative drawings; locked plan rooms with sign-in logs and escorts (requirements that may not be placed on a CMMC POA&M) | POL-04 4.4 | SP 800-171 R2 3.8.4, 3.10.3, 3.10.4; 32 CFR 170.21(a)(2)(iii) |
| Subcontractors | DFARS 252.204-7012 flow-down in every subcontract involving CUI; check the subcontractor's SPRS status before award; share CUI only through SYS-C2 | POL-01 4.8 | DFARS 252.204-7012(m); 252.204-7021(d)(4) |
| DoD reporting | 72-hour DIBNet report; 90-day preservation; malware to DC3; three certificate holders | POL-03 4.6 | DFARS 252.204-7012(c)-(e) |
| SPRS and CMMC | Annual assessment by group internal audit before each SPRS posting; affirmations by the division president as affirming official | POL-01 4.10 | DFARS 252.204-7019, -7020; 32 CFR Part 170 |
| Building turnover | Turnover checklist: default credentials changed, remote access documented, programs placed in the operations repository | POL-02 4.9 | IA-5; CM-6 |

### 3.3 Janitorial and Security Services supplement (SUP-JS), to be re-issued
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Consumer reports | Adjudicator-only access; standalone disclosure and authorization; pre-adverse action notices; destruction on schedule | POL-02 4.12; POL-04 4.7 | N56-R02 (15 U.S.C. 1681b(b)); N56-R01 (16 CFR 682.3) |
| Employment eligibility | E-Verify case within 3 business days after hire; I-9 retention per 8 CFR 274a.2(b)(2); breach of E-Verify data reported to DHS immediately | POL-04 4.7; POL-03 4.5 | FAR 52.222-54(b); Fla. Stat. 448.095(2) (worked example); E-Verify MOU Article II.A.9, II.A.16 |
| Customer-site credentials | Badges disabled and keys recovered on the last shift; agency PIV cards returned; weekly reconciliation at sites with more than 20 officers | POL-02 4.5 | FAR 52.204-9(b); customer contracts |
| Post orders at sensitive buildings | Second-barrier and escort rules at the revenue department building; CJIS AT-3 training topics at criminal justice buildings | POL-05 4.4, 4.6 | C-GOVERNMENT-R02 (Pub. 1075 2.B.2, 2.B.3.3); C-GOVERNMENT-R03 (CJISSECPOL v6.1 AT-3) |
| Installation business | Group supply chain screening for every camera, recorder, and network product; panel credentials only in the group vault | POL-01 4.9; POL-02 4.1 | FAR 52.204-25(b)(2), (d) |
| Monitoring service | Console workstations without email; alarm suppression alerts to supervisors | POL-02 4.7 | Monitoring contracts |

## 4. Janitorial and Security drift: conflicts with 2026 group policy
The division's 2022 policy set was written before the 2023 acquisition. Where it conflicts, **group policy governs now** (POL-01 4.5), but branch staff follow the document they know, so the conflicts are real risks (P01 JS-008).

| Topic | Division policy (2022) | Group policy (2026) | Effect |
|---|---|---|---|
| Consumer report access | Any branch manager may view reports | Adjudicators only (POL-02 4.12) | About 310 users with access (JS-003; POAM-025) |
| Record retention | "Keep personnel files permanently" | Retention schedule and disposal (POL-04 4.7) | Over-retention of consumer reports and I-9 copies (JS-006; POAM-026) |
| Customer-site credentials | Returned "at the next supervisor visit" | Last day; same-day report if not recovered (POL-02 4.5) | About 4 days of exposure (JS-009; POAM-007) |
| Equipment purchasing | Installer chooses products | Group screening for every product (POL-01 4.9) | Unconfirmed manufacturers (JS-001; POAM-022, POAM-023) |
| Panel credentials | Spreadsheet per branch | Group vault (POL-02 4.1) | JS-013; POAM-002 |
| Incident severity | Three-level branch scale | One group scale (POL-03 4.2) | Inconsistent escalation from the monitoring station |
| AI use | Not addressed | Inventory and approval (POL-01 4.13) | Applicant screening and report drafting started without review (JS-004, JS-016) |

**Why the drift happened.** The acquisition integration plan covered payroll and identity, but not policy. **Fix:** POL-01 4.14 now requires an acquired business to adopt group policy within 180 days, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Facilities Support, Construction) and on re-issue (Janitorial and Security).
