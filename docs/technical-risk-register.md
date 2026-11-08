# Miami Space Port — Technical Risk Register

**Status:** Initial qualitative register for planning; ratings are preliminary and require engineering review.  
**Scale:** Likelihood and impact are Low / Medium / High. No quantitative risk score is implied.

| ID | Risk | Likelihood | Impact | Mitigation / evidence |
|---|---|---|---|---|
| R-01 | System/simulation coupling makes components hard to reuse | Medium | High | Enforce explicit environment boundary; contract tests; code review checklist |
| R-02 | Integration dependencies and initialization order cause unpredictable behavior | High | High | Dependency graph, lifecycle manager, startup/shutdown tests, integration logs |
| R-03 | Unclear subsystem contracts create interface drift | Medium | High | Versioned contracts, ownership, compatibility tests |
| R-04 | Fault propagation is undefined across subsystems | Medium | High | Fault taxonomy, propagation invariants, canonical degraded scenarios |
| R-05 | Non-deterministic simulation undermines regression evidence | Medium | High | Seeded/replayable scenarios, bounded time model, ten-run CI evidence |
| R-06 | Radiation causes memory corruption or device failure | Medium | High | Mission-specific radiation analysis, ECC/error telemetry, redundancy, qualification |
| R-07 | Thermal control cannot reject compute/storage heat | Medium | High | Thermal model, power-aware workload limits, fault injection, hardware testing |
| R-08 | Communications outages interrupt command/data flow | High | Medium | Local autonomy, persistent queues, priority policy, store-and-forward tests |
| R-09 | Storage exhaustion or corruption causes loss of critical data | Medium | High | Capacity monitoring, integrity checks, replication/backup policy, recovery drills |
| R-10 | Power constraints force compute/storage shedding | Medium | High | Power budgets, load priorities, graceful degradation, restart verification |
| R-11 | Launch vibration/shock damages payload electronics | Low/Medium | High | Mechanical design review and mission-specific qualification testing |
| R-12 | Cyber compromise affects commands, updates, or data integrity | Medium | High | Threat model, authenticated commands, signed software, key lifecycle, audit |
| R-13 | Facility concept is mistaken for approved/operational infrastructure | Medium | High | Clearly label concept status; regulatory, environmental, and safety studies before claims |
| R-14 | Vendor examples are mistaken for qualified component selections | Medium | Medium | Maintain vendor-neutral requirements; verify exact part and qualification evidence |
| R-15 | Program roadmap assumes flight opportunities not under project control | Medium | Medium | Keep flight application opportunistic; prioritize ground/simulation readiness |

## Required risk workflow

1. Assign an owner and review date to every open risk.
2. Link each risk to requirements, scenarios, and verification evidence.
3. Reassess likelihood and impact after tests or architecture changes.
4. Escalate any safety-critical or mission-assurance risk for independent review.
5. Do not close a risk solely because a demonstration succeeds; record the scope and limits of the evidence.

## Important limitation

This is a preliminary qualitative planning register. It is not a formal hazard analysis, FMEA, fault tree, cybersecurity assessment, environmental qualification report, or regulatory determination.
