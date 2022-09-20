import { connect } from 'react-redux';
import Login from '../components/login/Login.js';
import { UserMannType } from '../actions';
// TODO: mapStateToProps
function mapStateToProps(state) {
	return {}
}
// TODO: mapDispatchToProps
function mapDispatchToProps(dispatch) {
	return {
		LOGIN: function(username, password, history) {
			console.log("username: " + username);
			console.log("password:" + password);
			setTimeout(function() {
				dispatch({type: UserMannType.LOG_IN});
				history.push({pathname:'/Home'});
			}, 1000);
		}
	};
}
// TODO: connect
var LoginReactReducer = connect(
  mapStateToProps,
  mapDispatchToProps
)(Login);
// TODO: export
export default LoginReactReducer;
