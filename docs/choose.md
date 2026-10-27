# Choose an input that fits the task

[Illustrated collection](../README.md) · [All setup notes](catalog.md)

Start with the action you want to perform, then the movements or equipment available to you. A detector, a mapping layer and a target application all need to agree. These are source-derived starting points, not independently tested recommendations.

## Follow the whole chain

```text
Human action           Detector / interface      Mapping             Result
voice or sound   →     microphone            →  commands       →    computer action
eye movement     →     supported eye tracker →  calibration    →    selection / typing
hand movement    →     tracking camera       →  gesture rules  →    cursor / control
physical object  →     sensor / interface    →  event mapping  →    app / game / sound
```

No single project supports every row. Check its own record for the actual equipment, host, target and limitations.

## Pick a concrete starting point

| You want to try | Project | Decisive requirement |
| --- | --- | --- |
| Speech or sound → desktop commands | [Talon](catalog.md#talon) | Microphone and a supported desktop OS |
| Gaze → on-screen typing | [OptiKey](catalog.md#optikey) | Windows and a tracker supported by the chosen version |
| Gaze → music | [EyeHarp](catalog.md#eyeharp) | Compatible tracker and the project's software route |
| Sip / puff → mapped commands | [QuadStick](catalog.md#quadstick) | Existing QuadStick hardware; check stock before buying |
| Printed paper → interactive programs | [Paper Playground](catalog.md#paper-playground) | Camera, printed codes and a development setup |
| Controller tilt → game aiming | [JoyShockMapper](catalog.md#joyshockmapper) | Supported gyroscope-equipped controller |
| Mouth and breath → computer input | [LipSync](catalog.md#lipsync) | Dedicated hardware build and available components |

## Questions that change the choice

| Question | Why it matters |
| --- | --- |
| Do you want text, a command, a pointer or an expressive control? | Dictation, shortcuts, cursor movement and musical expression are different outputs. |
| What input can be repeated comfortably and reliably? | Select the interaction around the person and task; a visually impressive demo is not a fit assessment. |
| Is a webcam enough, or does the project require a tracker/sensor? | Gaze and hand-tracking products may depend on specific hardware. |
| Which operating system and application receive the action? | Producing tracking data does not itself make every app controllable. |
| Can you calibrate and recover from mistakes? | Dwell timing, thresholds, lighting and an exit method affect usability. |
| Does the route require buying or building hardware? | A software download can still depend on a separate commercial or DIY interface. |

## Practical distinctions

**Speech versus non-speech sound.** Speaking a phrase, dictating text, and making a pop or hiss are different signals. Check what the selected project actually recognizes and which command set must be installed.

**Gaze versus head tracking.** Eye position and head orientation are different measurements. A project asking for a supported eye tracker should not be treated as a generic webcam app. Calibrate the exact setup before relying on its selection behavior.

**Tracking versus control.** A tracker or SDK may output coordinates, gestures or pose values. You still need a mapping and a receiving program. A research demonstration may have shown one specific integration only.

**An alternative input versus an access solution.** An unusual controller can be playful; a purpose-built access interface can be essential. This catalog makes no clinical or universal-suitability claim. For an individual setup, the user's preferences and observed results determine whether it helps.

## A small first trial

1. Choose one low-stakes action, such as moving a pointer in a test window or triggering one shortcut.
2. Confirm the exact detector/interface, OS and receiving application in the project's setup note.
3. Follow upstream calibration or mapping instructions. Keep an accessible way to stop or reset the test.
4. Record the action that worked, the action that failed and the conditions. Use the [test-report template](../.github/ISSUE_TEMPLATE/test-report.yml) to contribute a precise result.

## Search by the equipment or outcome

```sh
python3 scripts/catalog.py search "microphone"
python3 scripts/catalog.py search "Windows" --status released
python3 scripts/catalog.py search "视线" --json
```

The [specialist collections](landscape.md) cover alternative controllers, eye tracking, access technology, voice typing, WebHID and MIDI in more depth. Follow them when your choice needs more detail than a short project record.
