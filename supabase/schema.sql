-- Blackout: player memory.
-- Run this once in the Supabase SQL editor (Database, SQL Editor, New query, paste, Run).
--
-- One table, append-only. Every answer a player gives is one row. The game derives
-- everything else (the void, streaks, topic accuracy) from these rows, on the device.

create table if not exists public.attempts (
  id          uuid primary key,                       -- generated on the device, so offline entries have stable ids
  user_id     uuid not null references auth.users (id) on delete cascade,
  qid         text not null,                          -- question id, e.g. as-dx-01
  topic       text not null,                          -- topic id, e.g. aortic-stenosis-diagnosis
  ok          boolean not null,
  ctx         text not null check (ctx in ('planet', 'boss', 'void')),
  at          timestamptz not null,                   -- when the player answered, device clock
  device      text,
  created_at  timestamptz not null default now()      -- when the row reached the server; used for incremental pulls
);

create index if not exists attempts_user_created on public.attempts (user_id, created_at);
create index if not exists attempts_user_qid on public.attempts (user_id, qid);

-- Row-level security: a signed-in player sees and writes only their own rows.
alter table public.attempts enable row level security;

drop policy if exists "players read own attempts" on public.attempts;
create policy "players read own attempts"
  on public.attempts for select
  using (auth.uid() = user_id);

drop policy if exists "players insert own attempts" on public.attempts;
create policy "players insert own attempts"
  on public.attempts for insert
  with check (auth.uid() = user_id);

-- The game upserts on id so a retried sync never duplicates. Updates only touch a row the player owns.
drop policy if exists "players update own attempts" on public.attempts;
create policy "players update own attempts"
  on public.attempts for update
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

-- No delete policy on purpose: the log is append-only.

-- Handy views for looking at progress from the dashboard (respect the same policies).
create or replace view public.topic_accuracy as
  select user_id, topic,
         count(*) filter (where ctx <> 'void') as attempts,
         count(*) filter (where ctx <> 'void' and ok) as correct
  from public.attempts
  group by user_id, topic;
