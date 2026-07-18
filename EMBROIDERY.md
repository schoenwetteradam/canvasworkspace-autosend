# Sending to the embroidery machines (helper notes)

This repo automates the **ScanNCut DX cutter**. Her embroidery machines are
separate and use Brother's *own* transfer tools — nothing in this repo is
needed for them, and you should **not** try to drive them through the
folder-watcher. This page just records how each one works so it's all in one
place.

## Brother Aveneer (EV1) — the easy one: laptop → machine over Wi‑Fi

Use Brother's free **Design Database Transfer** for Windows. It sends `.pes`
embroidery designs from the laptop to the Aveneer wirelessly — no USB stick,
no tablet. This is the officially supported path, so prefer it over any
workaround.

**One-time setup (you do this once):**

1. Put the **laptop and the Aveneer on the same home Wi‑Fi.** They must share
   one network or the transfer won't find the machine.
2. Download **Design Database Transfer** from Brother's support site
   (search “Design Database Transfer” on support.brother.com) and install it
   on the laptop. It's free.
3. Open it → **Network Machine Settings → Add**. The Aveneer should appear as
   a machine on the network. Select it and register it.
4. Make a desktop shortcut named plainly (e.g. *Design Database Transfer*) so
   she can find it.

**Her everyday flow** (there's a printable large-print card for this):

1. Have the `.pes` design saved on the laptop.
2. Open Design Database Transfer, pick the design, click **Transfer**.
3. Wait for **“Finished outputting data.”**
4. On the Aveneer: **Embroidery → Pocket icon → Wi‑Fi symbol →** tap the
   design.
5. Hoop the fabric and press **Start** on the machine.

**Limit to be honest about:** Design Database Transfer *sends* finished `.pes`
files; it does not create or digitize them. Designs come from the machine's
built-ins, purchased `.pes`, the Artspira app, or digitizing software.

*(The Aveneer can also receive designs wirelessly from the **Artspira** phone/
tablet app — best for creating brand-new designs on the go. Same machine, two
valid paths: Design Database Transfer from the laptop, Artspira from a tablet.)*

## Baby Lock Valiant — memory stick only

The 10-needle Valiant has **no wireless**. Save the design as `.pes` (it also
accepts `.pen`, `.phc`, `.dst`) onto a USB memory stick, plug the stick into
the machine, and pick the design on its screen. There's nothing to automate
here — a USB stick is already the simplest route. Best kept for bigger,
multi-color jobs when you're around to help.

## Baby Lock (IQ Visionary) & serger

Her main sewing/quilting machine and the serger take no design files — she
just sews. No setup needed.

## Which to reach for

| She wants to… | Use |
| --- | --- |
| Cut paper/fabric | ScanNCut DX — the laptop folder-watcher in this repo |
| Embroider from the laptop | **Aveneer + Design Database Transfer** (Wi‑Fi) |
| Create a new design on a tablet, then embroider | Aveneer + **Artspira** app |
| Big multi-color embroidery | Valiant + **USB stick** |
| Just sew or quilt | Baby Lock sewing machine / serger |
