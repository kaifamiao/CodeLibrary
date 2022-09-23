import { connect } from 'react-redux';
import Home from '../components/home/Home.js';
import { UserMannType } from '../actions';
// TODO: mapDispatchToProps
function mapStateToProps(state) {
	return {
		isLogin:state.isLogin
	}
}
// TODO: mapDispatchToProps
function mapDispatchToProps(dispatch) {
	return {
		LOGOUT: function(history) {
			dispatch({type: UserMannType.LOG_OUT});
			history.push("/");
		}
	};
}
// TODO: connect
var HomeReactReducer = connect(
  mapStateToProps,
  mapDispatchToProps
)(Home);
// TODO: export
export default HomeReactReducer;
