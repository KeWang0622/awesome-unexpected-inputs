# Awesome Unexpected Inputs: setup notes

[Back to the illustrated collection](../README.md) · [中文入口](../README.zh-CN.md)

These are brief, source-derived routes into each project, not substitute installation manuals or executed test reports. Follow the linked upstream instructions for the exact version and device.

## Voice and sound

<a id="lipsurf"></a>

### LipSurf

**Voice\-operated browsing** · Available setup · Source reviewed 2026-10-26

**Device / input:** Chrome on Windows, macOS, Linux or Chromebook

**You need:** Microphone; LipSurf extension; Free daily allowance; paid unlimited plan

1. Install the extension\.
2. Allow microphone access\.
3. Use its command help to navigate\.

**Limits:** Controls supported browser workflows\. Free plan limits daily commands\.

[Project](https://www.lipsurf.com/) · [Primary evidence](https://www.lipsurf.com/)

**Evidence:** Developer describes supported platforms and voice commands\.

<a id="mac-vocal-shortcuts"></a>

### macOS Vocal Shortcuts

**Personal sound shortcuts** · Available setup · Source reviewed 2026-10-26

**Device / input:** Apple silicon Mac

**You need:** Microphone

1. Open Accessibility → Vocal Shortcuts\.
2. Choose an action\.
3. Repeat the chosen utterance during setup\.

**Limits:** Requires Apple silicon\. Each utterance needs training\.

[Project](https://support.apple.com/en-euro/guide/mac-help/mchlf4548bb6/27/mac/27) · [Primary evidence](https://support.apple.com/en-euro/guide/mac-help/mchlf4548bb6/27/mac/27)

**Evidence:** Apple describes custom utterances and on\-device recognition\.

<a id="mac-voice-control"></a>

### macOS Voice Control

**Navigate a Mac by voice** · Available setup · Source reviewed 2026-10-26

**Device / input:** Mac

**You need:** Microphone; Supported recognition language

1. Enable Voice Control in Accessibility settings\.
2. Open its tutorial\.
3. Use Show Commands to discover actions\.

**Limits:** Standard Dictation is unavailable while Voice Control runs\.

[Project](https://support.apple.com/en-ie/guide/mac-help/mh40719/27/mac/27) · [Primary evidence](https://support.apple.com/en-ie/guide/mac-help/mh40719/27/mac/27)

**Evidence:** Apple documents commands and the built\-in tutorial\.

<a id="parrot-py"></a>

### Parrot\.py

**Custom sound controls** · Research / prototype · Source reviewed 2026-10-26

**Device / input:** Windows; macOS; Linux X11

**You need:** Microphone; 64\-bit Python 3\.8

1. Record labeled sounds\.
2. Train and inspect the model\.
3. Configure actions and run play\.py\.

**Limits:** Prototype; training required\. Gaze control requires separate software\.

[Project](https://github.com/chaosparrot/parrot.py) · [Primary evidence](https://github.com/chaosparrot/parrot.py)

**Evidence:** README documents recording, training and playback\.

<a id="talon"></a>

### Talon

**Hands\-free desktop commands** · Available setup · Source reviewed 2026-10-26

![Conceptual workflow for Talon](../assets/talon.svg)

**Device / input:** Windows; macOS; Linux X11

**You need:** Microphone; Compatible command set; Free speech engine; optional paid Talon\+

1. Install Talon\.
2. Configure speech recognition and commands\.
3. Practice commands or sound actions\.

**Limits:** Linux Wayland unsupported\. Eye pointing needs compatible tracking hardware\.

[Project](https://talonvoice.com/) · [Primary evidence](https://talonvoice.com/docs/reference/official.html)

**Evidence:** Official installation and input documentation\.

<a id="voiceattack"></a>

### VoiceAttack

**Speak a command sequence** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows

**You need:** Microphone; Paid registration beyond the limited free trial

1. Install and select the microphone\.
2. Create a phrase with actions\.
3. Test the command in its target application\.

**Limits:** Trial limits profiles and commands\. Macros require configuration\.

[Project](https://www.voiceattack.com/) · [Primary evidence](https://www.voiceattack.com/VoiceAttackHelpV2.pdf)

**Evidence:** Developer manual describes profiles and command actions\.

<a id="windows-voice-access"></a>

### Windows Voice Access

**Offline voice control** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows 11 22H2 or later

**You need:** Microphone; Initial language\-model download

1. Enable Voice Access in Accessibility settings\.
2. Download the language and configure microphone\.
3. Complete the interactive guide\.

**Limits:** Supported languages vary\. Initial setup needs internet\.

[Project](https://support.microsoft.com/en-us/accessibility/windows/voice-access/get-started-with-voice-access) · [Primary evidence](https://support.microsoft.com/en-us/accessibility/windows/voice-access/get-started-with-voice-access)

**Evidence:** Microsoft documents setup and the interactive guide\.

## Eyes and face

<a id="android-camera-switches"></a>

### Android Camera Switches

**Face gestures select controls** · Available setup · Source reviewed 2026-10-26

**Device / input:** Compatible Android device

**You need:** Front camera; Switch Access

1. Open Switch Access setup\.
2. Choose Camera Switch and assign gestures\.
3. Adjust gesture size and hold time\.

**Limits:** Cannot operate alongside other camera apps\. Initial setup may require assistance\.

[Project](https://support.google.com/accessibility/android/answer/11150722?hl=en) · [Primary evidence](https://support.google.com/accessibility/android/answer/11150722?hl=en)

**Evidence:** Google documents gesture assignments and setup\.

<a id="eyegestures"></a>

### EyeGestures Demo

**Prototype gaze input** · Source / DIY build · Source reviewed 2026-10-26

**Device / input:** Python\-capable computer

**You need:** Webcam; Python dependencies

1. Install eyeGestures and obtain examples\.
2. Run examples/simple\_example\_v4\.py\.
3. Calibrate at the documented viewing distance\.

**Limits:** Developer integration required\. Dependency installation may need adjustment\.

[Project](https://github.com/NativeSensors/EyeGestures) · [Primary evidence](https://github.com/NativeSensors/EyeGestures)

**Evidence:** README documents package installation and example execution\.

<a id="eyeharp"></a>

### EyeHarp

**Perform music with gaze** · Available setup · Source reviewed 2026-10-26

![Conceptual workflow for EyeHarp](../assets/eyeharp.svg)

**Device / input:** Windows

**You need:** Separate Tobii eye tracker for gaze; Registration and license key; Free basic piano; paid full edition

1. Register and download EyeHarp\.
2. Install and activate the emailed key\.
3. Connect the tracker and choose an instrument\.

**Limits:** Tracker calibration is required\.

[Project](https://eyeharp.org/) · [Primary evidence](https://eyeharp.org/faq/)

**Evidence:** Developer FAQ explains installation, trackers and editions\.

<a id="eyemine"></a>

### EyeMine 2

**Play Minecraft with gaze** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows

**You need:** Paid Minecraft Java Edition license \(1\.14\.4\); Compatible eye tracker

1. Install EyeMine and the supported Minecraft version\.
2. Configure the eye tracker\.
3. Start with the beginner keyboard\.

**Limits:** Not a console or mobile Minecraft solution\. Tracker compatibility varies\.

[Project](https://www.specialeffect.org.uk/how-we-can-help/eyemine) · [Primary evidence](https://www.specialeffect.org.uk/how-we-can-help/eyemine)

**Evidence:** SpecialEffect specifies the supported game and input setup\.

<a id="gazeplay"></a>

### GazePlay

**Gaze\-controlled games** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows; macOS; Linux

**You need:** Compatible eye tracker

1. Install the platform build\.
2. Configure the tracker input\.
3. Choose a game\.

**Limits:** Direct Tobii integration is Windows\-specific\. Other trackers need pointer emulation\.

[Project](https://gazeplay.github.io/GazePlay/) · [Primary evidence](https://gazeplay.github.io/GazePlay/)

**Evidence:** Project site provides downloads and tracker requirements\.

<a id="iphone-eye-tracking"></a>

### iPhone Eye Tracking

**Look to select iPhone controls** · Available setup · Source reviewed 2026-10-26

**Device / input:** Supported iPhone

**You need:** Front camera; Stable, well\-lit placement

1. Enable Eye Tracking in Accessibility\.
2. Follow the calibration dots\.
3. Look at a control to dwell\-select\.

**Limits:** Model support varies\. Recalibration occurs when enabled\.

[Project](https://support.apple.com/en-sa/guide/iphone/iph66057d0f6/ios) · [Primary evidence](https://support.apple.com/en-sa/guide/iphone/iph66057d0f6/ios)

**Evidence:** Apple documents calibration and dwell selection\.

<a id="look-to-speak"></a>

### Look to Speak

**Gaze\-selected spoken phrases** · Available setup · Source reviewed 2026-10-26

**Device / input:** Android phone

**You need:** Front camera

1. Install and allow camera access\.
2. Complete the setup tutorial\.
3. Use eye movements to select a phrase\.

**Limits:** Selects prepared content rather than unrestricted dictation\.

[Project](https://play.google.com/store/apps/details?id=com.androidexperiments.looktospeak) · [Primary evidence](https://play.google.com/store/apps/details?id=com.androidexperiments.looktospeak)

**Evidence:** Google listing describes selection and on\-device processing\.

<a id="optikey"></a>

### OptiKey

**Gaze typing and desktop access** · Available setup · Source reviewed 2026-10-26

![Conceptual workflow for OptiKey](../assets/optikey.svg)

**Device / input:** Windows

**You need:** Supported eye tracker for gaze

1. Match tracker to OptiKey version\.
2. Install the appropriate edition\.
3. Configure pointing and dwell selection\.

**Limits:** Version 4 drops several older Tobii trackers; check compatibility\.

[Project](https://optikey.org/) · [Primary evidence](https://github.com/OptiKey/OptiKey/wiki/Optikey-versions) · [Source code](https://github.com/OptiKey/OptiKey)

**Evidence:** Version matrix documents hardware compatibility changes\.

<a id="project-gameface"></a>

### Project Gameface

**Face\-operated cursor prototype** · Archived / legacy · Source reviewed 2026-10-26

**Device / input:** Windows; Android

**You need:** Camera; Platform\-specific setup

1. Follow the relevant platform README\.
2. Grant camera access\.
3. Configure gestures and movement sensitivity\.

**Limits:** Archived; no ongoing upstream maintenance\. Separate platform implementations\.

[Project](https://github.com/google/project-gameface) · [Primary evidence](https://github.com/google/project-gameface)

**Evidence:** Google archived the repository on September 5, 2025\.

<a id="webgazer-ball-game"></a>

### WebGazer Ball Collision Demo

**A webcam gaze game** · Research / prototype · Source reviewed 2026-10-26

**Device / input:** Browser\-equipped computer

**You need:** Webcam; Camera permission

1. Open the Ball Collision demo\.
2. Allow camera access and calibrate\.
3. Look toward the target ball\.

**Limits:** Updates are not guaranteed from February 2026\. Calibration quality varies\.

[Project](https://webgazer.cs.brown.edu/) · [Primary evidence](https://webgazer.cs.brown.edu/) · [Source code](https://github.com/brownhci/WebGazer)

**Evidence:** Project page links the gaze game and calibration guidance\.

## Head and body

<a id="aitrack"></a>

### AITrack

**Webcam simulator head tracking** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows

**You need:** Webcam; opentrack

1. Download AITrack\.
2. Configure opentrack to receive its UDP output\.
3. Start both programs and center tracking\.

**Limits:** Requires a separate opentrack installation\. Lighting and camera placement matter\.

[Project](https://github.com/AIRLegend/aitrack) · [Primary evidence](https://github.com/AIRLegend/aitrack)

**Evidence:** README documents opentrack integration and camera requirements\.

<a id="body-synth"></a>

### Body Synth

**Body movement plays music** · Research / prototype · Source reviewed 2026-10-26

**Device / input:** Compatible browser

**You need:** Webcam; Microphone for optional voice commands

1. Launch the experiment and allow camera access\.
2. Adjust movement sensitivity\.
3. Move to generate notes\.

**Limits:** Browser experiment; availability may change\. Camera framing and sensitivity need adjustment\.

[Project](https://experiments.withgoogle.com/body-synth) · [Primary evidence](https://experiments.withgoogle.com/body-synth)

**Evidence:** Creator's experiment page explains movement and voice controls\.

<a id="eviacam"></a>

### Enable Viacam

**Webcam head mouse** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows; Linux

**You need:** Webcam

1. Install the suitable build\.
2. Run the camera configuration wizard\.
3. Adjust speed and dwell timing\.

**Limits:** Published Windows requirements list older releases; verify your system\.

[Project](https://eviacam.crea-si.com/) · [Primary evidence](https://eviacam.crea-si.com/index.php)

**Evidence:** Official site provides downloads and configuration guidance\.

<a id="mac-head-pointer"></a>

### macOS Head Pointer

**Head\-operated pointer** · Available setup · Source reviewed 2026-10-26

**Device / input:** Mac

**You need:** Built\-in or connected camera

1. Enable Head Pointer in Pointer Control\.
2. Choose the camera and movement settings\.
3. Configure an alternative click action\.

**Limits:** Pointer movement and clicking require separate configuration\.

[Project](https://support.apple.com/en-ie/guide/mac-help/mchlb2d4782b/27/mac/27) · [Primary evidence](https://support.apple.com/en-ie/guide/mac-help/mchlb2d4782b/27/mac/27)

**Evidence:** Apple describes head movement and alternative clicking\.

<a id="opentrack"></a>

### opentrack

**Look around game worlds** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows; Linux; macOS

**You need:** Webcam for neuralnet input; Compatible game

1. Install an appropriate build\.
2. Select neuralnet input and game output\.
3. Start tracking and center the view\.

**Limits:** Available builds differ by platform\. Game output must be supported\.

[Project](https://github.com/opentrack/opentrack) · [Primary evidence](https://github.com/opentrack/opentrack/wiki/AI-Face-Tracking/3d839e36c47074ad40de570e1abfb0dce865fd37)

**Evidence:** Preserved project\-wiki revision documents neural\-network face tracking\.

<a id="smoothtrack"></a>

### SmoothTrack

**Phone\-powered head tracking** · Available setup · Source reviewed 2026-10-26

**Device / input:** Supported iPhone or Android phone; PC

**You need:** Paid SmoothTrack app; Free opentrack; Compatible phone tracking support

1. Install opentrack on the PC\.
2. Configure the documented UDP connection\.
3. Position the phone and start tracking\.

**Limits:** Phone compatibility varies; Android requires ARCore\. Network restrictions can block UDP\.

[Project](https://smoothtrack.app/) · [Primary evidence](https://smoothtrack.app/)

**Evidence:** Developer provides phone\-to\-PC setup instructions\.

## Hands in air

<a id="touchfree"></a>

### Ultraleap TouchFree \(legacy\)

**Touchless screen interaction** · Archived / legacy · Source reviewed 2026-10-26

**Device / input:** Windows

**You need:** Separate Ultraleap Hand Tracking Camera; Administrator installation access; Appropriate Ultraleap license

1. Consult setup guide and confirm installer availability\.
2. Connect the dedicated camera and run Camera Setup\.
3. Choose and tune the interaction mode\.

**Limits:** Installer links lead to a generic page or gateway error\. Commercial deployment needs separate licensing\.

[Project](https://docs.ultraleap.com/TouchFree/touchfree-user-manual/setup.html) · [Primary evidence](https://docs.ultraleap.com/TouchFree/touchfree-user-manual/setup.html) · [Source code](https://github.com/ultraleap/TouchFree)

**Evidence:** Documentation survives; old source repository archived, current installer chain unresolved\.

## Objects and surfaces

<a id="makey-makey"></a>

### Makey Makey Piano and Scratch

**Objects become touch controls** · Available setup · Source reviewed 2026-10-26

**Device / input:** USB computer

**You need:** Purchased Makey Makey board; Alligator clips; Conductive objects

1. Connect the board by USB\.
2. Open the piano or Scratch example\.
3. Hold EARTH and touch connected inputs\.

**Limits:** Input objects must conduct electricity\. Requires the hardware board\.

[Project](https://makeymakey.com/blogs/how-to-instructions/lesson-two-hands-on-a-makey-makey) · [Primary evidence](https://makeymakey.com/blogs/how-to-instructions/lesson-two-hands-on-a-makey-makey)

**Evidence:** Manufacturer lesson demonstrates piano and Scratch\.

<a id="paper-playground"></a>

### Paper Playground

**Paper becomes a program interface** · Source / DIY build · Source reviewed 2026-10-26

![Conceptual workflow for Paper Playground](../assets/paper-playground.svg)

**Device / input:** Computer

**You need:** Webcam; Printer; Local project setup

1. Follow Installation and Device Setup\.
2. Create and print encoded papers\.
3. Move papers while viewing program output\.

**Limits:** Requires installation and camera alignment\. Projector is optional\.

[Project](https://phetsims.github.io/paper-land/) · [Primary evidence](https://phetsims.github.io/paper-land/) · [Source code](https://github.com/phetsims/paper-land)

**Evidence:** PhET project documents tangible programs and Creator\.

<a id="reactivision"></a>

### reacTIVision

**Physical objects control software** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows; macOS; Linux

**You need:** Camera; Printed fiducial markers; TUIO or MIDI receiver

1. Print the supplied markers\.
2. Start the camera tracker\.
3. Connect a TUIO client or MIDI receiver\.

**Limits:** No bundled synthesizer or visualization engine\. Check older binary compatibility\.

[Project](https://reactivision.sourceforge.net/) · [Primary evidence](https://reactivision.sourceforge.net/)

**Evidence:** Project describes marker recognition and output protocols\.

## Tilt and motion

<a id="joyshockmapper"></a>

### JoyShockMapper

**Gyro aiming in PC games** · Available setup · Source reviewed 2026-10-26

![Conceptual workflow for JoyShockMapper](../assets/joyshockmapper.svg)

**Device / input:** Windows; Linux source builds

**You need:** DualSense, DualShock 4, paired Joy\-Cons, or Switch Pro Controller

1. Download a release\.
2. Connect a supported controller\.
3. Load and calibrate a game configuration\.

**Limits:** Linux builds may require fixes\. Sensitivity needs per\-game tuning\.

[Project](https://github.com/Electronicks/JoyShockMapper) · [Primary evidence](https://github.com/Electronicks/JoyShockMapper)

**Evidence:** Current official fork documents controllers and configuration\.

<a id="microbit-theremin"></a>

### micro:bit Scratch Theremin

**Tilt\-controlled musical pitch** · Source / DIY build · Source reviewed 2026-10-26

**Device / input:** Scratch\-compatible computer; micro:bit

**You need:** Scratch Link; Bluetooth connection

1. Set up Scratch Link and connect micro:bit\.
2. Open the supplied project\.
3. Tilt forward and backward to change pitch\.

**Limits:** Uses board tilt, not hand distance\. Requires compatible Scratch connectivity\.

[Project](https://microbit.org/projects/make-it-code-it/scratch-theremin/) · [Primary evidence](https://microbit.org/projects/make-it-code-it/scratch-theremin/)

**Evidence:** Foundation tutorial supplies the project and connection guidance\.

<a id="mobile-mouse-air"></a>

### Mobile Mouse Air Mouse

**A phone becomes an air mouse** · Available setup · Source reviewed 2026-10-26

**Device / input:** iPhone; Mac or Windows computer

**You need:** Paid Mobile Mouse app; Computer server; Wi\-Fi connection

1. Install the app and server\.
2. Confirm the connection with trackpad mode\.
3. Open Air Mouse and hold its trigger\.

**Limits:** Separate server required for this workflow\. Release trigger to reposition\.

[Project](https://mobilemouse.com/guides/iphone-air-mouse/) · [Primary evidence](https://mobilemouse.com/guides/iphone-air-mouse/)

**Evidence:** Developer guide describes the Wi\-Fi air\-mouse workflow\.

## Breath and switches

<a id="acat"></a>

### Intel ACAT

**Switch\-selected communication** · Available setup · Source reviewed 2026-10-26

**Device / input:** Windows

**You need:** Compatible actuator or webcam

1. Install the base ACAT release\.
2. Configure an actuator in Dashboard\.
3. Launch scanning and compose a message\.

**Limits:** Input setup is device\-specific\. Not every gesture is a supported actuator\.

[Project](https://github.com/intel/acat) · [Primary evidence](https://github.com/intel/acat)

**Evidence:** Intel provides the toolkit and actuator configuration\.

<a id="lipsync"></a>

### LipSync 4\.1

**Mouth and breath computer controls** · Source / DIY build · Source reviewed 2026-10-26

**Device / input:** Computers; Compatible mobile devices

**You need:** LipSync joystick and hub; Components, fabrication or maker assistance

1. Build or request the documented hardware\.
2. Connect the hub and choose a mode\.
3. Calibrate joystick and pressure settings\.

**Limits:** Custom hardware required\. Listed interface cable is currently unavailable\.

[Project](https://github.com/makersmakingchange/LipSync) · [Primary evidence](https://github.com/makersmakingchange/LipSync)

**Evidence:** Maintainer supplies hardware, firmware and build documentation\.

<a id="quadstick"></a>

### QuadStick Manager

**Adjustable sip\-and\-puff commands** · Available setup · Source reviewed 2026-10-26

![Conceptual workflow for QuadStick Manager](../assets/quadstick.svg)

**Device / input:** Windows

**You need:** QuadStick hardware; new units currently sold out; Mounting arm

1. Connect QuadStick and open the Sip/Puff tab\.
2. Adjust pressure thresholds and timing\.
3. Save preferences to QuadStick\.

**Limits:** Vendor currently lists controller models sold out\. Actions depend on the selected profile\.

[Project](https://www.quadstick.com/downloads) · [Primary evidence](https://quadstick.s3.amazonaws.com/documents/user_manual/um/sip_puff_tab.htm)

**Evidence:** Manufacturer manual documents pressure settings; QMP 4 installer remains downloadable\.
