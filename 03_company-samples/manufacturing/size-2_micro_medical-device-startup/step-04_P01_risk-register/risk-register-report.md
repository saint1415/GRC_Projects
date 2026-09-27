# Risk Register Report: Cris Santos Company | Manufacturing | Micro

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (medical device startup) |
| Size tier | Micro (7 employees) |
| Vertical | Manufacturing (NAICS 334510) |
| Method | NIST SP 800-30 Rev. 1 (Tables G-2 to G-5, H-3, I-2) |
| Also supports | The cybersecurity risk assessment FDA expects in the premarket submission (guidance section V.A.2), for the development and release environment. The device's own threat model and cybersecurity risk assessment are separate design history records (P03 G-024, G-025) |
| Prepared | 2026-07-31 by the QA/RA Manager and the Head of Engineering, with the Operations Manager and the MSP lead technician |
| Updated | 2026-08-12 (R-023 added and R-011 updated from P07 testing); 2026-08-26 (R-018, R-019 reviewed with P10); 2026-08-31 (R-020, R-024 accepted) |
| Approved | 2026-08-31 by the CEO |

## 1. Scope and risk framing
**Scope.** The whole business and its key vendors: the systems in `../00_company-facts.md` section 3 (SYS-01 to SYS-09), the pre-production units, the planned AI-001 function, and the vendors that hold or handle the company's code, keys, and records: the source code and CI service vendor, the eQMS vendor, the cloud provider, the productivity suite vendor, the MSP, and the contract manufacturer.

**Two kinds of harm are rated.** Most risks today hurt the business (schedule, runway, intellectual property). Some are design weaknesses that would hurt patients once WM-1 is in hospitals (R-001, R-002, R-004, R-005, R-021). Those are rated for their impact after clearance, because the design is being fixed now.

**Risk tolerance and who can accept risk:**
- Low and Very Low: the Operations Manager (corporate IT) or the Head of Engineering (product) may accept.
- Moderate: only the CEO may accept, with a treatment plan or a written reason.
- High and Very High: not accepted. The CEO approves a dated treatment plan instead. A risk that could affect patient safety after clearance is never accepted at High.

This is the company's first documented risk assessment. The safety risk management file in the eQMS covers hazards to patients from the device; it is not a cybersecurity risk assessment.

## 2. Method
1. **Identify.** Threat sources and events came from SP 800-30 Appendices D and E, the BIA (P05), the gap analysis (P03), the cloud mapping (P04), and interviews with all 7 employees and the MSP lead technician (2026-07-20 to 2026-07-31).
2. **Rate likelihood.** The likelihood of initiation (adversarial) or occurrence (non-adversarial) was rated, along with the likelihood that the event causes adverse impact. The two were combined with **Table G-5**.
3. **Rate impact.** Impact was rated with **Table H-3**, using the BIA impact categories (P05 section 3). For a startup spending about $190,000 a month, a submission slip of a month or a lost signing key is High or Very High.
4. **Determine risk.** Risk level comes from **Table I-2**. The overall likelihood and risk level columns in `risk-register.csv` were computed from the two tables by script, not assigned by hand.

## 3. Results

| Risk level | Count |
|---|---|
| High | 4 |
| Moderate | 17 |
| Low | 3 |
| **Total** | **24** |

Status: 13 Open, 9 In progress, 2 Closed (R-020 and R-024 accepted).

### Top risks
| Risk ID | Risk | Level | Treatment | Owner | Due |
|---|---|---|---|---|---|
| R-001 | Signing key stolen, misused, or lost | High | HSM-backed key with two-person approval; signing only through the release pipeline | Head of Engineering | 2026-12-31 |
| R-002 | Shared hub maintenance password and shared API key exploited in the field | High | Unique per-device credentials and certificates; maintenance page off by default | Firmware Engineer | 2026-12-31 |
| R-003 | 510(k) held or delayed for incomplete cybersecurity documentation | High | P03 premarket readiness roadmap; pre-submission meeting 2026-11 | QA/RA Manager | 2027-02-26 |
| R-005 | Known exploited vulnerability in a third-party component ships unnoticed | High | SBOM in every build; weekly monitoring against NVD and the KEV catalog | Head of Engineering | 2026-12-31 |
| R-023 | Hub API key readable in CI build logs | Moderate | Logs purged 2026-08-12; rotate the key; per-device certificates | Cloud Software Engineer | 2026-09-30 |
| R-008 | Cloud tenant takeover through the shared owner account | Moderate | Break-glass account; named least-privilege roles; alerts | Cloud Software Engineer | 2026-09-30 |

**The common theme is trust in the release path.** The company signs firmware with a key anyone who steals one laptop could use (R-001), ships every unit with the same secrets (R-002, R-023), cannot see what third-party code it ships (R-005), and has not yet written the documents FDA will ask for (R-003). Fixing R-001, R-002, and R-005 also produces most of the evidence R-003 needs.

**Risks found or changed during the work:**
- R-023: added on 2026-08-12 after P07 testing found the hub API key in CI build logs. The debug step was removed and the logs purged the same day.
- R-011: the P07 assessor found a former firmware contractor's repository account still active 5 months after the engagement ended. It was removed on 2026-08-11. The repository audit log showed no pushes or clones after 2026-03-13.
- R-022: the maintenance page was disabled by configuration on the 8 evaluation hubs, and the partner hospital's security team was told, on 2026-08-14.

## 4. Treatment summary
- **Funded (approved by the CEO on 2026-08-31; about $41,000 one-time and $9,500 a year):**
  - Third-party penetration test of the WM-1 system with one retest: about $28,000 one-time
  - HSM-backed key service, private certificate authority, and release pipeline work: about $1,800 a year plus engineering time
  - SBOM generation and vulnerability monitoring tooling: about $2,400 a year
  - Lab workstations added to the MSP contract (EDR, patching) and lab network segmentation: about $1,500 one-time and $1,200 a year
  - Security awareness training with phishing simulations and a secure embedded development course: about $3,500 one-time and $600 a year
  - ISAO membership for medical device vulnerability sharing: about $3,500 a year
  - Independent assessment and policy work in 2026 (P07, P06): about $8,000 one-time
- **Accepted:** R-020 (Moderate; hurricane, with a pre-storm step for the key backup and lab units), R-024 (Low; laptops encrypted).
- **Contract actions:** security terms in the contract manufacturer quality agreement (R-009) by 2026-12-31; lab workstations added to the MSP contract (R-007, R-016) by 2026-10-31.

## 5. Approval
- CEO: approved all treatment plans, the two acceptances, and the budget on 2026-08-31. Moderate risks R-004, R-006 to R-012, R-014 to R-019, R-021, and R-023 have dated treatment plans and are not accepted.
- Next full review: July 2027, or sooner at design freeze (target 2026-12-31), before the 510(k) is submitted, or after an incident.
