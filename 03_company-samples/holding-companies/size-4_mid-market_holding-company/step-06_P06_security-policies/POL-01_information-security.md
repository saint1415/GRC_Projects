# Information Security Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. and its subsidiaries (CSC Building Supply, LLC; CSC Home Services, LLC; CSC Fabrication, LLC; CSC Consumer Finance, LLC) |
| Policy ID | POL-01 |
| Owner | vCISO |
| Approved by | CEO (risk appetite approved by the board) |
| Approval date | 2026-09-22 |
| Effective date | 2026-10-01 (replaces the 2024 group policy) |
| Review cycle | Annually (next review 2027-09-30), and after an acquisition, a major change, or a significant incident |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PL-1, PS-8, RA-3, CA-2, CA-5, SA-4, SA-9, SR-6 |
| CSF 2.0 | GV.OC-03, GV.RM-02, GV.RM-05, GV.RR-01, GV.RR-02, GV.RR-04, GV.PO-01, GV.PO-02, GV.OV-01, GV.SC-05, GV.SC-06 |
| FTC Safeguards Rule (Finance) | 16 CFR 314.3(a); 314.4(a), (b), (d)(1), (f), (g), (i) |
| HIPAA (group health plan) | 45 CFR 164.308(a)(1), (a)(1)(ii)(A)-(C), (a)(2), (a)(8), (b)(1); 164.314(b); 164.316 |
| Supporting standards | See `standards-index.md` (STD-01 to STD-13) |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at the holding company and at each subsidiary, and give every other security policy and standard its authority. The program protects the confidentiality, integrity, and availability of group, employee, customer, and plan information and the safety of customers and workers.

For CSC Consumer Finance ("Finance"), this policy set, the System Security Plan, and the Finance supplement form the written information security program required by the FTC Safeguards Rule (16 CFR 314.3(a)). For the group health plan, this policy set and the plan security procedures (STD-13) are the policies and procedures the sponsor maintains for plan ePHI (45 CFR 164.316(a)).

## 2. Scope
All workforce members (directors, officers, employees, contractors, and temporary staff) of Cris Santos Company, Inc. and each subsidiary, at every site and when working remotely. It covers all systems and data the group owns or uses, including the Shared Corporate Services Platform, each subsidiary's own systems, plant equipment, and systems that service providers run for the group. **A company the group acquires comes under this policy on the closing date**, under the day-1 control set in statement 4.13.

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board of directors and audit committee | Approve the risk appetite; the audit committee receives the group cybersecurity report each quarter |
| CEO | Approves group policies and the security budget; accepts High risks |
| CFO | Executive sponsor of the program; system owner of the SCSP; accepts Moderate risks; chairs the monthly cyber risk forum and the Benefits Committee |
| vCISO | Owns this policy and the program strategy; approves standards; reports to the audit committee |
| Security Manager | Runs the program day to day; Qualified Individual for Finance; HIPAA Security Official for the group health plan |
| VP of Information Technology | Operates the shared platform; owns recovery and configuration |
| General Counsel | Legal and regulatory requirements register; breach and notification decisions; contract security terms |
| VP of Human Resources | Security steps in hiring, transfers, and terminations; sanctions; HIPAA Privacy Official for the plan |
| Subsidiary Presidents | Accountable for cybersecurity risk in their subsidiary; approve their staff's access; attend the monthly cyber risk forum; raise any new software, AI feature, or vendor before purchase |
| Finance President | Directs and oversees the Qualified Individual for Finance (16 CFR 314.4(a)(2)) |
| Co-sourced internal audit firm | Independent annual control assessment (P07) |
| All workforce | Follow these policies; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program, documented in POL-01 to POL-05, the supporting standards, and the System Security Plan. Finance must maintain a Finance supplement covering its Safeguards Rule duties, and the Benefits Committee must maintain plan security procedures (STD-13). (PM-1; GV.PO-01; 314.3(a); 164.316(a))
4.2 The Security Manager is the group security lead, Finance's Qualified Individual, and the plan's HIPAA Security Official. Each designation must be in writing and reaffirmed each year. Finance retains responsibility for its compliance, and the Finance President must direct and oversee the Qualified Individual. (PM-2; GV.RR-02; 314.4(a)(1)-(2); 164.308(a)(2))
4.3 A group risk assessment must be performed at least annually (each July) and after an acquisition or major change, using NIST SP 800-30 Rev. 1. It must cover Finance customer information and plan ePHI. Every risk must be recorded in the risk register with an owner, a treatment, and a due date. (RA-3; PM-9; ID.RA-05; 314.4(b); 164.308(a)(1)(ii)(A)-(B))
4.4 **Risk acceptance authority.** Risk owners (director level or above) may accept Low and Very Low risks; the CFO, Moderate; the CEO, High, for up to 12 months with a dated treatment plan, reported to the audit committee. Very High risks may not be accepted, except by a board exception of up to 90 days. Subsidiary Presidents may not accept risks to the shared platform, Finance customer information, or plan PHI. No risk that could plausibly harm a customer or worker may be accepted above Low. (PM-9; GV.RM-02)
4.5 The vCISO must report to the audit committee each quarter on the risk appetite measures, top risks, POA&M status, incidents, and roadmap progress. The Qualified Individual must report in writing to Finance's Board of Managers each September on the status of Finance's program and material matters. (PM-9; GV.OV-01; 314.4(i))
4.6 Security policies must be reviewed at least annually and after major changes, acquisitions, or incidents. Standards must be reviewed at least annually by their owners. (PL-1; GV.PO-02; 164.316(b)(2)(iii))
4.7 Exceptions to any security policy or standard must be requested in writing, risk-rated, approved under 4.4, recorded in the risk register, and time-limited to 12 months or less. (PL-1)
4.8 **Sanctions.** Workforce members who violate security policies must be sanctioned in proportion to intent and harm: retraining, written warning, suspension, or termination. HR must document each sanction; the plan Privacy Official also logs sanctions involving plan PHI. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))
4.9 **Suppliers.** Before any supplier receives access to group systems, employee data, Finance customer information, or plan PHI, procurement must complete a security review scaled to the supplier's tier (STD-03), and the contract must carry security and incident notice terms. Finance service providers need the Finance President's sign-off; plan business associates need a BAA before any PHI is shared. Purchasing must not issue a purchase order without the review, **including subsidiary purchases and new features in existing tools.** (SA-4; SA-9; GV.SC-05; GV.SC-06; 314.4(f); 164.308(b)(1))
4.10 Critical suppliers must be reassessed each year, including a review of their SOC 2 report or equivalent and the controls the group must operate on its side (P09). (SR-6; GV.SC-07; 314.4(f)(3))
4.11 Security controls must be independently assessed at least annually (P07) by an assessor who does not operate them, and after major changes. Results must feed the POA&M. (CA-2; CA-5; 314.4(d)(1), (g); 164.308(a)(8))
4.12 **Change triggers.** New systems, new suppliers with data access, new AI features, and acquisitions must be assessed for security risk before go-live, and the Finance program and plan procedures adjusted where they are affected. (RA-3; GV.RM-06; 314.4(g))
4.13 **Acquisitions.** Before signing, the VP of Corporate Development must complete the cyber due diligence checklist (STD-10). No acquired company may connect to group systems until a compromise assessment is done and the day-1 control set is in place: EDR on every device, MFA on email, removal of the seller's and former providers' administrator access, and backup of key data. Full integration must be complete within 180 days of closing unless the CEO approves an exception. (SA-9; RA-3; GV.SC-06)
4.14 The holding company must protect Finance's customer information as the Safeguards Rule requires and protect plan ePHI as the plan documents require. These duties must be written into the intercompany services agreement and the plan documents. (SA-9; GV.OC-05; 314.4(a)(3); 164.314(b))
4.15 **Monthly cyber risk forum.** The CFO chairs a monthly forum with the subsidiary Presidents, the vCISO, and the Security Manager to review new risks, purchases, incidents, and progress. (PM-9; GV.RM-05)
4.16 Security policies, risk assessments, assessments, and incident records must be kept for at least 6 years from creation or last effective date, whichever is later (STD-12). (SI-12; 164.316(b)(2)(i))
4.17 AI tools that touch Restricted data, or that affect decisions about credit, employment, or customer safety, must be approved through the AI governance process before use (STD-05; P10). (PM-9; GV.RM-01)

## 5. Compliance and enforcement
Violations are handled under the sanctions statement (section 4.8). Compliance is checked through the annual independent assessment (P07), quarterly access reviews, and the metrics reported to the audit committee.

## 6. Exceptions
Exceptions follow section 4.7. They must be written, risk-rated, approved by the right level under section 4.4, and expire within 12 months.

## 7. Related documents
POL-02 to POL-05; `standards-index.md`; System Security Plan (P02); Risk Register and appetite statements (P01); CSF 2.0 group profile and gap analysis (P03); Finance supplement; plan security procedures (STD-13); intercompany services agreement; FTC Safeguards Rule, 16 CFR Part 314; HIPAA, 45 CFR Part 164
