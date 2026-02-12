# RPL Timezone Converter

A small, self-contained HTML/JS tool that displays UTC and a selected timezone's local time, lets you set a 24‑hour (military) target time (date + hour:minute:second), and shows a live countdown to that target. Designed to work fully offline and handle daylight‑savings adjustments where the browser's Intl implementation supports it.

## Features
- **UTC + Local clocks** (updates every second)
- **Target time** input with Date / Hour / Minute / Second (24‑hour) for both UTC and local (auto‑sync)
- **DST-aware** conversions using `Intl.formatToParts` and robust wall‑time → UTC conversion
- **All timezones included** (uses `Intl.supportedValuesOf('timeZone')` when available, with a fallback IANA list)
- **Offline-ready** — no network requests, Base64 logo embedded

## Usage 
1. Open `clock.html` in a browser (double-click or open via `file://`).
2. Select a timezone (default: `UTC`).
3. Set a target date and time with the Date / Hour / Minute / Second controls.
4. The countdown displays "Time to Target" and updates every second.
