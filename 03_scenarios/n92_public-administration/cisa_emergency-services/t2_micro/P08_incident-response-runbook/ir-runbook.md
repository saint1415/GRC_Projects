# Incident Response Runbook: Computer-aided dispatch outage from ransomware

| Field | Value |
|---|---|
| Organization | Cris Santos Company (Private ambulance (EMS) provider) |
| Tier / Vertical | Micro / Emergency Services |
| Incident type | Computer-aided dispatch outage from ransomware |
| Framework | NIST SP 800-61 Rev. 3 (CSF 2.0 Community Profile) |
| Runbook owner | [FILL] |
| Last tested | [FILL] |

## 0. Roles and contacts (Govern)
| Role | Primary | Backup | Contact |
|---|---|---|---|
| Incident commander | [FILL] | | |
| Technical lead / IT provider | [FILL] | | |
| Legal counsel | [FILL] | | |
| Cyber insurance carrier | [FILL: policy #, hotline] | | |
| Communications | [FILL] | | |

## 1. Preparation checks (Identify / Protect)
- [ ] Offline or immutable backups verified within the last [FILL] days (CP-9)
- [ ] Contact list and out-of-band communications channel ready (IR-8)
- [ ] Logging retained for at least [FILL] days (AU-11)

## 2. Detection and declaration (Detect / RS.MA)
| Trigger | Source | Action |
|---|---|---|
| [FILL: indicator specific to Computer-aided dispatch outage from ransomware] | [FILL] | Open incident ticket and notify the incident commander |

**Declare an incident when:** [FILL: criteria]. **Record the time of discovery.** Notification clocks may start here.

## 3. Analysis (RS.AN)
1. [FILL: Scope affected systems and data]
2. [FILL: Preserve evidence: memory, logs, images, with chain of custody]
3. [FILL: Determine whether regulated data was accessed or acquired (see `notification-matrix.csv`)]

## 4. Containment and eradication (RS.MI)
1. [FILL]
2. [FILL]

## 5. Reporting and communication (RS.CO)
Follow `notification-matrix.csv`. Legal counsel confirms each obligation before notification.

## 6. Recovery (RC.RP / RC.CO)
Restore in BIA priority order (P05): [FILL: ordered list]. Validate integrity before reconnecting. Communicate restoration status to stakeholders.

## 7. Post-incident (ID.IM)
- Lessons-learned meeting within [FILL] days
- Update P01 risk register and P07 POA&M
