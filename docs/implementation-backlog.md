# Engineering Backlog — SSOS Alignment and Miami Space Port Extensions

This backlog translates the supplied SSOS plan into trackable work packages and adds Miami Space Port orbital-data and port-operations work. Items are proposed repository backlog entries; they are not claims that implementation is complete.

## Epic A — Structural separation layer

### A1 — Define system/environment boundary
**Acceptance:** no subsystem directly accesses simulation parameters; environment interaction uses a documented interface; architecture and review checklist updated.

### A2 — Introduce simulation controller abstraction
**Acceptance:** controller owns world state, scenario progression, and fault scheduling; subsystems can execute without simulator dependency.

### A3 — Refactor embedded simulation logic
**Acceptance:** direct environment calls removed from subsystem modules; interface abstractions replace them; existing demos continue to pass.

## Epic B — Architectural definition

### B1 — Define subsystem contracts
**Acceptance:** input/output specifications, responsibility boundaries, error semantics, and versioning policy documented for each subsystem.

### B2 — Define system-level state model
**Acceptance:** global states enumerated; transition diagram and entry/exit conditions published; subsystem-to-global state mapping documented.

### B3 — Formalize failure propagation rules
**Acceptance:** fault classification, propagation paths, containment expectations, and one validated example published.

## Epic C — Structured simulation framework

### C1 — Define world model abstraction
**Acceptance:** world/environment interface and discrete/continuous time assumptions documented; parameters separated from subsystem logic.

### C2 — Structured initial-condition schema
**Acceptance:** JSON schema or equivalent defined; configuration validator implemented; reproducible example scenario checked in.

### C3 — Fault model framework
**Acceptance:** fault taxonomy, trigger model, severity, affected component, duration, and recovery behavior represented in configuration; controller executes faults.

## Epic D — Integration validation

### D1 — Define system lifecycle model
**Acceptance:** INIT, NOMINAL, DEGRADED, RECOVERY lifecycle documented with entry/exit criteria; safe/shutdown states considered by hazard review.

### D2 — Scenario-based validation
**Acceptance:** canonical scenarios execute automatically; scenario outputs and expected invariants are checked in CI.

### D3 — System-level regression harness
**Acceptance:** multi-subsystem integration test, deterministic pass/fail criteria, replayable logs, and bounded execution time integrated into release workflow.

## Epic E — Operational evidence (v0.9 gate)

### E1 — Canonical integrated lifecycle demonstration
**Acceptance:** one unattended, reproducible scenario demonstrates INIT → NOMINAL → DEGRADED → RECOVERY; controller used; transitions traceable in logs.

### E2 — Canonical scenario and fault set
**Acceptance:** at least two system-level scenarios and at least five structured fault types; every fault exercised in at least one scenario; configuration automatically validated.

### E3 — Deterministic system-level CI
**Acceptance:** system-level scenario runs in CI; at least ten consecutive runs without nondeterministic failure; replay-quality logs and documented runtime/pass-fail criteria.

## Epic F — Orbital data infrastructure

### F1 — Define workload and data-class profiles
**Acceptance:** telemetry, command, payload, autonomy, and archive classes have documented priority, retention, integrity, latency, and transfer objectives.

### F2 — Define storage service abstraction
**Acceptance:** device-independent interface exposes capacity, health, integrity, read/write status, and fault events; vendor/device specifics remain behind adapters.

### F3 — Build storage fault scenarios
**Acceptance:** corrupted data, uncorrectable read, controller restart, storage exhaustion, and thermal/power degradation scenarios are replayable.

### F4 — Validate disrupted-link data services
**Acceptance:** persistent prioritized queues survive link interruption; replay/acknowledgment behavior and data integrity are tested after reconnection.

### F5 — Complete technology trade study
**Acceptance:** candidate SSD, MRAM, FRAM, RRAM, DRAM, and archival options compared against mission-specific environmental, capacity, endurance, power, and qualification requirements. No part is selected without evidence.

## Epic G — Port and mission operations

### G1 — Establish facility requirements register
**Acceptance:** functional requirements, site assumptions, interfaces, safety constraints, and open regulatory questions are documented.

### G2 — Define payload integration and ground segment concept
**Acceptance:** payload receipt, inspection, integration, test, custody, communications, and operational handoff processes are diagrammed.

### G3 — Define mission control authority and procedures
**Acceptance:** command authorization, shift handover, anomaly escalation, event logging, and contingency responsibilities are documented.

### G4 — Build concept-level program model
**Acceptance:** cost, schedule, capacity, and revenue assumptions are explicitly labeled as estimates and linked to evidence; no illustrative simulator value is represented as a forecast.

## Cross-cutting definition of done

Every merged core feature must have: requirement linkage, interface documentation, tests, failure behavior, observability/logging, reproducible configuration where relevant, review approval, and evidence captured in the repository. Standalone PoCs remain exempt from core integration gates until promoted.
