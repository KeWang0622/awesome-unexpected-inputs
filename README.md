![Awesome Unexpected Inputs — Make a move\. Make something happen\.](assets/cover.png)

# Awesome Unexpected Inputs

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Catalog checks](https://github.com/KeWang0622/awesome-unexpected-inputs/actions/workflows/check.yml/badge.svg)](https://github.com/KeWang0622/awesome-unexpected-inputs/actions/workflows/check.yml) [![CC0](https://img.shields.io/badge/catalog-CC0-173e30.svg)](LICENSE)

**English** · [简体中文](README.zh-CN.md)

**Make a move\. Make something happen\.**

An illustrated collection of ways to control computers with voice, gaze, movement, breath and everyday objects\. Each project connects a human input to a concrete action\.

**33 projects · 7 categories** — 24 Available setup · 4 Source / DIY build · 3 Research / prototype · 2 Archived / legacy.

[Setup notes](docs/catalog.md) · [Choose a starting point](docs/choose.md) · [Research & related work](docs/landscape.md) · [Offline search](docs/tooling.md) · [Contribute](CONTRIBUTING.md)

Cover and cards are original conceptual illustrations, not screenshots or test evidence. This catalog reviews published sources; we have not independently tested the listed setups. Every entry links its primary evidence and setup limits.

## Six places to start

| | |
| --- | --- |
| [![Talon: Hands\-free desktop commands](assets/talon.svg)](docs/catalog.md#talon)<br>**[Talon](docs/catalog.md#talon)**<br>Hands\-free desktop commands<br>*Available setup*<br>Needs: Microphone | [![OptiKey: Gaze typing and desktop access](assets/optikey.svg)](docs/catalog.md#optikey)<br>**[OptiKey](docs/catalog.md#optikey)**<br>Gaze typing and desktop access<br>*Available setup*<br>Needs: Supported eye tracker for gaze |
| [![EyeHarp: Perform music with gaze](assets/eyeharp.svg)](docs/catalog.md#eyeharp)<br>**[EyeHarp](docs/catalog.md#eyeharp)**<br>Perform music with gaze<br>*Available setup*<br>Needs: Separate Tobii eye tracker for gaze | [![QuadStick Manager: Adjustable sip\-and\-puff commands](assets/quadstick.svg)](docs/catalog.md#quadstick)<br>**[QuadStick Manager](docs/catalog.md#quadstick)**<br>Adjustable sip\-and\-puff commands<br>*Available setup*<br>Needs: QuadStick hardware; new units currently sold out |
| [![Paper Playground: Paper becomes a program interface](assets/paper-playground.svg)](docs/catalog.md#paper-playground)<br>**[Paper Playground](docs/catalog.md#paper-playground)**<br>Paper becomes a program interface<br>*Source / DIY build*<br>Needs: Webcam | [![JoyShockMapper: Gyro aiming in PC games](assets/joyshockmapper.svg)](docs/catalog.md#joyshockmapper)<br>**[JoyShockMapper](docs/catalog.md#joyshockmapper)**<br>Gyro aiming in PC games<br>*Available setup*<br>Needs: DualSense, DualShock 4, paired Joy\-Cons, or Switch Pro Controller |

## Explore the collection

[Voice and sound](#voice-and-sound) · [Eyes and face](#eyes-and-face) · [Head and body](#head-and-body) · [Hands in air](#hands-in-air) · [Objects and surfaces](#objects-and-surfaces) · [Tilt and motion](#tilt-and-motion) · [Breath and switches](#breath-and-switches)

<a id="voice-and-sound"></a>

## Voice and sound

Speech, commands and non\-speech sounds mapped to computer actions\.

- **[LipSurf](https://www.lipsurf.com/)** — Navigate browser pages, dictate text, and invoke commands using a microphone and a Chrome extension\. *Available setup* · [Evidence](https://www.lipsurf.com/) · [Setup & limits](docs/catalog.md#lipsurf).
- **[macOS Vocal Shortcuts](https://support.apple.com/en-euro/guide/mac-help/mchlf4548bb6/27/mac/27)** — Associate a trained word or custom sound with a chosen Mac action\. *Available setup* · [Evidence](https://support.apple.com/en-euro/guide/mac-help/mchlf4548bb6/27/mac/27) · [Setup & limits](docs/catalog.md#mac-vocal-shortcuts).
- **[macOS Voice Control](https://support.apple.com/en-ie/guide/mac-help/mh40719/27/mac/27)** — Use spoken commands to open apps, click controls, scroll pages, and dictate text on a Mac\. *Available setup* · [Evidence](https://support.apple.com/en-ie/guide/mac-help/mh40719/27/mac/27) · [Setup & limits](docs/catalog.md#mac-voice-control).
- **[Parrot\.py](https://github.com/chaosparrot/parrot.py)** — Train personally chosen clicks, chirps, or other non\-speech sounds to trigger keyboard and mouse actions\. *Research / prototype* · [Evidence](https://github.com/chaosparrot/parrot.py) · [Setup & limits](docs/catalog.md#parrot-py).
- **[Talon](https://talonvoice.com/)** — Operate desktop software through spoken commands and short mouth sounds; optionally combine them with gaze pointing\. *Available setup* · [Evidence](https://talonvoice.com/docs/reference/official.html) · [Setup & limits](docs/catalog.md#talon).
- **[VoiceAttack](https://www.voiceattack.com/)** — Turn spoken phrases into game controls, application shortcuts, and multi\-step macros\. *Available setup* · [Evidence](https://www.voiceattack.com/VoiceAttackHelpV2.pdf) · [Setup & limits](docs/catalog.md#voiceattack).
- **[Windows Voice Access](https://support.microsoft.com/en-us/accessibility/windows/voice-access/get-started-with-voice-access)** — Control Windows and compose text with speech recognition that runs locally after its language model is downloaded\. *Available setup* · [Evidence](https://support.microsoft.com/en-us/accessibility/windows/voice-access/get-started-with-voice-access) · [Setup & limits](docs/catalog.md#windows-voice-access).

<a id="eyes-and-face"></a>

## Eyes and face

Eye tracking and facial movement for typing, selection, games and music\.

- **[Android Camera Switches](https://support.google.com/accessibility/android/answer/11150722?hl=en)** — Map facial gestures to scanning and selection actions, using a phone's front camera as switch input\. *Available setup* · [Evidence](https://support.google.com/accessibility/android/answer/11150722?hl=en) · [Setup & limits](docs/catalog.md#android-camera-switches).
- **[EyeGestures Demo](https://github.com/NativeSensors/EyeGestures)** — Run a webcam gaze\-calibration example as a starting point for a custom gaze interface\. *Source / DIY build* · [Evidence](https://github.com/NativeSensors/EyeGestures) · [Setup & limits](docs/catalog.md#eyegestures).
- **[EyeHarp](https://eyeharp.org/)** — Play a musical instrument by selecting notes with gaze; head tracking or another pointer can also control it\. *Available setup* · [Evidence](https://eyeharp.org/faq/) · [Setup & limits](docs/catalog.md#eyeharp).
- **[EyeMine 2](https://www.specialeffect.org.uk/how-we-can-help/eyemine)** — Control Minecraft with a gaze\-operated onscreen interface for movement, building, and mining\. *Available setup* · [Evidence](https://www.specialeffect.org.uk/how-we-can-help/eyemine) · [Setup & limits](docs/catalog.md#eyemine).
- **[GazePlay](https://gazeplay.github.io/GazePlay/)** — Play small games using eye movement through an eye tracker that controls the pointer\. *Available setup* · [Evidence](https://gazeplay.github.io/GazePlay/) · [Setup & limits](docs/catalog.md#gazeplay).
- **[iPhone Eye Tracking](https://support.apple.com/en-sa/guide/iphone/iph66057d0f6/ios)** — Use the front camera to move a focus pointer with your eyes and select controls by dwelling\. *Available setup* · [Evidence](https://support.apple.com/en-sa/guide/iphone/iph66057d0f6/ios) · [Setup & limits](docs/catalog.md#iphone-eye-tracking).
- **[Look to Speak](https://play.google.com/store/apps/details?id=com.androidexperiments.looktospeak)** — Select prepared phrases or pictures with eye movements and have the phone speak the selection\. *Available setup* · [Evidence](https://play.google.com/store/apps/details?id=com.androidexperiments.looktospeak) · [Setup & limits](docs/catalog.md#look-to-speak).
- **[OptiKey](https://optikey.org/)** — Select an onscreen keyboard and desktop controls with gaze, dwell, or a compatible switch; composed text can be spoken aloud\. *Available setup* · [Evidence](https://github.com/OptiKey/OptiKey/wiki/Optikey-versions) · [Setup & limits](docs/catalog.md#optikey).
- **[Project Gameface](https://github.com/google/project-gameface)** — Combine head movement with facial gestures to move a cursor and trigger configured actions\. *Archived / legacy* · [Evidence](https://github.com/google/project-gameface) · [Setup & limits](docs/catalog.md#project-gameface).
- **[WebGazer Ball Collision Demo](https://webgazer.cs.brown.edu/)** — Move an orange ball toward a blue target with estimated gaze in a browser demonstration\. *Research / prototype* · [Evidence](https://webgazer.cs.brown.edu/) · [Setup & limits](docs/catalog.md#webgazer-ball-game).

<a id="head-and-body"></a>

## Head and body

Move a pointer, look around a game world or shape sound through motion\.

- **[AITrack](https://github.com/AIRLegend/aitrack)** — Estimate head position from a webcam and send it to opentrack for compatible simulator controls\. *Available setup* · [Evidence](https://github.com/AIRLegend/aitrack) · [Setup & limits](docs/catalog.md#aitrack).
- **[Body Synth](https://experiments.withgoogle.com/body-synth)** — Make music by moving your body in front of a webcam; optionally speak commands to change chords or instruments\. *Research / prototype* · [Evidence](https://experiments.withgoogle.com/body-synth) · [Setup & limits](docs/catalog.md#body-synth).
- **[Enable Viacam](https://eviacam.crea-si.com/)** — Translate head motion into pointer movement using an ordinary webcam, with dwell clicking available\. *Available setup* · [Evidence](https://eviacam.crea-si.com/index.php) · [Setup & limits](docs/catalog.md#eviacam).
- **[macOS Head Pointer](https://support.apple.com/en-ie/guide/mac-help/mchlb2d4782b/27/mac/27)** — Move the Mac pointer with head motion captured by a camera, pairing it with a chosen alternative click action\. *Available setup* · [Evidence](https://support.apple.com/en-ie/guide/mac-help/mchlb2d4782b/27/mac/27) · [Setup & limits](docs/catalog.md#mac-head-pointer).
- **[opentrack](https://github.com/opentrack/opentrack)** — Turn head motion into view movement in compatible games, including a webcam\-based neural\-network input option\. *Available setup* · [Evidence](https://github.com/opentrack/opentrack/wiki/AI-Face-Tracking/3d839e36c47074ad40de570e1abfb0dce865fd37) · [Setup & limits](docs/catalog.md#opentrack).
- **[SmoothTrack](https://smoothtrack.app/)** — Use a phone camera as a head tracker for PC games through opentrack\. *Available setup* · [Evidence](https://smoothtrack.app/) · [Setup & limits](docs/catalog.md#smoothtrack).

<a id="hands-in-air"></a>

## Hands in air

Hand tracking becomes touchless control with the specified tracking hardware\.

- **[Ultraleap TouchFree \(legacy\)](https://docs.ultraleap.com/TouchFree/touchfree-user-manual/setup.html)** — Operate screen controls with tracked hand movement and hover or virtual\-plane selection\. *Archived / legacy* · [Evidence](https://docs.ultraleap.com/TouchFree/touchfree-user-manual/setup.html) · [Setup & limits](docs/catalog.md#touchfree).

<a id="objects-and-surfaces"></a>

## Objects and surfaces

Paper, markers and conductive materials become program interfaces\.

- **[Makey Makey Piano and Scratch](https://makeymakey.com/blogs/how-to-instructions/lesson-two-hands-on-a-makey-makey)** — Connect conductive everyday objects to keyboard inputs, then use them to play a browser piano or control Scratch\. *Available setup* · [Evidence](https://makeymakey.com/blogs/how-to-instructions/lesson-two-hands-on-a-makey-makey) · [Setup & limits](docs/catalog.md#makey-makey).
- **[Paper Playground](https://phetsims.github.io/paper-land/)** — Arrange printed, encoded papers to control interactive web programs, sound, and other outputs through a camera\. *Source / DIY build* · [Evidence](https://phetsims.github.io/paper-land/) · [Setup & limits](docs/catalog.md#paper-playground).
- **[reacTIVision](https://reactivision.sourceforge.net/)** — Track printed markers on physical objects and send their movement to TUIO clients or MIDI software\. *Available setup* · [Evidence](https://reactivision.sourceforge.net/) · [Setup & limits](docs/catalog.md#reactivision).

<a id="tilt-and-motion"></a>

## Tilt and motion

Gyroscopes, phones and small boards produce aiming, pointing and musical control\.

- **[JoyShockMapper](https://github.com/Electronicks/JoyShockMapper)** — Map a compatible controller's gyroscope to mouse aiming and configure flick\-stick or motion bindings for PC games\. *Available setup* · [Evidence](https://github.com/Electronicks/JoyShockMapper) · [Setup & limits](docs/catalog.md#joyshockmapper).
- **[micro:bit Scratch Theremin](https://microbit.org/projects/make-it-code-it/scratch-theremin/)** — Tilt a micro:bit to change musical pitch in a Scratch project\. *Source / DIY build* · [Evidence](https://microbit.org/projects/make-it-code-it/scratch-theremin/) · [Setup & limits](docs/catalog.md#microbit-theremin).
- **[Mobile Mouse Air Mouse](https://mobilemouse.com/guides/iphone-air-mouse/)** — Move an iPhone in the air to steer a computer pointer while holding an onscreen trigger\. *Available setup* · [Evidence](https://mobilemouse.com/guides/iphone-air-mouse/) · [Setup & limits](docs/catalog.md#mobile-mouse-air).

<a id="breath-and-switches"></a>

## Breath and switches

Purpose\-built interfaces map sip/puff, switches and compact movements to input\.

- **[Intel ACAT](https://github.com/intel/acat)** — Use configured switches or camera\-based actuators to select a scanning keyboard and communicate through speech output\. *Available setup* · [Evidence](https://github.com/intel/acat) · [Setup & limits](docs/catalog.md#acat).
- **[LipSync 4\.1](https://github.com/makersmakingchange/LipSync)** — Combine a mouth\-operated joystick with sip\-and\-puff inputs to control a mouse or gamepad through an open hardware hub\. *Source / DIY build* · [Evidence](https://github.com/makersmakingchange/LipSync) · [Setup & limits](docs/catalog.md#lipsync).
- **[QuadStick Manager](https://www.quadstick.com/downloads)** — Configure sip\-and\-puff pressure thresholds and mappings for QuadStick's game and computer controls\. *Available setup* · [Evidence](https://quadstick.s3.amazonaws.com/documents/user_manual/um/sip_puff_tab.htm) · [Setup & limits](docs/catalog.md#quadstick).

## Curation, not a compatibility promise

Entries need a concrete outcome, primary evidence and explicit requirements. Research demonstrations, archived projects and installable software are labeled separately. Public source does not automatically mean an open-source license. Review dates record source inspection, not successful device tests.

Original catalog prose and diagrams: [CC0](LICENSE). Scripts: [MIT](LICENSE-CODE). Linked projects keep their licenses. Read the [method](docs/methodology.md), [visual credits](assets/README.md), [testing protocol](docs/testing.md), and [contribution guide](CONTRIBUTING.md).

**Source review / 资料核查：2026-10-26** · [Machine-readable catalog](data/projects.json) · [Changelog](CHANGELOG.md)

**Explore next:** [awesome-device-afterlife](https://github.com/KeWang0622/awesome-device-afterlife) · [Awesome iPhone Duo](https://github.com/KeWang0622/awesome-iphone-duo)
