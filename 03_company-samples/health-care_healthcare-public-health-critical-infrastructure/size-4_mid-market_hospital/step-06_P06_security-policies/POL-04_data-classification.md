# Data Classification and Handling Policy

| Field | Value |
|---|---|
| Organization | Cris Santos Company, Inc. |
| Policy ID | POL-04 |
| Owner | Compliance and Privacy Officer |
| Approved by | Chief Operating Officer |
| Approval date | 2026-09-17 |
| Effective date | 2026-10-01 (replaces the 2023 policy) |
| Review cycle | Annually (next review 2027-09-30) |
| Implements (SP 800-53 Rev. 5) | RA-2, MP-1, MP-4, MP-6, SC-8, SC-12, SC-13, SC-28, SA-3(2), SI-12, CP-9, CM-8 |
| CSF 2.0 | ID.AM-05, ID.AM-08, PR.DS-01, PR.DS-02, PR.DS-10, PR.DS-11 |
| HIPAA Security Rule | 164.310(d), (d)(2)(i)-(iv); 164.312(a)(2)(iv), (c), (e); 164.308(a)(7)(ii)(A) |
| Other rules | 42 CFR 482.24(b)(1) (retention at least 5 years) |
| Supporting standards | STD-04 (medical device and OT security), STD-08 (encryption and key management) |

## 1. Purpose
Classify hospital information so that everyone handles it according to the harm its loss would cause, and set the minimum protections for each class.

## 2. Scope
All information the hospital creates, receives, maintains, or transmits, in any form, including data stored in medical devices, test environments, AI tools, and paper downtime records.

## 3. Classes
| Class | Examples | Minimum handling |
|---|---|---|
| **Restricted** | PHI and ePHI (records, images, fetal strips, device data with identifiers), affiliated practice PHI, Social Security numbers, payment data, credentials, security configurations | Need-to-know access; encrypted at rest and in transit; no personal email or unapproved cloud; no unapproved AI tools; logged access |
| **Confidential** | Contracts, financials, workforce records without PHI, vendor reports, risk register | Internal sharing by role; encrypted in transit; approved storage only |
| **Internal** | Policies, procedures, schedules, downtime forms (blank) | Workforce only |
| **Public** | Website content, published notices | No restriction |

## 4. Policy statements
4.1 Data owners (department leaders) must classify the data in their systems; when unsure, treat data as Restricted. (RA-2; ID.AM-05)

4.2 Restricted data must be encrypted at rest on endpoints, servers, removable media, cloud storage, and backups, and in transit over any network outside the data center, using approved algorithms (STD-08). (SC-28; SC-8; SC-13; 164.312(a)(2)(iv); 164.312(e)(2)(ii))

4.3 **Medical devices.** Devices that store Restricted data and cannot encrypt it must be on a restricted device network, inventoried with that attribute, and scheduled for replacement or compensating controls under STD-04. (CM-8; SC-28; 164.310(d)(2)(iii))

4.4 **Disposal and return.** No hard drive, device, or leased equipment that may hold Restricted data may leave the hospital, including returns to manufacturers or lessors, without sanitization to NIST SP 800-88 or a certificate of destruction from the vendor. Biomedical engineering keeps the certificates. (MP-6; ID.AM-08; 164.310(d)(2)(i)-(ii))

4.5 **Test data.** Production PHI may not be used in test, training, or development environments. Use synthetic or de-identified data; any exception needs Privacy Officer approval, production-level controls, and a deletion date. (SA-3(2); PR.DS-01)

4.6 **AI tools.** Restricted data may be entered only into AI tools approved under the AI governance process with a BAA that prohibits training on hospital data (STD-05; P10). (SA-9; PR.DS-01)

4.7 **Backups.** Backups of Restricted data must be encrypted, isolated from the production directory, and kept in write-once storage for at least 35 days. (CP-9; PR.DS-11; 164.308(a)(7)(ii)(A))

4.8 **Paper downtime records.** Paper records created during downtime are Restricted: kept in the unit's locked downtime binder, scanned or back-entered within 72 hours of recovery, and destroyed only by HIM after reconciliation. (MP-4; 482.15(b)(5))

4.9 Medical records must be retained at least 5 years (42 CFR 482.24(b)(1)), or longer where Florida law or the HIM retention schedule requires; security documentation for 6 years (POL-01 4.13). (SI-12; GV.PO-02)

4.10 **Integrity.** Changes to drug libraries, dispensing profiles, and interface mappings must be approved, logged, and monitored for unauthorized change. (SI-7; 164.312(c))

## 5. Compliance and enforcement
Checked by encryption reports, device return certificates, test environment reviews, and the P07 assessment. Violations follow POL-01 4.8.

## 6. Exceptions
Under POL-01 4.7. Unencryptable medical devices are tracked as exceptions with compensating controls.

## 7. Related documents
POL-01; POL-05; STD-04; STD-05; STD-08; P04 control map; HIM retention schedule
