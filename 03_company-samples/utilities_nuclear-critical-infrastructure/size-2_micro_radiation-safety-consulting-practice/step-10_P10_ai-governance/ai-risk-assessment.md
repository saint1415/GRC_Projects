# AI Risk Assessment: Calibration Drift Prediction for Client Survey Instruments

| Field | Value |
|---|---|
| Organization | Cris Santos Company, LLC (radiation safety consulting practice) |
| Tier / Vertical | Micro / Nuclear Reactors, Materials, and Waste |
| AI use case | AI-001: the SYS-02 vendor's machine-learning drift prediction module, piloted in the calibration laboratory since 2026-05-04 |
| Why this use case | Adapted from the registry default ("predictive maintenance for non-safety plant equipment"). The practice owns no plant equipment. The closest real use is predicting which client radiation survey instruments will drift out of tolerance, which is predictive maintenance for the equipment the practice services |
| Framework | NIST AI RMF 1.0 (AI 100-1). AI 600-1 is not applied to AI-001, which is not generative; it is referenced for AI-002 and AI-003 |
| Assessor / date | Calibration Laboratory Technician with the Office Manager and the Principal Health Physicist (as RSO), 2026-09-08 |
| Decision | Principal Health Physicist (owner), 2026-09-15 |
| Inventory | `ai-use-case-inventory.csv` (3 use cases) |

## 1. GOVERN
- **Accountable owner:** the Calibration Laboratory Technician.
- **Decision authority:** the owner (Medium tier). The owner is also the RSO named on the practice's license, so the same person judges the radiation safety side. Compensating check: the annual independent assessment (P07) and the conditions in section 6, which are written as hard rules rather than judgment calls.
- **Policies that apply:**
  - POL-04 4.6: approved AI tools only; AI-001 is the only entry, for instrument data only, under the conditions in section 6; no Client Security-Related or Restricted information in any AI tool.
  - POL-02 A.5: supplier terms approved before a vendor holds client information.
  - POL-02 C.2: no client information in public AI chatbots (AI-003).
- **Approved-tools list:** kept by the Office Manager in POL-04 4.6.
- **Scale for a Micro practice:** there is no AI committee. The owner, the Calibration Laboratory Technician, and the Office Manager review AI use at the monthly security meeting.

**How the pilot started.** The vendor switched the module on for all customers in a product update. The Calibration Laboratory Technician began using its weekly list on 2026-05-04 to order the lab queue. Nobody reviewed the vendor's data-use terms, which allow pooled customer data for product improvement (P09 Part B; P01 R-016).

## 2. MAP
| Item | Description |
|---|---|
| Purpose and intended use | Each week, list client instruments whose calibration history suggests they are likely to be found out of tolerance at their next calibration. The lab uses the list to suggest early recalls to clients, to schedule repairs, and to plan loaner meters |
| Users | Calibration Laboratory Technician; the owner as backup |
| Affected people | Indirectly: clients' workers who rely on survey meters to find radiation. No decisions are made about individuals |
| Data | Inputs: instrument make, model, and serial number; dates and results of past calibrations (as-found and as-left readings); repair history; client name and site; a free-text location field. Outputs: a drift risk score and the top contributing factors. **Free-text location notes for 2 Part 37 clients name the rooms that hold their category 2 devices.** Technician initials appear in the records |
| Build or buy | Buy: vendor SaaS module inside SYS-02. **The vendor trains it on pooled data from all its customers, and its analytics features were outside the tested scope of its SOC 2 report** |
| Not intended | Lengthening any calibration interval; skipping or shortening a calibration; deciding pass or fail; issuing certificates; judging technician performance; any statement to a client that its instrument "does not need" calibration. Enabling any of these requires re-assessment |

**Applicable laws and rules:**
| Rule | Applies? | Why |
|---|---|---|
| Sector AI rules | None found | The vertical profile lists no sector AI rule, and no NRC or Florida rule on AI use by materials licensees or their service providers was identified |
| Clients' calibration duties | **Yes, as a boundary** | Clients must calibrate survey instruments periodically (10 CFR 20.1501(c)), and medical licensees "before first use, annually, and following a repair that affects the calibration" (10 CFR 35.61(a)), or the Agreement State equivalents. The model may make a recall earlier; it may never be used to argue for a later one |
| Part 37 client contracts (37.43(d) flow-down) | **Yes, for the location notes** | Notes that say where a client keeps its category 2 device are treated as Client Security-Related under POL-04. They must not feed a pooled model |
| FTC Act Section 5 | Indirectly | Applies to the vendor's accuracy claims, and to the practice's own claims if it tells clients its recalls are "predictive". Keep the vendor's claims in the procurement file and describe the tool modestly to clients |
| State AI laws (for example Colorado SB26-189) | No | AI-001 makes no consequential decisions about individuals, and the practice operates in Florida |

## 3. Risk tier
**Tier: Medium** (repository rubric, `00_universal-framework/projects/step-10_P10_ai-governance/README.md`), with conditions.

**Why not High.** The rubric makes a use case High if it "can affect physical safety or critical infrastructure operations." AI-001 is advisory and one-directional:
- every instrument is still calibrated against the reference source and passes or fails on the technician's readings;
- intervals are set by the clients' rules and never lengthened because of the model;
- the model can only cause an instrument to come in **earlier**.
A wrong score therefore wastes a recall or misses an early warning, but it cannot leave an instrument in service longer than it would have been without the model.

**Why not Low.** It runs on client data that includes sensitive site details, its output reaches clients as recommendations about radiation safety instruments, and the vendor trains it on pooled data the practice does not control.

**Escalation triggers (re-tier to High and re-assess):**
- any use of the score to lengthen an interval, skip a check, or pass an instrument;
- automatic recall messages to clients without the technician's review;
- use on instruments a reactor client uses inside its plant, or on any instrument a client credits in its Part 37 security program;
- use of the data to judge technicians.

## 4. MEASURE
The vendor ran the module on the practice's 2025 history at the practice's request, and the Calibration Laboratory Technician checked 20 cases by hand on 2026-09-04. In 2025 the lab performed 1,580 calibrations, and 118 instruments were found out of tolerance as received.

| Trustworthy characteristic | Test or metric | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Share of 2025 out-of-tolerance instruments the model would have flagged (target at least 60% to be worth using) | 74 of 118 (63%); 160 instruments flagged in total, so 74 of 160 flags (46%) were correct | Yes (barely) |
| Safe | No instrument calibrated later than its due date because of the model; model shown only as advisory | 0 late calibrations since 2026-05-04 (lab log); the screen shows a score, never a pass or fail | Yes |
| Secure and resilient | SYS-02 SOC 2 Type 2; MFA for all users; analytics in the tested scope | SOC 2 covers the platform but not the analytics features; MFA only for the 2 administrators | **Partial** |
| Accountable and transparent | Clients told why an early recall is suggested; nothing implies the due date changed | Early recall emails since May said "our system predicts your meter may fail" with no further explanation | **No** |
| Explainable and interpretable | Top contributing factors shown for each score | Shown (drift trend, age, time since repair); the technician found them sensible in 18 of 20 checked cases | Yes |
| Privacy-enhanced | No Client Security-Related details in model inputs; written limits on pooled training | Location notes for 2 Part 37 clients name the irradiator rooms; vendor terms allow pooled use | **No** |
| Fair, with harmful bias managed | Compare the detection rate for older analog meters (few digital records) with all other instruments; flag a gap over 20 percentage points | Older analog meters: 9 of 25 detected (36%); all others: 65 of 93 (70%). Gap of 34 points, flagged | **No (flagged)** |

**Bias finding.** The model sees fewer data points for older analog meters, and those meters belong mostly to small clients (portable gauge users, small clinics) that cannot afford newer instruments. The harm is not that these clients are refused service; it is that they get less early warning than everyone else. Until the gap closes, the lab treats the model as silent on analog meters and sends every analog meter's owner a manual reminder 30 days before its due date.

## 5. MANAGE
**Human in the loop:**
- The Calibration Laboratory Technician reviews the weekly list and decides each early recall. Nothing is sent to a client automatically.
- Hard rule in the lab procedure: "The drift score may move a recall earlier. It must never be used to delay a calibration, lengthen an interval, or decide pass or fail."
- The owner, as RSO, reviews any proposed change to how the score is used before it starts.

**Data protection:**
- By 2026-10-31, replace free-text location notes with building and room codes; the key to the codes stays in each client's restricted folder (POL-04 4.3).
- By 2026-11-30, obtain the vendor's written opt-out from pooled training, or written terms that the practice's data is de-identified and stripped of free text before pooling. If neither is offered, switch the module off.
- MFA for all SYS-02 users (POAM-005).

**Client communication:** early recall messages say "trend analysis of past calibrations suggests an early check; your calibration due date has not changed."

**Monitoring:**
- Quarterly: back-test the last quarter (detection rate overall and for analog meters), logged against P01 R-016.
- Monthly: count model-driven early recalls and any instrument found out of tolerance that the model scored low.

**Incident handling:** an instrument returned to a client with a wrong certificate is handled under the lab's quality procedure and reviewed by the owner as RSO. A vendor security incident affecting client data is handled under POL-03 and the P08 runbook, including the 24-hour Part 37 client notice if location notes are involved.

**Decommissioning:** switch the module off and ask the vendor to confirm deletion of the practice's data from pooled training sets if the data-use terms are not fixed by 2026-11-30, if the overall detection rate falls below 50% for two quarters, or if the vendor changes its terms.

## 6. Decision
**Approve with conditions.** Owner, 2026-09-15.

The pilot continues only under these conditions:
1. The hard rule in section 5 is written into the lab procedure by 2026-09-30.
2. Location notes are replaced with codes by 2026-10-31.
3. Pooled-training opt-out or written de-identification terms by 2026-11-30; otherwise the module is switched off.
4. All SYS-02 users on MFA by 2026-10-15.
5. Analog meters get manual 30-day reminders, and the model is ignored for them, until the detection gap is under 20 points.
6. Early recall messages use the wording in section 5.

**Related decisions for the other inventory entries.**
- **AI-002 (suite AI assistant):** stays off. It would search everything a user can reach, which today includes all 6 clients' Part 37 folders. It may be reconsidered only after the restricted folders are in place (POAM-002) and a P10 assessment, using AI 600-1 for generative risks, shows that it cannot surface Client Security-Related information to staff a client has not approved.
- **AI-003 (public chatbots):** prohibited for any Client Security-Related, Restricted, or Confidential information. The June 2026 event (a client implementing procedure pasted into a public chatbot) was reported to the client on 2026-08-07 and is covered in training (POAM-006).
