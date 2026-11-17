# Course maintenance instructions

This repository manages a Chinese D2L learning course. Follow the user's latest instructions and read `docs/teaching-spec.md`, `curriculum.json`, and `progress.json` before preparing a lesson.

- Keep the agreed cadence: one 40-minute lesson daily at 20:00 Asia/Taipei.
- Use relative repository paths. This repository must work on ChatGPT Work cloud and on a local checkout.
- Publish complete, verified lesson packages and progress together. Do not claim unexecuted code was tested or unconfirmed lessons were completed.
- Use the official textbook and repository links stored in the curriculum. Preserve source attribution and any applicable upstream license notices.
- Keep credentials, raw personal feedback, private run metadata, local absolute paths and large downloaded datasets out of commits.
- Use short-lived scratch files under ignored `work/`. Do not rewrite existing lesson IDs or overwrite user submissions.
- Refresh the remote branch before publishing. Prefer a normal fast-forward commit; never force-push over concurrent work.
- Store public lesson delivery progress in `progress.json`. Scheduling and authentication belong to the cloud task's private settings.
