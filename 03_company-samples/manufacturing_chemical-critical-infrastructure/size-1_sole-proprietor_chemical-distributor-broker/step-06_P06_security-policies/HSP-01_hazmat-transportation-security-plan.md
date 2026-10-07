# Hazmat Transportation Security Plan

| Field | Value |
|---|---|
| Organization | Cris Santos Company (specialty chemical distributor, broker), principal place of business in Florida (home office) |
| Plan ID | HSP-01, version 1.0 |
| Required by | 49 CFR 172.800(b)(10): the business offers large bulk quantities (cargo tanks of about 15,140 L) of UN2014, hydrogen peroxide 50%, Division 5.1, Packing Group II |
| Senior management official (172.802(b)(1)) | Owner |
| Adopted | 2026-10-05 |
| Review | At least annually, each September, and after any change in products, suppliers, carriers, or threat (172.802(c)). Next review 2027-09-30 |
| Handling | Restricted (POL-01 8.1). Shown to suppliers and carriers only in the parts they implement. A copy is available at or through the principal place of business on request of an authorized DOT or DHS official (172.802(d)) |
| Related | POL-01 (information security); P01 risk register; P08 runbook |

## 1. Purpose and covered shipments
This plan covers every shipment the business offers of hydrogen peroxide 50% (UN2014), in cargo tanks and, by choice, in totes. Totes are not required to be covered, but the same diversion threat applies. The plan covers the functions the business performs as an offeror: taking the order, verifying the buyer and ship-to, preparing the bill of lading (BOL), booking the carrier, authorizing the pickup, and supporting the load until delivery. Filling, loading, placarding, and dock security are the supplier's functions under the supplier's own plan. Driving and en route custody are the carrier's.

## 2. Roles and security duties (172.802(b)(2))
| Position | Security duties | How they are told to act |
|---|---|---|
| Owner (senior management official) | Runs this plan; performs every verification step in section 4; decides holds and reports | This plan; annual in-depth training (section 8) |
| Supplier shipping office (each hydrogen peroxide terminal) | Releases a load only against a pickup number the owner entered in the supplier portal or gave by phone; checks the driver's license and truck number at the dock; calls the owner on any mismatch; holds all releases if the owner cannot be reached | Written standing instruction sent 2026-10-05; acknowledgment requested by 2026-10-31 |
| Carrier (approved bulk carriers only) | Keeps its own 172.800 security plan; delivers direct with no unattended stops; calls on any delay over 2 hours | Written carrier terms with each rate confirmation |
| Covering distributor (when the owner is unavailable) | Answers calls; tells suppliers to hold; never authorizes a release | Coverage arrangement (POL-01 11.3) |

## 3. Transportation security risk assessment (172.802(a))
The business handles no hazmat, so its risks are in the information that controls release and movement. The full ratings are in P01 (computed with SP 800-30 Tables G-5 and I-2). Location-specific risks at the terminals are assessed in each supplier's plan. The broker's part is the release decision those terminals act on.

| Threat | How it would happen here | P01 | Level | Measure (section 4) |
|---|---|---|---|---|
| Fictitious pickup | Forged pickup authorization from a hijacked or spoofed email sends a criminal's truck to the terminal | R-001 | Very High | 4.2, 4.3, 4.6 |
| Diversion by order fraud | Impostor customer (lookalike domain, 2026-06-17) or new fictitious buyer orders hydrogen peroxide to a new address | R-003 | Moderate | 4.4 |
| Shipment data exposure | Attacker reads BOLs, tracking links, and schedules in email to plan a theft en route | R-001, R-008 | Very High, Moderate | 4.3, 4.5, 4.6 |
| En route theft or tampering | Unattended stop, unplanned route, or a carrier without a plan | (carrier's plan) | Not rated by the broker | 4.5 |
| Insider | Not present today (no employees); a future hire could misuse release authority | n/a | n/a | 4.1 |
| Unavailable owner | No one to hold a release or answer a carrier | R-011 | Moderate | 4.7 |

**Threat level changes.** When the owner learns of elevated threat (a DHS bulletin, a producer's warning, a theft in the region, or a suspicious order), the owner moves to the elevated measures in section 4.8 until the threat passes.

## 4. Security measures
### 4.1 Personnel security (172.802(a)(1))
No employees. Before any person is hired into a position that can take orders, authorize releases, or see pickup numbers, the owner confirms identity and work authorization, checks references and employment history, and keeps the record, consistent with federal and Florida employment and privacy law.

### 4.2 Pickup authorization (172.802(a)(2), unauthorized access)
1. Each release has a single-use pickup number. The owner enters it in the supplier's order portal, or gives it to the shipping office by phone at a number from the phone's saved contacts. **Never by email alone.**
2. The authorization names the carrier, the driver name, the truck and trailer numbers, and the pickup window. The supplier's clerk checks the driver's license and truck at the dock. The business does not collect license numbers (POL-01 8.7).
3. Any change to carrier, driver, truck, or window is valid only after the owner confirms it by calling the carrier's dispatch at a number from the approved carrier list.
4. The supplier holds the load and calls the owner on any mismatch, any unexpected caller, or any request that arrives only by email.

### 4.3 Protecting the information that releases loads
1. Email, accounting, and bank accounts use MFA (POL-01 7.2). The email account has no forwarding rules except those the owner sets and reviews monthly (POL-01 7.6).
2. Pickup numbers, schedules, and tracking links are Restricted. They go only to the supplier and carrier for that load.
3. Messages that ask for urgency, secrecy, or a change of routine are treated as suspicious and verified by phone.

### 4.4 Know your customer (hydrogen peroxide)
1. **New customer:** the owner verifies the business (state registration, a site visit or a call to the published main number, and a credit check), gets a signed end-use statement before the first order, and confirms with the producer that it accepts the customer.
2. **Existing customer, new ship-to or new contact:** the owner calls the known buyer at the number on file. The owner never uses a number given in the request.
3. **Red flags** that stop the order and trigger a report (section 7): a lookalike domain; a new ship-to that is a residence, a storage unit, or a freight forwarder; a request for unusual concentration or quantity; cash or card payment from a new buyer; reluctance to give end-use information.

### 4.5 En route security (172.802(a)(3))
1. Bulk hydrogen peroxide moves only with carriers on the approved bulk carrier list. Each has confirmed in writing that it has its own 49 CFR 172.800 security plan and trains its drivers under 172.704.
2. Loads move direct from the terminal to the customer with no unattended stops. Drop-trailer delivery is not allowed.
3. The owner records each load in transit on the workbook and the printed list (POL-01 11.4). The owner confirms delivery with the consignee by phone the same day.
4. A load more than 2 hours late with no contact from the carrier is escalated: call the carrier dispatch, then the consignee, then follow the P08 runbook if the load cannot be located.

### 4.6 Records
BOLs, pickup authorizations, and the in-transit list are kept under POL-01 8.5. They are stored only in MFA-protected systems and the monthly backup.

### 4.7 When the owner is unavailable
Suppliers hold all releases. The covering distributor answers calls but never authorizes a release. The ERI provider continues to answer emergency calls (172.604).

### 4.8 Elevated threat measures
- Bulk releases only in daylight windows, with a call from the owner to the supplier on the morning of pickup.
- Delivery confirmation by phone within 1 hour of the scheduled arrival.
- No new hydrogen peroxide customers or ship-to addresses until the threat passes.

## 5. Shipping papers and emergency response information
5.1 BOLs are built only from the product description sheet (POL-01 8.2).
5.2 Each BOL shows the ERI provider's number and the company's contract number (172.201(d); 172.604(b)(2)).
5.3 New products follow POL-01 6.3: HMT check, SDS to the ERI provider, written confirmation before the first BOL.

## 6. Contingency
Suppliers hold releases when the owner cannot be reached. The owner holds bulk releases when a hurricane warning covers the route or the home office.

## 7. Security incidents and reporting
Any failed verification, suspicious order, missing load, or compromise of an account that touches releases is a security incident. Follow POL-01 section 10 and the P08 runbook: hold related releases, call the supplier and carrier, report to local law enforcement and, for hydrogen peroxide, to the producer, and log it the same day.

## 8. Training plan (172.802(b)(3); 172.704(a)(4)-(5))
| Training | Who | When | Record |
|---|---|---|---|
| Security awareness (172.704(a)(4)), within the recurrent HMR course | Owner (and any future hazmat employee within 90 days of hire) | By 2026-10-31, then every 3 years | Course certificate and test |
| In-depth security training on this plan (172.704(a)(5)): objectives, structure, procedures, duties, actions in a breach | Owner, delivered and tested by the hazmat training provider | By 2026-11-30; every 3 years; within 90 days after any revision of this plan | Training record with the five 172.704(d) elements |
| Social engineering and payment-fraud module | Owner | Yearly | Completion record |

## 9. Plan maintenance (172.802(c)-(d))
This plan and its risk assessment are kept in writing for as long as they are in effect. The owner reviews them each September and after any change listed in the header. After each revision, the owner notifies each supplier and carrier whose duties changed and replaces every copy. A copy is kept in the records folder, which is backed up, and one printed copy is kept in the home office.

| Version | Date | Change | Approved by |
|---|---|---|---|
| 1.0 | 2026-10-05 | First plan | Owner |
