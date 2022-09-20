import { UserMannType } from '../actions';
// TODO: reducer
var isLogin=false;
// TODO: indexReducer
function indexReducer(state = isLogin, action) {
	switch (action.type) {
		case UserMannType.LOG_IN:
			// Login
			return true;
		case UserMannType.LOG_OUT:
			// Logout
			return false;
		default:
		  	return state;
	}
}
// TODO: export indexReducer
export default indexReducer;
