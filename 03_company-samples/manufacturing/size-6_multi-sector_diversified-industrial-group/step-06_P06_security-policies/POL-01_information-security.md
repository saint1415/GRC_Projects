# Information Security Policy (Group)

| Field | Value |
|---|---|
| Organization | Cris Santos Company Holdings, Inc. and all divisions (Medical Devices, Medical Supply Distribution, Engineering and Product Testing Services) and corporate shared services |
| Policy ID | POL-01 |
| Owner | Group CISO |
| Approved by | Board risk committee |
| Effective date | 2026-10-01 |
| Review cycle | Annually (next review 2027-09-30), and after major changes, acquisitions, or incidents |
| Implements (SP 800-53 Rev. 5) | PM-1, PM-2, PM-9, PM-10, PL-1, PL-2, PS-8, RA-3, SA-3, SA-4, SA-9, CA-2, CA-7, CA-8(1), SI-12, SR-3 |
| CSF 2.0 | GV.OC-03, GV.PO-01, GV.PO-02, GV.RR-02, GV.RR-04, GV.RM-01, GV.OV-01, GV.SC-05, ID.RA-01, ID.IM-01 |
| Regulatory basis | FD&C Act 524B(b)(1)-(3) (N31-33-R05); 21 CFR 820.10(c); HIPAA 164.308(a)(1), (a)(2), (a)(8), (b)(1) and 164.316 for the DCC (N62-R01); 48 CFR 52.204-21 and 32 CFR 170.15 for Distribution (N42-R04, N42-R02); Reg S-K Item 106 (N42-R07) |
| Division supplements | Medical Devices supplement (v2026); Distribution supplement (v2025, re-issue due 2026-12-31); Testing supplement (v2025). See `division-supplements.md` |

## 1. Purpose
Set up one information security program for the whole group, assign who is accountable at group and division level, and give every other group policy and every division supplement its authority. The program protects patients who depend on the group's devices, hospital and federal customers, testing clients, and the group's own information and systems.

## 2. Scope
All workforce members of Cris Santos Company Holdings, Inc. and its divisions (employees, contractors, and temporary staff), all systems and data the group owns or operates, including operational technology at plants and distribution centers, laboratory test networks, the device software release chain, and systems operated for the group by service providers, contract manufacturers, and suppliers. Fielded devices are covered for the processes the group controls (design, release, updates, and vulnerability handling).

## 3. Roles and responsibilities
| Role | Responsibility |
|---|---|
| Board risk committee | Oversees cyber and product security risk; approves this policy; accepts Very High risks |
| Group CISO | Owns the program and group policies; operates common controls through SYS-G1 to SYS-G3; co-accepts High risks |
| Group Chief Risk Officer | Owns the group risk register and ERM roll-up (NIST IR 8286 Rev. 1); chairs the Group AI council; co-accepts High risks |
| Group Chief Privacy Officer | Owns data classification and business associate oversight for the DCC |
| Group General Counsel | Owns BAAs, NDAs, federal contract terms, the notification matrix, and the information barrier rules |
| Chief Product Security Officer (Medical Devices) | Owns product security: SPDF, PSIRT, CVD, SBOM, and the 524B(b)(1) monitoring plans |
| Division presidents | Accept Moderate risks for their divisions |
| Division security and compliance leads | Maintain division supplements and registers; accept Low risks |
| DCC HIPAA security official | Designated in writing for the device cloud's business associate duties (45 CFR 164.308(a)(2)) |
| Group internal audit | Independently assesses common controls once and samples division controls |
| Disclosure committee | Decides SEC materiality of cybersecurity incidents |
| All workforce | Follow group policy and their division supplement; report suspected incidents immediately |

## 4. Policy statements
4.1 The group must maintain one information security program aligned to NIST CSF 2.0 that also meets each division's binding requirements: section 524B and the QMSR for Medical Devices, the HIPAA Security Rule for the DCC, and FAR 52.204-21 for Distribution. (PM-1; GV.PO-01)

4.2 The Group CISO is accountable for the program. The Chief Product Security Officer is accountable for product security. Medical Devices must designate a HIPAA security official for the DCC in writing. (PM-2; GV.RR-02; 164.308(a)(2))

4.3 Each division and corporate must complete a risk analysis at least annually and after major changes, using NIST SP 800-30 Rev. 1. Division risks that cross divisions, sit in shared services, or need a group decision must roll up to the group register. (RA-3; PM-9; ID.RA-01; 164.308(a)(1)(ii)(A)-(B))

4.4 **Risk acceptance authority:** Low, the division security and compliance lead; Moderate, the division president; High, the Group Chief Risk Officer with the Group CISO, reported to the board risk committee; Very High, the board risk committee only. Patient-safety risks rated High must be treated, not accepted. (PM-9; GV.RM-01)

4.5 **Division supplements.** A division may add stricter requirements in a written supplement. A supplement must not weaken group policy. Each supplement must be re-aligned within 90 days after a group policy changes, and each division security and compliance lead must attest alignment every year. (PL-1; GV.PO-02)

4.6 **Common controls.** Corporate control providers must maintain the common control catalog. Each division must document, for each of its systems, which controls it inherits and which responsibilities remain with the division, and must confirm that documentation every year. Acquired sites must be brought onto common controls within 12 months of closing, or carry a dated exception. (PL-2; PM-10; CA-2; GV.RR-02)

4.7 **Secure product development.** Every device and related system (device cloud, update service, build and signing pipeline) must be developed under the SPDF procedure in the QMS: threat modeling, security requirements, security testing, SBOM generation in every build, and HSM-held signing keys with two-person approval. No product line may be signed outside the HSM service after 2027-03-31. (SA-3; SR-3; PR.PS-06; 524B(b)(2)-(3); 21 CFR 820.10(c))

4.8 **Vulnerability monitoring and disclosure.** The PSIRT must operate a published CVD policy, monitor every marketed product (including legacy products outside 524B) against vulnerability sources and the CISA KEV catalog, and keep the group's ISAO membership active. (RA-5; SI-5; ID.RA-08; 524B(b)(1))

4.9 **Third parties.** No vendor may receive Restricted information without a security review and the contract terms its data requires: a BAA or subcontractor BAA for PHI, FAR 52.204-21 flowdown for Federal contract information, SBOM and vulnerability notice clauses for software components, and confidentiality terms for testing client data. (SA-9; SA-4; SR-3; GV.SC-05; 164.308(b)(1); 52.204-21(c))

4.10 **Evaluation and independence.** Group internal audit must assess common controls at least annually and sample each division's controls. Any penetration test or security test of a Medical Devices product or system by the Testing division must carry a signed statement that the testers did not design, build, or operate what they test. (CA-2; CA-7; CA-8(1); ID.IM-01; 164.308(a)(8))

4.11 **Exceptions** to any group policy or supplement must be requested in writing, risk-rated, approved under 4.4, recorded in the division register, and limited to 12 months or less. (PL-1)

4.12 Security policies, procedures, risk analyses, assessments, and required actions must be retained for 6 years from creation or last effective date, whichever is later. Records required by the QMSR and 21 CFR 803 and 806 follow the QMS retention schedule when it is longer. (SI-12; 164.316(b)(2)(i))

4.13 **AI systems.** No AI system that is part of a device, processes PHI or client confidential data, or makes or supports decisions about people may be deployed or materially changed without registration in the group AI inventory and approval under the Group AI Standard (P10). (RA-3; PL-2; GV.RM-01)

4.14 **Sanctions.** Workforce members who violate security policies, including the information barrier, must be sanctioned in proportion to intent and harm. HR must document every sanction. (PS-8; GV.RR-04; 164.308(a)(1)(ii)(C))

## 5. Compliance and enforcement
Violations are handled under 4.14. Compliance is checked through the annual common control assessment and division samples (P07), the annual supplement attestations, and division access reviews.

## 6. Exceptions
Exceptions follow section 4.11.

## 7. Related documents
POL-02 to POL-05; `division-supplements.md`; common control catalog (P02); group and division risk registers (P01); Group AI Standard (P10); SPDF and PSIRT procedures (Medical Devices QMS).
