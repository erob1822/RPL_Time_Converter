# Quick Guide: Making RPL Timezone Converter Available Offline on iPhone

## Overview

This repository now includes an "Iphone Test" folder with everything needed to make the RPL Timezone Converter work completely offline on iPhone devices.

## What Was Added

The "Iphone Test" folder contains:

1. **service-worker.js** - Caches files for offline use
2. **Updated index.html** - Includes service worker registration
3. **Enhanced manifest.json** - Better iOS PWA support
4. **README_IPHONE_OFFLINE.md** - Comprehensive installation guide
5. **Original files** - logo.jpg and all necessary assets

## Quick Start for iPhone Users

### Step 1: Deploy the App

Choose one of these options:

**Option A: GitHub Pages (Recommended)**
1. Copy contents of "Iphone Test" folder to the `docs` folder
2. Commit and push to GitHub
3. Enable GitHub Pages in repository settings (use `docs` folder)
4. Wait 1-2 minutes for deployment

**Option B: Other Hosting**
- Deploy to Netlify, Vercel, or any web host
- Must use HTTPS for service workers to work

### Step 2: Install on iPhone

1. Open the deployed URL in Safari on your iPhone
2. Tap the Share button (square with up arrow)
3. Select "Add to Home Screen"
4. Tap "Add"

### Step 3: Use Offline

1. The app icon appears on your home screen
2. After first visit, works completely offline
3. Test by enabling Airplane Mode - everything still works!

## Key Features for Offline Use

✅ **Fully Cached** - All files stored locally after first visit  
✅ **No Internet Required** - Works in Airplane Mode  
✅ **Home Screen Icon** - Launches like a native app  
✅ **Standalone Display** - No Safari browser UI when launched  
✅ **Auto Updates** - Gets latest version when online  

## File Structure

```
Iphone Test/
├── index.html              # Main app with service worker registration
├── service-worker.js       # Handles offline caching
├── manifest.json           # PWA configuration
├── logo.jpg               # App icon
└── README_IPHONE_OFFLINE.md # Detailed installation guide
```

## Important Notes

- **HTTPS Required**: Service workers only work over HTTPS (or localhost)
- **iOS 11.3+**: Requires iOS 11.3 or later for full PWA support
- **Safari Recommended**: Best compatibility with Safari browser
- **First Visit Online**: Must visit once while online to cache files

## Detailed Guide

For complete installation instructions, troubleshooting, and technical details, see:
**`Iphone Test/README_IPHONE_OFFLINE.md`**

## Testing Locally

To test before deploying:

```bash
# Navigate to Iphone Test folder
cd "Iphone Test"

# Start a local server (Python)
python3 -m http.server 8000

# Or use Node.js
npx http-server -p 8000
```

Then access from iPhone Safari at: `http://YOUR_COMPUTER_IP:8000`

## Original Files Unchanged

The original `docs` folder and all other files remain unchanged. The "Iphone Test" folder is completely separate for testing and deployment.

---

**Need Help?** Check the detailed guide in `Iphone Test/README_IPHONE_OFFLINE.md`
