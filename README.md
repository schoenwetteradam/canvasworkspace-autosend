# CanvasWorkspace Auto-Send

Watches a folder on your Windows laptop. Whenever you drop a finished cut
file into it, the script opens CanvasWorkspace in a browser, imports the
file, and sends it to your linked ScanNCut DX so it's sitting in the
machine's queue by the time you walk downstairs.

## What this is (and isn't)

- Brother doesn't publish a developer API for CanvasWorkspace or the
  ScanNCut DX. This tool works by driving the real CanvasWorkspace
  *website* the same way you would with a mouse — clicking Import,
  picking your file, clicking "Send to my machine" — just done by code
  instead of by hand.
- Because it depends on the website's current layout, **Brother
  changing their site can break it**. That's expected with this kind of
  tool; when it breaks, you re-find the button and update `config.json`
  (see "Finding selectors" below), you don't need to touch the Python.
- It **does not** and cannot start the actual cut on the machine — that
  still requires you to load the mat and tap Start on the ScanNCut's own
  screen. That's a safety gate Brother built into the machine itself,
  not something this script can or should bypass.
- This does not work for the Aveneer/Artspira side — Artspira is
  mobile-app only, with no desktop or browser version to automate
  against.
- This is a **cutting** workflow only. It does **not** do embroidery —
  embroidery needs an embroidery machine and different files (e.g.
  `.pes`). The ScanNCut can still *support* embroidery by cutting
  perfect appliqué pieces, but it won't stitch.

## Quick start

- **Setting it up?** Follow **[SETUP.md](SETUP.md)** — a step-by-step
  Windows walkthrough written for whoever installs this.
- **Just want to use it every day?** See the printable large-print guide
  (`scan-n-cut-guide`): design → save into the folder → go downstairs →
  load the mat → press Start.

- **Sending to her embroidery machines?** That's separate from this repo —
  see **[EMBROIDERY.md](EMBROIDERY.md)**. In short: the Aveneer takes designs
  from the laptop wirelessly via Brother's free *Design Database Transfer*; the
  Baby Lock Valiant takes a USB stick.

There are three double-click launchers so nobody has to type commands:

| File | What it does |
| --- | --- |
| `first_time_setup.bat` | Installs everything, once. |
| `run_login_setup.bat` | Saves the CanvasWorkspace login. |
| `run_watcher.bat` | Starts the folder watcher (the one that runs all day). |

## Folder structure

```
canvasworkspace-autosend/
├── README.md
├── requirements.txt
├── config.example.json   -> copy to config.json and edit
├── login_setup.py         -> run once to save your login session
├── watcher.py              -> the script that runs continuously
└── .gitignore
```

## One-time setup

1. Install Python 3.11+ from python.org (check "Add python.exe to PATH"
   during install).
2. Open a terminal in this folder and run:
   ```
   pip install -r requirements.txt
   playwright install chromium
   ```
3. Copy `config.example.json` to `config.json` and edit:
   - `watch_folder`: the folder you'll save finished cut files into
     (e.g. `C:\Users\Adam\CutFiles\ToSend`). This is just a regular
     folder you create yourself — pick wherever you already save
     exported .fcm/.svg files from your design software.
4. Run `python login_setup.py`. A real browser window opens — log in to
   CanvasWorkspace normally, then press Enter in the terminal. This
   saves your session to `storage_state.json` so the watcher doesn't
   need you to log in every time.
5. Run `python watcher.py`. Leave it running in the background.
6. Drop a `.fcm` or `.svg` file into your watch folder — the script
   should open a browser, import it, and send it to your machine.

## Finding selectors

`config.json` has three placeholders under `"selectors"` that tell
Playwright which buttons to click. I can't see your logged-in
CanvasWorkspace account, so these need to be filled in once, by you:

1. Open CanvasWorkspace in Chrome, log in.
2. Press F12 to open DevTools, click the arrow/cursor icon (top-left of
   DevTools), then click the actual "Import" button on the page.
3. DevTools highlights the matching HTML. Right-click it in DevTools →
   Copy → Copy selector.
4. Paste that into `config.json` under `import_button`.
5. Repeat for the file upload input and the "Send to my machine" button.

## Running it automatically at login (optional)

Once it's working reliably, use Windows Task Scheduler to launch
`run_watcher.bat` at login so you never have to remember to start it —
full steps are in **[SETUP.md](SETUP.md)** (Step 8).

## Security note

`storage_state.json` contains your live login session — treat it like a
password. It's already excluded in `.gitignore` so it won't get pushed
to GitHub, but double check before your first commit.
