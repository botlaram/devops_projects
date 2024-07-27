import nox

DEFAULT_TEST_DIRECTORIES=['./tests']

@nox.session
def run_script(session):
    """run main"""
    # Install dependencies
    session.install('-r', 'requirements.txt')

    # Run the scrip
    session.chdir("src")

    # Run main.py
    session.run('python', 'main.py')

@nox.session
def tests(session):
    """run test cases"""
    # Install dependencies
    session.install('-r', 'requirements.txt')
    session.env["FORCE_COLOUR"] = "1"
    
    # pass test case dir as args to pytest
    if session.posargs:
        args=session.posargs
    else:
        args=DEFAULT_TEST_DIRECTORIES
  
    # Run tests
    session.run('python', '-m', 'pytest')
