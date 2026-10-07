# Incident Response Runbook: Insider Unauthorized Access to a High-Profile Patient's Record

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed 112-bed community acute-care hospital) |
| Tier / Vertical | Mid-Market / Healthcare and Public Health |
| Incident type | A workforce member (employee, contracted clinician, agency nurse, or affiliated practice user) views or discloses a patient's record without a work reason. Worked example: a local public figure is admitted after a car crash, and several staff open the record within hours |
| Why this incident | It is the most common privacy breach in hospitals, it is the High risk P01 R-014, and today's EHR monitoring would catch it only if the patient was flagged as VIP (gap 7) |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-02 4.13 (EHR access monitoring); POL-03; POL-05 4.2; POL-01 4.8 (sanctions) |
| Companion documents | `ir-runbook.md` (ransomware); `notification-matrix.csv` |
| Runbook owner | Compliance and Privacy Officer (incident lead) |
| Approved | 2026-09-17 by the Chief Operating Officer |
| Last tested | Not yet. Tabletop with HR, the Medical Staff Office, communications, and counsel planned for 2027-02 |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | Decides |
|---|---|---|---|
| Incident lead | Compliance and Privacy Officer | Outside privacy counsel | Investigation scope, breach determination, notices |
| Technical support | Information Security Manager | Security analyst | EHR audit pulls, access analytics, account actions |
| Workforce actions | HR Director (employees); Medical Staff Office Manager (physicians); agency coordinator (agency staff); Director of Physician Services (practice users) | Department leader | Interviews, suspension, sanctions under POL-01 4.8 and the medical staff bylaws |
| Executive escalation | Chief Operating Officer | CEO | High-profile or 500-plus cases; media strategy |
| Communications | Director of Marketing and Communications | Outside crisis PR (through counsel) | Media statements; no comment on any individual patient |
| Patient liaison | Patient experience manager with the Privacy Officer | n/a | Contact with the affected patient or family |
| Law enforcement liaison | Counsel | Director of Security | Referral if theft, sale, or harassment is suspected |

**Confidentiality of the investigation.** Investigate quietly, on a need-to-know basis, and do not access the patient's record more than necessary to investigate. Investigation notes are Restricted (POL-04).

## 1. Preparation checks (Identify / Protect)
- [x] Break-the-glass with reason prompt on VIP-flagged, employee, and behavioral health records (AC-3)
- [x] EHR audit trail kept 6 years in the write-once archive (AU-9, AU-11)
- [x] Sanctions policy and log (PS-8; P03 Met)
- [ ] Behavior-based EHR access analytics with monthly review (POL-02 4.13; POAM-007, due 2026-12-31). **Gap: today only VIP and employee-record alerts**
- [ ] Automatic VIP flag for public figures at registration (P01 R-014). **Gap: flag set manually by the House Supervisor**
- [x] Decision log template with discovery and determination dates (POAM-023, in progress)
- [x] Pre-approved holding statement for media questions about a patient's privacy (counsel-approved 2026-09-17)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| Break-the-glass or VIP access alert | EHR VIP report (daily) | Privacy Officer reviews within 1 business day |
| Analytics alert: many users opening one record, access to coworkers or neighbors, access with no care relationship | Access analytics (from 2026-12) | Privacy Officer reviews within 1 business day |
| Complaint from a patient or family ("someone talked about my visit") | Privacy hotline; patient experience | Open a case the same day |
| Staff report of a coworker's snooping or a social media post | Hotline; supervisor | Open a case the same day |
| Media inquiry about details of a patient's care | Communications | Open a case; holding statement only |

**Severity:** Severity 2 by default. Escalate to severity 1 (CMT involvement) if PHI was posted publicly, sold, or given to the media; if 500 or more individuals are involved; or if a physician with privileges is involved.

**Record the date and time of discovery** (POL-03 4.3). Under 45 CFR 164.404(a)(2), discovery is the first day the breach is known, or by reasonable diligence would have been known, to any workforce member. For the worked example, if a nurse saw a coworker browsing the record on day 1 and said nothing, the HIPAA clock may have started on day 1, not when the complaint arrives.

## 3. First 72 hours
| Time | Step | Who | Done when |
|---|---|---|---|
| Day 0 | Open the case in the incident register with discovery time; preserve the EHR audit trail for the patient (all access since admission) | Privacy Officer; security analyst | Audit export saved to the case file |
| Day 0 | Flag the record as VIP if not flagged; enable break-the-glass | HIM Director | Flag on |
| Day 0-1 | For each user who opened the record, compare the access with the care team, assignments, orders, and documentation; mark each access as explained or unexplained | Privacy Officer with the unit manager | Access table complete |
| Day 1 | For unexplained accesses: restrict or suspend the users' EHR access pending review (HR or the Medical Staff Office decides for employees and physicians; the sponsor for agency and practice users) | HR Director; Medical Staff Office Manager | Accounts restricted |
| Day 1-2 | Interviews with each user (with HR or the Medical Staff Office); written statements | Privacy Officer; HR Director | Statements on file |
| Day 1-3 | Check whether information left the hospital: social media, messages, media contact, printing, screenshots on personal phones | Privacy Officer; Information Security Manager | Disclosure finding recorded |
| Day 2-3 | Widen the search: did the same users open other records without a reason in the last 12 months? | Security analyst | Look-back results |
| Day 3 | Severity review; brief the COO if severity 1 criteria are met | Privacy Officer | Severity confirmed |

## 4. Analysis and breach determination (RS.AN)
An access by a workforce member without a work reason is an impermissible use of PHI. It is **presumed a breach** unless a documented risk assessment shows a low probability that the PHI was compromised (45 CFR 164.402).

**Exception to check first.** The definition of breach excludes an unintentional acquisition, access, or use of PHI by a workforce member acting in good faith and within the scope of authority, if it is not further used or disclosed in a way the Privacy Rule does not permit (164.402, paragraph (1)(i)). A nurse who opens the wrong chart by mistake and closes it may fit this exception. Curiosity browsing does not.

**Four-factor assessment (record each in the decision log):**
| Factor | Questions for this incident |
|---|---|
| 1. Nature and extent of the PHI | Which screens were viewed: demographics only, or diagnoses, toxicology, behavioral health, or photographs? How identifiable? |
| 2. The unauthorized person | Was it a workforce member bound by confidentiality and training, or did it reach someone outside the hospital? |
| 3. Whether PHI was actually acquired or viewed | Audit trail shows screens and time on each; printing or screenshots? |
| 4. Extent to which the risk was mitigated | Signed attestation that the user did not keep or share the information; removal of posts; sanctions |

**Typical outcomes:**
- Viewing by a workforce member with no further disclosure, confirmed by interview and attestation: still usually a reportable breach unless the assessment supports a low probability of compromise. Counsel decides with the Privacy Officer, and the reasoning goes in the log.
- Any disclosure outside the hospital (social media, media, family or friends): a breach; notify.

**Number affected.** Usually 1 patient, plus any others found in the look-back. For the worked example, plan for fewer than 500.

## 5. Containment and corrective action (RS.MI)
1. Remove or restrict the users' access until HR, the Medical Staff Office, or the sponsor decides.
2. Ask any outside recipient or platform to remove posted information; record each request.
3. Apply sanctions in proportion to intent and harm (POL-01 4.8): retraining, written warning, suspension, termination, or loss of privileges; for agency and practice users, removal from the hospital's systems and notice to their employer. Document each sanction in the sanctions log.
4. Report the look-back results and fix the cause (missing VIP flag, missing analytics, unclear role access).

## 6. Notification and communication (RS.CO)
Follow `notification-matrix.csv`. Counsel confirms each notice.

| When | Action | Owner |
|---|---|---|
| As soon as determined | Four-factor assessment and determination recorded (decision log) | Compliance and Privacy Officer |
| Without unreasonable delay | Call the affected patient or the patient's representative before the letter, if counsel agrees; offer a contact person | Privacy Officer; patient liaison |
| Within 30 days of determination | Florida individual notice under Fla. Stat. 501.171(4), or the HIPAA notice with a copy to the Department of Legal Affairs under the deemed-compliance path | Privacy Officer and counsel |
| Without unreasonable delay, no later than 60 days after discovery | HIPAA individual notice by first-class mail (164.404) | Privacy Officer and counsel |
| Within 60 days after the end of the calendar year | HHS breach log entry for breaches under 500 (164.408(c)) | Privacy Officer |
| Only if 500 or more | HHS at the same time as individuals; media if more than 500 residents of a state; Florida Department of Legal Affairs within 30 days | Privacy Officer and counsel |
| If an affiliated practice user was the snooper or a practice patient was viewed | Notify the practice (its own user) or, for a practice's patient, give the practice business associate notice (164.410; services agreement 5 business days) | Director of Physician Services with the Privacy Officer |
| If theft, sale, or harassment is suspected | Referral to law enforcement; any written or oral request to delay notice is handled under 164.412 | Counsel |

**Media.** The hospital never confirms or denies that a person is a patient, beyond what the patient has authorized or the facility directory allows. Statements say only that the hospital investigates every report, takes action under its policies, and notifies affected patients as the law requires.

## 7. Recovery and follow-up (RC.CO, ID.IM)
- Close the case when notices are sent, sanctions are documented, and corrective actions are assigned.
- Brief the unit, without names, on what happened and why access is monitored (POL-05 4.2).
- Update P01 R-014 with the case count and the analytics status; report the case in the quarterly audit committee report.
- Retain the case file, decision log, notices, and sanctions records for 6 years (45 CFR 164.414(b); POL-01 4.13).
- After-action review within 30 days for severity 1 cases.
