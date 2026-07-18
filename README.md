# canvasworkspace-autosend
1. Set up the GitHub repo
1.	Go to github.com → New repository → name it canvasworkspace-autosend → Private (keeps your setup off public view) → Create.
2.	Download the 6 files above into a folder on your laptop, e.g. C:\Users\Adam\canvasworkspace-autosend.
3.	Open PowerShell in that folder (Shift+Right-click the folder → "Open PowerShell window here"), then:
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/canvasworkspace-autosend.git
   git push -u origin main
2. Install Python
1.	Download Python 3.11+ from python.org/downloads.
2.	Run the installer — check "Add python.exe to PATH" at the bottom of the first screen before clicking Install. This is the step people miss and then nothing works from the terminal.
3.	Confirm it worked — open a new PowerShell window and run python --version. You should see a version number.
3. Install the project dependencies
In PowerShell, inside the project folder:
pip install -r requirements.txt
playwright install chromium
The second command downloads a Chromium browser Playwright controls directly — separate from your normal Chrome, so it won't interfere with your everyday browsing.
4. The folder to save your cut files to
This is a folder you create yourself — nothing from Brother auto-populates it. Make one now:
mkdir C:\Users\Adam\CutFiles\ToSend
This becomes your "drop zone." Whatever software you're designing cut files in, export/save the finished .fcm or .svg file into this folder instead of wherever you'd normally save it — the watcher script picks it up from there automatically.
5. Configure the script
1.	Copy config.example.json → rename the copy to config.json, in the same folder.
2.	Open config.json and set:
json
   "watch_folder": "C:\\Users\\Adam\\CutFiles\\ToSend"
(Note the double backslashes — that's required in JSON on Windows.)
3. Leave the selectors fields as REPLACE_ME for now — you'll fill those in next.
6. Log in once
python login_setup.py
A real browser window opens to CanvasWorkspace. Log in normally, confirm your ScanNCut DX is linked under your account, then go back to the PowerShell window and press Enter. This saves your session so the script won't need you to log in every time.
7. Find the real button selectors
With that same CanvasWorkspace browser tab open and logged in:
1.	Press F12 to open DevTools.
2.	Click the cursor icon top-left of the DevTools panel (or Ctrl+Shift+C).
3.	Click the actual "Import" button on the page — DevTools jumps to and highlights the matching HTML.
4.	Right-click that highlighted line → Copy → Copy selector.
5.	Paste it into config.json as "import_button".
6.	Do the same for the file upload element and the "Send to my machine" button.
I can't see your logged-in account, so this step has to happen on your end — but it's a five-minute, repeatable process, not coding.
8. Run it
python watcher.py
Leave that window open. Drop a test .fcm file into C:\Users\Adam\CutFiles\ToSend and watch it open a browser, import, and send.
9. (Optional) Run it automatically at login
Task Scheduler → Create Task → Trigger: "At log on" → Action: Start a program → Program: python, Arguments: C:\Users\Adam\canvasworkspace-autosend\watcher.py. Now it's always running in the background without you remembering to launch it.
Try steps 1–6 and let me know what you hit — step 7 is the one most likely to need a back-and-forth since I'm working blind on the actual page layout.

