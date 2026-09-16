-- もしもし相談室 MVP
-- Supabase SQL Editor でそのまま実行できます。

create extension if not exists pgcrypto;

create table if not exists public.consultations (
  id uuid primary key default gen_random_uuid(),
  figure_name text not null check (figure_name in ('楠木正成', '小野篁', '平重盛', '空海')),
  concern text not null check (char_length(concern) <= 1200),
  answer jsonb not null,
  figure_version text,
  source_version text,
  created_at timestamptz not null default now()
);

create table if not exists public.feedback (
  id uuid primary key default gen_random_uuid(),
  consultation_id uuid references public.consultations(id) on delete set null,
  helpful boolean not null,
  created_at timestamptz not null default now()
);

create index if not exists consultations_created_at_idx
  on public.consultations (created_at desc);

create index if not exists feedback_created_at_idx
  on public.feedback (created_at desc);

alter table public.consultations enable row level security;
alter table public.feedback enable row level security;

-- MVPではStreamlitサーバー側から Supabase Secret Key を使って保存します。
-- Secret Key はRLSをバイパスできるため、GitHubやブラウザ側へ絶対に公開しないでください。
-- anon / authenticated 向けの公開ポリシーは作成しません。
