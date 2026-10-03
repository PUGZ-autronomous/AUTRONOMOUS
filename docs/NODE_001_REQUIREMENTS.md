# NODE-001: home host and replaceable control devices

Owner requirement, 3 October 2026: AUTRONOMOUS runs on the PC at home. The current travel laptop must be replaceable without interrupting the system or losing its work.

## Responsibilities

| Location | Responsibility |
| --- | --- |
| Home PC, NODE-001 | Run the service and workers; own persistent business state, schedules, files, model credentials and logs. |
| Travel laptop or phone | Display the control room and submit instructions through authenticated private access. |
| GitHub repository | Keep source code, reviewed changes and documentation. |
| Separate protected backup | Recover node state and business files if the home disk or PC fails. |

This is a deployment requirement, not an installed topology. The foundation build is still local demo software. Its web engine history is not yet durable.

## Acceptance checks before unattended use

1. Close the control browser and shut down the travel laptop. Workers and schedules continue on NODE-001.
2. Reconnect from a second authorised device. The same tasks, pause state, business files and reconciled data appear.
3. Reboot NODE-001. Services restart without an interactive desktop login; new-run pause remains unchanged. No admitted task is silently duplicated. Incomplete external actions are reconciled before retry.
4. Restore a backup to a replacement node. Essential work is recoverable without the travel laptop. The original and replacement node cannot both execute the same scheduled business actions.
5. Revoke a lost device's private-network access and application sessions from another trusted device. NODE-001 keeps operating. Revoke any SSH keys or credentials actually held on the lost device as well.

## Access and data boundaries

The control laptop must not be the only place storing task queues, service credentials, business files or recovery information. Do not keep the home system alive through a terminal on that laptop.

Private-network reachability and application identity are separate controls. The inherited web pages automatically create a privileged local session, so the current app must remain bound to localhost. Real remote operator authentication, device/session revocation and the access proxy still need implementing and checking. No public router forwarding is part of this plan.

Losing the laptop should affect access, not the worker runtime. It can still expose logged-in accounts or downloaded data. Device revocation and account recovery must be possible independently of that laptop.

GitHub stores code; it is not the runtime-state backup. Include the actual persistent databases and business files in the node backup, and protect credential backups separately. Recovery must preserve pauses and approval boundaries.

## Information needed for installation

- CPU model and RAM capacity.
- Storage type, capacity and available space; files/Windows installation to preserve.
- GPU model, if any.
- Current operating system.
- Whether it can use wired Ethernet and remain powered on.
- Firmware support for restoring power after an outage.

Select the operating system, drive layout and any purchases after checking these details. Before enabling a live worker, finish durable state, task admission/cancellation, bounded provider use, backups and remote access checks.
