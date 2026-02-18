from flask import Flask

# The Elastic Beanstalk Python platform looks for an application 
# object named 'application' by default.
application = Flask(__name__)

@application.route('/')
def hello_world():
    return '<h1>Experiment No: 5 - Success!</h1><p>This application is running on Amazon Elastic Beanstalk (PaaS).</p>'

# run the app.
if __name__ == "__main__":
    # Setting debug=True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()