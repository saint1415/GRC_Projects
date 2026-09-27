# Enterprise Risk Register Report: Cris Santos Company | Manufacturing | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded connected medical device manufacturer; plants FL-1, MN-1, TX-1) |
| Size tier | Enterprise (12,000 employees) |
| Vertical | Manufacturing (NAICS 334510) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) for each risk; NIST IR 8286 Rev. 1 for integration into enterprise risk management (ERM) |
| Also satisfies | HIPAA risk analysis and risk management for the business associate services (45 CFR 164.308(a)(1)(ii)(A)-(B)); the security risk management input to section 524B processes (21 U.S.C. 360n-2(b)(2)); input to the Reg S-K Item 106 description of risk management processes |
| Prepared | 2026-06-01 to 2026-07-31 by the GRC team with the Product Security Office for the CISO; updated 2026-08-28 with Internal Audit findings (P07) |
| Approved | Executive risk committee (chaired by the Chief Risk Officer), 2026-09-08; reviewed by the risk and technology committee of the board, 2026-09-10 |

## 1. Scope and risk framing
**Scope.** Enterprise IT, the three plants and their OT networks, the Device Data Cloud (DDC), the RCM platform, the Consumer Health Platform, the Device Software Factory, the fielded device fleet, the acquired infusion business, and about 2,400 suppliers. Business processes and impact values come from the enterprise BIA (P05). DSF-MES is also covered at system level in the SSP (P02).

**Two kinds of cybersecurity risk.** A device maker carries risk to its own operations and data (enterprise risk) and risk to patients through its products (product risk). Both use the same method and scale here. Product security risk assessments for each device, which rate exploitability and patient harm as FDA's premarket guidance describes, live in each product's risk management file under the QMS. This register carries the enterprise view of those product risks, so the board sees them next to plant, data, and disclosure risks.

**Three lines.** Risk owners in the business, engineering, and IT (first line) own and treat risks. The GRC team and the Chief Risk Officer (second line) run this method and roll risks up into the enterprise risk register. Internal Audit (third line) tests controls independently (P07).

**Risk appetite (board-approved, 2026-02).** Qualitative statements set by the board:
- **Patient safety:** very low appetite for harm to patients from the cybersecurity of devices or services.
- **Product integrity:** very low appetite for any path by which unapproved code could reach a fielded device.
- **Regulatory and disclosure:** very low appetite for noncompliance with FDA, HIPAA, FTC, or SEC requirements.
- **Operations continuity:** low appetite for disruption of patient-facing services; moderate for plant disruption covered by finished-goods buffers.
- **Health data:** low appetite for unauthorized disclosure of patient or consumer health data.
- **Growth and innovation (acquisitions, AI):** moderate appetite, provided risks are identified and funded before or at the time of the decision.

**Risk tolerance (measurable, per enterprise risk).** The highest residual risk level each enterprise risk may carry without a board-reported treatment plan. A risk above its threshold is **Outside tolerance** in the register.

| Enterprise risk | Tolerance threshold |
|---|---|
| ER-01 Patient safety from product and service cybersecurity | Low |
| ER-02 Software and firmware supply chain integrity | Low |
| ER-03 Operations continuity: IT, cloud, and plants | Moderate |
| ER-04 Compromise of patient and consumer health data | Moderate |
| ER-05 Third-party, supplier, and contract manufacturer risk | Moderate |
| ER-06 Regulatory, product compliance, and disclosure | Low |
| ER-07 Integration of the acquired infusion business | Moderate |
| ER-08 Responsible use of AI | Moderate |

**Who can accept risk:**
| Residual level | Acceptance authority |
|---|---|
| Very Low, Low | Risk owner (vice president or director) with GRC concurrence |
| Moderate | CISO with the accountable executive (the VP Product Security and the CQRO must concur for product risks) |
| High | Executive risk committee (Chief Risk Officer, CIO, CTO, COO, CISO, CQRO, General Counsel), reported to the board risk and technology committee |
| Very High | CEO and CFO jointly, reported to the board risk and technology committee at its next meeting |

Patient-safety and product-integrity risks (ER-01, ER-02) at High or above cannot be accepted without a dated treatment plan. Any acceptance expires after 12 months.

## 2. Method
1. **Identify.** Threat sources and events from SP 800-30 Appendices D and E, the medical device threat picture (exploitation of fielded devices, software supply chain attacks, ransomware against manufacturers), the BIA (P05), the gap analysis (P03), PSIRT and ISAO intelligence, and the Internal Audit assessment (P07).
2. **Rate likelihood.** Likelihood of initiation (adversarial) or occurrence (non-adversarial), and likelihood of adverse impact, combined with **Table G-5**.
3. **Rate impact.** **Table H-3**, calibrated to the BIA impact values (P05 section 3). Patient harm across many hospitals is Very High.
4. **Determine risk.** **Table I-2**. The `overall_likelihood` and `risk_level` columns were computed by script from the tables, not assigned by hand.
5. **Integrate with ERM (NIST IR 8286 Rev. 1).**
   - Each cybersecurity risk is a row in this register, with an owner, a treatment, and a key risk indicator (KRI).
   - Each row is normalized into one of **8 enterprise risks (ER-01 to ER-08)** in the Chief Risk Officer's enterprise risk register, with an ERM category.
   - **Aggregation rule:** an enterprise risk's exposure equals its highest constituent risk level, and the profile also reports how many constituent risks sit outside tolerance. This keeps one severe risk from being averaged away.
   - The enterprise risk profile (section 4) is what the board risk and technology committee sees each quarter.

## 3. Results
| Risk level | Count |
|---|---|
| Very High | 1 |
| High | 10 |
| Moderate | 30 |
| Low | 24 |
| **Total** | **65** |

By threat source type: Adversarial 28, Structural 28, Accidental 7, Environmental 2.
By treatment: Mitigate 55, Accept 7, Avoid 2, Share/Transfer 1.
By status: In progress 34, Open 24, Closed (accepted) 7.
**24 risks are outside tolerance** and each has a dated treatment plan.

## 4. Enterprise risk profile (roll-up for the board)
| ID | Enterprise risk | ERM category | Risks | Very High | High | Moderate | Low | Exposure (highest) | Tolerance | Outside tolerance |
|---|---|---|---|---|---|---|---|---|---|---|
| ER-01 | Patient safety from product and service cybersecurity | Clinical and product safety | 11 | 1 | 3 | 3 | 4 | **Very High** | Low | 7 |
| ER-02 | Software and firmware supply chain integrity | Operational and product | 12 | 0 | 3 | 7 | 2 | **High** | Low | 10 |
| ER-03 | Operations continuity: IT, cloud, and plants | Operational | 7 | 0 | 1 | 1 | 5 | **High** | Moderate | 1 |
| ER-04 | Compromise of patient and consumer health data | Compliance and reputational | 9 | 0 | 1 | 2 | 6 | **High** | Moderate | 1 |
| ER-05 | Third-party, supplier, and contract manufacturer risk | Operational | 5 | 0 | 0 | 5 | 0 | **Moderate** | Moderate | 0 |
| ER-06 | Regulatory, product compliance, and disclosure | Compliance | 7 | 0 | 1 | 3 | 3 | **High** | Low | 4 |
| ER-07 | Integration of the acquired infusion business | Strategic | 8 | 0 | 1 | 5 | 2 | **High** | Moderate | 1 |
| ER-08 | Responsible use of AI | Strategic and clinical | 6 | 0 | 0 | 4 | 2 | **Moderate** | Moderate | 0 |

**Reading the profile:**
- **ER-01 (patient safety)** carries the only Very High risk: exploitation of legacy fielded devices (R-001). The VM-500 operating system reaches end of support in 2027-06, and 62,000 IV-300 pumps still use first-generation wireless modules (R-008, R-009).
- **ER-02 (supply chain integrity)** has the most risks outside tolerance (10), because its tolerance is Low and three conditions add up: the legacy IV-300 signing workstation (R-010), unsigned firmware build provenance (R-002), and checksum-only programming at MN-1 (R-022). Internal Audit's finding of default passwords on MN-1 fixture controllers added R-062.
- **ER-06 (regulatory and disclosure)** is outside tolerance mainly because the SEC materiality process has never been exercised for a fielded-device incident, where field actions, FDA reports, and customer systems raise questions a ransomware scenario does not (R-017).
- **ER-07 (acquisition)** has one High risk, MN-1 ransomware reaching OT (R-020), but it also drives risks recorded under other enterprise risks (R-008, R-010, R-022, R-062). Integration is due 2027-06-30.
- **ER-05 and ER-08** are within tolerance, but both depend on actions due in 2026 Q4 (supplier BAAs, AI reviews).

## 5. Top risks (Very High and High)
| Risk ID | Risk | Level | Enterprise risk | Treatment | Owner | Due |
|---|---|---|---|---|---|---|
| R-001 | Exploitation of a legacy fielded device (VM-500 or IV-300 first-generation) at multiple hospitals | Very High | ER-01 | Customer advisory; module swap and replacement programs; end-of-support dates; edge isolation (POAM-023) | VP Product Security | 2027-06-30 |
| R-002 | Malicious or unapproved code is built, signed, and distributed | High | ER-02 | Signed firmware provenance (POAM-004); promotion gate for all lines (POAM-010); reproducible builds | Chief Technology Officer | 2027-03-31 |
| R-003 | Ransomware across enterprise IT and plants | High | ER-03 | MN-1 segmentation (POAM-006); OT-compatible EDR; enterprise exercise | CISO | 2027-03-31 |
| R-004 | RCM outage delays urgent arrhythmia notifications | High | ER-01 | Automate recovery; retest (POAM-026) | Vice President, Remote Monitoring Services | 2027-01-31 |
| R-005 | PHI exfiltration from the DDC or RCM platform | High | ER-04 | Egress anomaly detection; data minimization | Director of Security Operations | 2027-03-31 |
| R-008 | Unauthorized drug library pushed through a first-generation IV-300 key | High | ER-01 | Module swap; key rotation; library signature check (POAM-023) | Vice President, Integration Management Office | 2027-06-30 |
| R-009 | VM-500 end-of-support operating system | High | ER-01 | End-of-support notice; trade-in; extended OS support (POAM-023) | VP Product Security | 2027-06-30 |
| R-010 | Legacy IV-300 signing key stolen, misused, or lost | High | ER-02 | Migrate to the HSM service (POAM-001); log forwarding (POAM-011) | Director of Build and Release Engineering | 2027-01-31 |
| R-017 | Late or inaccurate disclosure of a material fielded-device incident | High | ER-06 | Device scenario in the playbook; tabletop 2026-11-19 (POAM-014) | General Counsel | 2026-11-30 |
| R-020 | Ransomware or OT intrusion stops MN-1 pump production | High | ER-07 | Segmentation (POAM-006); MES replacement (POAM-009) | Vice President, Integration Management Office | 2027-03-31 |
| R-022 | Tampered firmware loaded at MN-1 stations | High | ER-02 | Signature verification at stations (POAM-019) | Vice President, Manufacturing Systems | 2027-03-31 |

## 6. Themes from the 2026 analysis
1. **Legacy products (ER-01).** Section 524B does not reach the 2019 VM-500 clearance or the 2021 IV-300 clearance, but the company still has to monitor and fix those devices under its QMS, MDR, and correction duties and FDA's postmarket guidance. Their older designs (shared keys, an operating system near end of support) are the main reason R-001 is Very High.
2. **The code-to-device path (ER-02).** The HSM service, two-person signing, and SBOMs are strong for current lines. The weak points are the exceptions: the legacy signing workstation (R-010), CI runner tokens (R-011), missing firmware provenance (R-002), and MN-1 stations (R-022, R-062).
3. **The acquired infusion business (ER-07).** MN-1 carries a flat OT network, shared logins, an unsupported MES, vendor remote tools outside PAM, and late terminations (R-020, R-021, R-023, R-054, R-055). Integration funding is approved and due 2027-06-30.
4. **Business associate and consumer duties (ER-04, ER-06).** Five inherited subcontractors lack BAAs (R-024), customer notice terms are not all captured (R-018), and the consumer app needs an FTC rule procedure and kit governance (R-006).
5. **Disclosure (ER-06).** A fielded-device scenario raises materiality questions the ransomware playbook does not cover: patient safety, field actions and their cost, FDA reports, and incidents that start in customer systems (R-017).
6. **AI (ER-08).** Four of 11 use cases lack committee review, and AI-001 training data under-represents women and patients with a BMI of 35 or more (R-038, R-039).

## 7. Treatment summary
- **Funded (2026 Q4 to 2027 Q2), about $14.6 million:** IV-300 first-generation module swap program brought forward ($7.8M), MN-1 OT segmentation and MES replacement ($2.9M), MN-1 identity federation and PAM for vendors ($0.9M), legacy signing migration into the HSM service with a new key ceremony ($0.35M), firmware provenance and runner workload identity ($0.6M), VM-500 extended OS support contract ($1.2M), RCM recovery automation ($0.4M), supplier SBOM program and binary analysis tools ($0.3M), consumer app kit governance ($0.15M), and outside counsel for the disclosure tabletop ($0.04M). Items map to the POA&M in P07.
- **Accepted (7):** R-029, R-044, R-047, R-050, R-052, R-059, R-063. Each is Low residual with strong existing controls, accepted at the right level (section 1) and reviewed within 12 months.
- **Avoided (2):** R-040, R-041. Unapproved generative AI domains are blocked, and AI resume ranking is disabled until review.
- **Transferred in part (1):** R-048, hurricane damage, through property and business interruption insurance plus DC-2 failover.
- **Very High risk R-001:** not accepted as is. The CEO and CFO approved the treatment plan and a residual target of High on 2026-09-08; the board risk and technology committee reviewed it on 2026-09-10.

## 8. Board reporting
**Risk and technology committee of the board (quarterly):** the enterprise risk profile (section 4), every Very High and High risk with its treatment status and KRI trend, risks outside tolerance, new risks since the last meeting (R-062 this quarter), field actions and customer advisories issued, and risk acceptances made. The 2026-09-10 meeting received this report, the Internal Audit results (P07), and the regulatory roadmap (P03).
**Audit committee (quarterly):** Internal Audit results, SOX IT general control status (R-049), and the disclosure controls topics (R-017, R-019). The audit committee also reviews the annual Item 106 disclosure draft, which describes this process.
**Management:** the executive risk committee meets monthly and reviews KRIs for all risks outside tolerance.

## 9. Approval
- Executive risk committee: approved the register, treatments, and acceptances, 2026-09-08.
- CEO and CFO: approved the treatment plan and residual target for Very High risk R-001, 2026-09-08.
- Risk and technology committee of the board: reviewed the enterprise risk profile, 2026-09-10.
- Next full review: June to July 2027, or sooner after a major change, incident, acquisition, or new product launch. KRIs are refreshed quarterly.
