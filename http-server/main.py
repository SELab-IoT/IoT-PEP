from application import app

import application.pep_registration
import application.access_control
import application.device_registration
import application.login

print("PEP Server Starting...\n")
app.run(host='166.104.185.70', port=8080, debug=True)
