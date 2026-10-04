# Incident Response Runbook: Student Identity Fraud (Account Takeover, Refund Diversion, and Fraudulent Applicants)

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (PE-backed private, for-profit college) |
| Tier / Vertical | Mid-Market / Educational Services |
| Incident type | (A) **Student portal account takeover** with changed refund bank details and diverted Title IV credit balance refunds; (B) **fraudulent online applicants** (synthetic or stolen identities) enrolling to obtain Title IV funds. Both can happen together |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Policy basis | POL-03 Incident Response Policy (4.1, 4.4); POL-02 4.4 to 4.6; STD-04 Student identity and account recovery standard |
| Companion documents | `ir-runbook.md` (ransomware); `notification-matrix.csv`; BIA (P05 BP-05, BP-06, BP-09); risk register (P01 R-005, R-006) |
| Runbook owner | Bursar (business lead, variant A), Vice President of Enrollment Management (business lead, variant B), with the Information Security Manager (security lead) |
| Approved | 2026-09-17 by the Chief Information Officer |
| Last tested | Not yet. Fraud tabletop scheduled 2027-01-20 (POAM-014) |

## 0. Why this runbook exists
These are the college's most frequent real losses. In the 2025-26 award year, attackers used reused passwords to take over 23 student portal accounts and diverted $61,400 of credit balance refunds; only $38,000 was recovered, and the college repaid the students. In fall 2025, 310 online applications were flagged as likely fraudulent; 41 reached enrollment and 6 received a Pell disbursement. The cases were handled by the business office and admissions alone: no root-cause analysis, no FSA report, no referral to the Office of Inspector General (OIG), and no check for wider compromise (P07 IR-4, IR-6). This runbook makes them security incidents with legal duties.

## 1. Roles (Govern)
| Role | Primary | Backup | Responsibility |
|---|---|---|---|
| Business lead (A: refunds) | Bursar | Chief Financial Officer | Refund holds, bank recalls, repaying students within the deadline |
| Business lead (B: applicants) | Vice President of Enrollment Management | Director of Admissions Operations | Application holds, identity re-verification, enrollment status |
| Security lead | Information Security Manager | Senior security analyst | Scope, containment, account resets, detection updates |
| Financial aid | Director of Financial Aid | Associate director | Aid holds, disbursement cancellations, return of Title IV funds, FSA coordination |
| Compliance | Chief Compliance Officer | General Counsel | FSA report, OIG referrals, notification decisions, decision log |
| Records | Registrar | Associate registrar | FERPA disclosure records; enrollment status corrections |
| CMT chair (if escalated) | Chief Information Officer | President and CEO | Declares severity 1 (10 or more students, or signs of a wider compromise) |
| Communications | Director of Marketing and Communications | n/a | Student messages and scripts |

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| A student reports a missing refund or an unrecognized bank change | Student; Bursar's office; service desk | Open a security incident (POL-03 4.2); start variant A |
| Several bank changes from the same IP range, device, or bank routing number within a day | SIEM detection (due 2027-01-31, POAM-006); Bursar's daily bank-change report (interim) | Hold all affected refunds; start variant A |
| Credential stuffing against the student portal (many failed sign-ins across accounts) | Identity provider; MSSP | Block sources; force resets for accounts with successful sign-ins; start variant A |
| Applications sharing addresses, phones, devices, or document images; IDs that fail validation | Admissions identity checks; verification service (from January 2027); financial aid verification | Hold the applications and any aid packaging; start variant B |
| A third party (bank, FSA, another college, law enforcement) reports suspected fraud tied to the college | External notice | Start the matching variant; preserve the notice |

**Severity:**
- **Severity 3:** a single account or applicant, no sign of a pattern. Business lead with the security lead.
- **Severity 2:** 2 to 9 accounts or applicants, or any pattern. Chief Compliance Officer engaged.
- **Severity 1:** 10 or more students or applicants, any compromise of staff or servicer accounts, or evidence that records beyond the student's own were accessed. Convene the crisis management team (POL-03 4.4).

**Record the date and time of discovery in the incident log.** Knowledge of any employee starts the FTC 30-day clock if the event turns out to be a notification event (314.4(j)(2)).

## 3. Variant A: account takeover and refund diversion
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 h | Freeze refunds to every bank account changed in the last 30 days for the affected accounts, and to any account sharing the same routing and account number | Bursar | Hold list in the incident log |
| 0-1 h | Disable the affected portal accounts; revoke sessions; reset passwords and MFA through identity-proofed recovery only (STD-04) | Security lead | Accounts secured |
| 0-2 h | Ask the bank to recall or freeze any refund paid in the last 5 business days to a changed account | Bursar | Recall requests sent |
| 0-4 h | Pull sign-in and change history from the identity provider and the SIS for each account: what else the attacker viewed or changed (transcripts, addresses, aid documents) | Security lead | Scope recorded per account |
| 0-4 h | Hunt for the same indicators (IP ranges, devices, routing numbers) across all student accounts | Security lead with the MSSP | Hunt results recorded |
| Same day | **File the FSA breach report** for the suspected breach of student information (SAIG agreement) | Chief Compliance Officer | Intake form submitted |
| Within the 14-day limit | **Pay each affected student the credit balance owed**, by a verified method, no later than 14 days after the credit balance occurred (34 CFR 668.164(h)(2)). If the original payment date leaves less time, pay the same week | Bursar | Payment records |
| Within 5 days | Record the unauthorized disclosure in each affected student's FERPA disclosure record (34 CFR 99.32(a)) | Registrar | Records updated |
| Within 5 days | Notification decisions (section 5) | Chief Compliance Officer with counsel | Decision log |

## 4. Variant B: fraudulent applicants
| Time | Step | Who | Done when |
|---|---|---|---|
| 0-1 day | Hold the flagged applications, any aid packaging, and any pending disbursement | Vice President of Enrollment Management; Director of Financial Aid | Holds in the CRM, SIS, and FAMS |
| 0-2 days | Re-verify identity through the verification service or a live video check against the ID; ask for documents through a channel the applicant did not supply | Admissions identity team | Result per applicant |
| 0-3 days | Link analysis: shared addresses, phones, emails, devices, document images, bank accounts | Security lead with Institutional Research | Ring list |
| 0-5 days | For enrolled students found fraudulent: correct enrollment status with the Registrar; cancel or return Title IV funds as the aid rules require (financial aid office procedure) | Director of Financial Aid; Registrar | Corrections logged |
| Within 10 business days of the credible-information determination (college standard) | **Refer to the OIG** any credible information that an applicant may have used a false identity or committed other fraud in the application (34 CFR 668.16(g)(1)); refer any sign that an employee or the servicer took part (668.16(g)(2)) | Chief Compliance Officer | Referral record |
| As needed | Notify any person whose real identity was stolen to apply, once counsel confirms what can be said | Chief Compliance Officer with counsel | Letters sent |
| Ongoing | Feed indicators into the admissions fraud checks and the CRM | Vice President of Enrollment Management | Rules updated |

**Do not let AI-001 scores drive fraud decisions.** The admissions scoring model (P10) is not a fraud tool. Every hold and every referral rests on identity evidence reviewed by a person.

## 5. Notification and reporting (RS.CO)
**Follow `notification-matrix.csv`.** Typical outcomes:

| Situation | Notices |
|---|---|
| Account takeover of a few students; the attacker saw only those students' records | FSA breach report (suspected breach of student information); FERPA disclosure records; state breach law for each student's state of residence, because a user name with its password is personal information in many states (Florida worked example: Fla. Stat. 501.171(1)(g)1.b.); no FTC notice unless 500 or more consumers |
| Credential stuffing affecting 500 or more students with unauthorized access to customer information (aid or bank data) | All of the above, plus the **FTC notice within 30 days of discovery** (314.4(j)); Florida Department of Legal Affairs if 500 or more Floridians; consumer reporting agencies if more than 1,000 Floridians are notified at once |
| Fraudulent applicants with no access to other people's records | OIG referral (668.16(g)(1)); notice to identity-theft victims as counsel advises; FSA as FSA guidance and counsel direct |
| A staff, servicer, or vendor account was used | Escalate to severity 1; FSA report; OIG referral if Title IV fraud by an agent is suspected (668.16(g)(2)); servicer notice duties under its contract and Fla. Stat. 501.171(6) |

Voluntary reports to the FBI (IC3) are recommended for organized fraud. The cyber insurer is notified through its hotline for any fraud loss, because the policy may cover social engineering and funds transfer losses.

## 6. Recovery and prevention (RC.RP, PR.AA)
- Restore refunds to verified accounts; lift holds only after identity is confirmed.
- Apply the STD-04 controls as each goes live: step-up MFA and prior-contact confirmation for bank changes (2026-11-30), a 3-business-day hold on refunds to new accounts, MFA by default for students (2027-03-31), applicant document and liveness verification (January 2027).
- Add each case's indicators to the SIEM detections and the admissions checks.

## 7. Post-incident (ID.IM)
- Lessons learned within 30 days of closure, with root cause (for example, reused passwords, a help-desk reset verified by date of birth only) and remediation (POL-03 4.12).
- Update P01 R-005 and R-006, the POA&M (POAM-001, POAM-013, POAM-015), and training content (POAM-005).
- Report the events, losses, and referrals in the Qualified Individual's next written board report (314.4(i)(2)).
- Keep the incident file, decision log, payments, and referral records for at least 6 years.
