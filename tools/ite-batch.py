"""Wire a new ITE batch into the game and run the style checks.

Usage, from the repo root:
  python tools/ite-batch.py <facts-fragment.md|-> <lo> <hi> <topic-file.json> [...] [--set <set-id>]

Pass "-" as the facts fragment to skip the facts append; --set names the set in index.json (default ite).

Appends the facts fragment to docs/facts/ite-2025.md (once), bumps the status line to "items 1 to <hi>",
adds the topic files to the ITE set in topics/index.json (once), then checks every question in those files:
stems over 118 characters, correct answer markedly longer or shorter than every distractor, absolute words
in distractors, and any reference to the exam, an item, a distractor, the other options or "the answer".
Exit code 1 if anything is flagged. Run tools/check-topics.py afterwards for the structural validation.
"""
import json, re, sys, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    args = sys.argv[1:]
    set_id = 'ite'
    if '--set' in args:
        i = args.index('--set'); set_id = args[i + 1]; del args[i:i + 2]
    frag, lo, hi, files = args[0], int(args[1]), int(args[2]), args[3:]
    facts = os.path.join(ROOT, 'docs', 'facts', 'ite-2025.md')
    s = open(facts, encoding='utf-8').read()
    if frag != '-' and f'## Item {lo}.' not in s:
        s = re.sub(r'Status: first pass, items 1 to \d+\.', f'Status: first pass, items 1 to {hi}.', s)
        s = s.rstrip('\n') + '\n' + open(frag, encoding='utf-8').read()
        open(facts, 'w', encoding='utf-8').write(s)
    idx_path = os.path.join(ROOT, 'blackout', 'topics', 'index.json')
    idx = json.load(open(idx_path, encoding='utf-8'))
    st = next(x for x in idx['sets'] if x['id'] == set_id)
    for f in files:
        if f not in st['topics']:
            st['topics'].append(f)
    json.dump(idx, open(idx_path, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

    qs = []
    for f in files:
        qs += json.load(open(os.path.join(ROOT, 'blackout', 'topics', f), encoding='utf-8'))['questions']
    print('n', len(qs), 'difficulty', dict(collections.Counter(q['difficulty'] for q in qs)),
          'multi', sum(q['type'] == 'multi' for q in qs), 'fixed', sum(q.get('order') == 'fixed' for q in qs))
    flags = 0
    for q in qs:
        opts = ([q['a']] if isinstance(q['a'], str) else q['a']) + q['d']
        if len(q['q']) > 118:
            print('long stem', q['id'], len(q['q'])); flags += 1
        if q['type'] == 'single' and q.get('order') != 'fixed':
            L = sorted(len(o) for o in opts)
            if len(q['a']) == L[-1] and len(q['a']) > 1.3 * L[-2]:
                print('long-answer tell', q['id'], len(q['a']), L[-2]); flags += 1
            if len(q['a']) < 0.6 * min(len(o) for o in q['d']):
                print('short-answer tell', q['id']); flags += 1
        for o in q['d']:
            if re.search(r'\b(always|never|everyone|all |anyone|only)\b', o, re.I):
                print('absolute', q['id'], '::', o); flags += 1
        for k in ('q', 'why'):
            if re.search(r'\bexam\b|\bitems?\b|distractor|the other option|the answer\b', q[k], re.I):
                print('reference', q['id'], k); flags += 1
        if not re.search(r'[.!?]$', q['why'].strip()):
            print('why not a sentence', q['id']); flags += 1
    print('flags', flags)
    sys.exit(1 if flags else 0)

if __name__ == '__main__':
    main()
