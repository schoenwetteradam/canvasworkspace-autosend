# Setup Walkthrough (for the helper)

This guide is written for **whoever is setting the tool up** — not the person
who'll use it every day. Do this once on her Windows laptop. After it's
working, her whole job is: *save a design into a folder, walk downstairs, press
Start.* (There's a separate large-print guide for her: `scan-n-cut-guide` /
the printable page.)

Set aside about 30–45 minutes the first time. None of these steps can damage
the laptop or the machine.

---

## What you're building

A small program that sits in the background and watches one folder. When a
finished cut file (`.fcm`, `.svg`, or `.dxf`) appears in that folder, it opens
Brother's CanvasWorkspace website, imports the file, and clicks **Send to my
machine** — so the design is queued on her ScanNCut DX by the time she walks
downstairs.

**It cannot press Start on the machine.** The blade only moves after she taps
Start on the machine itself — a safety gate Brother built in. Nothing here
changes that.

**It does not do embroidery.** This is a *cutting* workflow only.

---

## Before you start — check these

- [ ] The laptop is **Windows** (this walkthrough is Windows-specific).
- [ ] The **ScanNCut DX is on Wi‑Fi** and linked to a Brother/CanvasWorkspace
      account. On the machine: *Settings → Wireless LAN Setup*, then link it to
      the account at canvasworkspace.brother.com.
- [ ] You know the **CanvasWorkspace login** (email + password) for that
      account.

---

## Step 1 — Install Python

1. Go to **python.org → Downloads** and install Python 3.11 or newer.
2. **Important:** on the very first install screen, tick
   **“Add python.exe to PATH”** before clicking Install. If you miss this,
   the commands below won't be found.

## Step 2 — Install the tool's requirements

1. Put this whole folder somewhere permanent, e.g.
   `C:\ScanNCutAutoSend\`. Don't run it from Downloads.
2. Double‑click **`first_time_setup.bat`**.
   - A black window opens and installs everything it needs (this can take a few
     minutes and downloads a copy of Chromium — that's expected).
   - When it says **“Setup finished”**, close the window.

*(If double‑clicking is blocked, open the folder, click the address bar, type
`cmd`, press Enter, then type `first_time_setup.bat` and press Enter.)*

## Step 3 — Create her “To Send” folder

Make a normal folder she'll save designs into, for example:

```
C:\Users\HERNAME\CutFiles\ToSend
```

Anything she saves *here* gets sent. Pick somewhere easy for her to reach —
putting a shortcut to it on the Desktop is a kindness.

## Step 4 — Fill in `config.json`

1. In this folder, copy `config.example.json` and rename the copy to
   **`config.json`**.
2. Open `config.json` in Notepad and set `watch_folder` to the folder from
   Step 3. Use **double backslashes**, like the example:

   ```json
   "watch_folder": "C:\\Users\\HERNAME\\CutFiles\\ToSend"
   ```

3. Leave the three `selectors` as `REPLACE_ME` for now — you'll fill them in
   Step 6.

## Step 5 — Save her login once

1. Double‑click **`run_login_setup.bat`**.
2. A real browser window opens. **Log in to CanvasWorkspace** and make sure the
   dashboard shows her linked machine.
3. Go back to the black window and press **Enter**.
4. It saves the session to `storage_state.json` so she never has to log in
   again. *(Treat that file like a password — it's already excluded from git.)*

## Step 6 — Tell it which buttons to click (the fiddly bit)

The website changes over time, so the tool needs to be shown *which* buttons to
press. You do this once by copying three “selectors”.

1. Open CanvasWorkspace in **Chrome** and log in.
2. Press **F12** to open Developer Tools.
3. Click the little **arrow/cursor icon** at the top‑left of the Developer
   Tools panel (tooltip: “Select an element…”).
4. Click the real **Import** button on the page. Chrome highlights its HTML.
5. **Right‑click that highlighted line → Copy → Copy selector.**
6. Paste it into `config.json` as the value of `import_button`.
7. Repeat for:
   - the **file‑chooser input** that appears after you click Import → paste
     into `file_input`,
   - the **Send to my machine** button → paste into `send_to_machine_button`.

A filled‑in `config.json` looks roughly like:

```json
{
  "watch_folder": "C:\\Users\\HERNAME\\CutFiles\\ToSend",
  "selectors": {
    "import_button": "#import-btn",
    "file_input": "input[type=file]",
    "send_to_machine_button": "button.send-to-machine"
  }
}
```

*(Your actual values will look different — that's fine. What matters is that
they came from her live account.)*

## Step 7 — Test it

1. Double‑click **`run_watcher.bat`**. It should say
   *“Watching … for new cut files”*.
2. In another window, drop a real `.fcm` or `.svg` into the To Send folder.
3. A browser should open by itself, import the file, and send it. Check the
   machine — the design should appear in its queue.
4. If it worked, load a scrap on the mat and press **Start** on the machine to
   confirm the whole chain end‑to‑end.

If it fails, see **Troubleshooting** below — the most common cause is a
selector from Step 6 that no longer matches.

## Step 8 — Start it automatically at login (optional but recommended)

So she never has to remember to launch anything:

1. Press **Windows key**, type **Task Scheduler**, open it.
2. **Create Basic Task…** → name it *Scan N Cut Auto‑Send*.
3. Trigger: **When I log on**.
4. Action: **Start a program** → Browse to **`run_watcher.bat`** in this
   folder.
5. Finish. Now the watcher starts quietly every time she turns the laptop on.

To have it run truly hidden, tick *“Run whether user is logged on or not”* in
the task's properties — optional.

---

## Troubleshooting

| What you see | What it usually means | What to do |
| --- | --- | --- |
| `config.json not found` | You skipped Step 4 | Copy `config.example.json` → `config.json` and fill it in |
| `No saved session found` | Login wasn't saved | Run `run_login_setup.bat` again (Step 5) |
| Browser opens but nothing gets clicked / “Automation failed” | Brother changed their website, so a selector is stale | Redo Step 6 for the button that failed |
| It sends, but the design never reaches the machine | Machine offline or not linked | Check the machine's Wi‑Fi and that it's linked to the same account |
| `python is not recognized` | PATH wasn't ticked in Step 1 | Reinstall Python and tick **Add python.exe to PATH** |

When it breaks after months of working fine, it's almost always a website
change (Step 6), not a broken laptop. Re‑copying the three selectors fixes it.

---

## What she never has to do

Just so it's clear where your job ends and hers begins — she never touches any
of the above. Her entire routine is on the printable one‑page guide: design,
save into the folder, go downstairs, load the mat, press Start.
