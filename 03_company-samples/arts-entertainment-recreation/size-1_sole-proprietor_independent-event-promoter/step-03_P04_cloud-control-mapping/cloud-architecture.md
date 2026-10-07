# SaaS Architecture and Control Placement: Cris Santos Company | Arts, Entertainment, and Recreation | Sole Proprietorship

**Organization:** Cris Santos Company (independent event promoter with one leased room) | **Tier:** Sole Proprietorship | **Provider:** SaaS only (no IaaS or PaaS)
**System:** Ticketing and Venue Operations Platform (TVOP), as defined in the system profile (P02)

## 1. Diagram
Control IDs on each node are the ones in `cloud-control-map.csv`. Dashed lines are flows the owner wants to remove or that carry a gap.

```mermaid
flowchart LR
  subgraph Owner["Owner devices and network (customer responsibility)"]
    L["Laptop<br/>SC-28"]
    P["Owner's phone<br/>authenticator app"]
    S["2 scanning phones<br/>AC-11"]
    W["The Room's Wi-Fi<br/>SC-7 (gap: shared with crews)"]
  end
  subgraph PCI["PCI DSS validated service providers"]
    TIX["Ticketing platform (SYS-01)<br/>hosted checkout; scanner app<br/>IA-2(1) (gap), AC-2 (gap), AU-6, CP-9, SI-12"]
    PROC["Payment processor (SYS-02)<br/>payment fields; payouts<br/>IA-2(1), SC-28"]
  end
  subgraph SaaS["Other SaaS"]
    WEB["Website builder (SYS-03)<br/>event pages embed the checkout<br/>IA-5 (gap), CM-7 (gap)"]
    MAIL["Email and files (SYS-04)<br/>IA-2(1), AC-3"]
    MKT["Email marketing and social (SYS-05)"]
    ACC["Accounting (SYS-06)"]
  end
  FAN["Patrons' browsers and phones"]
  ASSIST["Marketing assistant (uses owner logins: gap)"]
  DOOR["Door contractor staff (shared login: gap)"]
  FAN -->|TLS checkout| TIX
  FAN -->|event pages| WEB
  WEB -->|embedded checkout widget| TIX
  TIX -->|payment fields| PROC
  PROC -->|payouts| BANK["Business bank"]
  L --> W
  S --> W
  W -->|TLS| TIX
  L -->|TLS| MAIL
  P -->|MFA prompts| MAIL
  P -->|MFA prompts| PROC
  ASSIST -.->|owner's login| TIX
  ASSIST -.->|owner's login| WEB
  DOOR -.->|shared door login| S
  TIX -.->|monthly patron export| L
  L -.->|upload| MKT
  FAN -.->|card numbers by email or text (stopped)| MAIL
```

## 2. Layers
| Layer | Components | Key controls | Responsibility |
|---|---|---|---|
| Identity | SYS-01, website, email, processor portal, accounting logins | IA-2(1), IA-5, AC-2 | Customer configures; vendors provide MFA and roles |
| Data | Patron records and exports, contracts, settlement sheets | SI-12, AC-3, CP-9 | Vendors protect data inside their services; the owner decides what is exported, shared, and kept |
| Payment page | Hosted checkout and the website pages that embed it | CM-7, SA-9 | Vendor and processor run the checkout; the owner controls everything else on the embedding page |
| Endpoints | Laptop, owner's phone, scanning phones | SC-28, AC-11 | Customer |
| Network | The Room's router and Wi-Fi | SC-7 | Customer (internet line from the landlord) |
| Logging | SYS-01 activity log, email sign-ins | AU-2 (vendor), AU-6 (customer) | Shared: vendor records, owner reviews |
| SaaS applications and hosting | Ticketing, processor, website builder, productivity, accounting platforms | Inherited (AC-3, AU-2, SC-28, CP-9, PE family) | Provider |

## 3. Shared responsibility for SaaS
All three major cloud providers' shared responsibility models (SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM) agree on the SaaS split: the provider runs the application, the platform, and the facilities; **the customer always keeps its identities and accounts, its data, and its devices.** That is why 11 of the 15 rows in the control map are the owner's, 2 are shared, and 2 are the provider's. A vendor's PCI DSS AOC or SOC 2 report never covers these layers. No IaaS provider equivalents table is needed, because the business runs no infrastructure.

The same split applies to PCI DSS. The ticketing vendor and processor hold and protect card data, which is why the processor assigned SAQ A. But the owner controls the **web page that embeds the checkout**. A script added to that page can draw a fake payment form over the real one, so PCI SSC added an SAQ A eligibility criterion in January 2025: the merchant confirms its site is not susceptible to attacks from scripts that could affect its e-commerce systems (PCI SSC blog, 2025). That makes the website builder account and its scripts part of the owner's card security, even though no card number ever touches the owner's systems when things work as designed.

## 4. Findings from the mapping
1. **The two accounts that control the checkout have the weakest sign-in.** SYS-01 and the website use one shared password and no MFA, while email and the processor portal have MFA. Tracked as P01 R-001 and R-002.
2. **Unreviewed scripts sit next to the checkout widget.** The social pixel, analytics tag, and chat widget plugin run on event pages; the chat plugin can add code to every page. Tracked as P01 R-002 and P03.
3. **Patron data leaves the vendors through exports.** Monthly exports go to the laptop, cloud storage, and the email marketing service; 4 had public share links (found during this mapping and turned off 2026-07-28). Tracked as P01 R-005.
4. **Inherited controls depend on the vendors' reports** and on the owner operating the customer controls they list (MFA, user removal, log review, prompt notice of suspected compromise), reviewed in P09.
