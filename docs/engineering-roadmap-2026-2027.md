# Miami Space Port — Integrated Engineering Roadmap

**Planning basis:** SSOS 2026 structural consolidation plan, adapted to the Miami Space Port concept.  
**Status:** Proposed project plan; dates and sequencing are planning targets, not committed delivery dates.

## Strategic intent

Move from demonstration-led progress toward architecture-led maturity while preserving independent proof-of-concept experimentation. The SSOS reference explicitly prioritizes operational readiness, system integration, observability, and flight-representative evidence over isolated feature counts.

## Workstreams

1. **A — Structural separation:** system/environment boundary, simulation controller, removal of embedded simulation logic.
2. **B — Architectural definition:** subsystem contracts, global state model, failure propagation invariants.
3. **C — Structured simulation:** world model, reproducible initial conditions, structured fault taxonomy.
4. **D — Integration validation:** lifecycle model, canonical scenarios, system-level regression.
5. **E — Operational evidence:** integrated lifecycle demo, canonical scenario/fault set, deterministic CI.
6. **F — Orbital data infrastructure:** workload profiles, storage abstraction, resilience requirements, link-outage and integrity validation.
7. **G — Port and mission operations:** facility requirements, payload flow, ground segment, operating model, safety and regulatory discovery.

## Quarterly sequence

### Q1 — Structural separation and requirements baseline
- Define system/simulation boundary and simulation controller responsibilities.
- Publish subsystem contract template and interface inventory.
- Establish initial mission/data workload classes.
- Create facility and ground-segment requirements register.
- Record assumptions, dependencies, and open decisions.

### Q2 — Architecture and first integrated scenario
- Baseline subsystem contracts and global lifecycle state model.
- Define fault classification and propagation invariants.
- Create world-model and initial-condition schemas.
- Demonstrate one reproducible multi-subsystem scenario.
- Define orbital data service interface and storage health telemetry.

### Q3 — Structured simulation and degraded operations
- Formalize scenario time, world state, and controller API.
- Implement at least two canonical scenarios.
- Exercise structured faults across thermal, power, communications, storage, and subsystem availability.
- Model communications outage and store-and-forward recovery.
- Produce initial facility/operations concept review.

### Q4 — Operational evidence and v0.9 candidate
- Run canonical lifecycle and degraded-mode demonstrations.
- Integrate deterministic system-level regression into CI.
- Require ten consecutive stable CI runs as specified by the SSOS v0.9 evidence gate.
- Publish logs and replayable configurations.
- Evaluate v0.9 architecture/operational grammar candidate readiness.

### 2027 — v1.0 ground-representative candidate
- Freeze public subsystem interfaces and define deprecation/backward-compatibility policy.
- Maintain at least three canonical scenarios.
- Demonstrate stable regression across releases.
- Identify the minimal flight-extractable subset and hardware abstraction boundary.
- Complete documentation needed for mission-specific adaptation.
- Keep internal implementation and standalone PoCs open to innovation.

## Release gates

### v0.9 — Architectural and operational grammar candidate
Required evidence:
- A–D structural layers defined.
- Canonical lifecycle scenario demonstrates INIT → NOMINAL → DEGRADED → RECOVERY.
- Simulation controller is used; subsystem logic has no direct environment access.
- At least two canonical system-level scenarios and five structured fault types are documented and exercised.
- Scenario configuration is automatically validated.
- System-level CI has no nondeterministic failures across at least ten consecutive runs.
- Logs support replay and execution bounds/pass-fail criteria are documented.

### v1.0 — Ground-representative stable platform
Proposed criteria from the SSOS reference:
- Stable subsystem contracts, versioning/deprecation policy, and backward compatibility commitment.
- Fully documented lifecycle and enforced simulation boundary.
- At least three canonical scenarios and stable regression across releases.
- Minimal deployable/flight-extractable core identified.
- Hardware abstraction boundary clarified.
- Mission adaptation documentation prepared.

## Parallel PoC policy

Standalone subsystem demonstrations may continue in independent repositories. They are not blocked by core structural constraints. A PoC is promoted into the SSOS core only after its interfaces, lifecycle behavior, integration effects, observability, and regression evidence are reviewed.

## Program governance

Each work item should identify an accountable owner, requirement linkage, dependencies, acceptance criteria, verification method, evidence artifact, and status. Safety-critical requirements require independent review. Scope changes should update the requirements register and traceability matrix.

## Planning caveat

The SSOS reference labels Phase 3 as flight-representative demonstration (2026–27) and Phase 4 as opportunistic flight application (TBD). This project roadmap preserves that distinction: it does not make the Miami Space Port schedule dependent on a flight opportunity.
