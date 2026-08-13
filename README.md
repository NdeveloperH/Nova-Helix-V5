# Nova Helix

**An AI companion that lives on *your* computer — not in someone else's cloud.**

Nova Helix is a desktop AI assistant for Windows, powered by language models running
**entirely on your own hardware**. No account required to chat. No server round-trips.
No usage surveillance. What you tell Nova Helix stays on your machine.

🌐 **Website:** https://ndeveloperh.github.io/Nova-Helix-V5/

---

## What makes it different

- **100% local** — the models, your conversations, and your memories all live on your PC.
  Unplug the internet and Nova Helix keeps working.
- **It remembers you** — persistent memory across sessions, with semantic recall: it finds
  what matters by *meaning*, not just keywords. Erase it any time; erased means erased.
- **A companion, not a chatbox** — a warm, focused colleague with real personality, live
  status that shows exactly what it's doing (reading, recalling, thinking, drafting), and
  a desktop presence you can theme to your taste.
- **Honest by design** — it tells you what it doesn't know instead of making things up,
  and cites its sources when it searches.
- **Built for real hardware** — the Free tier runs on standard laptops. Higher tiers scale
  up to flagship-class local models for high-end GPUs.

## Tiers

| | Free | Pro | Ultra |
|---|---|---|---|
| Price | **$0** | **$20/mo** | **$33/mo** |
| Local chat companion | ✔ | ✔ | ✔ |
| Persistent memory + semantic recall | ✔ | ✔ | ✔ |
| Runs on standard laptops | ✔ | ✔ | ✔ |
| Stronger everyday models | | ✔ | ✔ |
| Expanded theme library | | ✔ | ✔ |
| Flagship-class local models | | | ✔ |
| Heavy coding & large projects | | | ✔ |
| Voice & live desktop experiences | | | ✔ |

## Under the hood (the short version)

- A custom high-performance inference engine written in **Rust + CUDA**, with a
  CPU path tuned so the Free tier genuinely runs on ordinary laptops.
- A native desktop app built with **Flutter**.
- Offline licence verification — your licence works without phoning home.
- Signed updates.

*This repository is the public showcase for Nova Helix. The product itself is
commercial software; the source is not published here.*

## Contact

Reach the developer via [GitHub](https://github.com/NdeveloperH) — open an issue on this repository.
