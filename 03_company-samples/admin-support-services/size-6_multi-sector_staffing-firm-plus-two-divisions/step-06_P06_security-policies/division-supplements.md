# Division Supplements to Group Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. |
| Authority | POL-01 section 4.5: a supplement may add stricter or division-specific requirements, never weaker ones; it must be re-aligned within 90 days after a group policy changes and attested every year |
| Owner | Each division security and compliance lead; alignment reviewed by the Group CISO |
| Status date | 2026-09-10 (group policies v2026 approved; effective 2026-10-01) |

## 1. How group policy and supplements fit together
| Layer | Examples | Who approves |
|---|---|---|
| Group policy (POL-01 to POL-05) | MFA for all workforce, one severity scale, no contract no data, privacy review for new feeds | Board risk committee or Group CISO |
| Group standards | Logging standard, cloud guardrails, retention schedule, Group AI Standard (P10) | Group CISO; Group Chief Privacy Officer |
| **Division supplement** | Regulator-, client-, and system-specific standards (for example, E-Verify users, client-issued accounts, the Federal Solutions enclave, home health emergency preparedness) | Division president, after Group CISO alignment review |
| Division procedures | Runbooks and work instructions | Division security and compliance lead |

## 2. Supplement status
| Division | Supplement version | Last aligned to group policy | Status | Action |
|---|---|---|---|---|
| Staffing | v2026 | 2026-06-20 (to the 2026 draft group policies) | Aligned; minor update for the final 2026 policies due by 2026-12-30 (90 days after the effective date) | Confirm alignment |
| Consulting | v2026 | 2026-07-15 | Aligned, but missing the client-account register rule and the subcontractor BAA rule (POL-02 4.7; POL-01 4.8) | Add both by 2026-10-31 |
| Home Health | v2023 | 2023-11 (written at acquisition) | **Drifted** (group gap 3; EV-063); conflicts listed in section 4 | Re-issue by 2026-11-30 (POAM-020) |

## 3. What each supplement adds
### 3.1 Staffing supplement (employer of record; focus division)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| E-Verify users | Named accounts only; E-Verify on the termination checklist; monthly reconciliation of users to HR; tutorial before access | POL-02 4.1, 4.6 | MOU Art. II.A.3, II.A.5, II.A.15 |
| E-Verify outages | Record each day E-Verify is unavailable and keep the record with the Form I-9 | POL-04 4.8 | Fla. Stat. 448.095(2)(c) (worked example; other state E-Verify laws handled the same way) |
| I-9 archive | Archive readable only by the compliance role; object-level access logging and object lock; documented index and retrieval | POL-04 4.5 | 8 CFR 274a.2(e)(5), (g)(1)(i), (g)(1)(iv) |
| Background checks | Every consumer report, including drug screen reports from the testing provider, goes through the pre-adverse and adverse action workflow | POL-04 4.5 | 15 U.S.C. 1681b(b)(3)(A); 1681m(a) |
| Lobby kiosks | Kiosks on a segmented network with no staff resources reachable; kiosk images rebuilt nightly | POL-02 | CSF PR.IR-01 |
| Client submittals | No SSNs or dates of birth in email to clients; badge data through the client portal | POL-04 4.4 | Fla. Stat. 501.171(2) |
| Client VMS integrations | One service identity per client; keys rotated every 90 days | POL-02 4.5 | CSF PR.AA-01 |
| AI in recruiting | Knockout questions only from the central library, after legal review; no auto-advance or auto-reject without council approval; notices where law requires | POL-01 4.13 | NYC Admin. Code 20-870 et seq.; Title VII 703(k); ADA 42 U.S.C. 12112(b)(6) |
| Pay disruption | Associate text and branch scripts ready for a late or repeated payroll | POL-03 4.9 | State wage-payment laws (generic) |
| MSP program data | One client's program data never visible to another client or a non-participating supplier; tenant audit logs reviewed monthly | POL-02 4.2 | Client contracts; P09 |

### 3.2 Consulting supplement (business associate; federal contractor)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Client-issued accounts | Register of every client account; removal request within 1 business day of roll-off; quarterly reconciliation with each client | POL-02 4.7 | 164.308(a)(3)(ii)(C) |
| Client PHI | Request samples, not full extracts, unless the engagement plan says otherwise; label PHI in the repository; no external sharing links on labeled content; purge or return at engagement close | POL-04 4.4, 4.10 | 164.502(b); 164.504(e)(2)(ii)(J) |
| Subcontractors | No independent subcontractor touches client PHI without a subcontractor BAA | POL-01 4.8 | 164.308(b)(2); 164.504(e)(2)(ii)(D) |
| Client notices | Register of each client's BAA notice term (72 hours for 23 clients; 10 business days standard) | POL-03 4.5 | 164.410; client BAAs |
| Models built on client data | Per-client models unless the client's BAA permits data aggregation | POL-01 4.13 | 164.504(e)(2)(i)(B) |
| Federal Solutions enclave | Federal contract information stays in the enclave; enclave patches within 30 days; visitor log at the Federal Solutions office; flow-down of 52.204-21 to subcontracts | POL-02 4.13; POL-04 4.5 | 48 CFR 52.204-21(b)(1), (c) |
| Federal contractor E-Verify | Verify each employee assigned to a federal contract within the clause's timelines | POL-02 | 48 CFR 52.222-54(b); MOU Art. II.B |

### 3.3 Home Health supplement (covered entity; Medicare-certified home health agency)
| Topic | Division requirement | Group policy it builds on | Driver |
|---|---|---|---|
| Patient data outside the EHR | No routine feed of patient data to corporate or any vendor without a HIPAA permission, a BAA covering the service, and a minimum-necessary protocol approved by the Privacy Officer | POL-04 4.4 | 164.502(b); 164.514(d)(3); 164.308(b)(1) |
| Field tablets | Group endpoint management and EDR on every tablet; 5-minute lock; secure messaging only | POL-02 4.10; POL-05 4.6 | 164.308(a)(5)(ii)(B); 164.312(a)(2)(iii) |
| Per diem clinicians | EHR accounts expire at the Staffing assignment end date | POL-02 4.6 | 164.308(a)(3)(ii)(C) |
| Emergency preparedness | All-hazards risk assessment includes a prolonged cyber outage; priority patient list printed daily during declared emergencies; plan, policies, communication plan, and training reviewed at least every 2 years; exercises at least annually | POL-03 | 42 CFR 484.102(a)-(d) |
| Clinical records | Retention 5 years after discharge unless state law is longer; records to patients within 4 business days or at the next visit | POL-04 4.8 | 42 CFR 484.110(c), (e) |
| Decision support tools | Every patient care decision support tool inventoried; inputs reviewed for protected traits; mitigation documented | POL-01 4.13 | 45 CFR 92.210 |
| Recording consent | Consent field completed before any ambient recording | POL-05 4.9 | Fla. Stat. 934.03(2)(d) (worked example) |

## 4. Home Health drift: conflicts with 2026 group policy
The 2023 Home Health standards were written at acquisition, before the 2025 and 2026 group policies. Where they conflict, **group policy governs now** (POL-01 4.5), but staff follow the document they know, so the conflicts are real risks (P01 HH-007; P07 PL-1 findings).

| Topic | Home Health standard (2023) | Group policy (2026) | Effect |
|---|---|---|---|
| Termination | Next business day | Within 4 hours; per diem accounts expire at assignment end (POL-02 4.6) | Longer exposure window (HH-009) |
| Endpoint protection | Antivirus on laptops only | EDR on all managed devices including tablets (supplement 3.3) | 28% of tablets without EDR (HH-002) |
| Log retention | 90 days in the EHR export | 1 year searchable, 6 years archived (logging standard) | Breach scoping limited |
| Incident severity | Home Health 3-level scale | One group scale (POL-03 4.2) | Inconsistent escalation |
| New data feeds | IT approval only | Privacy impact assessment (POL-01 4.9) | The visit-pay feed went live without one (group gap 1; EV-031) |
| AI use | Not addressed | AI inventory and approval (POL-01 4.13) | Hospitalization risk model and recording pilot not reviewed (HH-010, HH-011) |
| Common control inheritance | Not addressed | Division must document inheritance (POL-01 4.6) | Group gap 6 (POAM-021) |

**Why the drift happened.** The supplement was written by the acquired company's IT team in 2023 and had no owner after that team moved under the Group CISO. **Fix:** POL-01 4.5 now requires re-alignment within 90 days of any group change and an annual attestation, and the Group CISO's policy office tracks supplement versions in the policy register.

## 5. Attestation
Each division security and compliance lead signs an annual statement: "The division supplement does not weaken any group policy and reflects all group policy changes made in the last 12 months." The first attestations are due 2026-12-31 (Staffing, Consulting) and on re-issue (Home Health).
