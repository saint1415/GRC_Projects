# AI Governance Risk Assessment: Enterprise AI Portfolio and Facial Recognition for Facility Access

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded facilities support contractor operating government buildings in 8 states and DC) |
| Tier / Vertical | Enterprise / Government Services and Facilities |
| Scope | Enterprise AI portfolio (12 use cases in `ai-use-case-inventory.csv`), with a full assessment of facial recognition for facility access in section 5: AI-001, face verification (1:1) pilots at 3 customer sites, and AI-002, a county request for face identification (1:N) of the public, which the company declined |
| Framework | NIST AI RMF 1.0 (AI 100-1) and its Playbook; NIST AI 600-1 (Generative AI Profile) for AI-010 and AI-012; repository risk tier rubric (`00_universal-framework/projects/step-10_P10_ai-governance/README.md`) |
| Assessor / date | AI governance committee (chaired by the Chief Technology Officer), meeting of 2026-08-26. The GRC team prepared the portfolio review; the Director of Data and Analytics' data science team ran the AI-001 measurements (June and July 2026 pilot logs); the Chief Privacy Officer reviewed the legal analysis with outside counsel. Internal Audit observed without voting |
| Decision | Executive risk committee, 2026-09-10, on the committee's recommendation (section 10); reported to the risk committee of the board the same day |

## 1. Portfolio summary
| Measure | Result |
|---|---|
| Use cases in the inventory | 12 |
| Risk tier | High 5, Medium 5, Low 2 |
| Status | In production 7, Pilot 3, Suspended 1, Not approved 1 |
| Committee review complete | 7 of 12 |
| Not yet reviewed | 5: AI-004, AI-005, AI-009, AI-011, AI-012 (all due 2026-11-30, POAM-021) |
| Use cases that process biometric data | 2 (AI-001 in pilot; AI-002 declined) |
| Use cases that can affect physical safety or building operations | 6 (AI-001, AI-002, AI-003, AI-004, AI-005, AI-007) |
| High-tier use cases with bias testing only on vendor data | 1 (AI-001); AI-011 has none and stays suspended |

**Main findings:**
1. **The face verification pilots started before committee review.** Three customers ordered face verification at staff entrances in 2026-02 to 2026-04. The work went through the Facility Services Portal as an ordinary PACS configuration change, so it never reached AI intake. 1,850 people are enrolled. Consent is incomplete, 37 templates were kept past the 30-day deletion rule, and the match rate misses its target at one site.
2. **Bias evidence for face verification rests on vendor data.** An initial screen of one site's logs suggests older and Black employees are rejected more often. Local testing, including an impostor test, is due 2027-03-31.
3. **Five use cases entered without review,** through the AQ-1 acquisition (video analytics and license plate recognition), vendor feature releases (SOC triage, resume ranking), and a team pilot (technician assistant). The one High-tier case among them, resume ranking (AI-011), is switched off.
4. **The 1:N request was declined.** The company will not identify members of the public in county lobbies (AI-002; P01 R-045).

## 2. GOVERN: AI governance committee operating model
**Charter.** The committee was formed in 2025-11 under POL-01 and reports to the executive risk committee. Its risks roll up to enterprise risk ER-08 "Responsible use of AI and biometrics" (P01), which the board risk committee reviews quarterly. The committee also decides on biometric and video analytics features in customer systems, even when they are not machine learning, because the risks are similar (POL-05 4.7).

**Members:** Chief Technology Officer (chair); Chief Privacy Officer; CISO; Chief Compliance Officer; the General Counsel's delegate; Chief Human Resources Officer; Vice President, Remote Operations; Vice President, Building Technology Platforms; President, Security Integration; Director of OT Security; Director of Data and Analytics. Internal Audit attends as a non-voting observer. For a use case in a customer building, the customer's facilities or security lead and the customer's counsel are invited.

**Decision rights by tier:**
| Tier | Who approves | Required before production |
|---|---|---|
| High | Committee vote, then the executive risk committee | Impact assessment; local validation and bias testing before deployment; human review design; notice to affected people (and consent for biometrics); monitoring plan; customer written order for customer systems |
| Medium | Committee vote | Human oversight design; output quality monitoring; AI disclosure where people interact with it; privacy and security review |
| Low | Committee chair (fast track) | Approved-tool listing (STD-05.3); data handling rules (POL-04) |

**Who decides what in customer buildings.** The customer owns the building, the access control and video systems, and the decision to use face verification, video analytics, or license plate recognition on its employees and visitors. The company configures and operates these features on the IBOP, holds the data in the customer's tenant, and **can refuse to operate a use it considers unsafe or unlawful**. A customer order is necessary but never sufficient (POL-05 4.7).

**Intake and inventory.** Any new AI or biometric use, including features switched on inside existing vendor products and features in acquired businesses' installed base, must be registered before use (POL-05 4.6 and 4.7; STD-05.4). After the AI-001 finding, two blocks were added: an FSP change ticket that enables a biometric, analytics, or AI feature now requires an inventory ID, and procurement cannot issue a purchase order for an AI-enabled product without one. The GRC team owns the inventory.

**Policies:** POL-04 4.1 (face templates are Restricted), 4.5 (templates deleted within 30 days after withdrawal or departure), 4.8 (no Restricted data in AI tools without committee approval and no-training terms); POL-05 4.6 (approved tools only) and 4.7 (no AI, biometric, video analytics, or license plate recognition feature in a customer system without an approved P10 assessment and the customer's written order); STD-05.3 Approved AI Tools List; STD-05.4 AI, Biometric, and Video Analytics Features Standard.

**Cadence:** monthly committee meetings; quarterly monitoring review for every High-tier use case; annual re-review of every use case; re-review after any vendor model update.

**Why 5 use cases lack review.** AI-004 and AI-005 came with AQ-1's installed base in 2025-10, before the committee existed, and were expanded under customer orders. AI-009 and AI-011 were switched on by vendor feature releases. AI-012 began as a 60-technician pilot in 2026-06 and its intake form arrived in 2026-07. All five have review dates of 2026-11-30 (POAM-021).

**Watch item.** NIST released a concept note for an AI RMF Critical Infrastructure Profile on 2026-04-07. The committee will map its process to the profile when NIST publishes it; AI RMF 1.0 remains the reference here.

## 3. MAP: portfolio context and applicable rules
| Rule | Applies? | Why |
|---|---|---|
| State breach notification and data security laws | Yes, for AI-001 and for any use case holding personal information | Each state where affected individuals reside. Florida worked example: biometric data as defined in Fla. Stat. 501.702, with a name, is personal information (501.171(1)(g)1.a.(VI)); the company must take reasonable measures (501.171(2)) and, as a third-party agent for customer data, notify the customer within 10 days of a breach determination (501.171(6)(a)) |
| Florida Digital Bill of Rights (Fla. Stat. 501.701 et seq.) | No | A "controller" must exceed $1 billion in global gross annual revenue **and** either earn 50% or more of that revenue from selling online advertisements, operate a consumer smart speaker and voice command service, or operate an app store offering at least 250,000 applications. The company's $4.8 billion revenue passes the first test but it meets none of the three others |
| Florida public records law (worked example) | Yes, for records held for state and local customers | Contractor duties under Fla. Stat. 119.0701; security system plan exemption in 119.071(3)(a); the biometric exemption in 119.071(5)(g) covers only friction ridge records, fingerprints, palm prints, and footprints (section 5.3) |
| FERPA (34 CFR Part 99) | Yes, for student data at university customers | The company is a school official for student cardholder records (99.31(a)(1)(i)(B)) and may not redisclose them (99.33(a)). Student templates at pilot site P2 are handled the same way |
| FTC Act Section 5 | Indirectly | Accuracy and privacy claims the company makes to customers (for example in Security Integration proposals) and vendor claims the company relies on. The FTC's May 18, 2023 policy statement on biometric information and its December 2023 order against a national pharmacy chain over facial recognition without reasonable safeguards show the safeguards the FTC has expected: accuracy and bias testing, notice, deletion, and vendor oversight |
| Title VII of the Civil Rights Act and the Uniform Guidelines | Yes, for AI-011 | Disparate impact remains in the statute (42 U.S.C. 2000e-2(k)). The four-fifths rule in 29 CFR 1607.4(D) is the screen the committee will use before any re-enable |
| FAR 52.204-21 and CUI rules (32 CFR Part 2002) | Yes, for AI-008, AI-010, and AI-012 | Federal work orders hold FCI; GSA CUI drawings must stay in the CUI enclave and may not be uploaded to any AI tool |
| State cybersecurity exhibits (SP 800-53 Rev. 5 Moderate) | Yes, for AI features on the IBOP | AI-001, AI-003, AI-004, AI-005, and AI-007 run inside or through the IBOP boundary (P02) |
| Colorado SB26-189 and Texas HB 149 | No | The company does no business in Colorado or Texas. The repository rubric still borrows its consequential-decision categories, including essential government services, from laws like Colorado's, which is why AI-002 is tiered against that category |
| Federal facial recognition at GSA buildings | Not in scope | Physical access control at the 64 federal buildings is GSA's and the Federal Protective Service's, using PIV cards. The company will not propose face recognition at federal buildings |

## 4. Risk tiering
Rubric: `00_universal-framework/projects/step-10_P10_ai-governance/README.md` (repository-defined). High = a substantial factor in a consequential decision about a person, or able to affect physical safety or critical infrastructure operations. A government building's access control and HVAC are critical infrastructure operations in this sector.

| ID | Use case | Tier | Status | Committee review | Biometric |
|---|---|---|---|---|---|
| AI-001 | Face verification (1:1) at staff entrances of 3 customer sites | High | Pilot (1,850 enrolled) | Reviewed 2026-08-26 (after the pilots started) | Yes |
| AI-002 | Face identification (1:N) of the public in county lobbies (county request) | High | Not approved | Reviewed 2026-07-22 (declined) | Yes |
| AI-003 | ROC alarm prioritization | High | In production (3 ROCs) | Reviewed 2026-01-21 | No |
| AI-004 | Video analytics alerts at 186 buildings | Medium | In production | Not reviewed (due 2026-11-30) | No (to be confirmed) |
| AI-005 | License plate recognition at 9 garages | Medium | In production | Not reviewed (due 2026-11-30) | No |
| AI-006 | Fault detection and diagnostics on BAS trend data | Low | In production | Reviewed 2025-12-10 | No |
| AI-007 | Closed-loop HVAC optimization pilot at 12 buildings | High | Pilot | Reviewed 2026-03-18 | No |
| AI-008 | FSP work order triage | Medium | In production | Reviewed 2026-02-18 | No |
| AI-009 | SOC alert triage assistant | Low | In production | Not reviewed (due 2026-11-30) | No |
| AI-010 | Enterprise generative AI assistant (about 4,200 users) | Medium | In production | Reviewed 2025-12-10 | No |
| AI-011 | Applicant resume screening and ranking | High | Suspended | Not reviewed (due 2026-11-30) | No |
| AI-012 | Generative AI technician assistant (FSP mobile app) | Medium | Pilot (60 technicians) | Not reviewed (due 2026-11-30) | No |

**Tiering notes:**
- **AI-003 is High** although operators see every alarm, because a wrong ranking could delay the response to a forced door or a freeze alarm. Fire, duress, and forced-door alarms are pinned to the top by fixed rules so the model cannot bury them.
- **AI-004 and AI-005 are Medium** because a person verifies every alert and no door or gate decision depends on the model alone. Enabling face matching in video, hotlist alerting on plates, or sharing with law enforcement would re-tier them to High.
- **AI-007 is High** because it writes setpoints to occupied government buildings. The bounds in the BAS are the safety control, not the model.
- **AI-010 is Medium rather than Low** because Restricted data (other than CUI and face templates) is allowed in its approved tenant.

## 5. Full assessment: facial recognition for facility access (AI-001 and AI-002)
### 5.1 MAP: AI-001 face verification (1:1)
| Item | Description |
|---|---|
| Purpose and intended use | Stop badge sharing and lost-badge misuse at staff entrances. The reader checks that the live face matches the enrolled template of the badge presented. It is a second factor; the badge is always required |
| Sites | **P1:** a Florida state agency headquarters, employee entrance, 4 readers, 920 enrolled, live since 2026-02-09. **P2:** a public university research building, 4 readers, 610 enrolled faculty, staff, and graduate students, live since 2026-03-02. **P3:** a county courthouse staff entrance, 3 readers, 320 enrolled court and county staff, live since 2026-04-13 |
| Users and operators | ROC credentialing clerks (enrollment records), controls and security technicians (configuration), customer guards (fallback desk). Vice President, Remote Operations is the operating owner; the Chief Technology Officer is the accountable executive (R-044) |
| Affected people | 1,850 enrolled volunteers; people who declined (they use badge plus PIN); visitors and the public are not enrolled and are not scanned |
| Data | Inputs: an enrollment image captured at a staffed station, converted to a face template; live images at the reader. Outputs: match score and result, logged with the access event. Templates are stored in the customer's PACS tenant, encrypted with the tenant key (P07 SC-28 Satisfied) and not exportable from the console (R-008). **Default retention was indefinite** |
| Build or buy | Buy: the PACS software vendor's face verification module, hosted by the company on Cloud provider A. The vendor's model is pretrained; templates never leave the IBOP, but vendor support sessions through the OT remote access gateway can reach the PACS database, and the contract is silent on template access and on demographic performance data |
| Not intended | Identifying anyone without a badge; use on visitors or the public; use by police or for investigations; use as evidence for discipline without the customer's human review of the event and video; use at federal buildings. These are prohibited in the configuration standard (STD-05.4) and in each customer order |

### 5.2 MAP: AI-002 face identification (1:N), declined
A county customer asked in 2026-06 for watch-list alerting in the public lobbies of its government center: every person entering would be compared with a county watch list and guards alerted on a match. This changes the purpose from verifying a known, consenting employee to identifying unknown members of the public who came to use county services. One-to-many search also carries a much higher chance of misidentification than one-to-one verification, and the request had no review, correction, or appeal design. The committee declined it on 2026-07-22 (P01 R-045, treatment Avoid). Section 10 records the conditions under which the company would look at it again.

### 5.3 Laws and rules for face templates
| Rule | Applies? | Analysis |
|---|---|---|
| State breach and biometric definitions | **Yes, treated as biometric data** | Each state where enrolled people reside, through counsel's state matrix. Florida worked example: personal information includes "an individual's biometric data as defined in s. 501.702" with a name (501.171(1)(g)1.a.(VI)). Section 501.702 defines biometric data as data generated by automatic measurements of an individual's biological characteristics used to identify a specific individual, and **excludes physical or digital photographs and video or audio recordings or data generated from them**. Because the readers capture live camera images, whether these templates fall inside the definition is **unsettled; counsel to confirm**. The company treats them as biometric data and as personal information either way (POL-04 4.1; P03 G-226) |
| Third-party agent duties | Yes | As the customers' third-party agent (Florida example): reasonable security (501.171(2)), breach notice to the customer within 10 days of a breach determination (501.171(6)(a)), and secure disposal (501.171(8)). The customer contracts require notice within 24 hours, which is shorter |
| Public records (Florida worked example) | **Open question for customers' counsel** | The agency biometric exemption in Fla. Stat. 119.071(5)(g) covers only friction ridge records, fingerprints, palm prints, and footprints. **It does not name face templates.** Whether the security system plan exemption (119.071(3)(a)) or another exemption protects them is for the P1 agency's and the P3 county's counsel. As a contractor the company keeps exempt records confidential and routes requests to the customer's custodian within 1 business day (119.0701; POL-04 4.9; P01 R-034) |
| FERPA (site P2) | Yes | Templates of graduate students are part of the student cardholder records the university designated the company to maintain. Use only for the contracted purpose and no redisclosure without the university's direction (34 CFR 99.33(a); POL-04 4.4) |
| FTC Act Section 5 | Indirectly | Security Integration marketing must not overstate accuracy or claim the system is free of bias. Claims must match the local test results |
| Customer contracts | Yes | State cybersecurity exhibit (P1), county security addendum (P3), and university contract (P2): Restricted data handling, 24-hour incident notice, and the customer's retention schedule apply to templates |
| Florida Digital Bill of Rights | No | The company is not a "controller" (section 3) |

### 5.4 Risk tier
**High** for both use cases. AI-001 controls physical access to government buildings (critical infrastructure physical security), processes biometric data, and repeated false rejections affect people's access to their workplace. AI-002 would identify members of the public seeking essential government services. Minimum controls for High: human review before action, pre-deployment bias testing, impact assessment (this document), notice to affected people, and ongoing monitoring. **AI-001 is missing two of these: pre-deployment bias testing and complete notice and consent.**

### 5.5 MEASURE: AI-001 trustworthy characteristics (pilot logs 2026-06-01 to 2026-07-31)
| Characteristic | Test / metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | False non-match rate (FNMR): genuine people rejected per attempt. Target 2.0% or less at each site | 109,400 attempts. Overall 2.1%. P1 1.8% (62,400 attempts); P2 2.1% (31,800); P3 3.6% (15,200; backlit entrance) | **No** (P2, P3) |
| Valid and reliable | False match rate (FMR): impostor accepted. Target 0 accepts in a 2,000-attempt impostor test per site | Not tested locally; vendor laboratory data only | **Not measured** |
| Safe | No one refused entry on a face result alone; fallback works | Badge plus PIN or the guard desk resolved all 2,338 rejections; average added delay 35 seconds | Yes |
| Secure and resilient | Templates encrypted with tenant keys; not exportable; vendor access controlled | Encryption and export block in place (P07 SC-28 Satisfied). Vendor support sessions are brokered and recorded, but the contract does not limit template access | **Partial** |
| Accountable and transparent | Standard written notice, signed consent before enrollment, signage at each entrance | Signed consent on file for 1,214 of 1,850 (P1 480 of 920; P2 610 of 610; P3 124 of 320). Signage at P2 only. Customers issued their own notices; the fallback was not documented at P3 | **No** |
| Explainable and interpretable | Guards can see the match score and the enrolled image when a match fails | Available at all 3 sites | Yes |
| Privacy-enhanced | Templates deleted within 30 days after withdrawal or departure (POL-04 4.5); no vendor use of templates | 37 templates held past 30 days (deletion is manual); no contract term on vendor use | **No** |
| Fair, with harmful bias managed | FNMR by group against the thresholds in 5.6 | Initial screen flags two groups at P1 (5.6) | **No** |

### 5.6 Bias testing: initial screen and plan
Face matching accuracy can differ by demographic group. NIST's Face Recognition Vendor Test report on demographic effects (NISTIR 8280, December 2019) documented such differences across many algorithms, and they vary by algorithm and threshold, so the vendor's general claims cannot stand in for testing on the people actually enrolled.

**Initial screen (site P1 only).** The P1 agency's human resources office provided voluntary self-reported demographic data for 702 of its 920 enrolled employees, linked to match results by the agency and returned to the company only in aggregate.
| Group (P1) | FNMR | Ratio to P1 overall (1.8%) | Result |
|---|---|---|---|
| Age 60 and over | 2.9% | 1.6 | **Flagged** |
| Black employees | 2.7% | 1.5 | **Flagged** |
| Women | 1.9% | 1.1 | Pass |
| Under age 40 | 1.5% | 0.8 | Pass |
| Wearing head coverings (12 people) | 5.0% | 2.8 | Reported, not scored (fewer than 15 people) |

**What the screen means.** Older and Black employees at P1 are rejected more often. Because the badge-plus-PIN fallback always works, the harm is delay and repeated friction rather than denied entry, but it falls unevenly and is not acceptable for any expansion. The screen covers one site and has no impostor test, so it is not the pre-deployment bias test the High tier requires.

**Local testing plan (POAM-021, due 2027-03-31):**
- **Metrics:** FNMR per group at the operating threshold from real attempts; FMR per group from a controlled impostor test with volunteer pairs (2,000 attempts per site).
- **Groups compared:** age band (under 40, 40 to 59, 60 and over), sex, self-reported race and ethnicity (voluntary, collected by each customer, reported to the company only in aggregate), and people wearing eyeglasses or head coverings. At P2, students and employees are also compared.
- **Thresholds:** each group's FNMR no more than 1.25 times the site's overall FNMR and no more than 3.0%; zero false accepts in each group's impostor test. Groups with fewer than 15 people are reported but not scored.
- **Rules:** the match threshold may not be lowered to cut rejections without a new impostor test, because that raises the false match rate. Results go to each customer and the committee.
- **Frequency:** before any expansion, then quarterly while in use, and after any vendor model update.

### 5.7 MANAGE: AI-001
**Human-in-the-loop design:**
- The face match is never the only factor. The badge is always required, and a failed match never locks anyone out: badge plus PIN, or the guard desk with a visual check, is always available.
- Match results are never used as evidence for discipline, attendance, or investigations, and are never given to police, without the customer's human review of the event and the video.
- ROC operators cannot enroll anyone; enrollment happens only at a staffed station after signed consent is recorded.

**Notice and consent:**
- One company standard notice and consent form for all sites, stating purpose, data kept, retention, who sees results, and how to withdraw (P09 P1.1, P2.1, P3.2).
- Signage at every face verification entrance.
- Declining or withdrawing has no effect on employment, studies, or access; the badge-plus-PIN lane stays open.

**Data handling:**
- Templates are Restricted (POL-04 4.1), encrypted with tenant keys, and stay in the customer's tenant.
- Deletion within 30 days after withdrawal, departure, or the customer's retention date (POL-04 4.5). Monthly reconciliation against each customer's departure list until automated deletion is built with the retention jobs (POAM-020).
- Vendor contract amendment: no use of templates or images for training or any other purpose; template access during support only under an approved ticket in a recorded gateway session; demographic performance data for the deployed model version; notice of model changes; 24-hour incident notice.

**Monitoring:** monthly FNMR by site; quarterly FNMR by group; monthly retention reconciliation; complaints to the customer's human resources office and the Vice President, Remote Operations. Results are tracked in P01 R-044 and reported to the committee quarterly.

**Incident handling:** theft or exposure of templates follows the P08 runbook: breach determination by the Chief Privacy Officer, treating templates as biometric data (P08 step 7.3), customer notice within 24 hours under the contracts, and the third-party agent notice under state law (Florida example: within 10 days under 501.171(6)(a)). A wrong match that let an impostor in is handled as a security incident at the customer's building.

**Decommissioning:** stop the pilot at a site and delete all its templates if the vendor has not signed the data terms by 2026-10-31, if a flagged group's FNMR does not improve by the next quarterly report, if the impostor test records any false accept that the vendor cannot explain and fix, or if the customer's counsel concludes the templates would be disclosable public records.

## 6. Other High-tier use cases
| ID | Key risk | Controls in place | Open items |
|---|---|---|---|
| AI-003 ROC alarm prioritization | A true alarm ranked low waits in the queue | Every alarm shown and acknowledged; fire, duress, and forced-door alarms pinned by fixed rules; weekly check that no confirmed true alarm waited more than 5 minutes because of ranking (none in 2026) | Re-validate after each vendor model update; check that alarms from older buildings with noisier sensors are not ranked low as a group |
| AI-007 HVAC optimization pilot | An unsafe setpoint written to an occupied building (P01 R-046) | Setpoint bounds enforced by the BAS; operator override; fallback to the building schedule; no writes to life-safety, smoke control, or laboratory exhaust | Annual bounds review with each customer's building engineer; no expansion beyond 12 buildings until a full cooling season of results is reviewed (2027-10) |
| AI-011 resume ranking | Adverse impact against protected groups in technician hiring (P01 R-049) | Ranking switched off 2026-08-20; recruiters review all applicants | Adverse impact analysis using the four-fifths rule (29 CFR 1607.4(D)) on the 2026-02 to 2026-08 rankings, and counsel review, before any re-enable |

## 7. MEASURE: portfolio testing plan
| Use case | Metric | Groups or segments compared | Threshold for action |
|---|---|---|---|
| AI-001 face verification | FNMR and FMR (section 5.6) | Age band; sex; race and ethnicity; eyeglasses and head coverings; students and employees at P2 | Ratio above 1.25 or FNMR above 3.0%; any false accept |
| AI-003 alarm prioritization | Time a confirmed true alarm waited because of ranking | Segment; building age; alarm type | Any true alarm delayed more than 5 minutes |
| AI-004 video analytics | False alert rate; confirmation that face recognition functions are disabled | Site; camera type; time of day | False alerts above 20% of alerts at a site; any face function enabled |
| AI-005 license plate recognition | Read accuracy | Plate type; issuing state | Read accuracy below 95% for any plate group |
| AI-007 HVAC optimization | Out-of-bounds writes blocked; comfort complaints | Building | Any out-of-bounds write that was not blocked; complaints above the building's baseline |
| AI-011 resume ranking | Selection rate by group | Sex; race and ethnicity (where self-reported) | Any group below four-fifths of the highest group's rate |
| AI-008 work order triage | Share of urgent requests under-prioritized | Segment; customer type | Above 2% of urgent requests |

## 8. MANAGE: portfolio controls
- **Monitoring:** each High-tier use case reports its metrics quarterly to the committee (inventory column `monitoring`); a threshold breach triggers re-review within 30 days.
- **Generative AI (AI-010, AI-012):** controls follow NIST AI 600-1 for the risks that matter here: confabulation (answers cite sources; technicians follow manufacturer manuals), information security (prompt injection testing before AI-012 leaves pilot), data privacy (POL-04 4.8; no CUI or face templates), and value chain and component integration (provider terms with no training on company data).
- **Incident handling:** AI incidents (unsafe output, bias finding, data misuse, an unapproved feature found switched on) are logged in SOC case management and follow P08 where security, personal data, or building safety is involved.
- **Third parties:** vendors of AI and biometric features are tier-1 in the third-party program; contracts must require notice of material model changes and prohibit training on company or customer data (POL-04 4.8).
- **Decommissioning:** a use case is retired if it fails its thresholds twice in a row, if the vendor changes data-use terms, or if the customer withdraws its order; the inventory records retirement and the deletion of data.

## 9. Links to other deliverables
| Deliverable | Link |
|---|---|
| P01 risk register | ER-08 risks R-044, R-045, R-046, R-048, R-049, R-050; template theft R-008 (ER-03); public records disclosure R-034 |
| P02 SSP | The face verification module and its 11 readers are inside the IBOP boundary; cardholders use the face match only as a second factor (P02 section 11) |
| P03 gap analysis | G-226 (biometric data as personal information, Met); G-167 (retention, Partially met) |
| P06 policies | POL-04 4.1, 4.4, 4.5, 4.8, 4.9; POL-05 4.6, 4.7; STD-05.3; STD-05.4 |
| P07 POA&M | POAM-021 (committee reviews, vendor data terms, local bias testing); POAM-020 (retention jobs) |
| P08 runbook | Template theft is in scope of the intrusion runbook (sections 4 and 7) |
| P09 SOC 2 | SL-1 Privacy criteria P1.1, P2.1, P3.2, and P4.3 depend on the AI-001 conditions |

## 10. Decisions
The executive risk committee approved these decisions on 2026-09-10, on the AI governance committee's recommendation of 2026-08-26:
1. **AI-001: approved with conditions.** The pilots may continue at P1, P2, and P3 for people already enrolled, with **no new enrollments and no new sites**, only if:
   - the 37 templates held past 30 days are deleted by 2026-09-30;
   - the vendor contract amendment in section 5.7 is signed by 2026-10-31 (POAM-021);
   - the standard notice, signed consent forms, signage at every entrance, and a documented fallback at P3 are in place by 2026-11-30, and the templates of anyone who has not signed by then are deleted (P09 P1.1, P2.1, P3.2);
   - P3 entrance lighting is corrected and FNMR re-measured by 2026-12-31;
   - the P1 agency's and P3 county's counsel give a written view on the public records status of templates by 2026-12-31;
   - local bias testing with impostor tests is complete at all three sites by 2027-03-31 (POAM-021), with automated deletion live with the retention jobs (POAM-020).
   Expansion to other entrances or customers requires a new assessment and two consecutive quarterly reports with no flagged group.
2. **AI-002: not approved.** The company will not configure or operate 1:N identification of the public (P01 R-045, treatment Avoid). The Chief Technology Officer's letter to the county, due 2026-09-30, explains why. The company would look at it again only on a written county request that includes the county attorney's legal review, a human review, correction, and appeal process, and a narrower purpose.
3. **AI-004, AI-005, AI-009, AI-012:** may continue in their current scope until committee review by 2026-11-30; no expansion. For AI-004, every site must confirm by 2026-10-31 that face recognition functions are disabled.
4. **AI-011:** ranking stays disabled until committee review and the adverse impact analysis are complete.
5. **AI-003 and AI-007:** continue; AI-007 stays at 12 buildings until the 2027 cooling season review.
6. **Intake:** the FSP change ticket and procurement blocks (section 2) stay in place; Internal Audit will test them in the 2027 assessment.
