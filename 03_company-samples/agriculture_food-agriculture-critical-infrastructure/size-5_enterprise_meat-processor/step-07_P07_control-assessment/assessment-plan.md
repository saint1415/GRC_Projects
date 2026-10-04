# Security Assessment Plan and Report: Cris Santos Company | Food and Agriculture | Enterprise

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. (publicly traded further processor of meat products) |
| System assessed | Plant Production and Cold-Chain Monitoring System (PPCM), CSC-SYS-PPCM-001, per the SSP (P02), including the enterprise common controls it inherits |
| Tier / Vertical | Enterprise / Food and Agriculture |
| Procedures | NIST SP 800-53A Rev. 5, Release 5.2.0 (determination statements from NIST OSCAL content, `00_universal-framework/frameworks/sp800-53a_objectives.csv`) |
| Assessor(s) and independence | Internal Audit (third line): an IT audit manager, three IT auditors, and a co-sourced OT security specialist under the Chief Audit Executive, who reports functionally to the audit committee. None of the assessors designs or operates the controls; the co-sourced specialist's firm has no other engagement with the company's OT. The GRC team (second line) supported scoping only |
| Assessment window | 2026-07-13 to 2026-08-28 (fieldwork); report issued 2026-09-04; presented to the audit committee and the risk committee on 2026-09-10 |
| Plants tested on site | PLT-03, PLT-05, PLT-07, PLT-08 (see section 2), plus DC-03 for refrigeration controls |
| Also satisfies | Annual assessment for the PPCM authorization (P02 section 4.2); verification evidence for the PLT-07 food defense plan where controls overlap (21 CFR 121.150) |

## 1. Scope and controls selected
Enterprise tier scope: 40 or more controls. **42 controls (AC 5, AT 2, AU 5, CA 1, CM 6, CP 4, IA 3, IR 3, MA 1, PE 1, PS 1, RA 2, SA 2, SC 1, SI 4, SR 1), 293 determination statements.** Controls were selected because they:
- address the Very High and High risks in P01 (multi-plant ransomware, PLT-08, setpoint integrity, cold-chain concentration, refrigeration remote access, recovery);
- support the High gaps in P03 (electronic CCP record integrity, change reassessment, materiality);
- protect formulation and setpoint integrity, the reason the PPCM is categorized High (P02 section 6);
- are common controls the PPCM inherits that no other assessment covered this year (OT remote access, OT monitoring, OT inventory).

Depth and coverage follow SP 800-53A (basic, focused, comprehensive). The last column shows determination statements Satisfied / Other than satisfied.

| Control | Why selected (risk ID or requirement) | Depth | Coverage | Population | Sample | S / OTS |
|---|---|---|---|---|---|---|
| AC-2 | R-021; R-002 | Comprehensive | Comprehensive | About 4,200 IT and OT account events on PPCM components (2026-01-01 to 2026-06-30); 1,310 terminations of plant staff with OT or MES access (96 at PLT-08) | 60 account events (random); 60 terminations (stratified: 50 integrated plants, 10 PLT-08) | 22 / 4 |
| AC-3 | R-004 | Focused | Focused | About 610 MES user accounts | 25 users (random) | 1 / 0 |
| AC-5 | R-003; 21 CFR 121.135(a) | Comprehensive | Comprehensive | About 1,900 recipe and setpoint-range releases in the MES (2026-01 to 2026-06); HMI override logs for 30 days at the 4 sampled plants | 60 releases (random); all overrides in 30 days (312) analyzed | 1 / 1 |
| AC-6 | R-004 | Focused | Focused | 2,140 PAM elevation sessions to MES and OT engineering hosts | 25 sessions (random) | 1 / 0 |
| AC-17 | R-011; R-002; R-006 | Focused | Comprehensive | 65 OT vendors; remote access paths at 8 plants and 4 DCs | 100% | 2 / 2 |
| AT-2 | R-024 | Basic | Focused | About 12,000 workforce (about 9,450 at plants) | 60 training records (random, stratified by plant); phishing results for 6 months | 8 / 2 |
| AT-3 | R-025; 21 CFR 121.4(b)(2) | Focused | Focused | 186 workers assigned to PLT-07 actionable process steps; 41 OT engineers and integrator staff | 25 agency workers and 25 employees at PLT-07 (stratified); 10 OT engineers | 8 / 1 |
| AU-2 | R-013; R-003 | Focused | Focused | n/a (configuration) | 6 event types generated in test at 2 plants and the MES | 5 / 1 |
| AU-6 | R-028 | Comprehensive | Comprehensive | 26 weeks of SOC review records; 52 OT log sources across 8 plants | 5 weeks (random); 100% of OT log sources | 2 / 1 |
| AU-9 | R-013; 9 CFR 417.5(d) | Focused | Comprehensive | 8 plant historians; log archive account | 100% | 1 / 1 |
| AU-11 | R-013 | Basic | Basic | n/a (configuration) | Retention settings inspected | 1 / 0 |
| AU-12 | R-013 | Basic | Focused | n/a (configuration) | 8 historians; MES; records platform | 2 / 1 |
| CA-7 | R-001 | Focused | Basic | 6 monthly metric packages | 3 months (random) | 11 / 0 |
| CM-2 | R-007 | Focused | Focused | About 680 HMIs and 64 OT servers | 60 components (random, 4 plants) | 4 / 1 |
| CM-3 | R-023; 9 CFR 417.4(a)(3) | Comprehensive | Comprehensive | About 610 plant OT changes (2026-01-01 to 2026-06-30) | 40 changes (random, stratified by plant) | 8 / 2 |
| CM-5 | R-003 | Focused | Focused | n/a (configuration) | MES and HMI configuration at 4 plants | 5 / 1 |
| CM-6 | R-016 | Focused | Comprehensive | About 120 OT devices with web or network management interfaces at the 4 sampled plants and DC-03 | 100% | 5 / 1 |
| CM-7 | R-022 | Focused | Focused | HMIs and OT servers at 4 plants | 60 components (random) | 5 / 1 |
| CM-8 | R-063 | Comprehensive | Comprehensive | About 3,300 OT assets in the inventory | 60 physical assets traced to the inventory (random, 4 plants) | 5 / 1 |
| CP-2 | R-005; R-008 | Comprehensive | Focused | n/a (plan) | PPCM contingency plan v3 examined; 6 interviews | 22 / 2 |
| CP-4 | R-008 | Focused | Focused | 8 plant OT restore tests due; 1 MES DR test | 100% | 4 / 1 |
| CP-9 | R-065; 9 CFR 417.5(e) | Focused | Focused | About 4,300 backup jobs for PPCM components in the period | 25 jobs (random); 1 restore observed | 5 / 1 |
| CP-10 | R-008 | Focused | Focused | 1 MES DR test | 100% | 1 / 1 |
| IA-2 | R-013; 9 CFR 417.5(b) | Basic | Focused | About 2,900 records platform and MES users; PLT-08 eHACCP and HMIs | 25 sign-ins (random); PLT-08 walkthrough | 1 / 1 |
| IA-2(1) | R-047 | Focused | Comprehensive | 46 privileged MES, cloud, and OT engineering accounts | 100% | 1 / 0 |
| IA-5 | R-016 | Focused | Comprehensive | About 120 OT devices (as CM-6); PAM vault | 100% | 8 / 2 |
| IR-4 | R-060; 9 CFR 417.3(b) | Focused | Focused | 212 security incidents (68 OT-related) | 25 OT incidents (random) plus all 4 PLT-08 incidents | 11 / 2 |
| IR-6 | R-024 | Basic | Focused | 212 incidents; 20 worker interviews | 25 incidents; 20 workers | 2 / 0 |
| IR-8 | R-010; Form 8-K Item 1.05 | Comprehensive | Focused | n/a (plan) | Plan and materiality playbook examined; interviews with General Counsel, CFO, CISO, SVP FSQA | 15 / 2 |
| MA-4 | R-011 | Focused | Comprehensive | 1,940 vendor sessions through the gateway; legacy paths | 25 sessions (random); 100% of legacy paths | 6 / 2 |
| PE-3 | R-030; 21 CFR 121.135(a) | Basic | Focused | 4 plants | Walkthroughs; 25 badge log entries per plant | 12 / 0 |
| PS-4 | R-021 | Comprehensive | Comprehensive | 1,310 terminations | 60 (same sample as AC-2) | 4 / 1 |
| RA-3 | R-009 | Focused | Basic | n/a | 2026 risk assessment (P01) examined | 8 / 0 |
| RA-5 | R-026 | Focused | Focused | About 1,180 OT vulnerability findings | 60 findings (random) | 7 / 2 |
| SA-9 | R-005; R-064 | Focused | Comprehensive | 38 tier-1 OT and cold-chain vendors | 100% | 4 / 2 |
| SA-22 | R-007 | Focused | Comprehensive | Unsupported component list | 100% | 1 / 1 |
| SC-7 | R-001; R-002 | Comprehensive | Focused | n/a (architecture) | Reachability tests from the corporate network at PLT-05 and from the PLT-08 office VLAN; firewall reviews at 4 plants | 4 / 2 |
| SI-2 | R-026 | Focused | Focused | About 1,180 OT findings and 212 IT patches | 25 IT patches (random); OT findings from the RA-5 sample | 9 / 1 |
| SI-3 | R-001 | Focused | Focused | OT Windows hosts at 4 plants | 100% | 7 / 1 |
| SI-4 | R-028; R-006 | Focused | Focused | 8 plants and 4 DCs | OT monitoring alerts tested at 2 plants; coverage review at all sites | 10 / 2 |
| SI-7 | R-004; R-003 | Comprehensive | Focused | n/a | Release signature verification tested; 60 active setpoints compared with released recipes at 4 plants | 5 / 1 |
| SR-6 | R-064 | Focused | Comprehensive | 38 tier-1 vendors | 100% | 0 / 1 |

## 2. Sampling method
Internal Audit used **attribute sampling** for controls that operate on a population of transactions, and inspection of the full population where a data analytic or a full walk could test every item.
- **Plant selection (two-stage sampling).** OT controls run at each plant, so plants were the first-stage sampling unit. Three plants were selected on risk: PLT-08 (not integrated), PLT-05 (no OT DMZ), and PLT-07 (the only Part 121 facility). One more, PLT-03, was selected at random from the remaining five. Transactions at those plants were then sampled. Results are reported for the PPCM as a whole; a finding at a risk-selected plant is not extrapolated to unselected plants, but the related common control is rated on the evidence.
- **Key manual controls, large populations (over 250 items):** 60 items, random selection, based on 95% confidence, a 5% tolerable deviation rate, and zero expected deviations (the standard attribute sampling table gives 59; rounded to 60). Used for AC-2, PS-4, AT-2, CM-2, CM-7, CM-8, RA-5, and AC-5 releases. Stratified by plant where the population spans plants.
- **Key manual controls, populations of 50 to 250, or high-risk change populations:** 40 items, random selection, from Internal Audit's methodology table. Used for CM-3.
- **Automated or configuration-enforced controls, and lower-risk controls:** the configuration is inspected once, then 25 items confirm it operated consistently through the period. Used for AC-3, AC-6, CP-9, IA-2, IR-4, IR-6, MA-4, and SI-2.
- **Recurring controls:** weekly, 5 occurrences; monthly, 3 occurrences; annual, the single occurrence.
- **Configuration and data-analytic tests:** 100% of the population (for example, all 312 HMI overrides in 30 days at the sampled plants, all 65 OT vendors, all 120 OT devices with management interfaces at the sampled sites).
- **Evaluation:** one deviation in a sample of 60 is tolerable only if the upper deviation limit stays under 5%. Any deviation in a control that protects formulation or setpoint integrity (AC-5, CM-5, SI-7) or CCP record integrity (AU-9, IA-2) makes the statement Other than satisfied.

Random selections used the audit software's seeded random number generator; seeds and selections are in the workpapers (EV references).

## 3. Methods and objects
- **Examine:** policies and standards (P06), the SSP (P02), identity governance and PAM records, OT directory exports, MES workflow and release records, HMI override logs, historian and records platform configuration, OT change tickets and PLC download events, backup and DR test reports, vulnerability reports, the vendor register, the incident response plan and materiality playbook, disclosure committee minutes.
- **Interview:** Vice President, Engineering; Director of OT Security; Director of Security Operations; Director of Identity and Access Management; Director of Refrigeration and Process Safety; SVP FSQA; the four sampled plants' Plant Managers, FSQA managers, and controls engineers; General Counsel; CFO; CISO; 20 randomly selected plant workers.
- **Test:** access tests with test accounts in the MES validation environment; release signature verification; comparison of 60 active HMI setpoints with released recipes; credential tests on OT management interfaces (with vendor approval, during sanitation windows); reachability tests from the corporate network at PLT-05 and from the PLT-08 office VLAN; OT monitoring test alerts; a backup restore observation; a deletion attempt against the log archive.

## 4. Rules of engagement
- **No testing could affect food safety or worker safety.** OT tests ran only during scheduled sanitation windows with no product on the lines, with the plant controls engineer and the plant FSQA manager present. No test wrote to a PLC, changed a setpoint, or touched a safety instrumented function or ammonia detection.
- Refrigeration controller tests at DC-03 and PLT-05 were read-only, with the Director of Refrigeration and Process Safety's approval and a refrigeration technician present, following the PSM site rules.
- MES tests ran only in the validation environment.
- Reachability tests used an audit-owned laptop with no company data, pre-approved by the CISO and the plant managers, and stopped at the first successful connection to an OT host.
- No formulation or food defense content left company systems. Screenshots in workpapers are redacted.
- Critical exposures were reported to the CISO and the system owner within 24 hours. One was: manufacturer default passwords on the DC-03 refrigeration controller and two PLT-04 X-ray systems (reported 2026-08-13; changed 2026-08-14).
- Findings were validated with control owners before the report was issued.

## 5. Schedule and deliverables
| Date | Milestone |
|---|---|
| 2026-07-13 | Kickoff; document requests |
| 2026-07-20 to 2026-08-21 | Fieldwork (examine, interview, test); plant visits in sanitation windows: PLT-03 (2026-07-25), PLT-07 (2026-08-01), PLT-05 and DC-03 (2026-08-13), PLT-08 (2026-08-15) |
| 2026-08-24 to 2026-08-28 | Finding validation with control owners |
| 2026-09-04 | Report issued to the COO, CISO, Vice President, Engineering, and SVP FSQA |
| 2026-09-10 | Presented to the audit committee and the risk committee |

Deliverables: this plan and report, `assessment-results.csv` (293 rows), and `poam.csv` (24 items).

## 6. Results summary
| Result | Determination statements |
|---|---|
| Satisfied | 244 |
| Other than satisfied | 49 |
| **Total** | **293** |

**Controls with at least one Other than satisfied statement: 34 of 42:** AC-2, AC-5, AC-17, AT-2, AT-3, AU-2, AU-6, AU-9, AU-12, CM-2, CM-3, CM-5, CM-6, CM-7, CM-8, CP-2, CP-4, CP-9, CP-10, IA-2, IA-5, IR-4, IR-8, MA-4, PS-4, RA-5, SA-9, SA-22, SC-7, SI-2, SI-3, SI-4, SI-7, SR-6.

**Fully Satisfied (8):** AC-3, AC-6, AU-11, CA-7, IA-2(1), IR-6, PE-3, RA-3.

**Fully Other than satisfied:** SR-6 (a single determination statement).

**Themes:**
1. **Two non-conforming plants.** PLT-08 and PLT-05 account for most findings in boundary protection (SC-7), remote access and maintenance (AC-17, MA-4), monitoring (SI-3, SI-4, AU-6), inventory (CM-8), baselines (CM-2, CM-7), and backups (CP-9). The common controls work where they have been deployed; they have not been deployed there yet.
2. **Setpoint integrity has one weak link.** The central MES enforces two-person approval and signs every release (AC-5 in the MES, SI-7 on receipt). At the HMI, supervisors overrode cure and brine setpoints 312 times in 30 days at the sampled plants without a second person, a central log, or a comparison with the released recipe (AC-5, AU-2, CM-5, SI-7). Most overrides were routine adjustments, but none was reviewed by FSQA.
3. **Recovery is not yet proven at enterprise scale** (CP-2, CP-4, CP-10).
4. **Disclosure readiness for a food company's likely material incident** (IR-8).
5. **People controls at the edges:** plant awareness completion, agency food defense training, and late OT account removal (AT-2, AT-3, PS-4, AC-2).

**Strengths:** physical access to restricted rooms (PE-3), least privilege and PAM (AC-6, IA-2(1)), the log archive (AU-11, AU-9 for the archive), continuous monitoring reporting (CA-7), workforce incident reporting (IR-6), and the risk assessment process (RA-3) were all Satisfied.

**New finding during testing:** manufacturer default passwords on the DC-03 refrigeration controller and two PLT-04 X-ray systems (IA-05e.). Added to the risk register as R-016 and to POAM-012.

## 7. POA&M summary
`poam.csv` holds 24 items: 19 from this assessment, 3 carried from the P03 gap analysis (POAM-006, POAM-023, POAM-024), and 2 from the AI council review in P10 (POAM-020, POAM-021), so leadership tracks one list.

| Risk level | Items |
|---|---|
| High | 12 |
| Moderate | 11 |
| Low | 1 |

| Status | Items |
|---|---|
| In progress | 19 |
| Open | 5 |

## 8. Conclusion
Internal Audit concludes that the PPCM control environment is **effective with exceptions**. Enterprise common controls for privileged access, logging, physical security, and monitoring operate effectively where they are deployed. The exceptions concentrate in the two plants that do not yet meet the plant OT standard (PLT-05 and PLT-08) and in one enterprise-wide design gap, HMI setpoint overrides. Management accepted all findings and committed to the POA&M dates. The COO used this report for the conditional authorization in P02 section 4.2.
