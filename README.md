# Miami Space Port 2026

**Dream. Build. Launch.** An open-source concept for a next-generation Miami spaceport, combining a facility-development vision with a spacecraft and mission-operations simulator.

## Project

This repository contains a browser-based mission-control simulator and planning documents for the Miami Space Port concept. The project uses the Space Station Operating System (SSOS) 2026 plan as its planning foundation.

## Run locally

No build step or dependencies are required.

1. Clone or download this repository.
2. Open `index.html` in a modern browser.
3. Use **Inject fault** to simulate a thermal-control anomaly, then **Recover systems** to exercise the recovery lifecycle.

## Simulator capabilities

- Live mission-control telemetry for altitude, velocity, power, life support, thermal regulation, and communications.
- Operational lifecycle: **INIT → NOMINAL → DEGRADED → RECOVERY**.
- Fault injection and recovery sequence with a timestamped operations log.
- Conceptual facility status for launch complex, payload integration, and ground network.
- Illustrative program economics dashboard.

## Repository map

- `index.html` — interactive mission operations simulator.
- `docs/space-station-os-2026-roadmap.md` — SSOS planning roadmap.
- `docs/facility-development.md` — facility and operating model.
- `docs/experience-storyboard.md` — six-scene concept storyboard.
- `scenarios/thermal-control-fault.md` — fault-injection and recovery exercise.

## Project status

This is a concept and simulation project. Telemetry, budgets, facility readiness, and operational behaviors are illustrative—not live spacecraft data, approved engineering designs, or financial forecasts.

## License

The project is distributed under the MIT License. See [LICENSE](LICENSE).
