# Builds exampacket/exampacket.tex from scribes/main.tex and the weekly packets.
# Run from the repo root: python exampacket/build_exampacket.py .  then pdflatex in exampacket/ (three passes).
import re, pathlib, sys

repo = pathlib.Path(sys.argv[1])
out = repo / 'exampacket'
(out / 'tex').mkdir(parents=True, exist_ok=True)
BS = chr(92)

# The questions most likely on the exam, 2--3 per week.
PICK = {
    1: ['pp:membership', 'wp:kcopies'],
    2: ['pp:balls', 'pp:coupon', 'pp:bday365'],
    3: ['pp:leader3', 'pp:triangle'],
    4: ['pp:five', 'pp:unitary'],
    5: ['pp:dj', 'wp:deutsch'],
    6: ['pp:bv', 'pp:simon', 'wp:indep4'],
    7: ['pp:grover8', 'wp:mean8', 'pp:amp100'],
}

blocks = {}
for f in sorted((repo / 'weeklypackets/tex').glob('week*.tex')):
    s = f.read_text(encoding='utf8')
    for m in re.finditer(r'\\begin\{exercisebox\}.*?\\end\{exercisebox\}', s, re.S):
        lab = re.search(r'\\label\{((?:pp|wp):[^}]+)\}', m.group(0))
        if lab:
            blocks[lab.group(1)] = m.group(0)

for w, labs in PICK.items():
    body = [BS + 'practiceweek{' + str(w) + '}', '']
    for lab in labs:
        body += [blocks[lab], '']
    (out / f'tex/practice_week{w}.tex').write_text('\n'.join(body), encoding='utf8')

main = (repo / 'scribes/main.tex').read_text(encoding='utf8')

preamble = r'''
% Practice questions after each week (not part of the submitted scribes).
\theoremstyle{definition}
\newcounter{practiceweek}
\newtheorem{pproblem}{Practice Problem}
\renewcommand{\thepproblem}{\arabic{practiceweek}.\arabic{pproblem}}
\crefname{pproblem}{Practice Problem}{Practice Problems}
\Crefname{pproblem}{Practice Problem}{Practice Problems}
\newcommand{\scr}[1]{\cref{#1}, p.~\pageref{#1}}
\newcommand{\uses}[1]{\noindent\textit{Scribes:} #1.\par}
\AtBeginEnvironment{wsolution}{\setlength{\parskip}{0.35em}}
\makeatletter
\newcommand{\practiceweek}[1]{%
    \par\FloatBarrier
    \vspace{0.4in}%
    \needspace{2.5in}%
    \setcounter{practiceweek}{#1}%
    \setcounter{pproblem}{0}%
    \phantomsection
    \addcontentsline{toc}{lecture}{Practice questions, week #1}%
    \hrule
    \vspace{0.1in}
    \noindent\textbf{Practice questions for week #1} (likely exam questions, with solutions)\par
    \vspace{0.1in}
    \hrule
    \vspace{0.1in}
}
\makeatother
'''

# Load the scribe style files from ../scribes, and add the practice definitions.
main = main.replace(BS + 'documentclass[a4paper,11pt,final]{article}',
                    BS + 'documentclass[a4paper,11pt,final]{article}\n' + BS + 'makeatletter\n'
                    + BS + 'def' + BS + 'input@path{{../scribes/}}\n' + BS + 'makeatother', 1)
main = main.replace(BS + 'begin{document}', preamble + '\n' + BS + 'begin{document}', 1)
main = main.replace('% My scribes for all the lectures, in one document.',
                    '% Exam copy: my scribes (../scribes/tex) with practice questions after each week.\n'
                    '% Generated from scribes/main.tex; build from this folder, three passes.', 1)

# Insert each week's practice questions before the next \newweek, and week 7 after the last lecture.
weeks = [m.start() for m in re.finditer(r'^\\newweek\{', main, re.M)]
assert len(weeks) == 7, len(weeks)
last = main.index(BS + 'input{tex/lecture_2026-10-08}')
last = main.index('\n', last) + 1
inserts = [(weeks[i], i) for i in range(1, 7)] + [(last, 7)]
for pos, w in sorted(inserts, reverse=True):
    main = main[:pos] + BS + 'input{tex/practice_week' + str(w) + '}\n\n' + main[pos:]

(out / 'exampacket.tex').write_text(main, encoding='utf8')
print('problems', sum(len(v) for v in PICK.values()))
