# Incident Response Runbook: Insider Access to FTI, CJI, or Motor Vehicle Records

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed GovTech systems integrator serving state and local agencies) |
| Tier / Vertical | Mid-Market / Public Administration |
| Incident type | A company employee or contractor looks up, searches, exports, or discloses FTI (AG-01), CJI (AG-02, AG-39, or AG-02's agency-hosted systems), motor vehicle record information (AG-04), or benefits data (AG-03) without a work reason. Examples: browsing a neighbor's tax case, checking a relative's criminal history, looking up an ex-partner's address in motor vehicle records |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile); CSF GV.RR-04 and DE.CM-03 |
| Policy basis | POL-03 Incident Response Policy (4.2, 4.4, 4.5, 4.12); POL-05 4.6; POL-01 4.8 (sanctions) |
| Companion documents | `ir-runbook.md` (ransomware); `notification-matrix.csv`; risk register (P01 R-005, R-029, R-047); STD-02 (access analytics, due 2027-01-31) |
| Runbook owner | Director of Contracts and Compliance (case lead) with the Security Operations Manager (evidence lead) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Insider tabletop with HR and counsel scheduled 2027-02-17 (POL-03 4.8) |

## 0. Why this runbook exists
About 300 staff can reach regulated records: 186 with CJI access, 64 in the FTI enclave, 48 with motor vehicle data, and about 45 support staff with read access to every regulated tenant (P07 AC-6). Unauthorized inspection of FTI is a federal crime even without disclosure (IRC 7213A), and the agency must report it within 24 hours (Pub. 1075 sec. 1.8). Obtaining motor vehicle record information for a use not permitted is unlawful (18 U.S.C. 2722(a)) and gives each individual a civil action with liquidated damages of $2,500 (2724). Today the company cannot detect browsing (P03 PB-18; POAM-006), so most cases will start with a tip or an agency question, which makes speed and evidence handling even more important.

**What makes it different from ransomware.** The suspect is a colleague who may still have access, may see the response, and has employment rights. The response is led by the Director of Contracts and Compliance with counsel and HR, not by IT alone, and it is kept to a small need-to-know group.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Case lead | Director of Contracts and Compliance | General Counsel | Opens the case; agency notices; decision log |
| Evidence lead | Security Operations Manager | Director of Information Security | Pulls and preserves audit records; suspends access |
| Legal | General Counsel with outside employment and breach counsel | n/a | Privilege; interviews; referrals to law enforcement |
| HR | HR Director | HR business partner | Employment actions; interview logistics; sanctions record |
| Data owner contact | The affected agency's security contact (AG-01 disclosure officer; AG-02 local agency security officer; AG-39 terminal agency coordinator; AG-04 records custodian; AG-03 information security manager) | Named alternates | Agency decisions and the agency's own reporting |
| Executive | Chief Operating Officer (severity 1 under POL-03 4.12) | CEO | Approves suspension of a senior employee; external statements |

**Need-to-know.** Only the people above, the suspect's executive (if not involved), and the forensic examiner know about the case. Use the out-of-band channel if the suspect works in IT, security, or cloud operations.

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A colleague reports that someone looked up a record without a reason | Workforce report under POL-05 4.4 | Case lead opens a case within 1 hour of the report |
| An agency asks why a company account viewed a record | Agency security contact | Same; treat the agency question as discovery |
| An individual complains (for example a taxpayer or supervisee who learned their record was viewed) | Agency; customer support | Same |
| Access analytics flag: searches by name with no linked ticket, views of records outside the user's assigned tenant or project, views of staff or celebrity records, bulk exports (live from 2027-01-31) | SIEM weekly review (STD-02) | Security Operations Manager refers to the case lead within 1 hour |
| TIGTA, the IRS Office of Safeguards, a CJIS Systems Agency, or a court asks about access | Agency or counsel | Case lead and counsel open a case at once |

**Declare** when there is reason to believe a workforce member accessed regulated data without a work reason, even before it is confirmed. For FTI, the report to TIGTA and the Office of Safeguards must not wait for an internal investigation (Pub. 1075 sec. 1.8.4). **Record the time of discovery** (T0).

## 3. First 24 hours (RS.MA, RS.MI)
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 h | **Preserve evidence first, quietly:** export the application audit records for the user (all tenants, 1 year back), identity provider sign-ins, and any export or download logs to the evidence store; place a legal hold | Security Operations Manager | Records exported with hashes; hold issued |
| 0-1 h | **Tell the data owner agency (suspected):** AG-01 disclosure officer for FTI (so it can report within 24 hours); AG-02 or AG-39 for CJI (CJISSECPOL IR-6); AG-04 for motor vehicle records; AG-03 for benefits data | Director of Contracts and Compliance | Call logged; written follow-up through the secure channel |
| 0-2 h | **Stop further access:** suspend the user's access to all regulated tenants and agency systems, revoke sessions and tokens, and collect the security key. Choose the method with HR and counsel: administrative leave or a pretext access change, so evidence is not destroyed | Security Operations Manager with HR | Access removed; nothing else changed |
| 0-4 h | Engage counsel (employment and, if a breach is likely, breach counsel through the insurer hotline) | General Counsel | Counsel engaged |
| 4-24 h | **Scope:** which records, which agencies, which data elements, over what period; whether anything was copied, printed, photographed, or disclosed; and whether other users show the same pattern | Security Operations Manager under counsel | Scope memo (privileged) |
| By T0 + 24 h | Confirm with AG-01 that it has reported to TIGTA and the Office of Safeguards; report directly if the company cannot confirm (Pub. 1075 sec. 1.8.2) | Director of Contracts and Compliance | Confirmation recorded |

## 4. Investigation and employee interview (RS.AN)
1. Counsel plans the interview with HR. Two company representatives are present; the employee is told the purpose. Follow company employment policy and any rights the employee has. Do not promise confidentiality or outcomes.
2. Ask for the work reason for each access in the scope memo. Compare answers with tickets, project assignments, and the agency's records.
3. If the facts suggest a crime (for example IRC 7213A for FTI, or misuse of CJI), counsel coordinates any referral with the agency. TIGTA investigates unauthorized access to FTI; the agency and its CJIS Systems Agency decide on CJI referrals. The company does not interview the employee about criminal liability on law enforcement's behalf.
4. Keep the investigation proportionate: look at the employee's access to regulated data, not at unrelated personal activity.

## 5. Determinations and notices (RS.CO)
**Follow `notification-matrix.csv`.** Counsel confirms every notice.

| Decision point | Question | Decider | Basis |
|---|---|---|---|
| D1 | Was the access in good faith for a work purpose? If not, it is a "breach of security" for Florida tenants: good-faith employee access is excluded only if the information is not used for an unrelated purpose (Fla. Stat. 501.171(1)(a)) | Director of Contracts and Compliance with counsel | Scope memo; interview |
| D2 | Date of determination (starts the 10-day notice to each Florida agency, 501.171(6)(a)) | Same | Decision log |
| D3 | Number of individuals affected, by agency and state of residence; data elements | Same | Scope memo |
| D4 | For FTI: has AG-01 completed its TIGTA and Safeguards reports; what does AG-01 need for taxpayer notice decisions (Pub. 1075 sec. 1.8.5; IRC 7431)? | AG-01, with company facts | Agency decision |
| D5 | For CJI: has the sheriff reported the security violation to its CSO and the FBI (Security Addendum 4.01)? The FBI may require further action on the employee's access | AG-02 or AG-39 | Agency decision |
| D6 | For motor vehicle records: has AG-04 informed the state motor vehicle agency under its data-access terms? | AG-04 | Agency decision |
| D7 | Sanction under POL-01 4.8, and notice of the sanction to the agency | HR Director with counsel | Sanctions record |

**Timeline:**
| When | Action | Owner |
|---|---|---|
| T0 + 1 hour | Data owner agency told (section 3) | Director of Contracts and Compliance |
| T0 + 24 hours | AG-01 reports to TIGTA and the IRS Office of Safeguards (FTI cases) | AG-01; company confirms |
| No later than 10 days after determination | Third-party agent notice to each affected Florida agency, with everything it needs for its own notices; State B and State C agencies on the clocks counsel has mapped | Director of Contracts and Compliance and counsel |
| Agency: 30 days after determination | Florida individual notices, and the Department of Legal Affairs if 500 or more Floridians (Fla. Stat. 501.171(3)-(4)) | Agencies |

## 6. Recovery and closure (RC.RP)
- Remove or change access for the employee permanently, or restore it only after the agency agrees in writing.
- If others had the same access without need, reduce it (tenant-scoped support roles, POAM-002).
- Give the agency the final scope, actions taken, and the sanction outcome in writing.
- Complete refresher training within 30 days for staff involved, including witnesses who handled the data (POL-03 4.9; CJISSECPOL AT-2).
- Keep the case file, evidence, and notices for 7 years (POL-01 4.13).

## 7. Prevention lessons (ID.IM)
- Add the pattern to the weekly access analytics rules (STD-02).
- Review the role design that allowed the access (P01 R-005, R-029, R-047).
- Report case counts (not names) to the audit committee each quarter.
- Update this runbook and the notification matrix after each case.
