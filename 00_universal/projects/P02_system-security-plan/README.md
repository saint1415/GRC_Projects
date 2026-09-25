# P02. System Security Plan (SSP)

**Notion project:** Write a System Security Plan. A document describing a system's boundaries, controls, and responsible parties.

## Universal approach (macro to granular)

1. **Choose one system (macro).** Pick the system named in the scenario `_context.md`, or the most critical process from the BIA (P05).
2. **Set the boundary.** List everything inside the authorization boundary: components, data flows, and external connections.
3. **Categorize.** Identify information types (SP 800-60 Vol. 1 Rev. 1) and assign FIPS 199 impact levels for confidentiality, integrity, and availability. The system's category is the highest of the three (the "high-water mark").
4. **Select a baseline.** Use the SP 800-53B Low, Moderate, or High baseline that matches the category. Tailor it for the tier. Add the vertical's regulatory requirements as overlays, for example SP 800-171 for CUI.
5. **Document implementation (granular).** For each control, record status, responsible role, inheritance (system-specific, hybrid, or common/inherited from a provider), and a short implementation statement.
6. **Approve and maintain.** Record approval, the authorization decision, and review history.

The outline below follows the official **NIST SP 800-18 Rev. 2 System Security Plan Outline Example** (June 2026). Its headings were taken from NIST's docx outline.

## Outputs

| File | Purpose |
|---|---|
| `system-security-plan.md` | The SSP narrative, using the SP 800-18 Rev. 2 outline headings. |
| `control-implementation.csv` | One row per control: baseline, status, inheritance, responsible role, implementation statement. |

## Tier notes

- **Sole Proprietorship and Micro:** keep every heading but write short answers. Most controls are inherited from SaaS providers or the MSP, and the plan should say so.
- **Enterprise and Multi-Sector:** show common controls from corporate and shared platforms, and reference the common control catalog.

## Federal and FedRAMP note

FedRAMP's Rev 5 SSP template became "Legacy" (reference only) on 2026-06-24. The FedRAMP Consolidated Rules for 2026 become mandatory on 2027-01-01 (SRC-FEDRAMP-2026). Scenarios that sell cloud services to federal agencies should cite the current FedRAMP rules, not the legacy template.

## Quality checklist

- [ ] The boundary diagram and the component inventory agree.
- [ ] The FIPS 199 category is justified by the information types.
- [ ] Every baseline control has a status and an owner. Controls marked "not applicable" have a rationale.
- [ ] Inherited controls name the provider and the evidence source (for example, a SOC 2 report).

## Sources

SRC-800-18, SRC-FIPS-199, SRC-FIPS-200, SRC-800-60, SRC-800-53, SRC-800-53B, SRC-800-37, SRC-FEDRAMP-LEGACY, SRC-FEDRAMP-2026.
