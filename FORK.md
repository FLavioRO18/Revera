# Fork notes

This is a modified fork of [kota-zo/Orpheon](https://github.com/kota-zo/Orpheon)
(Orpheon, GPL-3.0), itself the continuation of
[Myspoti](https://github.com/kota-zo/myspoti), named as the origin per the
project's notice. Modifications are marked in the commit messages on `main`:

- Visible downloads in `Download/Orpheon` (was `Music/Orpheon`); older files
  in `Music/Orpheon` are still read.
- Lyrics and cover embedded in the downloaded file (USLT+SYLT / APIC for MP3,
  ©lyr / covr for M4A, Vorbis LYRICS + PICTURE + `.lrc` sidecar for FLAC),
  before the public scan or the private encryption.
- A lyrics badge in the track rows (checked over Wi-Fi only, cached).

Upstream license and credits are kept unchanged.

Note: GitHub disables workflows on a forked repository by default; Actions was
enabled on this fork on 2026-11-15 via the « I understand my workflows »
button on the Actions page, so pushes to `main` run the Android workflow.
(The first run after enabling, 43752727234, failed at startup with no jobs
and no logs — likely the enablement still propagating; re-triggered by the
next push.)
