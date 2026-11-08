# Miami Space Port 2026

**Dream. Build. Launch.** An open-source concept for a next-generation Miami spaceport, combining facility development, spacecraft and mission operations, Space Station OS (SSOS) architecture, and orbital data infrastructure.

## Project overview

This repository is a concept and engineering-planning project. It combines two supplied technical references:

- *Space Station OS 2026* — modular ROS 2-oriented space-station platform, system/simulation separation, subsystem contracts, lifecycle modeling, structured simulation, integration validation, and v0.9/v1.0 release criteria.
- Tom Coughlin, *Data Storage in Outer Space: Overcoming the Obstacles* (9 June 2026) — orbital data centers, radiation and thermal challenges, memory/storage technologies, local processing, and space communications.

The project translates those references into a proposed Miami Space Port architecture. Source-derived points, project proposals, and illustrative simulator values are distinguished in the documentation.

## Run locally

No build step or third-party dependencies are required for the browser simulator.

1. Clone or download this repository.
2. Open `index.html` in a modern browser.
3. Use **Inject fault** to simulate a thermal-control anomaly, then **Recover systems** to exercise the recovery lifecycle.

Validate scenario JSON files with:

```bash
python scripts/validate_scenarios.py
```

## Simulator capabilities

- Mission-control telemetry for altitude, velocity, power, life support, thermal regulation, and communications.
- Operational lifecycle exercise: **INIT → NOMINAL → DEGRADED → RECOVERY**.
- Fault injection and recovery sequence with an operations log.
- Conceptual facility status and illustrative program economics.
- Orbital data-node scenarios are provided as machine-readable planning fixtures; they are not yet connected to the browser simulator.

## Engineering documentation

- `docs/space-station-os-2026-roadmap.md` — SSOS source-aligned roadmap.
- `docs/integrated-system-architecture.md` — proposed four-domain system architecture and boundaries.
- `docs/orbital-data-infrastructure.md` — source-based storage/compute assessment and proposed requirements.
- `docs/engineering-roadmap-2026-2027.md` — integrated workstreams, quarterly plan, and release gates.
- `docs/technical-risk-register.md` — preliminary qualitative risks and mitigations.
- `docs/implementation-backlog.md` — A–G epics and acceptance criteria.
- `docs/facility-development.md` — facility and operating model.
- `docs/experience-storyboard.md` — six-scene concept storyboard.
- `scenarios/thermal-control-fault.md` — existing thermal fault exercise.
- `scenarios/orbital-data-center-nominal.json` — nominal orbital data-node scenario.
- `scenarios/orbital-data-center-degraded.json` — link/thermal degraded-mode scenario.
- `scripts/validate_scenarios.py` — standard-library scenario validator.
- `.github/workflows/scenario-validation.yml` — GitHub Actions scenario validation.

## Release direction

The SSOS planning basis defines v0.9 as an architectural and operational grammar candidate gated by structural layers A–D and operational evidence E. The v1.0 target is a ground-representative stable platform with stable public interfaces, documented lifecycle, at least three canonical scenarios, stable regression, and a defined flight-extractable subset.

## Project status and limitations

This is a concept and simulation project. Telemetry, budgets, facility readiness, and operational behaviors are illustrative—not live spacecraft data, approved engineering designs, financial forecasts, or a site/launch authorization. Orbital storage technologies discussed in the source material are candidates for study, not selected or flight-qualified components. Mission-specific requirements, safety analysis, environmental qualification, regulatory review, and independent engineering validation remain necessary.

## License

The project is distributed under the MIT License. See [LICENSE](LICENSE).
