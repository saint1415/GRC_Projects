# P04. Control-to-Cloud Architecture Mapping

**Notion project:** Map NIST 800-53 Controls to a Cloud Architecture. An annotated cloud diagram (AWS, Azure, or GCP) showing which controls apply where.

## Universal approach (macro to granular)

1. **Choose the provider and service models (macro).** The tier sets what is realistic. Sole Proprietorship and Micro are mostly SaaS. Small adds one IaaS/PaaS tenant. Mid-Market and above run multiple accounts or subscriptions, and often multiple clouds. Multi-Sector: record the tenancy and identity decision. Say whether divisions share the group identity provider with separate accounts, or get a separate tenant with their own identity. Use a separate tenant where a rule or contract requires its own boundary (for example, covered defense information in an external cloud must meet FedRAMP Moderate equivalency, DFARS 252.204-7012(b)(2)(ii)(D)). Name what limits blast radius: division-scoped administrator roles, privileged access management, conditional access, OT identities kept off the corporate directory, and one-way OT data paths.
2. **Draw the architecture in layers.** Identity, network, compute, data, management/logging, SaaS, and the connections to on-premises systems or OT.
3. **Assign responsibility per service.** Use the provider's official shared responsibility model (SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM). Label each control Provider, Customer, or Shared for each service model (SaaS, PaaS, IaaS).
4. **Place controls on components (granular).** Map SP 800-53 controls to the component that implements them. Include the controls that satisfy the vertical's regulatory requirements, and name the evidence source for each.
5. **Validate.** Check that the SSP boundary (P02) and this diagram agree. Every in-scope component should implement at least one control from the AC, AU, CM, IA, SC, and SI families, or inherit it.

## Outputs

| File | Purpose |
|---|---|
| `cloud-architecture.md` | Mermaid diagram (renders on GitHub) plus a layer-by-layer narrative. Replace it with a draw.io or Excalidraw export if you prefer. |
| `cloud-control-map.csv` | Component to control to responsibility to evidence. |

## Quality checklist

- [ ] Every component in the diagram has at least one row in the control map.
- [ ] Every responsibility assignment cites the provider's shared responsibility documentation.
- [ ] Customer-side identity, data protection, and logging controls are explicit, because they are always customer responsibilities.

## Sources

SRC-800-53, SRC-AWS-SRM, SRC-AZURE-SRM, SRC-GCP-SRM, SRC-FEDRAMP-2026 (for scenarios that serve federal agencies).
