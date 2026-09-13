# Hosting and player memory

Decided 2026-09-13.

- The game itself stays static on GitHub Pages: https://rpreble5.github.io/blackout/
- Player memory (every answer, from which the void and topic stats are
  derived) lives in Supabase, a hosted Postgres with sign-in.
- Sign-in is Google.
- The game is local-first: every answer is written to the phone at once and
  synced when possible. Offline play loses nothing. Two devices merge by
  union of their logs.

## What you need to do once

About fifteen minutes. The game runs fine before this is done; it just stays
local to each phone.

### 1. Create the Supabase project

1. Go to https://supabase.com, sign up or in, and create a new project.
   Any name; pick the region nearest you; set a database password and keep
   it somewhere (you will rarely need it).
2. When the project is ready, open **SQL Editor**, choose **New query**,
   paste the whole of `supabase/schema.sql` from this repo, and run it.
   It creates one table with row-level security so each player only ever
   touches their own rows.

### 2. Turn on Google sign-in

1. In Supabase go to **Authentication, Providers, Google** and switch it on.
   Copy the **callback URL** it shows (it looks like
   `https://<project>.supabase.co/auth/v1/callback`).
2. In Google Cloud Console (https://console.cloud.google.com), create or
   pick a project, then **APIs and Services, Credentials, Create
   credentials, OAuth client ID**, type **Web application**.
   - Authorized JavaScript origins: `https://rpreble5.github.io`
   - Authorized redirect URIs: the Supabase callback URL from step 1.
   If it asks you to configure the consent screen first, choose External,
   fill in the app name and your email, and you can leave it in testing
   mode with yourself as a test user.
3. Copy the client ID and client secret back into the Supabase Google
   provider settings and save.
4. In Supabase, **Authentication, URL Configuration**:
   - Site URL: `https://rpreble5.github.io/blackout/blackout/`
   - Redirect URLs: add `https://rpreble5.github.io/blackout/**` and, for
     local testing, `http://localhost:8765/**`.

### 3. Hand over two values

In Supabase, **Settings, API**: copy the **Project URL** and the
**anon public** key. Paste them here in chat, or put them into the two
constants near the top of the sync block in `blackout/index.html`:

```js
const SUPABASE_URL='https://xxxx.supabase.co',SUPABASE_KEY='eyJ...';
```

The anon key is meant to be public; the row-level security policies are
what protect the data. Never share the **service_role** key.

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
