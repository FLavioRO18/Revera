# Fork notes

**Revera** (`caruno-git/Revera`) is a modified GPL-3.0 fork of [Myspoti](https://github.com/kota-zo/myspoti) / [kota-zo/Orpheon](https://github.com/kota-zo/Orpheon), named as the origin per the project's GPL-3.0 notice (`LICENSE`, `AGENTS.md`).

Modifications in this fork:

- Rebranded package and app labels to **Revera** (`app.revera`, updates via `caruno-git/Revera`).
- Visible downloads saved in `Download/Revera` (with backwards-compatible reading of `Download/Orpheon` and `Music/Orpheon`).
- Lyrics and cover embedded in the downloaded file (USLT+SYLT / APIC for MP3, ©lyr / covr for M4A, Vorbis LYRICS + PICTURE + `.lrc` sidecar for FLAC), before the public scan or the private encryption.
- A lyrics badge in the track rows (checked over Wi-Fi only, cached).
- Server-verified profile badges and launcher icons (`ECDSA P-256`).
- Rust ARM64 CDN audio transport (`orpheon-audio-transport`) and Compose backdrop rendering optimizations.
- Login flow and diagnostic log improvements.

Upstream license (GPL-3.0) and credits are kept unchanged.
