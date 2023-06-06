init:
	pdm install

dev:
	pdm run nvim src/example/__main__.py

local:
	pdm run python -m example
