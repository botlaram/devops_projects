import nox

@nox.session
def run_script(session):
    # Install dependencies
    session.install('-r', 'requirements.txt')
    
    # Run main.py
    session.run('python', 'main.py')

@nox.session
def tests(session):
    # Install dependencies
    session.install('-r', 'requirements.txt')
    
    # Run tests
    session.run('pytest','test.py')
