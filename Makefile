install:
		poetry install

brain-games:
		poetry run brain-games

brain-even:
		poetry run brain-even

brain_calc:
		poetry run brain-calc

brain_gcd:
		poetry run brain-gcd

brain_progression:
		poetry run brain-progression

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user dist/*.whl --force-reinstall
		
lint:
		poetry run flake8 brain_games
