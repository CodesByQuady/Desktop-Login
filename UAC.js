// USER ACCESS CONTROL
// The object of the program is to allow the user to create a new account to sign in to the "website"
// After the user creates it's account and password, the user must sign in again to sign in.
// Front - End Development Attempt
var user_login = () => {
	alert('Welcome New User. Create a new account and password to unlock access to the full website.')
	const user_name = prompt('Enter A User Name.')
	console.log('Username: ',user_name)
	
	while (true) {
		var user_password = prompt('Password must be 8 characters long.')
		if (user_password.length < 8){
			alert("Your password isn't long enough, try again.")
			console.log('Failed password creation. Not long enough.')
			continue
		} else {
			alert('Password criteria is met.')
			console.log('Password created')
			break
		};
	};
	alert('Now re-enter your user name and password.')
	while (true){
		var login_attempt = prompt('Enter Your User Name.')
		if (login_attempt != user_name){
			alert('Username does not match, try again.')
			console.log('Fail')
			continue
		} else {
			var login_password = prompt('Username matches, now enter your password.')
			if (login_password != user_password) {
				alert('Password does not match. Re enter credientals.')
				continue
			} else {
				alert('Username and password are correct, welcome to the system.')
				console.log('Username: ',user_name,'Password: ',user_password,' Test complete.')
				break
			}
		}
	};

};

user_login()


