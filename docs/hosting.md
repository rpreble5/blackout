# Hosting and player memory

Decided 2026-09-13.

- The game itself stays static on GitHub Pages: https://rpreble5.github.io/blackout/
- Player memory (every answer, from which the void and topic stats are
  derived) lives in Supabase, a hosted Postgres with sign-in.
- Sign-in is Supabase's magic link by email (chosen 2026-09-13 over Google
  to avoid the OAuth setup).
- The game is local-first: every answer is written to the phone at once and
  synced when possible. Offline play loses nothing. Two devices merge by
  union of their logs.

Project: https://djxniucbbckvlnfngsys.supabase.co (ref `djxniucbbckvlnfngsys`).
The Supabase MCP server is configured in `.mcp.json` so Claude can run SQL
and read project settings once authenticated.

## What you need to do once

About fifteen minutes. The game runs fine before this is done; it just stays
local to each phone.

### 1. Create the Supabase project

1. Go to https://supabase.com, sign up or in, and create a new project.
   Any name; pick the region nearest you; set a database password. Yours is
   kept in `docs/local/secrets.md`, which git ignores, so it never reaches
   the public repo. The game never uses it.
2. When the project is ready, open **SQL Editor**, choose **New query**,
   paste the whole of `supabase/schema.sql` from this repo, and run it.
   It creates one table with row-level security so each player only ever
   touches their own rows.

### 2. Tell Supabase where the sign-in link should return

Magic-link email works out of the box, but the link must be allowed to
return to the game. In Supabase, **Authentication, URL Configuration**:

- Site URL: `https://rpreble5.github.io/blackout/blackout/`
- Redirect URLs: add `https://rpreble5.github.io/blackout/**` and, for local
  testing, `http://localhost:8765/**`.

Without this the link sends you to Supabase's default localhost page and
the sign-in does not complete. The built-in email sender allows only a few
messages an hour, which is plenty for one player; a custom SMTP provider can
be added later under **Authentication, SMTP Settings** if that ever bites.

### 3. Keys (done 2026-09-13)

The project URL and the publishable key are in the two constants near the
top of the sync block in `blackout/index.html`. The secret key is in the
git-ignored `docs/local/secrets.md` and is never used by the page:

```js
const SUPABASE_URL='https://djxniucbbckvlnfngsys.supabase.co',SUPABASE_KEY='sb_publishable_...';
```

The publishable key is meant to be public; the row-level security policies
are what protect the data. The secret key bypasses them, so it stays out of
the repo.

## How sync works

- Each answer becomes a log entry `{id, qid, topic, ok, ctx, at, device}`
  stored on the phone. `ctx` is planet, boss or void.
- When signed in, unsent entries are upserted to the `attempts` table by
  id, so retries never duplicate. Then any rows the phone hasn't seen are
  pulled by server arrival time and merged in.
- The void, the three-in-a-row release, what you have seen, and topic
  accuracy are all recomputed from the merged log. No state is stored that
  cannot be rebuilt.

## The void rules

- Any miss puts a question in the void (for multi-select, any error).
- A run opens with up to ten void questions, random, no repeats within the
  session, fewer if the void is smaller, none if it is empty.
- The void is a warm-up: misses do not cost lights.
- Three correct answers in a row to a question, counted wherever it is
  answered and across runs, release it from the void. A miss resets the
  streak and keeps it in.

## Looking at the data

In Supabase, **Table Editor, attempts** shows every row. The
`topic_accuracy` view gives correct over attempts per topic per player,
excluding void warm-ups.
