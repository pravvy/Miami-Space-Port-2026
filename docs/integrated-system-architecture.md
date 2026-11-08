# Miami Space Port — Integrated System Architecture

**Status:** Concept architecture and engineering planning baseline  
**Version:** 1.0-draft  
**Basis:** *Space Station OS 2026* (43-page planning presentation, 2026) and Tom Coughlin, *Data Storage in Outer Space: Overcoming the Obstacles* (9 June 2026, 38-page presentation).

## 1. Purpose and scope

Miami Space Port is being developed here as a conceptual spaceport, mission-operations, spacecraft-systems, and orbital-data-infrastructure program. This document translates the two supplied references into a coherent architecture proposal. It is not a certified engineering design, licensed launch-site plan, flight-qualified system, or approved business case.

The architecture has four cooperating domains:

1. **Port and ground segment:** facility planning, payload integration concept, ground communications, logistics, safety planning, and program management.
2. **Vehicle and station systems:** spacecraft/station subsystems, command and telemetry interfaces, operational lifecycle, and fault response.
3. **Space Station OS (SSOS) integration core:** modular ROS 2-oriented system architecture, simulation boundary, subsystem contracts, world model, lifecycle control, and system-level validation.
4. **Orbital data infrastructure:** edge compute, data storage, data movement, autonomy support, and resilient communications.

## 2. Architecture principles

- **System-of-systems first.** Integration behavior, initialization order, failure propagation, and observability are first-class design concerns.
- **Separate system logic from simulation logic.** Environment state and fault injection belong behind explicit simulation interfaces, not embedded in subsystem implementations.
- **Contract-first integration.** Each subsystem defines inputs, outputs, states, ownership, timing assumptions, error behavior, and versioning.
- **Autonomy with delayed connectivity.** Local nodes must maintain safe local behavior when Earth connectivity is intermittent; store-and-forward communication is an architectural assumption to validate.
- **Resilience by design.** Radiation, thermal extremes, launch shock/vibration, power limits, and communications outages are hazards to analyze and test.
- **Open experimentation, controlled integration.** Standalone proof-of-concept work remains welcome; only components that satisfy core integration criteria enter the stable SSOS core.
- **Evidence before maturity claims.** Demonstrations, repeatable scenarios, traceable logs, and deterministic regression are required for release gates.

## 3. Logical layers

| Layer | Responsibilities | Key interfaces / evidence |
|---|---|---|
| Port operations | Facility concept, payload flow, ground services, operational planning | Facility requirements, safety cases, readiness reviews |
| Mission operations | Mission planning, command authority, telemetry, event response | Command/telemetry schemas, procedures, audit logs |
| Vehicle/station systems | GNC, power, thermal, communications, life support, payloads | Subsystem contracts and state reporting |
| SSOS core | Lifecycle orchestration, integration, fault propagation, observability | ROS 2 nodes/interfaces, global state model, integration tests |
| Simulation and digital twin | World state, initial conditions, scenario progression, fault injection | Simulation controller API, reproducible scenario configs |
| Orbital data services | Compute, storage, data integrity, edge autonomy, relay/store-forward | Storage profiles, data integrity tests, link/service contracts |

## 4. Control and data boundaries

Subsystem logic should consume validated inputs through defined interfaces. It should not directly read simulator internals, wall-clock assumptions, or ad hoc environment variables. A simulation controller owns world state, scenario time, initial conditions, and fault scheduling. The same subsystem interface should remain usable in simulation and, after mission-specific adaptation and qualification, in a real system.

The mission-operations layer issues authorized commands and receives state/health telemetry. The SSOS core coordinates lifecycle and cross-subsystem state; it does not silently replace subsystem-local safety controls. Orbital data services expose explicit availability, integrity, capacity, power, and thermal status.

## 5. Operational lifecycle

The baseline lifecycle is:

`INIT → NOMINAL → DEGRADED → RECOVERY → NOMINAL`

- **INIT:** verify configuration, interfaces, dependencies, clocks/time sources, and subsystem readiness.
- **NOMINAL:** operate within configured limits; publish health and telemetry.
- **DEGRADED:** isolate or constrain affected functions, preserve safe operation, record the initiating fault and propagation.
- **RECOVERY:** execute authorized recovery steps, verify subsystem health and system invariants, and record evidence.
- **SAFE / SHUTDOWN:** proposed additional states for mission-specific safeing and controlled shutdown; transition rules require hazard analysis and approval.

The state machine is a proposed project-level model derived from the SSOS reference's canonical lifecycle demonstration requirement. Exact transitions and authority boundaries remain to be specified.

## 6. Orbital data infrastructure integration

The Coughlin presentation identifies radiation-induced soft and hard errors, thermal extremes, lack of convective cooling, launch/landing shock and vibration, and power/heat-dissipation limits as relevant challenges. It discusses SSDs with radiation-aware controllers and error correction, and non-volatile memory options such as MRAM, RRAM, and FRAM. It also describes local processing for robotic/AI operations and store-and-forward interplanetary networking.

For Miami Space Port, these become requirements to evaluate—not component selections or flight-readiness claims:

- define workload classes (telemetry, command, navigation products, science payload, autonomy/model data, archive);
- define retention, integrity, latency, throughput, availability, and recovery objectives per class;
- compare candidate memory/storage technologies against radiation, temperature, endurance, power, mass, and interface requirements;
- design for link interruption, local buffering, prioritized downlink, and authenticated replication;
- instrument storage health, error correction events, thermal state, power draw, and data-integrity checks;
- qualify the complete assembly in representative environmental and operational tests before any flight use.

## 7. Security, safety, and assurance

The concept requires threat modeling for command authorization, identity, key management, software provenance, update integrity, data confidentiality, and compromised nodes. Safety analysis must address loss of command link, corrupted data, compute overload, thermal excursions, power faults, and incorrect autonomy decisions. No safety-critical action should depend solely on an unverified AI output.

## 8. Interface and evidence artifacts

Required artifacts include:
- subsystem interface contracts and version policy;
- global state model and transition table;
- simulation controller and world-model API;
- initial-condition and fault/scenario schemas;
- canonical nominal and degraded scenarios;
- fault taxonomy and propagation maps;
- event/log format sufficient for replay;
- system-level CI report and release evidence;
- flight-extractable subset definition and hardware abstraction boundary.

## 9. Source-derived facts versus project proposals

**Source-derived:** SSOS is presented as a modular ROS 2-based platform; its 2026 structural themes are system/simulation separation, architecture definition, simulation structure, integration validation, and operational evidence. Coughlin's presentation describes space storage hazards, example memory/storage technologies, orbital data-center initiatives, and local processing/communications needs.

**Project proposals:** the four-domain Miami architecture, specific data classes, security requirements, lifecycle extensions, and integration interfaces above are design recommendations for this project. They require review, requirements validation, and engineering qualification.
