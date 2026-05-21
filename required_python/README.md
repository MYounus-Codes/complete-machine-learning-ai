# Required Python Curriculum

This folder is a self-contained, topic-based Python learning path designed for beginners and intermediate learners. Each topic contains focused examples, exercises, and three staged projects (basic / medium / advanced) so you can practice and build confidence progressively.

Quick links

- Overview: [required_python/README.md](required_python/README.md)
- Topics index: [required_python](required_python)

Structure

- `README.md` — this file with usage and contribution notes
- `<topic>/` — one folder per topic (e.g. `basics`, `loops`, `data_types`, `functions`, `oops`)
	- `README.md` — short topic overview and learning order
	- `*_intro.py` — readable examples for the topic
	- `*_exercises.py` — small, testable exercises
	- `projects/`
		- `basic/` — starter project (beginner-friendly)
		- `medium/` — intermediate project (multi-step)
		- `advanced/` — larger project (integrates concepts)

How to use this curriculum

1. Pick a topic folder (start with `basics` if you are new to Python).
2. Read the topic `README.md` and open the `*_intro.py` examples.
3. Run the exercises in `*_exercises.py` and try to solve them before looking at answers.
4. Build the `basic` project first, then try `medium`, and finally `advanced` when comfortable.
5. Keep your `.env` private — use the provided `.env.example` for configuration samples.

Running examples and projects

Most examples and projects are plain Python scripts with an `if __name__ == "__main__"` runner. To run an example or project from the repository root:

```bash
python -m required_python.basics.basics_intro
python -m required_python.loops.projects.basic.countdown_timer
```

Note: On Windows, use `python` that points to your virtual environment; on Unix/macOS the same commands apply.

Project progression guidance

- Basic projects: focus on correct use of the core language (variables, control flow, simple I/O). These should run with minimal dependencies.
- Medium projects: introduce composition (multiple functions / simple data structures) and basic error handling.
- Advanced projects: combine several ideas into a small system with clear separation of concerns (functions or classes) and simple input/output formatting.

Contribution and extension

- If you add or improve a topic, follow the existing folder layout and include:
	- a clear `README.md` describing the learning path for the topic
	- examples that are intentionally short and well-commented
	- exercises with expected behaviors
	- at least one project per level in the `projects/` subfolder
- Keep secrets out of the repository: never commit a real `.env` — use `.env.example` to show configuration variables.
- Make small, topic-scoped commits so changes are easy to review.

Repository tips

- Branching: create feature branches per topic (e.g. `topic/loops-enhancements`).
- Tests: the examples are executable scripts — if you add non-trivial logic consider adding simple unit tests under a `tests/` folder.
- Formatting: keep code readable; follow PEP 8 where practical.

Where to go next

- Start with `required_python/basics/README.md` or pick the topic you want to improve and follow its README learning order.

If you'd like, I can:

- Add unit tests for selected exercises.
- Create a small `Makefile` or `invoke` tasks to run examples quickly.
- Generate a single-page curriculum index that links directly to each file.

---

This README was updated to provide clearer guidance, runnable examples, and a predictable project progression for each topic.