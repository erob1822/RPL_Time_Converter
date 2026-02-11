# RPL Timezone Converter ⏰

A small, self-contained HTML/JS tool that displays UTC and a selected timezone's local time, lets you set a 24‑hour (military) target time (date + hour:minute:second), and shows a live countdown to that target. Designed to work fully offline and handle daylight‑savings adjustments where the browser's Intl implementation supports it.

## Features ✅
- **UTC + Local clocks** (updates every second)
- **Target time** input with Date / Hour / Minute / Second (24‑hour) for both UTC and local (auto‑sync)
- **DST-aware** conversions using `Intl.formatToParts` and robust wall‑time → UTC conversion
- **All timezones included** (uses `Intl.supportedValuesOf('timeZone')` when available, with a fallback IANA list)
- **Offline-ready** — no network requests, Base64 logo embedded

## Usage 🛠️
1. Open `clock.html` in a browser (double-click or open via `file://`).
2. Select a timezone (default: `UTC`).
3. Set a target date and time with the Date / Hour / Minute / Second controls.
4. The countdown displays "Time to Target" and updates every second.

## Notes on Daylight Saving Time (DST) ⚠️
- The app uses the browser's Intl timezone data to compute offsets and conversions. Most modern browsers include full TZ/DST support offline.
- Edge cases:
  - *Ambiguous times* (when clocks fall back) can map to two UTC instants.
  - *Non‑existent times* (when clocks jump forward) are handled by convergence logic; you can choose how to handle these cases if you prefer (warn/reject/choose earliest).

## Offline & Compatibility 🔌
- Works without internet — all resources are embedded and all logic runs in the browser.
- If the runtime's Intl implementation lacks full timezone data, some zones may not behave as expected. The UI will indicate "Invalid timezone" for unsupported zones.

## Testing Tips ✅
- To test offline: disconnect your machine, open `clock.html` locally and verify the timezone dropdown populates and countdown behaves.
- Try DST boundary dates (spring & fall transitions) for a zone like `America/New_York` to confirm conversions.

## Development Notes 🧰
- The main file is `clock.html`. It is now a clone of `docs/index.html` (used for GitHub Pages). Edit `clock.html` to make updates; if you want I can propagate those changes to `docs/index.html` and push them for you.
- I will not commit changes to your repository unless you explicitly ask me to.

---
If you'd like, I can add a small automated test page to exercise DST boundary cases or generate a compact list of the representative timezones used in the dropdown. 💡