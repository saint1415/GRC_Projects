# AI Risk Assessment: Predictive Maintenance for Non-Safety Plant Equipment

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radioactive and hazardous waste processor) |
| Tier / Vertical | Small / Nuclear Reactors, Materials, and Waste |
| AI use case | AI-001: predictive maintenance pilot on 6 plant assets since April 2026 |
| Framework | NIST AI RMF 1.0 (AI 100-1). AI 600-1 is not applied to AI-001, which is not generative. It is referenced for AI-002 |
| Assessor / date | Maintenance and Controls Supervisor with the IT Manager and the Radiation Safety Officer, 2026-08-25 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. GOVERN
- **Accountable owner:** Maintenance and Controls Supervisor.
- **Decision authority:** General Manager (Medium tier), or the President if the use case is re-tiered High.
- **Required reviewer:** the RSO must review any change that touches exhaust ventilation. Exhaust ventilation supports airborne contamination control during open waste handling, even though the fans are not credited as safety equipment.
- **Policies that apply:**
  - POL-01 4.9: security review and terms before any vendor connects to the OT network
  - POL-05 4.8: approved AI tools only
  - POL-04 4.4: no Security-Related or Restricted data in AI tools
- **Approved-tools list:** kept by the IT Manager. It lists AI-001 (pilot, 6 assets). No generative AI tool is approved yet (AI-002).
- **Scale for a Small company:** there is no AI committee. The Maintenance and Controls Supervisor, IT Manager, and RSO review AI use cases quarterly.

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Detect developing mechanical faults early and estimate remaining useful life, so maintenance can be planned during scheduled outages instead of after a breakdown |
| Assets in scope | Supercompactor hydraulic pump and motor, shredder gearbox, conveyor drive, drum handler, and 2 exhaust fan motors |
| Users / operators | Maintenance and Controls Supervisor and 3 maintenance technicians |
| Affected people | Indirectly: plant operators and health physics staff if equipment fails during work. No decisions are made about individuals |
| Data | Inputs: vibration, temperature, and motor current from wireless sensors; read-only PLC tags (run hours, load) through the on-site gateway; work order history. Outputs: anomaly scores, fault class, remaining-useful-life estimate. No personal data enters the model. Work orders name technicians, but that field is not sent to the vendor |
| Build or buy | Buy: vendor SaaS with a vendor-installed sensor gateway. **The gateway has its own cellular link and is connected to an OT switch. It was installed without a security review** (P01 R-016; P03 G-068) |
| Not intended | Automatic control of any equipment; changing PLC setpoints; extending or skipping time-based preventive maintenance; any use on radiation monitors, the vault security systems, or HEPA filter testing; evaluating technician performance. Enabling any of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules | None found | The vertical profile lists no sector AI rule. No NRC or Florida rule on AI use by materials licensees was identified. The license's radiological controls (ventilation during open handling, effluent monitoring under Chapter 64E-5) stay in force whatever the model says |
| 10 CFR Part 37 | Not directly | The model does not touch the vault or security systems. The gateway is a network security issue, handled under POL-01 4.9 and POAM-002 |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims. Keep the marketing and proposal claims the company relied on in the procurement file |
| State AI laws (e.g., Colorado SB26-189, Texas TRAIGA) | No | AI-001 makes no consequential decisions about individuals, and the company operates only in Florida. If the tool were ever used to judge technician performance, it would become an employment use and require a new assessment |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal/projects/P10_ai-governance/README.md`), with conditions.

**Why not High.** The rubric makes a use case High if it "can affect physical safety or critical infrastructure operations." AI-001 is advisory only:
- A person decides every maintenance action.
- The model cannot write to PLCs.
- Time-based maintenance is never reduced because of it.

The model can prompt earlier maintenance, but it cannot cause equipment to run longer than it otherwise would.

**Why not Low.** It runs in a critical infrastructure sector, its inputs come from the OT network, and a missed alert on an exhaust fan could degrade airborne contamination control.

**The tier depends on conditions.** Until the gateway is confirmed read-only and moved behind the OT firewall, the company cannot show that the vendor path cannot change PLC values. Until then, the pilot is limited to the current 6 assets, with no expansion.

**Escalation triggers (re-tier to High and re-assess):**
- any write access to PLCs or automatic actions
- use of model output to extend or skip time-based maintenance
- expansion to radiation monitors, security systems, or HEPA filter decisions
- use of the data to evaluate individual employees

## 4. MEASURE
| Trustworthy characteristic | Test / metric | Result (pilot, April-August 2026) | Pass? |
|---|---|---|---|
| Valid and reliable | Precision (confirmed alerts / all alerts) of at least 60%; recall on known degradation events of at least 80%; median lead time of at least 7 days | 23 alerts, 14 confirmed (61%); 4 of 5 known events caught (80%); median lead time 11 days. Missed: conveyor drive bearing | Yes (at threshold) |
| Safe | No maintenance deferred or skipped because of model output; exhaust fan alerts reviewed by the RSO | 0 deferrals; 7 fan alerts, all reviewed | Yes |
| Secure and resilient | Gateway security review; outbound-only connection behind the OT firewall; read-only PLC access verified; vendor SOC 2 or equivalent | Not reviewed; own cellular link; read-only access claimed by the vendor, not verified; no SOC 2 received | **No** |
| Accountable and transparent | Every alert and decision logged in the work order system with the approver | 23 of 23 logged | Yes |
| Explainable and interpretable | Each alert shows which sensor and feature drove it | Available in the vendor dashboard | Yes |
| Privacy-enhanced | No personal data sent; contract bars vendor reuse of company data for other customers without consent | No personal data sent; data-use terms not in the contract | **No** |
| Fair, with harmful bias managed | See the bias testing plan below | Exhaust fan false-alarm rate 57% (4 of 7 alerts) vs 31% (5 of 16) for other assets; overall 39% (9 of 23) | **No.** Disparity flagged |

**Bias and fairness testing plan.** AI-001 makes no decisions about people, so bias here means **uneven performance across asset groups and operating conditions**. Uneven performance can hide failures on the equipment that matters most.
- **Groups compared:**
  - asset type (exhaust fans, hydraulic, gearbox and drives)
  - operating condition (high-throughput days vs normal days)
  - season (June to September heat vs the rest of the year)
- **Metrics:** false-alarm rate, recall, and sensor data completeness for each group.
- **Threshold:** flag if any group's false-alarm rate exceeds the overall rate by more than 15 percentage points, or its recall falls below the overall rate by more than 15 points.
- **Cadence:** quarterly, plus before any expansion.
- **Finding:** the exhaust fans' false-alarm rate (57%) is 18 points above the overall rate (39%). The likely causes are the vendor's training fleet, which is mostly manufacturing fans with different duty cycles, and 9% sensor data dropouts at the fan location. Actions:
  - The vendor must retrain on site data.
  - Sensor placement will be fixed.
  - Until the gap closes, fan alerts are advisory and never reduce the RSO's attention to ventilation.
- **People.** The model must never be used to rate technicians. The work order approver field is excluded from any vendor analytics.

## 5. MANAGE
**Human-in-the-loop design:**
- The model creates draft work orders only.
- The Maintenance and Controls Supervisor approves, changes, or rejects each one.
- Exhaust fan alerts are also sent to the RSO, who decides whether open waste handling should pause.
- Time-based preventive maintenance and HEPA filter testing continue on their existing schedules, regardless of model output.

**Security conditions (due 2026-10-31):**
- The IT Manager completes a security review of the gateway.
- The gateway moves behind the OT firewall with outbound-only rules.
- Read-only PLC access is verified by a test with the controls integrator.
- The vendor signs the security addendum (named accounts, MFA, 24-hour incident notice).

**Monitoring:**
- Monthly performance report (precision, recall, lead time, data completeness), tracked in the risk register (R-027).
- Quarterly asset-group comparison under the bias testing plan.

**Incident handling:**
- A missed failure is reviewed by the Maintenance and Controls Supervisor and the vendor.
- Suspicious gateway behavior follows P08. The gateway is disconnected first.

**Decommissioning:**
- Disconnect the gateway and stop the pilot if the security conditions are not met by 2026-10-31.
- Stop if precision falls below 50% for 2 consecutive months.
- Stop if the vendor changes its data-use terms.
- On exit, the vendor must return or delete company data, with written confirmation.

## 6. Decision
**Approve with conditions.** General Manager, 2026-08-31. The pilot may continue on the current 6 assets **only if** the following are met by 2026-10-31:
1. The gateway security review, firewall placement, and read-only verification are complete (POAM-016; P01 R-016).
2. The contract includes the security addendum and data-use terms (no reuse of company data, return or deletion at exit).
3. The vendor has a retraining plan for the exhaust fan false-alarm gap.

Expansion beyond 6 assets requires two consecutive quarters with no bias flag and the conditions above closed.

**Related action for AI-002.** Public chatbots are prohibited for all company data (POL-05 4.8). The IT Manager will evaluate an enterprise generative AI tool with data protection terms against NIST AI 600-1 before any approval. Due 2026-12-31.
