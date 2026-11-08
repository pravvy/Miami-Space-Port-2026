# Orbital Data Infrastructure — Requirements and Technology Assessment

**Status:** Concept assessment; no hardware selected  
**Primary reference:** Tom Coughlin, *Data Storage in Outer Space: Overcoming the Obstacles*, 9 June 2026.

## 1. Why this belongs in the Miami Space Port program

The reference argues that autonomous or semi-autonomous robotic systems operating in space will need local compute and communications to reduce latency and support operations when Earth connectivity is constrained. It frames orbital data centers as enabling infrastructure for robotics, manufacturing, resource utilization, and a more distributed space economy. Miami Space Port should therefore treat data infrastructure as a mission-support capability, not simply a terrestrial IT room moved into orbit.

## 2. Environmental constraints identified by the reference

- Ionizing and non-ionizing radiation, including solar-storm events, can cause soft errors and permanent failures.
- High/low temperature extremes and the absence of convection complicate thermal control.
- Launch and landing impose shock and vibration on equipment.
- Power availability and heat-dissipation limits constrain compute density.
- Smaller semiconductor geometries may be more vulnerable to radiation-induced errors.

These are hazard categories from the source presentation. Mission orbit, shielding, dose, thermal boundary conditions, and qualification levels are not specified here and must be derived from a target mission environment.

## 3. Technology landscape described in the reference

| Technology / example | What the reference says | Miami Space Port assessment |
|---|---|---|
| SSDs | Popular for space storage; space SSDs may use radiation-hardened controllers and special error correction | Candidate primary storage class; evaluate controller, ECC, endurance, firmware, radiation behavior, and qualification evidence |
| DRAM | Faces significant radiation-induced soft and hard error challenges | Use only with an explicit mitigation and qualification strategy where mission requirements justify it |
| MRAM | Presented as non-volatile memory; Everspin PERSYST cited for system code and parametric data in space applications | Candidate for critical configuration/state retention; validate exact part and mission environment |
| RRAM | Identified as a possible non-volatile alternative | Research candidate; no selection implied |
| FRAM | Identified as a possible non-volatile alternative; Infineon memory portfolio cited | Candidate for frequent small writes and state retention; validate capacity/endurance/radiation details |
| HDD | Described as used on some missions and ISS laptops, including hermetically sealed helium drives | Not excluded categorically; assess mechanical risk, vibration, power, and mission fit |
| DNA / 5D optical crystal | Mentioned as emerging/long-term storage approaches | Exploratory archival research only; not assumed in baseline architecture |

The presentation names examples including Infineon, Everspin, Avalanche Technology, HPE/Kioxia, and Phison. Those examples are not endorsements, procurement recommendations, or proof that a specific current product meets a future Miami Space Port mission requirement.

## 4. Functional requirements to baseline

| ID | Requirement | Verification evidence |
|---|---|---|
| ODS-001 | Store command, telemetry, mission, and payload data with class-specific retention policy | Data-management test and retention audit |
| ODS-002 | Detect and report uncorrectable and corrected data errors | Injected-error test and health telemetry |
| ODS-003 | Support prioritized buffering during loss or degradation of Earth link | Link-outage simulation and queue replay |
| ODS-004 | Preserve critical configuration and state across restart | Power-cycle and recovery test |
| ODS-005 | Expose capacity, health, temperature, power, and integrity status | Telemetry contract and dashboard |
| ODS-006 | Support authenticated data transfer and software/configuration provenance | Security test and signed artifact verification |
| ODS-007 | Define degraded modes for storage exhaustion, thermal excursion, and controller fault | Scenario-based validation |
| ODS-008 | Permit technology substitution behind a stable storage service interface | Contract and compatibility tests |

Numeric limits for latency, capacity, bit-error rate, radiation tolerance, power, mass, and temperature are intentionally TBD until a target mission and workload are selected.

## 5. Proposed logical service model

- **Ingest service:** receives telemetry, payload products, logs, and mission files.
- **Policy manager:** assigns priority, retention, encryption, replication, and downlink rules.
- **Storage abstraction:** hides device-specific interfaces and exposes health/integrity semantics.
- **Integrity monitor:** performs checksums, error reporting, scrubbing, and restore verification.
- **Local compute service:** runs approved onboard processing and autonomy workloads.
- **Delay/disruption-tolerant transfer queue:** persists outbound/inbound bundles across link interruptions.
- **Ground synchronization:** reconciles records, manifests, and acknowledged transfers with mission control.

This service model is a project proposal, not a design specified by the Coughlin presentation.

## 6. Thermal and power strategy

The source emphasizes the lack of convective cooling and power/heat constraints. The project should model conductive paths, radiator interfaces, equipment duty cycles, peak and average power, thermal transients, and fault response. Candidate measures to study include workload throttling, staged shutdown, thermal-aware placement, redundancy isolation, and lower-power memory choices. No radiator sizing or thermal performance claim is made in this document.

## 7. Communications and autonomy

The source describes laser communications and an interplanetary internet concept based on store-and-forward networking, with local systems making autonomous decisions as communication nodes change over time. The project should evaluate hybrid RF/optical links, link acquisition and loss, store-and-forward queues, prioritization, time synchronization, and safe local autonomy. Actual link budgets, data rates, and latency require mission-specific analysis.

## 8. Validation plan

1. Establish mission environment assumptions and workload profiles.
2. Define device-level radiation, thermal, vibration, power, and data-integrity test requirements.
3. Validate storage abstraction and fault reporting in simulation.
4. Exercise link outages, corrupted blocks, controller reset, capacity exhaustion, and thermal degradation.
5. Verify data recovery and event replay after restart.
6. Conduct hardware-in-the-loop testing with selected components.
7. Complete mission-specific qualification and safety review before flight use.

## 9. Open decisions

- Target orbit and radiation environment.
- Payload and autonomy workload mix.
- Required capacity, throughput, latency, retention, and availability.
- Radiation shielding and component derating assumptions.
- Storage redundancy topology and data replication policy.
- Thermal architecture and allowable operating envelope.
- Ground/space network architecture and security authority.
- Procurement, lifecycle support, and component obsolescence strategy.

## 10. Source note

The assessment above summarizes and translates the supplied 38-page Coughlin Associates presentation dated 9 June 2026. It does not independently verify market announcements, vendor claims, projected launch costs, or individual product qualification status.
