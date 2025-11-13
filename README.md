# python_314_samples
Code Samples that demonstrates latest version of python

$ uv init
$ uv add pydantic
$ uv run user_demo.py
$ uv add typer


#Not sure why greet is not accepted. This gives error
uv run cli_builder_demo.py greet Krishna

#This works
uv run cli_builder_demo.py Krishna      
Hey Krishna, welcome to Python 3.14!

Got it. Since we had just one command, that was defaulted and typer
did not allow giving command explicitly.

If we have more than one command, then we have to explicitly give the command

$ uv run cli_builder_demo.py greet Krishna
Hey Krishna, welcome to Python 3.14!

$ uv run cli_builder_demo.py farewell Balaji
Goodbye Balaji, see you soon!

$ uv run print_demo.py 
$ uv add polars
$ uv run polars_demo.py
$ uv add playwright
$uv run playwright_demo.py gave error that playwright was not installed.
I need to run the command within virtual environment
$ venv
(python-314-samples) $ playwright install 

$ uv add tenacity
$ uv run retry_demo.py
$ uv add prefect
$ uv run workflow_demo.py

prefect seems to be not compatible with some libraries and python 3.14
so dropping it
$ uv remove prefect

