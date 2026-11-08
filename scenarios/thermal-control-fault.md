# Scenario: Thermal-Control Loop Fault

## Objective

Train operators to recognize degraded telemetry, coordinate fault isolation, and verify return to nominal operations.

## Initial conditions

- Vehicle state: NOMINAL.
- Telemetry: power, life support, thermal regulation, and communications within illustrative operating bands.
- Mission control: staffed; event logging enabled.

## Exercise sequence

1. **INIT:** load the scenario and verify telemetry timestamps and subsystem identifiers.
2. **NOMINAL:** establish a stable baseline and acknowledge the status summary.
3. **DEGRADED:** inject a simulated thermal-control loop instability. Confirm the alert, assess correlated telemetry, and identify affected functions.
4. **RECOVERY:** isolate the simulated fault, follow the approved exercise checklist, and monitor dependent systems.
5. **NOMINAL:** verify all recovery criteria, document the event, and close the exercise.

## Expected operator behaviors

- Acknowledge and classify the alert.
- Maintain a shared situation report and timestamped event log.
- Avoid unverified commands and record decision rationale.
- Confirm subsystem stability before declaring recovery.

## Debrief prompts

- Was the anomaly detected and communicated clearly?
- Did operators distinguish symptoms from root cause?
- Were recovery criteria explicit and independently checked?
- What procedure, interface, or training improvements are needed?

**Safety note:** This is a desktop training scenario using fictional telemetry. It is not an operational procedure for real spacecraft or safety-critical systems.