# Music during calls: emulator verification

This is an opt-in under **Settings → Playback → Music during calls**, off by default. It skips Revera's call-specific pause and temporarily hands off Media3's automatic focus handling while Android reports a call. Audio attributes, media volume and routing are unchanged. Android, the audio route and the browser can still pause, duck or mute playback. Revera does not force a restart for the opted-in case. If playback stopped before the call state was reported, try Play manually once the call is active.

## Source/JVM checks

From the repository root, run `python tools/check_call_music_locales.py` (no Android build). When builds are allowed, run from `base`:

```sh
./gradlew :app:testDebugUnitTest --tests '*CallPauseTest' --tests '*SettingsSearchTest'
```

## Run later on an emulator with a candidate APK already installed

Use a phone AVD with a dialer and working playback (API 31+ for audio-mode callbacks; repeat on API 29/30 to exercise the legacy telephony watcher). Start with a local music file to remove network, sign-in and DRM variables. Repeat with a downloaded song, a native Spotify track on an image with working Widevine, and Spotify with native audio disabled. Test Web Player only after verifying it plays outside a call; Chromium's own behavior is not controlled by the switch. Record the API, package/version, source and audio route.

1. With fresh preferences, verify the switch is off. Enable it in Classic, check it in Immersive, relaunch the app and check persistence. Turn it off in Immersive and check Classic. Search for the setting in both looks. Repeat the UI check in an RTL locale and a locale with partial translations, such as Arabic and Finnish.
2. Start a track with the switch **off**. Simulate an incoming call, answer it, then hang up. Compare with the previous release on the same image: normal focus and the existing call pause/resume rules should remain in effect. If a call paused a Web Player track, confirm that a manual pause during the call cancels the app's automatic resume. A track already paused before ringing must not start by itself.
3. Repeat with the switch **on** and the same track/route. Sample media position before ringing, twice during the active call (a few seconds apart) and after hang-up. Separately note whether music is audible. There should be no Revera `pause asked by phone call` or `play asked by phone call`; Media3 should switch to call mode and return to normal focus. If Android or WebView stops/mutes playback, record that result rather than counting an advancing position as proof of audio. Also try pressing Play during an active call and moving to the next song. Neither turning the setting on nor ending the call should restart a track you deliberately paused.
4. Toggle off during an active call; verify focus policy returns to normal. With the switch on but no call in progress, start a competing media app and confirm Revera still responds to normal focus loss. Verify disconnecting headphones still pauses local playback; a mirrored player should remain silent and Cast/Connect playback elsewhere should not receive phone-call transport commands.

From another terminal, substitute the actual emulator serial for `emulator-5554`. Use the dialer to answer if the modem command does not advance Telecom to an active call. Wait between phases to gather samples:

```sh
adb -s emulator-5554 logcat -v time -s Myspoti
adb -s emulator-5554 emu gsm call 15550100123
adb -s emulator-5554 emu gsm accept 15550100123
adb -s emulator-5554 shell dumpsys audio
adb -s emulator-5554 shell dumpsys media_session
adb -s emulator-5554 emu gsm cancel 15550100123
```

Look for `audio mode: …` (or `call state: …` on API 29/30), `music during calls: call mode`, and `music during calls: normal focus`. If no call transition is observed, record a call-detection failure for that AVD, not an opt-in pass. If available, compare the focus stack and playback state with listening observations. Emulator GSM calls have no voice audio: they cannot establish real cellular voice/media co-existence, Bluetooth call routing or OEM-specific behavior. Do not override audio modes, permissions or system muting to get a pass.

References: [Android Audio Focus](https://developer.android.com/media/optimize/audio-focus), [Emulator Console](https://developer.android.com/studio/run/emulator-console#telephony).
