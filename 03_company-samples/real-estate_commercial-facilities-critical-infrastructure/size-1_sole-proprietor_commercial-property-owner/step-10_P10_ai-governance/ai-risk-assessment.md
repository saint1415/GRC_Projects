# AI Use Assessment: Video Analytics on the Building Cameras (one page)

| Field | Value |
|---|---|
| Organization | Cris Santos Company (owner-operator of one mixed-use commercial building) |
| Tier / Vertical | Sole Proprietorship / Commercial Facilities |
| AI use cases | **AI-001:** "familiar faces" face recognition on the 2 entrance cameras (trial 2026-05-04 to 2026-07-21). **AI-002:** after-hours person and vehicle detection alerts on the rear service area and parking lot cameras (in use since installation in 2024) |
| Framework | NIST AI RMF 1.0 (Govern, Map, Measure, Manage), short form. AI 600-1 is not used: neither feature is generative |
| Assessor and decision | Owner, 2026-08-24; decision 2026-08-31 |
| Inventory | `ai-use-case-inventory.csv` (2 use cases) |

## 1. What they do (Map)
Both features are options in the cloud video service (SYS-02), turned on in the vendor portal.
- **AI-001** builds a face template for every person the entrance cameras see, groups repeat visitors, and lets the owner attach a name so the app announces "*name* arrived". The owner turned it on during a free trial and named 9 people (2 janitorial staff, the HVAC technician, and 6 tenant employees) without telling them. Nobody else was told either; the lobby sign says only that cameras are in use. The same cameras recorded **audio** by default.
- **AI-002** detects a person or vehicle in the rear service area or parking lot between 19:00 and 7:00 and sends the owner a push notification with a short clip. It does not identify anyone.
- **Vendor terms** allowed customer video to be used to improve the vendor's models unless the customer opts out. The owner opted out on 2026-07-24.

## 2. Rules that apply
| Rule | AI-001 | AI-002 | Why |
|---|---|---|---|
| FTC Act Section 5, 15 U.S.C. 45(a) (C-COMMERCIAL-FACILITIES-R02) | **Yes** | Yes | The FTC's *Policy Statement on Biometric Information and Section 5 of the FTC Act* (2023-05-18) lists practices it may treat as unfair, including failing to assess foreseeable harms before collecting biometric information and surreptitious or unexpected collection. AI-001 did both. The statement is still posted on ftc.gov; whether current FTC leadership applies it was not confirmed |
| Fla. Stat. 501.171 | **Unclear** | No | Personal information includes "biometric data as defined in s. 501.702". That definition covers automatic measurements of biological characteristics used to identify a person, but **excludes video recordings and data generated from them**. Whether face templates computed from camera video are covered is a question for counsel. The owner treats them as if they were |
| Fla. Stat. 934.03 | Audio: **Yes** | Audio: Yes | Interception of oral communications is lawful when all parties have given prior consent (934.03(2)(d)). Nobody consented to audio at the entrances. Whether any recorded speech was a protected "oral communication" is a question for counsel. Audio was turned off on 2026-07-21 and the recordings aged out under the 30-day retention |
| Florida Digital Bill of Rights | No | No | Applies only to controllers with more than $1 billion in global gross annual revenue (Fla. Stat. 501.702) |
| State AI laws (for example Colorado SB26-189) | No | No | The business operates only in Florida, and neither feature makes a consequential decision about a person |

## 3. Risk screen (repository rubric)
- **AI-001: Medium.** It identifies people but makes no decision about them, and controls no door. The tier does not change the answer: there is no business need that justifies building face templates of tenants' employees without notice, and POL-01 5.2 now bans face recognition.
- **AI-002: Medium.** It makes no decision, but an alert can lead the owner to call the police or confront someone, which affects a person. A human makes every decision. It would become **High** if alerts ever unlocked or locked doors or triggered automatic calls.

## 4. Measure (AI-002, 30 days of alerts, 2026-06-22 to 2026-07-21)
| Characteristic | Check | Result | Pass? |
|---|---|---|---|
| Valid and reliable | Share of after-hours person alerts that showed a real person | 41 alerts: 31 janitorial staff or tenants working late, 2 unknown people in the parking lot (both left), 8 false (shadows, rain, an animal). 33 of 41 real (80%) | Yes (target 70%) |
| Safe | Alerts cannot control doors or HVAC | Confirmed in settings: notifications only | Yes |
| Secure | Portal MFA; who can change analytics settings | No MFA yet; the installer is also an administrator (POAM-001, POAM-005) | **No** |
| Transparent | People told that analytics run | Sign says only "cameras in use" | **No** |
| Privacy-enhanced | No audio; no training on owner's video; clips kept no longer than video | Audio off 2026-07-21; opt-out 2026-07-24; clips follow the 30-day retention | Yes |
| Fair, harmful bias managed | Night-time detection across skin tones and clothing | **Not tested**: too few events to compare groups. Managed by the review rule in section 5 | Not measured |

## 5. Data-sharing rules and human review (Govern and Manage)
1. No AI or audio feature is turned on without a written P10 assessment and the owner's approval (POL-01 5.1, 9.3). Vendor "free trials" count.
2. No face recognition and no audio at any camera (POL-01 5.2).
3. Customer video must stay excluded from vendor model training; the owner rechecks the setting each July.
4. **For AI-002:** the owner watches the clip before acting. The owner never calls the police, confronts anyone, or reports a person to a tenant on an alert alone, and describes behavior, not appearance, in any report. Each month the owner counts real and false alerts; if fewer than 70% are real for two months, the detection zones are retuned or the feature is turned off.

## 6. Decision (approved 2026-08-31)
**AI-001: Retire.** Turned off on 2026-07-21; the owner asked the vendor on 2026-07-24 to delete all face templates and names, and the vendor confirmed deletion on 2026-08-12 (letter kept). Do not re-enable. P01 R-010.
**AI-002: Approve with conditions**, due 2026-09-30: (1) MFA on the video portal and the installer's account removed (POAM-001, POAM-005); (2) new signs at the entrances and parking lot: "Video recording in use. No audio. Motion alerts are reviewed by the owner"; (3) a short notice to tenants describing the cameras, the alerts, the retention, and the retired face feature. Reassess at the July 2027 review or before any change to the feature.
